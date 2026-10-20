# Mux41 — Multiplexador 4:1 de n bits

Classe: `hades.models.rtlib.muxes.Mux41`  
bbox: (0,0)..(4800,1800)

Y = A[S1S0].

## Linha

```
hades.models.rtlib.muxes.Mux41 <nome> <x> <y> @N 1001 32 00000000000000000000000000000000_B 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `valor` | binário `_B` |
| 3 | `delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `S1` | in | 1 | (0,600) | esq |
| `S0` | in | 1 | (0,1200) | esq |
| `A3` | in | n_bits | (600,0) | topo |
| `A2` | in | n_bits | (1800,0) | topo |
| `A1` | in | n_bits | (3000,0) | topo |
| `A0` | in | n_bits | (4200,0) | topo |
| `Y` | out | n_bits | (2400,1800) | base |

## Comportamento

- S1S0=00 → A0, 01 → A1, 10 → A2, 11 → A3.

## Notas

- Topo, da esquerda: A3, A2, A1, A0. S1 acima de S0.

## Exemplo

```
hades.models.rtlib.muxes.Mux41 i2 8400 6600 @N 1001 16 0000000000000011_B 1.0E-8
hades.signals.SignalStdLogicVector n6 16 2 i2 Y i1 A 2 2 10800 8400 10800 10800 2 10800 10800 18600 10800 0
```
