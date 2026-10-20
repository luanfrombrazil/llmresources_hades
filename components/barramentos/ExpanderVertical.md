# ExpanderVertical — Separa um barramento em n bits (saídas verticais)

Classe: `hades.models.rtlib.io.ExpanderVertical`  
bbox: (0,0)..(1200,4200) para n_bits=6 (dinâmico)

Yi = A[i]. Saídas à direita, Y{n-1} no topo.

## Linha

```
hades.models.rtlib.io.ExpanderVertical <nome> <x> <y> @N 1001 6 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | n_bits | (600,0) | topo |
| `Y0` | out | 1 | (1200,3600) | dir |
| `Y1` | out | 1 | (1200,3000) | dir |
| `Y2` | out | 1 | (1200,2400) | dir |
| `Y3` | out | 1 | (1200,1800) | dir |
| `Y4` | out | 1 | (1200,1200) | dir |
| `Y5` | out | 1 | (1200,600) | dir |

## Notas

- Símbolo dinâmico: bbox 1200 × 600·(n+1).
- A = (600, 0); Yi = (1200, 600·(n−i)).

## Exemplo

```
hades.models.rtlib.io.ExpanderVertical ex6 -24600 2400 @N 1001 6 1.0E-8
hades.signals.SignalStdLogic1164 n7 5 ex6 Y5 i17 A i6 A i15 A i25 A 12 2 12000 2400 21600 2400 2 21600 2400 21600 11400 2 3600 2400 12000 2400 2 12000 2400 12000 13200 2 12000 13200 13800 13200 2 13800 13200 13800 14400 2 -4200 2400 3600 2400 2 3600 2400 3600 14400 2 3600 14400 5400 14400 2 -9600 2400 -4200 2400 2 -4200 2400 -4200 9000 2 -23400 3000 -9600 2400 3 3600 2400 12000 2400 -4200 2400
```
