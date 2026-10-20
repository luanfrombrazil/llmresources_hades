# ALU — ULA do processador MicroJava

Classe: `hades.models.microjava.ALU`  
bbox: (0,0)..(4800,2400)

UserDefinedALU com outro símbolo; mesmos parâmetros.

## Linha

```
hades.models.microjava.ALU <nome> <x> <y> @N 1001 32 1.0E-8 16 15 16 9 3 4 5 12 6 8 9 10 11 12 13 14 15
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `delay` | atraso em s (`1.0E-8`) |
| 3 | `n_ops` | número de opcodes |
| 4 | `op_i` | código por OPC (tabela da UserDefinedALU) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `OPC` | in | log2(n_ops) | (0,1200) | esq |
| `A` | in | n_bits | (1200,0) | topo |
| `B` | in | n_bits | (3600,0) | topo |
| `Y` | out | n_bits | (2400,2400) | base |
| `CIN` | in | 1 | (600,0) | topo |
| `COUT` | out | 1 | (1200,2400) | base |
| `ZERO` | out | 1 | (3000,2400) | base |
| `NEG` | out | 1 | (3600,2400) | base |
| `EQ` | out | 1 | — | — |
| `OVF` | out | 1 | — | — |

## Comportamento

- EQ e OVF não têm posição no símbolo.

## Notas

- Prefira UserDefinedALU.

## Exemplo

```
hades.models.microjava.ALU ALU 47400 24000 @N 1001 32 1.0E-8 16 15 16 9 3 4 5 12 6 8 9 10 11 12 13 14 15
hades.signals.SignalStdLogic1164 n54_0_1_0 3 ALU ZERO MergeBEQ A1 NOT_Zero A 12 2 50400 26400 50400 27000 2 50400 27000 45600 27000 2 45600 5400 45600 3000 2 45600 3000 45600 600 2 45600 600 45600 -7200 2 45600 -7200 45600 -8400 2 45600 -8400 30600 -8400 2 30600 -8400 22200 -8400 2 22200 -8400 22200 -7200 2 22200 -8400 22200 -9600 2 22200 -9600 24600 -9600 2 45600 5400 45600 27000 1 22200 -8400
```
