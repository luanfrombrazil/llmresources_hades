# LED — LED

Classe: `hades.models.io.LED`  
bbox: (0,-600)..(1200,600)

Indicador de 1 bit.

## Linha

```
hades.models.io.LED <nome> <x> <y> @N 1001 0
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `cor` | 0=vermelho, 1=verde, 2=amarelo, 3=azul |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | 1 | (0,0) | esq |

## Comportamento

- 0 apagado, 1 aceso, outros: ciano.

## Notas

- Âncora = porta A.

## Exemplo

```
hades.models.io.LED LEDSTALL 40200 41400 @N 1001 0
hades.signals.SignalStdLogic1164 nSTL 2 HAZUNIT STALL LEDSTALL A 1 2 34800 41400 40200 41400 0
```
