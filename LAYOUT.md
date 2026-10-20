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
- Extremidade de segmento = porta, junção (≥3 segmentos) ou dobra (2 segmentos). Exceção: ponta de expansão (abaixo).
- Não prolongar fio além de uma dobra.
- Solda só em junções de ≥3 segmentos; dividir o segmento no ponto da junção.
- Não passar fio sobre porta de outro sinal.

## Estruturas repetidas e barramentos

Agrupar espacialmente objetos relacionados em formato de barramento.

| Situação | Regra |
|---|---|
| Blocos repetidos (vias de cache, bancos, bits) | mesma composição, ordem e y em todos; passo constante em x |
| Espaçamento | 1200 entre componentes do mesmo grupo; ≥ 4800 entre grupos |
| Consumidor de uma saída | alinhar porta sob porta (mesmo x): fio vertical de 1 segmento |
| Sinal comum a N destinos (distribuição) | trilho horizontal acima da fileira; derivação vertical por destino; solda em cada derivação |
| Ponta de expansão | barramento + projeto modular (blocos repetidos): estender o trilho além da última derivação, no sentido de crescimento, deixando a ponta solta para acrescentar módulos (ex.: cache 4 → 5/6 vias). Fora desse caso, terminar na última derivação |
| Vários trilhos paralelos | espaçamento 600 entre trilhos |
| N sinais para um destino (coleta) | faixas horizontais paralelas, uma por sinal, passo 600–1200, ordenadas para não cruzar (origens em escada) |

Exemplo (cache 4 vias, grupo = ROM válido, ROM tag, ROM dado):

```
via k: x0 = 12000 + 26400·k
  ROM valid  x0          (256×1)
  ROM tag    x0 + 7200   (256×22)     gap 1200
  ROM data   x0 + 14400  (256×32)     gap 1200; próximo grupo após 6000
  SelectBit  x0 + 3600   sob D do valid
  CompareEqual x0 + 8400 B sob D do tag
trilhos: tag y=-28800, índice y=-28200, acima de todas as ROMs;
  terminam em x=108000, além da última derivação (100800): ponta de expansão
saídas de dado → Mux41: faixas y = 600, 1200, 1800, 2400
```

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
