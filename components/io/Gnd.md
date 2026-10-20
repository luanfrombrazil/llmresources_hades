# Gnd — Terra (constante 0)

- **Classe HADES:** `hades.models.io.Gnd`
- **Categoria:** Entradas, saídas e fontes
- **Dimensões (bbox, relativo à âncora):** x -600..600, y 0..1500 → 1200 × 1500

## O que faz

Ligação fixa a '0'.

## Linha de componente

```
hades.models.io.Gnd <nome> <x> <y> @N 1001
```

Sem parâmetros além de `1001`.

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `GND` | bidirecional | 1 | (0, 0) | topo |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- Ativo só no início da simulação; após editar, pare e reinicie a simulação.

## Dicas

- Linha de componente não tem parâmetros além de `1001`.
- Para '1' constante use um `Ipin` com valor 1 ou um `Constant`/`SmallConstant`.

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\PIPELINE.hds`

```
hades.models.io.Gnd i27 100800 31200 @N 1001
hades.signals.SignalStdLogic1164 n78 2 i27 GND i25 nCS 2 2 100800 31200 100800 29400 2 100800 29400 103800 29400 0
```

A segunda linha é um sinal ligado à instância `i27`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
