# CompareEqual — Comparador de igualdade

Classe: `hades.models.rtlib.compare.CompareEqual`  
bbox: (0,0)..(3600,1800)

Y = (A == B).

## Linha

```
hades.models.rtlib.compare.CompareEqual <nome> <x> <y> @N 1001 5 0 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `valor` | saída exibida; use 0 |
| 3 | `delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | n_bits | (1200,0) | topo |
| `B` | in | n_bits | (2400,0) | topo |
| `Y` | out | 1 | (1800,1800) | base |

## Exemplo

```
hades.models.rtlib.compare.CompareEqual i9 13200 7200 @N 1001 5 0 1.0E-8
hades.signals.SignalStdLogic1164 n9 2 i9 Y FORWARDB C 3 2 15000 9000 15000 11400 2 15000 11400 11400 11400 2 11400 11400 11400 12600 0
```
