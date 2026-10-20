# And2Vertical — Porta AND de 2 entradas (símbolo vertical)

Classe: `hades.models.gates.And2Vertical`  
bbox: (0,0)..(2400,3600)

Y = A AND B. Entradas no topo, saída na base.

## Linha

```
hades.models.gates.And2Vertical <nome> <x> <y> @N 1001 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `t_delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `Y` | out | 1 | (1200,3600) | base |
| `A` | in | 1 | (600,0) | topo |
| `B` | in | 1 | (1800,0) | topo |

## Exemplo

```
hades.models.gates.And2Vertical i2 8400 27600 @N 1001 1.0E-8
hades.signals.SignalStdLogic1164 n19 2 FORWARDB1 Y i2 B 4 2 29400 16800 29400 22200 2 21000 22200 10200 22200 2 10200 22200 10200 27600 2 29400 22200 21000 22200 0
```
