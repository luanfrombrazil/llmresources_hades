# MergeBits — Junta n bits em um barramento

Classe: `hades.models.rtlib.io.MergeBits`  
bbox: (0,0)..(3000,1200) para n_bits=4 (dinâmico)

Y[i] = Ai. A0 = LSB.

## Linha

```
hades.models.rtlib.io.MergeBits <nome> <x> <y> @N 1001 4 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `Y` | out | n_bits | (600,1200) | base |
| `A0` | in | 1 | (2400,0) | topo |
| `A1` | in | 1 | (1800,0) | topo |
| `A2` | in | 1 | (1200,0) | topo |
| `A3` | in | 1 | (600,0) | topo |

## Notas

- Símbolo dinâmico: bbox 600·(n+1) × 1200.
- Y = (600, 1200); Ai = (600·(n−i), 0).

## Exemplo

```
hades.models.rtlib.io.MergeBits mg9 36000 38400 @N 1001 9 1.0E-8
hades.signals.SignalStdLogic1164 n35 2 i35 Y mg9 A3 3 2 31800 29400 33600 29400 2 33600 29400 39600 29400 2 39600 29400 39600 38400 0
```
