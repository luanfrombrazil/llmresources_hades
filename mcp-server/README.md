# Servidor MCP da biblioteca HADES

Expõe esta biblioteca como ferramentas [MCP](https://modelcontextprotocol.io) para qualquer cliente compatível
(Claude Desktop, Claude Code, Cursor, VS Code, ...). O modelo consulta componentes e regras, gera `.hds`/`.sym`
validados pelo `hdslib` e valida/renderiza arquivos existentes, sem precisar rodar Python localmente.

## Ferramentas

| Ferramenta | Uso |
|---|---|
| `list_docs`, `read_doc` | Guias da raiz (`FORMATO_HDS`, `LAYOUT`, `SUBCIRCUITOS`, ...). Também como recursos `hades://docs/<NOME>` |
| `search_components`, `get_component` | 384 componentes do hades.jar; documentação de `components/` quando existe |
| `list_native_types`, `describe_native_type` | Tipos do gerador (`hdslib.native()`), portas/bbox para parâmetros dados (símbolos dinâmicos) |
| `list_library`, `read_library_file` | Qualquer arquivo da biblioteca (exemplos, blocos, catálogo, scripts) |
| `build_design` | Especificação JSON → `.hds` + `.sym` validados (erros/avisos/notas do `hdslib`, cruzamentos, prévia PNG opcional) |
| `validate_hds` | Valida `.hds` existente (editor, mão ou LLM): `errors` (quebram carga/simulação), `lint` (regras de desenho), `warnings` |
| `render_hds` | Prévia PNG de um `.hds` |
| `make_rom`, `validate_rom` | Arquivos `.rom` no padrão de `ARQUIVOS_PARA_MEMORIA.md` |
| `list_workspace`, `read_workspace_file`, `write_workspace_file` | Pasta de trabalho montada em `/work` |

Prompts: `novo_circuito`, `corrigir_hds`.

### Especificação de `build_design`

```json
{
  "name": "TOPO",
  "components": [
    {"type": "Ipin", "name": "A", "x": 1200, "y": 1200, "params": {"v": "0"}},
    {"type": "And2", "name": "AND", "x": 4800, "y": 1200},
    {"type": "Opin", "name": "Y", "x": 10800, "y": 2400}
  ],
  "wires": [
    {"name": "n0", "paths": [["A.Y", [3600, 1200], [3600, 1800], "AND.A"]]},
    {"name": "n1", "paths": [["AND.Y", "Y.A"]]}
  ],
  "instances": [{"block": "SUB", "name": "U1", "x": 9600, "y": 6000}],
  "subcircuits": {"SUB": {"components": [], "wires": [], "symbol": "standard"}},
  "allow_open": ["AND.B"]
}
```

Pontos: `"INST.PORTA"` ou `[x, y]`. Cada caminho é uma polilinha ortogonal; vários caminhos no mesmo fio são
derivações (solda automática). `"auto_elbow": true` insere cantos. Símbolo do subcircuito: `"standard"` ou
`{"width", "height", "ports": [[pino, "L|R|T|B", pos]]}` (`PORTAS_MISTAS.md`).
`save_to` grava os arquivos no workspace quando `ok=true`.

## Instalação

### Docker, stdio (recomendado para uso local)

```bash
docker build -t hades-mcp .            # na raiz do repositório
# ou: docker pull ghcr.io/luanfrombrazil/llmresources_hades:latest
```

Claude Desktop (`claude_desktop_config.json`) / Cursor (`.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "hades": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-v", "/caminho/do/projeto:/work", "hades-mcp"]
    }
  }
}
```

Claude Code:

```bash
claude mcp add hades -- docker run -i --rm --user "$(id -u):$(id -g)" -v "$PWD:/work" hades-mcp
```

O volume `/work` é opcional; sem ele as ferramentas devolvem o conteúdo dos arquivos e as de workspace ficam
indisponíveis. No Linux, use `--user "$(id -u):$(id -g)"` (como acima; no JSON: `"--user", "1000:1000"` com o seu
uid/gid) para o servidor poder gravar na pasta montada; o usuário padrão da imagem é o uid 1000.
Todo acesso a arquivos fica restrito ao workspace (inclusive referências `../` e links simbólicos).

### Docker, HTTP (servidor compartilhado)

```bash
docker compose up -d                   # http://localhost:8000/mcp
# ou
docker run --rm -p 8000:8000 -e HADES_MCP_TRANSPORT=streamable-http hades-mcp
claude mcp add --transport http hades http://localhost:8000/mcp
```

Em servidor público, colocar atrás de um proxy HTTPS e não montar `/work` (ou montar pasta descartável):
o workspace é compartilhado entre todos os clientes.

### Sem Docker

```bash
pip install -e ./mcp-server        # a partir da raiz do repositório (a biblioteca não é copiada para o pacote)
HADES_WORKSPACE="$PWD" hades-mcp       # stdio; ou --transport streamable-http --port 8000
```

Variáveis: `HADES_LIB_ROOT` (raiz da biblioteca; detectada no repositório com `pip install -e` ou rodando dentro dele),
`HADES_WORKSPACE` (padrão `/work` se existir), `HADES_MCP_TRANSPORT`, `HADES_MCP_HOST`, `HADES_MCP_PORT`, `HADES_MCP_PATH`.

## Testes

```bash
pip install -e './mcp-server[test]'
python -m pytest -q mcp-server/tests
```

Cobrem: reprodução byte a byte de `examples/portas_mistas` via `build_design`; zero erros do validador em todos os
`.hds` de `examples/` e `blocks/` (e zero lint nos gerados pelo `hdslib`); detecção de largura/porta erradas;
`.rom`; `check_native()` contra o catálogo; ida e volta por um cliente MCP.

## Notas

- `hdslib.py` é importado direto de `tools/gerador/`: uma só fonte de regras para o gerador Python e o servidor.
- `validate_hds` usa `hdslib.native()` para componentes conhecidos (posições exatas para os parâmetros usados),
  o catálogo para os demais (posições dos parâmetros padrão; símbolos dinâmicos geram aviso) e o `.sym` para
  subcircuitos. `lint` reflete as regras desta biblioteca: arquivos salvos pelo editor costumam ter lint e ainda
  assim carregar.
- `tools/HadesIntro.java` continua exigindo o `hades.jar` (não distribuído aqui) e não faz parte da imagem.
