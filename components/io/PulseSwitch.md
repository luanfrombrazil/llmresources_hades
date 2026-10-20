# PulseSwitch — Chave de pulso

Classe: `hades.models.io.PulseSwitch`  
bbox: (-1200,-600)..(0,600)

Clique gera pulso 0-1-0.

## Linha

```
hades.models.io.PulseSwitch <nome> <x> <y> @N 1001 0.1
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `t_pulse` | duração em s |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `Y` | out | 1 | (0,0) | dir |

## Notas

- Clock manual.

## Exemplo

```
hades.models.io.PulseSwitch Pulse -15000 -600 @N 1001 0.2 
hades.signals.SignalStdLogic1164 n69 2 Pulse Y OR_CLK1 B 4 2 -6000 -600 -6000 -600 2 -10800 -600 -6600 -600 2 -6600 -600 -6000 -600 2 -15000 -600 -10800 -600 0
```
