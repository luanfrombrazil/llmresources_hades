# Nand2 — Porta NAND de 2 entradas

Classe: `hades.models.gates.Nand2`  
bbox: (0,0)..(3600,2400)

Y = NOT(A AND B).

## Linha

```
hades.models.gates.Nand2 <nome> <x> <y> @N 1001 1.0E-8
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
hades.models.gates.Nand2 i16 19800 21600 @N 1001 1.0E-8
hades.signals.SignalStdLogic1164 n43 2 MEMWB REGWRITE i16 A 4 2 114600 18600 115800 18600 2 115800 18600 115800 16800 2 115800 16800 19800 16800 2 19800 16800 19800 22200 0
```
