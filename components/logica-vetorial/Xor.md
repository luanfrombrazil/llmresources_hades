# Xor — XOR de redução / paridade (n bits → 1 bit)

Classe: `hades.models.rtlib.logic.Xor`  
bbox: (0,0)..(3600,1800)

Y = A[0] XOR … XOR A[n−1].

## Linha

```
hades.models.rtlib.logic.Xor <nome> <x> <y> @N 1001 2 0 1.0E-8
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
hades.models.rtlib.logic.Xor Exclude 66000 34800 @N 1001 2 0 1.0E-8
hades.signals.SignalStdLogic1164 n63 2 Exclude Y MergeOP A1 3 2 67800 36600 67800 40800 2 67800 40800 75000 40800 2 75000 40800 75000 43800 0
```
