# Layout, fios e reset

## Coordenadas

- Unidade HADES (2400 ≈ 1 polegada). Grade 600. x → direita, y → baixo; negativos permitidos.
- Âncora = origem do símbolo; posições de portas e bbox são relativas a ela.
  - Maioria: âncora no canto superior esquerdo (bbox começa em 0,0).
  - Ipin/IpinVector/PulseSwitch: âncora = porta Y, desenho à esquerda.
  - Opin/OpinVector/LED: âncora = porta A, desenho à direita.
  - Gnd: porta no topo. Subset/ShiftLeft/ShiftRightLogic: centrados em x.
- Fora da grade: flags ZERO/NEG/EQ/OVF da UserDefinedALU.

## Orientação dos símbolos

| Família | Entradas | Saídas |
|---|---|---|
| Portas horizontais (And2, Or2, Nand2, InvSmall, Nor4) | esq | dir |
| Portas verticais (And2Vertical, And3Vertical, InvVertical) | topo | base |
| RTLIB de dados (Add, Mux, RegRE, CompareEqual, logic.*, ALU) | dados no topo; controle (S, CLK, ENA, NR, OPC) à esq | base |
| MergeBits / Expander | topo | base |
| ExpanderVertical | topo | dir |
| Memórias | endereço/controle à esq, dado de escrita no topo | base |
| Subcircuitos (`.sym` padrão) | esq | dir |

## Posicionamento

1. Colunas por estágio da esquerda para a direita; dados de cima para baixo.
2. Folga ≥ 1200 entre bboxes.
3. Entradas do circuito numa coluna à esquerda, saídas à direita, passo 1200 em y.
4. Escolher âncoras que alinhem portas ligadas. Ex.: Mux21.Y (1800,1800) → RegRE.D (1800,0): mesmo x, `y_reg ≥ y_mux + 2400`; o fio é um segmento vertical.

## Fios

- Rota padrão (xa,ya)→(xb,yb): `(xa,ya)→(xa,ym)→(xb,ym)→(xb,yb)`, com ym num corredor livre.
- Vários destinos: tronco + ramos, solda em cada T.
- Não passar fio sobre porta de outro sinal.

## Reset e estado inicial

- `RegRE` começa em X independentemente do valor na linha. Prever NR=0 no início.
- Manual: Ipin `NR` (alternar 0→1).
- Automático: `ClockGen 1001 1000.0 5.0E-4 0.0 null` → `InvSmall` → NR (0 por 0,5 s, depois 1).
- `ClockGen`: `U` antes do offset; começa em 1.
- Ipin aplica seu valor inicial na simulação.

## Padrões

| Função | Montagem |
|---|---|
| Decodificador | Expander → inversores nos bits 0 → AND (ou MergeBits → `logic.And`) |
| Escrita síncrona em RAM/MipsRegBank | nWE = Nand2(WE, CLK); nCS ← Gnd |
| Endereço de palavra | ShiftRightLogic 2 → Subset dos bits baixos |
| Registrador sempre habilitado | ENA ← Ipin valor 1 |

Exemplo completo: `examples/mips_pipeline/README.md`.

## Nomes

- Instâncias descritivas em maiúsculas (`PC`, `MAIS4`) ou `i0…`. Pinos de subcircuito: nome da porta (`_I`/`_O` opcionais).
- Sinais `n0…` ou nomes curtos sem espaço.
