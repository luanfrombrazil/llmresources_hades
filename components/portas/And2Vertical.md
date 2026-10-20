# And2Vertical — Porta AND de 2 entradas (símbolo vertical)

- **Classe HADES:** `hades.models.gates.And2Vertical`
- **Categoria:** Portas lógicas de 1 bit
- **Dimensões (bbox, relativo à âncora):** x 0..2400, y 0..3600 → 2400 × 3600

## O que faz

Y = A AND B. Entradas em cima, saída embaixo.

## Linha de componente

```
hades.models.gates.And2Vertical <nome> <x> <y> @N 1001 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `t_delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `Y` | saída | 1 | (1200, 3600) | base |
| `A` | entrada | 1 | (600, 0) | topo |
| `B` | entrada | 1 | (1800, 0) | topo |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- Modelo de atraso de transporte; entradas e saída `StdLogic1164` (1 bit).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\FOWARDING UNIT.hds`

```
hades.models.gates.And2Vertical i2 8400 27600 @N 1001 1.0E-8
hades.signals.SignalStdLogic1164 n19 2 FORWARDB1 Y i2 B 4 2 29400 16800 29400 22200 2 21000 22200 10200 22200 2 10200 22200 10200 27600 2 29400 22200 21000 22200 0
```

A segunda linha é um sinal ligado à instância `i2`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
