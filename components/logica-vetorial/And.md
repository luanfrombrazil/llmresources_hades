# And — AND de redução (n bits → 1 bit)

Classe: `hades.models.rtlib.logic.And`  
bbox: (0,0)..(3600,1800)

Y = A[0] AND A[1] AND … AND A[n−1].

## Linha

```
hades.models.rtlib.logic.And <nome> <x> <y> @N 1001 6 0 1.0E-8
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

## Notas

- Decodificador: MergeBits (bits 0 invertidos) → And.

## Exemplo

```
hades.models.rtlib.logic.And Addi 27000 18000 @N 1001 6 0 1.0E-8
hades.signals.SignalStdLogic1164 n15 2 Addi Y MUX A 4 2 43800 21600 42600 21600 2 28800 19800 28800 21600 2 28800 21600 38400 21600 2 38400 21600 42600 21600 0
```
