# Nor — NOR de redução (n bits → 1 bit)

Classe: `hades.models.rtlib.logic.Nor`  
bbox: (0,0)..(3600,1800)

Y = NOT(A[0] OR … OR A[n−1]) (detecta zero).

## Linha

```
hades.models.rtlib.logic.Nor <nome> <x> <y> @N 1001 5 1 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `valor` | saída exibida; use 0 |
| 3 | `delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | n_bits | (1800,0) | topo |
| `Y` | out | 1 | (1800,1800) | base |

## Exemplo

```
hades.models.rtlib.logic.Nor NorRegD 73200 22800 @N 1001 5 1 1.0E-8
hades.signals.SignalStdLogicVector n43_0 5 3 RegDst Y RegBank AZ NorRegD A 10 2 39600 25200 39600 25800 2 39600 25800 43800 25800 2 43800 25800 43800 24600 2 43800 24600 43800 12000 2 54600 12000 63000 12000 2 43800 12000 54600 12000 2 54600 12000 54600 22200 2 54600 22200 71400 22200 2 71400 22200 75000 22200 2 75000 22200 75000 22800 1 54600 12000
```
