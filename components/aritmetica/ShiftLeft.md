# ShiftLeft — Deslocamento lógico à esquerda (quantidade fixa)

Classe: `hades.models.rtlib.arith.ShiftLeft`  
bbox: (-1800,0)..(1800,1800)

Y = A << shiftcount.

## Linha

```
hades.models.rtlib.arith.ShiftLeft <nome> <x> <y> @N 1001 32 2 00000000000000000000000000000000_B 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `shiftcount` | deslocamento fixo |
| 3 | `valor` | binário `_B` |
| 4 | `delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | n_bits | (0,0) | topo |
| `Y` | out | n_bits | (0,1800) | base |

## Notas

- Símbolo centrado em x na âncora.

## Exemplo

```
hades.models.rtlib.arith.ShiftLeft ShiftL_2b 56400 -600 @N 1001 32 2 00000000000000000000000000000000_B 1.0E-8
hades.signals.SignalStdLogicVector n20 32 3 ExtendSignal1 SignalExtended ShiftL_2b A ALUSrc A1 9 2 36600 26400 45000 26400 2 45000 26400 45000 25200 2 45000 14400 45000 -2400 2 45000 -2400 56400 -2400 2 56400 -2400 56400 -600 2 45000 20400 45000 14400 2 45000 14400 48600 14400 2 48600 14400 48600 15000 2 45000 20400 45000 25200 1 45000 14400
```
