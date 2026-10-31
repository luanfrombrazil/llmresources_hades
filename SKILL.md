---
name: hades-hds
description: Gera, edita, valida e explica esquemáticos .hds/.sym e arquivos .rom do simulador HADES (hades.jar) usando portas, posições e parâmetros extraídos do próprio hades.jar. Usar sempre que o pedido envolver HADES, arquivos .hds/.sym/.rom, circuitos digitais para o HADES (portas lógicas, mux, registradores, ULA, memória, caminho de dados MIPS monociclo/pipeline, cache) ou depurar um circuito que não carrega/simula.
---

# Biblioteca HADES para LLMs

Esta skill é a própria biblioteca: os caminhos abaixo são relativos à pasta desta skill.
Nunca inventar portas, posições ou parâmetros: tudo vem dos arquivos abaixo.

## Ordem de leitura

1. `FORMATO_HDS.md`: gramática do `.hds` (obrigatório antes de escrever qualquer arquivo).
2. `INDEX.md`: escolher componentes; abrir só `components/<cat>/<Componente>.md` dos que usar.
3. `LAYOUT.md`: posicionamento, fios, reset.
4. Hierarquia: `SUBCIRCUITOS.md` + `blocks/`; portas fora do padrão: `PORTAS_MISTAS.md`.
5. Memórias: `ARQUIVOS_PARA_MEMORIA.md`.
6. Projetos grandes: `GERADOR.md` (`tools/gerador/hdslib.py`, Python só com biblioteca padrão, valida antes de gravar).
7. `examples/`: arquivos completos e validados para copiar padrões.

Componente fora de `components/`: procurar em `catalog/` (`catalog/components.json`) e documentar antes (`ADICIONANDO_COMPONENTES.md`).

## Regras essenciais

- Unidades HADES, grade de 600, y cresce para baixo. Porta absoluta = âncora + posição relativa.
- Conectividade = lista `(instância, porta)` do sinal; segmentos só desenham, mas devem terminar nas portas.
- Largura do sinal = largura das portas; 1 bit = `SignalStdLogic1164`. Uma saída por sinal. Nomes `[A-Za-z0-9_]`.
- Circuito sequencial precisa de reset (registradores começam em X).
- Validar (`hdslib` ou o servidor MCP) e simular no HADES: o validador cobre geometria e conectividade, não comportamento.

## Ferramentas (opcional): servidor MCP

Se as ferramentas `hades` (`build_design`, `validate_hds`, `render_hds`, `get_component`, `make_rom`...) estiverem
disponíveis, preferi-las: geram/validam `.hds` sem rodar Python localmente. Instalação em `mcp-server/README.md`
(Docker: `docker run -i --rm -v "$PWD:/work" ghcr.io/luanfrombrazil/llmresources_hades`).

## Uso acadêmico

Ler a seção "Uso indevido e prejuízos" do `README.md`: não usar para entregar trabalhos avaliativos como próprios.
Ao ajudar alunos, priorizar explicar, revisar e depurar.
