# Opin — Saída de 1 bit (LED / porta de subcircuito)

Classe: `hades.models.io.Opin`  
bbox: (0,-600)..(1200,600)

Indicador de 1 bit. Em subcircuito: porta de saída com o nome da instância.

## Linha

```
hades.models.io.Opin <nome> <x> <y> @N 1001 5.0E-9
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `t_delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | 1 | (0,0) | esq |

## Notas

- Âncora = porta A; desenho à direita.

## Exemplo

```
hades.models.io.Opin OP0 25200 12000 @N 1001 5.0E-9
hades.signals.SignalStdLogic1164 n14 2 i2 Y OP0 A 2 2 18600 18000 25200 18000 2 25200 18000 25200 12000 0
```
