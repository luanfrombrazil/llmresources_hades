# Or — OR de redução (n bits → 1 bit)

Classe: `hades.models.rtlib.logic.Or`  
bbox: (0,0)..(3600,1800)

Y = A[0] OR … OR A[n−1].

## Linha

```
hades.models.rtlib.logic.Or <nome> <x> <y> @N 1001 3 0 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `valor` | saída exibida; use 0 |
| 3 | `delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | n_bits | (1800,0) | topo |
| `Y` | out | 1 | (1800,1800) | base |

## Exemplo

```
hades.models.rtlib.logic.Or i16 39000 8400 @N 1001 5 1 1.0E-8
hades.signals.SignalStdLogic1164 n6 2 i16 Y FORWARDB2 B 1 2 40800 10200 40800 13200 0
```
