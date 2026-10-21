# Gerador Python (`tools/gerador/`)

Alternativa a escrever `.hds` à mão em projetos grandes: componentes e fios descritos em Python, validados contra as regras desta biblioteca e gravados em `.hds`/`.sym`. Python 3, só biblioteca padrão (`Pillow` opcional, apenas para a prévia PNG).

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `hdslib.py` | Biblioteca genérica: catálogo `native()`, `Design`, `Block`, validador, `write()`, `render()`, `check_native()` |
| `exemplo_portas_mistas.py` | Exemplo mínimo: gera `examples/portas_mistas/PORTAS_MISTAS` seguindo `PORTAS_MISTAS.md` |
| `mips/make_pipeline.py` | Gera `examples/pipeline_patterson` (usa `top_pipeline.py`, `blocks.py`) |
| `mips/make_mono.py` | Gera `examples/monociclo_patterson` (usa `top_mono.py`, `blocks.py`, `blocks_mono.py`) |

Saída padrão: `saida/<projeto>` ao lado do script; 1º argumento troca a pasta. `make_pipeline.py` e `make_mono.py` reproduzem byte a byte os `.hds`/`.sym`/`.rom` dos exemplos.

## API (`hdslib.py`)

| Elemento | Uso |
|---|---|
| `Design(nome)` | circuito (`[name]`) |
| `d.add(tipo, inst, x, y, **k)` | componente nativo; âncora na grade de 600 |
| `d.addblock(block, inst, x, y)` | instância de subcircuito (`hades.models.Design`, caminho relativo `<nome>.hds`) |
| `d.P(inst, porta)` | posição absoluta da porta |
| `d.wire(nome, poly1, poly2, …)` | sinal; cada polilinha = lista de pontos ortogonais; várias polilinhas = derivações (solda automática em junção de 3+) |
| `d.expansion(pt, …)` | ponta de trilho solta permitida (`LAYOUT.md`, ponta de expansão) |
| `d.allow_open.add((inst, porta))` | entrada que pode ficar sem ligação |
| `errs, warns = d.build()` | valida e monta sinais; `d.notes` = avisos de padrão |
| `d.write(caminho)` | grava `.hds` |
| `d.crossings()` | nº de cruzamentos (para otimizar faixas) |
| `Block.standard(d)` | subcircuito no padrão HADES (entradas esq, saídas dir, L=4800, passo 600) |
| `Block(d, L, A, [(pino, lado, pos)])` | subcircuito com portas em qualquer lado (`'L' 'R' 'T' 'B'`; pos = y em L/R, x em T/B) |
| `block.write(pasta)` | grava `<nome>.hds` + `<nome>.sym` |
| `render(d, png)` | prévia PNG (Pillow) |
| `check_native(catalog/components.json)` | confere `native()` contra o catálogo; deve retornar `[]` |

Tipos de `native()` (parâmetros `**k`):

| Tipo | Classe | k |
|---|---|---|
| `Ipin`, `Opin` | io.Ipin / io.Opin | `v` (valor inicial do Ipin) |
| `IpinV`, `OpinV` | rtlib.io.IpinVector / OpinVector | `n` |
| `RegRE`, `Add`, `Mux21`, `Mux41`, `CmpEq`, `OrRed` | RTLIB | `n` (padrão 32) |
| `UALU` | UserDefinedALU 32, mapeamento MIPS (0 AND, 1 OR, 2 ADD, 6/7 SUB) | — |
| `Subset` | rtlib.io.Subset | `n`, `u`, `l` |
| `SelectBit` | rtlib.io.SelectBit | `n`, `i` |
| `SRL`, `SHL` | ShiftRightLogic / ShiftLeft | `n`, `s` |
| `ROM` | memory.ROM | `words`, `bits`, `file` |
| `RAM` | memory.RAM | `words`, `bits`, `file` opcional |
| `MipsRegBank` | memory.MipsRegBank 32×32 | `file` opcional |
| `Const`, `SConst` | Constant / SmallConstant | `n`, `v` (bits sem `_B`) |
| `Gnd` | io.Gnd | — |
| `And2`, `Or2`, `Nand2`, `And3`, `Inv` | gates (Inv = InvSmall) | `d` (atraso) |
| `Expander`, `ExpV`, `Merge` | Expander / ExpanderVertical / MergeBits | `n` |
| `ClockGen` | io.ClockGen | `p` (`"período duty offset"`) |

