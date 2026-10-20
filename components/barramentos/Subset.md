# Subset — Extrai uma faixa de bits

Classe: `hades.models.rtlib.io.Subset`  
bbox: (-1200,0)..(1200,600)

Y = A[upper:lower].

## Linha

```
hades.models.rtlib.io.Subset <nome> <x> <y> @N 1001 32 25 21 00000_B 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura da entrada A |
| 2 | `upper` | bit alto (inclusivo) |
| 3 | `lower` | bit baixo (inclusivo) |
| 4 | `valor` | binário `_B` com upper−lower+1 caracteres |
| 5 | `delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | n_bits | (0,0) | topo |
| `Y` | out | upper − lower + 1 | (0,600) | base |

## Notas

- Campos MIPS: opcode 31 26, rs 25 21, rt 20 16, rd 15 11, imm 15 0, funct 5 0.
- Campo rs: `1001 32 25 21 00000_B 1.0E-8`.

## Exemplo

```
hades.models.rtlib.io.Subset i9 16800 31800 @N 1001 32 15 11 00000_B 1.0E-8
hades.signals.SignalStdLogicVector n32 5 2 i9 Y IDEX RD 1 2 16800 32400 53400 32400 0
```
