# Layout, fios e padrões de projeto

## 1. Sistema de coordenadas

- Unidades HADES: 2400 unidades ≈ 1 polegada na tela.
- **Grade de 600.** Todas as 1.860 coordenadas de componentes dos seus arquivos são múltiplas de 600. Mantenha isso em componentes e fios.
- Eixo **x cresce para a direita, y cresce para baixo**. Coordenadas negativas são permitidas.
- A âncora `(x, y)` da linha de componente é a origem do símbolo. As posições das portas e o bbox nos docs são relativos a essa origem.
  - Na maioria dos componentes, a âncora é o canto superior esquerdo (bbox começa em `0 0`).
  - **Exceções:** `Ipin`/`IpinVector`/`PulseSwitch` (desenho à esquerda da âncora; a âncora é a própria porta `Y`), `Opin`/`OpinVector`/`LED` (desenho à direita; a âncora é a porta `A`), `Gnd` (porta no topo, desenho para baixo), `Subset`/`ShiftLeft`/`ShiftRightLogic` (símbolo centrado em x).
- Exceção fora da grade: as flags `ZERO/NEG/EQ/OVF` da `UserDefinedALU` ficam em x relativo 3000/3300/3600/3900.

## 2. Convenções de orientação dos símbolos

| Família | Entradas | Saídas |
|---|---|---|
| Portas lógicas horizontais (And2, Or2, Nand2, InvSmall, Nor4) | esquerda | direita |
| Portas verticais (And2Vertical, And3Vertical, InvVertical) | topo | base |
| RTLIB de dados (Add, Mux21, Mux41, RegRE, CompareEqual, logic.*, UserDefinedALU) | dados no **topo** | resultado na **base** |
| Seletores e controle (S do Mux, CLK/ENA/NR do RegRE, OPC da ULA, nWE/nCS) | **lado esquerdo** | — |
| MergeBits / Expander | bits no topo / barramento no topo | barramento na base / bits na base |
| ExpanderVertical | barramento no topo | bits à direita, de cima para baixo |
| Memórias (ROM, RAM, MipsRegBank) | endereços e controle à esquerda, dado de escrita no topo | dado lido na base |
| Subcircuitos (`.sym` padrão) | esquerda | direita |

Ou seja: o fluxo de dados das peças RTLIB é **de cima para baixo**, e o controle entra pela esquerda. Os seus circuitos de controle (CONTROLLER, ALUCONTROL) seguem a mesma regra, com as portas verticais.

## 3. Como posicionar

1. Organize o circuito em **colunas por estágio** (esquerda → direita) e, dentro delas, o fluxo de dados de cima para baixo.
2. Deixe pelo menos **1200** de folga entre os bboxes de componentes vizinhos, para os fios passarem.
3. Pinos de entrada do circuito (Ipin/IpinVector) numa coluna à esquerda, espaçados de 1200 em y. Pinos de saída (Opin/OpinVector) numa coluna à direita.
4. Calcule as portas a partir das âncoras:
   `porta_abs = (x_inst + x_rel, y_inst + y_rel)`.
5. Escolha as âncoras para alinhar portas que serão ligadas. Ex.: para ligar a saída `Y` (1800, 1800) de um Mux21 à entrada `D` (1800, 0) de um RegRE logo abaixo, use `x_reg = x_mux` e `y_reg ≥ y_mux + 1800 + 600`. O fio vira um único segmento vertical.

## 4. Como traçar fios

- Use só segmentos horizontais e verticais (o HADES aceita diagonais, mas ficam feios; há um no seu `MUX4.hds`).
- Rota padrão de uma saída (xa, ya) até uma entrada (xb, yb): `(xa,ya)→(xa,ym)→(xb,ym)→(xb,yb)`, com `ym` numa “faixa de roteamento” livre entre as linhas de componentes.
- Para um sinal com vários destinos (clock, reset, barramentos compartilhados), faça um **tronco** e **ramos**, e ponha um ponto de solda em cada junção em T. Veja o sinal `n1` em `examples/IFID.hds`.
- Evite passar um fio por cima de uma porta que não pertence ao sinal. Visualmente parece ligado, mas não está.

## 5. Padrões de projeto que você já usa (pipeline MIPS)

Extraídos de `HACKING AOC\Claude_Hades\PIPELINEPOSHAZ.hds`:

| Função | Como está montado |
|---|---|
| **PC** | `RegRE` de 32 bits; `D` vem de um `Mux21` (PC+4 × alvo de desvio); `ENA` = `And2(ENABLEWRITE, PCWRITE da Hazard Unit)`; `NR` do pino global de reset |
| **PC + 4** | `Add` 32 bits com `B` = PC e `A` = `Constant` 32 bits de valor 4 |
| **Endereço da ROM** | PC → `ShiftRightLogic` (32, shiftcount 2) → `Subset` para os bits baixos → `A` da `ROM` 1024×32 (endereço por palavra) |
| **Campos da instrução** | `Subset` 32 bits: opcode `31 26`, rs `25 21`, rt `20 16`, rd `15 11`, imediato `15 0`, funct `5 0` |
| **Banco de registradores** | `MipsRegBank 32 32`; `nCS` ligado a `Gnd`; `nWE` = `Nand2(REGWRITE do MEM/WB, CLK)`, para escrever só com o clock em 1 |
| **Memória de dados** | `RAM 1024 32`; `A` = `Subset 9 0` do resultado da ULA; `nCS` = `Gnd`; `nWE` = `InvSmall(MEMWRITE)` |
| **ULA** | `UserDefinedALU 32` com mapeamento `16 15 16 9 0 0 0 12 12 0…` (0=AND, 1=OR, 2=ADD, 6/7=SUB) |
| **Desvio no ID** | `CompareEqual` 32 bits entre `DR0` e `DR1` do banco |
| **Forwarding** | dois `Mux41` (FWDA/FWDB) com seletores da FORWARDING UNIT |
| **Registradores de pipeline** | subcircuitos IFID/IDEX/EXMEM/MEMWB feitos de `RegRE`, com `CLK`, `ENA` e `NR` comuns |
| **Clock e reset globais** | um `ClockGen` e um `Ipin` (NR), distribuídos para todos os registradores; LEDs de monitoramento nos sinais principais |
| **Decodificação no controle** | `ExpanderVertical` do opcode → `InvVertical` nos bits que devem ser 0 → `And3Vertical` em cascata → `MergeBits` para montar o barramento de controle |

## 6. Reset e estado inicial

- Registradores (`RegRE`) e o PC começam em **X** na simulação, independentemente do valor gravado na linha. Todo circuito sequencial precisa de um pulso de `NR = 0` no início.
- Nos seus pipelines, o reset é um `Ipin` (`NR`) que você alterna à mão.
- Reset automático: `ClockGen` com `1001 1000.0 5.0E-4 0.0 null` → `InvSmall` → `NR` (0 nos primeiros 0,5 s, depois 1). Usado em `examples/contador4/`.
- `ClockGen` fica em `U` antes do `offset` e começa em **1** quando o período começa.

## 7. Nomes

- Instâncias: nomes descritivos em maiúsculas (`PC`, `MAIS4`, `FWDA`, `MUXALU`) ou `i0, i1…`. Em subcircuitos, os pinos têm o nome da porta (`PC4_I`, `INSTRUCTION_O`).
- Sinais: `n0, n1, …` ou nomes curtos sem espaço (`nSEL`, `nPCE`).
- Sufixos que você usa nos registradores de pipeline: `_I` entrada, `_O` saída.
