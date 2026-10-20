# And3 — Porta AND de 3 entradas

Classe: `hades.models.gates.And3`  
bbox: (0,0)..(3600,2400)

Y = A AND B AND C.

## Linha

```
hades.models.gates.And3 <nome> <x> <y> @N 1001 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `t_delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `Y` | out | 1 | (3600,1200) | dir |
| `A` | in | 1 | (0,600) | esq |
| `B` | in | 1 | (0,1200) | esq |
| `C` | in | 1 | (0,1800) | esq |

## Exemplo

```
hades.models.gates.And3 AND3 4200 0 @N 1001 0.0
hades.signals.SignalStdLogic1164 n19 3 ENABLE Y PC ENA AND3 A 7 2 1800 -1200 3000 -1200 2 3000 -1200 5400 -1200 2 5400 -1200 9000 -1200 2 9000 -1200 9000 600 2 9000 600 9600 600 2 3000 -1200 3000 600 2 3000 600 4200 600 1 3000 -1200
```
