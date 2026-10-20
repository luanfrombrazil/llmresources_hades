# InvVertical — Inversor vertical (estilo DIN)

- **Classe HADES:** `hades.models.gatter.InvVertical`
- **Categoria:** Portas lógicas de 1 bit
- **Dimensões (bbox, relativo à âncora):** x 0..1200, y 0..1800 → 1200 × 1800

## O que faz

Y = NOT A. Entrada em cima, saída embaixo. Pacote `gatter` (não `gates`).

## Linha de componente

```
hades.models.gatter.InvVertical <nome> <x> <y> @N 1001 5.0E-9
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `t_delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | 1 | (600, 0) | topo |
| `Y` | saída | 1 | (600, 1800) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- Modelo de atraso de transporte; entradas e saída `StdLogic1164` (1 bit).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\CONTROLLER.hds`

```
hades.models.gatter.InvVertical i30 -600 11400 @N 1001 5.0E-9
hades.signals.SignalStdLogic1164 n21 2 i30 Y i23 C 1 2 0 13200 0 14400 0
```

A segunda linha é um sinal ligado à instância `i30`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
