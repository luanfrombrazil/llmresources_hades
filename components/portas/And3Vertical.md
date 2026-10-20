# And3Vertical — Porta AND de 3 entradas (símbolo vertical)

Classe: `hades.models.gates.And3Vertical`  
bbox: (0,0)..(2400,3600)

Y = A AND B AND C. Entradas no topo, saída na base.

## Linha

```
hades.models.gates.And3Vertical <nome> <x> <y> @N 1001 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `t_delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `Y` | out | 1 | (1200,3600) | base |
| `A` | in | 1 | (600,0) | topo |
| `B` | in | 1 | (1200,0) | topo |
| `C` | in | 1 | (1800,0) | topo |

## Exemplo

```
hades.models.gates.And3Vertical i24 -4800 14400 @N 1001 1.0E-8
hades.signals.SignalStdLogic1164 n29 2 i24 Y i14 B 1 2 -3600 18000 -2400 20400 0
```
