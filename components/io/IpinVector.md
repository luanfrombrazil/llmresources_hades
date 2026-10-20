# IpinVector — Entrada de n bits (chave interativa / porta de subcircuito)

Classe: `hades.models.rtlib.io.IpinVector`  
bbox: (-4800,-600)..(0,600)

Fonte de n bits. Em subcircuito: porta de entrada de barramento com o nome da instância.

## Linha

```
hades.models.rtlib.io.IpinVector <nome> <x> <y> @N 1001 32 00000000000000000000000000000000_B 1.0E-9 0
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `valor_inicial` | valor inicial, binário `_B` com n caracteres |
| 3 | `delay` | atraso em s (`1.0E-8`) |
| 4 | `formato` | exibição: 0=dec, 1=hex, 2=bin |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `Y` | out | n_bits | (0,0) | dir |

## Comportamento

- Clique incrementa; shift-clique decrementa.

## Notas

- Âncora = porta Y; desenho à esquerda (bbox fixo, independe de n).

## Exemplo

```
hades.models.rtlib.io.IpinVector OPCODE -24000 600 @N 1001 6 000000_B 1.0E-9 0
hades.signals.SignalStdLogicVector nOPC 6 2 OPCODE Y ex6 A 1 2 -24000 600 -24000 2400 0
```
