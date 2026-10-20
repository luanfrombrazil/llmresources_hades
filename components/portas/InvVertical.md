# InvVertical — Inversor vertical (estilo DIN)

Classe: `hades.models.gatter.InvVertical`  
bbox: (0,0)..(1200,1800)

Y = NOT A. Entrada no topo, saída na base. Pacote `gatter`.

## Linha

```
hades.models.gatter.InvVertical <nome> <x> <y> @N 1001 5.0E-9
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `t_delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | 1 | (600,0) | topo |
| `Y` | out | 1 | (600,1800) | base |

## Exemplo

```
hades.models.gatter.InvVertical i30 -600 11400 @N 1001 5.0E-9
hades.signals.SignalStdLogic1164 n21 2 i30 Y i23 C 1 2 0 13200 0 14400 0
```
