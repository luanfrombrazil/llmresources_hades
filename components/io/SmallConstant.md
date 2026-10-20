# SmallConstant — Constante de n bits (símbolo pequeno)

Classe: `hades.models.rtlib.io.SmallConstant`  
bbox: (0,0)..(1200,1200)

Constant com símbolo pequeno.

## Linha

```
hades.models.rtlib.io.SmallConstant <nome> <x> <y> @N 1001 5 11111_B 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `valor` | binário `_B` |
| 3 | `delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `Y` | out | n_bits | (600,1200) | base |

## Exemplo

```
hades.models.rtlib.io.SmallConstant C31 37800 12600 @N 1001 5 11111_B 1.0E-8
hades.signals.SignalStdLogicVector n16 5 2 C31 Y MuxJAL A1 1 2 38400 13800 38400 20400 0
```
