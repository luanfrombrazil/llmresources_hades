# IpinVectorLarge — Entrada de n bits (símbolo largo)

Classe: `hades.models.rtlib.io.IpinVectorLarge`  
bbox: (-14400,-600)..(0,600)

IpinVector com símbolo largo.

## Linha

```
hades.models.rtlib.io.IpinVectorLarge <nome> <x> <y> @N 1001 6 000000_B 1.0E-9 2
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `valor_inicial` | binário `_B` |
| 3 | `delay` | atraso em s (`1.0E-8`) |
| 4 | `formato` | 0=dec, 1=hex, 2=bin |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `Y` | out | n_bits | (0,0) | dir |

## Notas

- Prefira IpinVector.

## Exemplo

```
hades.models.rtlib.io.IpinVectorLarge Funct 21600 -12600 @N 1001 6 101010_B 1.0E-9 2
hades.signals.SignalStdLogicVector n28 6 2 Funct Y ExpanderFunct A 2 2 22200 -11400 22200 -12600 2 22200 -12600 21600 -12600 0
```
