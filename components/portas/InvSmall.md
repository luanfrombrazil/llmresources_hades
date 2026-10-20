# InvSmall — Inversor (símbolo pequeno, horizontal)

Classe: `hades.models.gates.InvSmall`  
bbox: (0,0)..(1800,1200)

Y = NOT A. Entrada à esquerda, saída à direita.

## Linha

```
hades.models.gates.InvSmall <nome> <x> <y> @N 1001 5.0E-9
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `t_delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | 1 | (0,600) | esq |
| `Y` | out | 1 | (1800,600) | dir |

## Exemplo

```
hades.models.gates.InvSmall i9 18000 12600 @N 1001 5.0E-9
hades.signals.SignalStdLogic1164 n7 4 ALUOP1 Y i2 A i9 A i1 A 9 2 10800 4800 11400 8400 2 11400 8400 14400 8400 2 14400 12600 14400 17400 2 14400 17400 15000 17400 2 14400 9600 14400 12600 2 14400 12600 18000 12600 2 18000 12600 18000 13200 2 14400 8400 14400 9600 2 14400 9600 15600 9600 2 14400 9600 14400 12600
```
