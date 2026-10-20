# Expander — Separa um barramento em n bits

Classe: `hades.models.rtlib.io.Expander`  
bbox: (0,0)..(3000,1200) para n_bits=4 (dinâmico)

Yi = A[i]. Y0 = LSB.

## Linha

```
hades.models.rtlib.io.Expander <nome> <x> <y> @N 1001 4 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | n_bits | (600,0) | topo |
| `Y0` | out | 1 | (2400,1200) | base |
| `Y1` | out | 1 | (1800,1200) | base |
| `Y2` | out | 1 | (1200,1200) | base |
| `Y3` | out | 1 | (600,1200) | base |

## Notas

- Símbolo dinâmico: bbox 600·(n+1) × 1200.
- A = (600, 0); Yi = (600·(n−i), 1200).

## Exemplo

```
hades.models.rtlib.io.Expander i2 -5400 9000 @N 1001 1 1.0E-8
hades.signals.SignalStdLogic1164 n18 2 i2 Y0 ZERO_O A 2 2 -4800 10200 -4800 11400 2 -4800 11400 -4200 11400 0
```
