# ExpanderVertical — Separa um barramento em n bits (saídas verticais)

- **Classe HADES:** `hades.models.rtlib.io.ExpanderVertical`
- **Categoria:** Manipulação de barramentos
- **Dimensões (bbox, relativo à âncora):** x 0..1200, y 0..4200 → 1200 × 4200 *(símbolo dinâmico: depende de n_bits, veja Dicas)*

## O que faz

Como Expander, mas as saídas saem pela direita, empilhadas de cima para baixo.

## Linha de componente

```
hades.models.rtlib.io.ExpanderVertical <nome> <x> <y> @N 1001 6 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

Exemplo abaixo para **n_bits = 6** (`1001 6 1.0E-8`). Para outros n, use as fórmulas em Dicas.

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | n_bits | (600, 0) | topo |
| `Y0` | saída | 1 | (1200, 3600) | direita |
| `Y1` | saída | 1 | (1200, 3000) | direita |
| `Y2` | saída | 1 | (1200, 2400) | direita |
| `Y3` | saída | 1 | (1200, 1800) | direita |
| `Y4` | saída | 1 | (1200, 1200) | direita |
| `Y5` | saída | 1 | (1200, 600) | direita |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- Yi = A[i].

## Dicas

- Símbolo dinâmico: largura 1200, altura 600·(n+1).
- Posições: `A` = (600, 0); `Yi` = (1200, 600·(n−i)) → Y{n-1} no topo, Y0 embaixo.

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\CONTROLLER.hds`

```
hades.models.rtlib.io.ExpanderVertical ex6 -24600 2400 @N 1001 6 1.0E-8
hades.signals.SignalStdLogic1164 n7 5 ex6 Y5 i17 A i6 A i15 A i25 A 12 2 12000 2400 21600 2400 2 21600 2400 21600 11400 2 3600 2400 12000 2400 2 12000 2400 12000 13200 2 12000 13200 13800 13200 2 13800 13200 13800 14400 2 -4200 2400 3600 2400 2 3600 2400 3600 14400 2 3600 14400 5400 14400 2 -9600 2400 -4200 2400 2 -4200 2400 -4200 9000 2 -23400 3000 -9600 2400 3 3600 2400 12000 2400 -4200 2400
```

A segunda linha é um sinal ligado à instância `ex6`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
