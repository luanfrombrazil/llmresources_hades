# Gnd — Terra (constante 0)

Classe: `hades.models.io.Gnd`  
bbox: (-600,0)..(600,1500)

Ligação fixa a '0'.

## Linha

```
hades.models.io.Gnd <nome> <x> <y> @N 1001
```

Sem parâmetros além de `1001`.

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `GND` | inout | 1 | (0,0) | topo |

## Comportamento

- Avaliado só no início da simulação.

## Notas

- Para 1 constante: `Ipin` com valor 1 ou `Constant`.

## Exemplo

```
hades.models.io.Gnd i27 100800 31200 @N 1001
hades.signals.SignalStdLogic1164 n78 2 i27 GND i25 nCS 2 2 100800 31200 100800 29400 2 100800 29400 103800 29400 0
```
