# LED — LED

- **Classe HADES:** `hades.models.io.LED`
- **Categoria:** Entradas, saídas e fontes
- **Dimensões (bbox, relativo à âncora):** x 0..1200, y -600..600 → 1200 × 1200

## O que faz

Indicador de 1 bit.

## Linha de componente

```
hades.models.io.LED <nome> <x> <y> @N 1001 0
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `cor` | 0=vermelho, 1=verde, 2=amarelo, 3=azul |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | 1 | (0, 0) | esquerda |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- '0' apagado, '1' aceso, outros valores ciano.

## Dicas

- Âncora = porta A (centro-esquerda).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\PIPELINEPOSHAZ.hds`

```
hades.models.io.LED LEDSTALL 40200 41400 @N 1001 0
hades.signals.SignalStdLogic1164 nSTL 2 HAZUNIT STALL LEDSTALL A 1 2 34800 41400 40200 41400 0
```

A segunda linha é um sinal ligado à instância `LEDSTALL`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
