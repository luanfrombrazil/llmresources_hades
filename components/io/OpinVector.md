# OpinVector — Saída de n bits (display / porta de subcircuito)

Classe: `hades.models.rtlib.io.OpinVector`  
bbox: (0,-600)..(4800,600)

Display de n bits. Em subcircuito: porta de saída de barramento com o nome da instância.

## Linha

```
hades.models.rtlib.io.OpinVector <nome> <x> <y> @N 1001 32 1.0E-9 0
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `delay` | atraso em s (`1.0E-8`) |
| 3 | `formato` | 0=dec, 1=hex, 2=bin |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | n_bits | (0,0) | esq |

## Notas

- Âncora = porta A; desenho à direita.

## Exemplo

```
hades.models.rtlib.io.OpinVector CTL 44400 40800 @N 1001 9 1.0E-9 0
hades.signals.SignalStdLogicVector nCTL 9 2 mg9 Y CTL A 2 2 36600 39600 36600 40800 2 36600 40800 44400 40800 0
```