Tipo novo: acrescentar em `native()` com portas/bbox de `components/<cat>/<Classe>.md` e rodar `check_native()`.

## Validação (`build()`)

| Nível | Regras |
|---|---|
| erro | segmento nulo/diagonal/fora da grade; ponta solta (exceto `expansion`); porta no meio de fio ou com 2+ segmentos; fio passando sobre porta; larguras ou tipos diferentes no sinal; ≠ 1 saída; < 2 conexões; porta em 2 sinais; sobreposição/toque entre sinais; portas coincidentes |
| aviso | fio atravessando caixa de componente; caixas sobrepostas; entrada aberta |
| nota (`d.notes`) | componente de dados (ROM, RAM, bancos, ULAs configuráveis) dentro de subcircuito (`SUBCIRCUITOS.md`) |

Os `make_*.py` abortam com erro ou aviso e imprimem as notas.

## Fluxo de trabalho

1. `place()`: componentes com âncoras escolhidas para alinhar portas (`LAYOUT.md`).
2. Fios por `d.P()` + pontos intermediários; faixas de volta como parâmetro (`LAYOUT.md`, mão dupla).
3. Subcircuitos: `Block.standard()` → validar → `Block(...)` com as portas finais (`PORTAS_MISTAS.md`).
4. `build()` sem erros/avisos → `write()` → `.rom` (`ARQUIVOS_PARA_MEMORIA.md`).
5. Abrir/simular no HADES. O validador cobre geometria e conectividade, não comportamento.

## Escrita no MipsRegBank (lição do monociclo)

`MipsRegBank` lê as saídas antes de escrever, na mesma avaliação, e escreve por nível. Consequências:
- Dado, endereço e enable vindos de registradores com atrasos diferentes geram corrida na borda (dado/endereço novos com enable antigo). Ativar `nWE` só depois que todos estabilizam (clock atrasado).
- Leitura do registrador recém-escrito só atualiza quando alguma entrada muda de novo; terminar a escrita (`nWE` → 1) antes do fim do ciclo força a releitura.
- Solução em `WBREG`: `nWE = NAND(RegWrite, CLK atrasado 40 ns)` (2 × InvSmall de 2.0E-8): escreve na 1ª metade do ciclo.

## Convenções do gerador

- Caminhos de subcircuitos e `.rom` sempre relativos (só o nome).
- Rótulos do `.sym`: `ClassLabel` centralizado (L/2, A−150); com portas na base: (L/2, A/2+150) se A < 6000, (L/2, A−750) se A ≥ 6000; `InstanceLabel` (L/2, A+450).

## Estado dos exemplos gerados

- `pipeline_patterson`: carregado e simulado no hades.jar; após o programa de teste, $1…$15 = 5, a, 14, 19, 2d, 14, 4, 14, a, a, a, 0, 0, f, 14 (hex), como esperado; bolha de load-use visível no PC.
- `monociclo_patterson`: carregado e simulado no hades.jar; PC = 0, 4, …, 20, 28, 2c, 34, 38, 0 (`beq` e `j` desviam); $1…$11 = 5, a, f, 5, 0, f, f, —, 14, —, 14 (hex; $8 e $10 não são escritos); mem[palavra 25] = f.
- `pipeline_patterson` tem ROM dentro de `CONTROL` e `ALUCTL` (nota do validador).
