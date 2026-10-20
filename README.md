# Biblioteca HADES para LLMs

Referência para gerar arquivos `.hds` (esquemáticos do simulador HADES, `hades.jar`). Portas, posições, bbox e formato de parâmetros extraídos do próprio `hades.jar`.

## Ordem de leitura

1. `FORMATO_HDS.md`: gramática do `.hds` (obrigatório).
2. `INDEX.md`: escolher componentes.
3. `components/<cat>/<Componente>.md`: parâmetros, portas, larguras, posições.
4. `LAYOUT.md`: posicionamento, fios, reset.
5. `SUBCIRCUITOS.md` + `blocks/`: hierarquia (`hades.models.Design`, `.sym`).
6. `ARQUIVOS_PARA_MEMORIA.md`: conteúdo de ROM/RAM/bancos de registradores (`.rom`).
7. `examples/`: arquivos completos e validados.

Componente fora de `components/`: ver `catalog/` e documentar antes (`ADICIONANDO_COMPONENTES.md`).

## Estrutura

```
FORMATO_HDS.md  LAYOUT.md  SUBCIRCUITOS.md  ARQUIVOS_PARA_MEMORIA.md  INDEX.md
ADICIONANDO_COMPONENTES.md  TEMPLATE_COMPONENTE.md
components/   44 componentes documentados, por categoria
blocks/       subcircuitos genéricos reutilizáveis
catalog/      384 componentes do hades.jar (md + components.json)
examples/     mux4, contador4, mips_pipeline
tools/        HadesIntro.java (extrai dados de qualquer componente)
```

## Regras essenciais

- Unidades HADES, grade de 600, y cresce para baixo.
- Porta absoluta = âncora da instância + posição relativa da porta.
- Conectividade = lista `(instância, porta)` do sinal; segmentos são só desenho, mas devem terminar nas portas.
- Largura do sinal = largura de todas as portas ligadas. 1 bit: `SignalStdLogic1164`.
- Uma saída por sinal. Nomes únicos, `[A-Za-z0-9_]`.
- Circuito sequencial precisa de reset (registradores começam em X).
