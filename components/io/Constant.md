# Constant — Constante de n bits

Classe: `hades.models.rtlib.io.Constant`  
bbox: (0,0)..(3600,1800)

Saída fixa de n bits.

## Linha

```
hades.models.rtlib.io.Constant <nome> <x> <y> @N 1001 32 00000000000000000000000000000100_B 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `valor` | constante, binário `_B` com n caracteres |
| 3 | `delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `Y` | out | n_bits | (1800,1800) | base |

## Notas

- Constante 4 de 32 bits: `1001 32 00000000000000000000000000000100_B 1.0E-8`.

## Exemplo

```
hades.models.rtlib.io.Constant MAIS4 -8400 24000 @N 1001 32 00000000000000000000000000000100_B 1.0E-8
hades.signals.SignalStdLogicVector n7 32 2 MAIS4 Y i3 A 1 2 -6600 25800 -6600 26400 0
```
