# ClockGen — Gerador de clock

Classe: `hades.models.io.ClockGen`  
bbox: (0,0)..(2400,2400)

Clock periódico de 1 bit.

## Linha

```
hades.models.io.ClockGen <nome> <x> <y> @N 1001 1.0 0.5 0.0
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `periodo` | s |
| 2 | `duty` | 0..1 |
| 3 | `offset` | s |
| 4 | `bindkey` | tecla ou `null`; opcional |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `clk` | out | 1 | (2400,1200) | dir |

## Comportamento

- t < offset: `U`. Depois: 1 por duty·periodo, 0 no resto do período, repete.

## Notas

- Porta `clk` (minúsculo).
- Reset automático: `ClockGen 1001 1000.0 5.0E-4 0.0 null` → `InvSmall` → NR (0 por 0,5 s, depois 1).

## Exemplo

```
hades.models.io.ClockGen CLK -17400 600 @N 1001 1.0 0.5 0.0 a
hades.signals.SignalStdLogic1164 n57 2 CLK clk i0 B 1 2 -15000 1800 -11400 1800 0
```
