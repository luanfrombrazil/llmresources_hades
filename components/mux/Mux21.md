# Mux21 — Multiplexador 2:1 de n bits

Classe: `hades.models.rtlib.muxes.Mux21`  
bbox: (0,0)..(3600,1800)

Y = S ? A1 : A0.

## Linha

```
hades.models.rtlib.muxes.Mux21 <nome> <x> <y> @N 1001 32 00000000000000000000000000000000_B 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `valor` | binário `_B` |
| 3 | `delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `S` | in | 1 | (0,1200) | esq |
| `A1` | in | n_bits | (1200,0) | topo |
| `A0` | in | n_bits | (2400,0) | topo |
| `Y` | out | n_bits | (1800,1800) | base |

## Comportamento

- S=0 → A0; S=1 → A1; S indefinido → X.

## Notas

- A1 à esquerda (x=1200), A0 à direita (x=2400).

## Exemplo

```
hades.models.rtlib.muxes.Mux21 i6 -1800 13800 @N 1001 32 00000000000000000000000011111110_B 1.0E-8
hades.signals.SignalStdLogic1164 n83 2 i30 Y i6 S 1 2 -2400 15000 -1800 15000 0
```
