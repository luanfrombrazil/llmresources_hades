# And2 — Porta AND de 2 entradas

Classe: `hades.models.gates.And2`  
bbox: (0,0)..(3600,2400)

Y = A AND B.

## Linha

```
hades.models.gates.And2 <nome> <x> <y> @N 1001 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `t_delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `Y` | out | 1 | (3600,1200) | dir |
| `A` | in | 1 | (0,600) | esq |
| `B` | in | 1 | (0,1800) | esq |

## Exemplo

```
hades.models.gates.And2 i1 15600 9000 @N 1001 1.0E-8
hades.signals.SignalStdLogic1164 n9 2 i1 Y i3 B 1 2 19200 10200 20400 10200 0
```
