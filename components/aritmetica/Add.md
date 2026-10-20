# Add — Somador de n bits

Classe: `hades.models.rtlib.arith.Add`  
bbox: (0,0)..(4800,2400)

SUM = A + B (sem carry).

## Linha

```
hades.models.rtlib.arith.Add <nome> <x> <y> @N 1001 32 UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU_B 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `valor` | binário `_B` |
| 3 | `delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | n_bits | (1200,0) | topo |
| `B` | in | n_bits | (3600,0) | topo |
| `SUM` | out | n_bits | (2400,2400) | base |

## Notas

- Saída é `SUM`, não `Y`.

## Exemplo

```
hades.models.rtlib.arith.Add i19 75600 19200 @N 1001 32 00000000000000000000000011110110_B 1.0E-8
hades.signals.SignalStdLogicVector n53 32 2 SHIFT4 Y i19 A 5 2 67200 21000 67200 21600 2 67200 21600 75000 21600 2 75000 21600 75000 18600 2 75000 18600 76800 18600 2 76800 18600 76800 19200 0
```
