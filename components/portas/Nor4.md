# Nor4 — Porta NOR de 4 entradas (estilo DIN)

Classe: `hades.models.gatter.Nor4`  
bbox: (0,0)..(3600,3000)

Y = NOT(A OR B OR C OR D). Pacote `gatter`.

## Linha

```
hades.models.gatter.Nor4 <nome> <x> <y> @N 1001 1.0E-8
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
| `D` | in | 1 | (0,2400) | esq |

## Exemplo

```
hades.models.gatter.Nor4 AUX -11400 4200 @N 1001 0.0
hades.signals.SignalStdLogic1164 n55_0_1_1 2 AUX Y AND_CLK B 4 2 -7200 2400 -7200 1800 2 -7200 2400 -7200 5400 2 -7800 5400 -7200 5400 2 -7200 1800 -6000 1800 0
```
