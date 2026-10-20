# SelectBit — Seleciona 1 bit de um barramento

Classe: `hades.models.rtlib.io.SelectBit`  
bbox: (-1200,0)..(1200,600)

Y = A[bitIndex]. Saída StdLogic1164: converte vetor de 1 bit em sinal de 1 bit.

## Linha

```
hades.models.rtlib.io.SelectBit <nome> <x> <y> @N 1001 1 0 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura de A |
| 2 | `bitIndex` | bit selecionado |
| 3 | `delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | n_bits | (0,0) | topo |
| `Y` | out | 1 (SignalStdLogic1164) | (0,600) | base |

## Notas

- Símbolo como Subset: A (0,0), Y (0,600).
- Uso típico: ROM/RAM de 1 bit (D é vetor de 1 bit) → SelectBit `1001 1 0 1.0E-8` → porta lógica.

## Exemplo

```
hades.models.rtlib.io.SelectBit i25 15600 -14400 @N 1001 1 0 1.0E-8
hades.signals.SignalStdLogic1164 n7 2 i25 Y i3 B 2 2 15600 -13800 15600 -6600 2 15600 -6600 22800 -6600 0
```
