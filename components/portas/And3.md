# And3 — Porta AND de 3 entradas

- **Classe HADES:** `hades.models.gates.And3`
- **Categoria:** Portas lógicas de 1 bit
- **Dimensões (bbox, relativo à âncora):** x 0..3600, y 0..2400 → 3600 × 2400

## O que faz

Y = A AND B AND C.

## Linha de componente

```
hades.models.gates.And3 <nome> <x> <y> @N 1001 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `t_delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `Y` | saída | 1 | (3600, 1200) | direita |
| `A` | entrada | 1 | (0, 600) | esquerda |
| `B` | entrada | 1 | (0, 1200) | esquerda |
| `C` | entrada | 1 | (0, 1800) | esquerda |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- Modelo de atraso de transporte; entradas e saída `StdLogic1164` (1 bit).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.1\Arquitetura e Organização de Computadores I\TP_Test\Testing.hds`

```
hades.models.gates.And3 AND3 4200 0 @N 1001 0.0
hades.signals.SignalStdLogic1164 n19 3 ENABLE Y PC ENA AND3 A 7 2 1800 -1200 3000 -1200 2 3000 -1200 5400 -1200 2 5400 -1200 9000 -1200 2 9000 -1200 9000 600 2 9000 600 9600 600 2 3000 -1200 3000 600 2 3000 600 4200 600 1 3000 -1200
```

A segunda linha é um sinal ligado à instância `AND3`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
