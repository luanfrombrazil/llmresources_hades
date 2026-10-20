# Ipin — Entrada de 1 bit (chave interativa / porta de subcircuito)

Classe: `hades.models.io.Ipin`  
bbox: (-1200,-600)..(0,600)

Fonte de 1 bit (chave). Em subcircuito: porta de entrada com o nome da instância.

## Linha

```
hades.models.io.Ipin <nome> <x> <y> @N 1001 null U
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `bindkey` | tecla de atalho ou `null` (pode vir vazio: `1001  U`) |
| 2 | `valor_inicial` | `0`, `1` ou `U` |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `Y` | out | 1 | (0,0) | dir |

## Comportamento

- Clique alterna 0/1; shift-clique: 0-1-U-Z.
- Valor inicial é aplicado na simulação.

## Notas

- Gerar como `1001 null 0` / `1001 null 1`.
- Âncora = porta Y; desenho à esquerda.

## Exemplo

```
hades.models.io.Ipin ALUOP1 10800 4800 @N 1001  U
hades.signals.SignalStdLogic1164 n7 4 ALUOP1 Y i2 A i9 A i1 A 9 2 10800 4800 11400 8400 2 11400 8400 14400 8400 2 14400 12600 14400 17400 2 14400 17400 15000 17400 2 14400 9600 14400 12600 2 14400 12600 18000 12600 2 18000 12600 18000 13200 2 14400 8400 14400 9600 2 14400 9600 15600 9600 2 14400 9600 14400 12600
```
