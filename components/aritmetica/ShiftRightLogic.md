# ShiftRightLogic — Deslocamento lógico à direita (quantidade fixa)

Classe: `hades.models.rtlib.arith.ShiftRightLogic`  
bbox: (-1800,0)..(1800,1800)

Y = A >> shiftcount (zeros à esquerda).

## Linha

```
hades.models.rtlib.arith.ShiftRightLogic <nome> <x> <y> @N 1001 32 2 00000000000000000000000000000000_B 1.0E-8
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

- Byte→palavra: shiftcount 2.

## Exemplo

```
hades.models.rtlib.arith.ShiftRightLogic SHIFT4 67200 19200 @N 1001 32 1 00000000000000000000000000000000_B 1.0E-8
hades.signals.SignalStdLogicVector n53 32 2 SHIFT4 Y i19 A 5 2 67200 21000 67200 21600 2 67200 21600 75000 21600 2 75000 21600 75000 18600 2 75000 18600 76800 18600 2 76800 18600 76800 19200 0
```
