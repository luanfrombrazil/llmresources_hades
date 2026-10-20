# Or2 — Porta OR de 2 entradas

- **Classe HADES:** `hades.models.gates.Or2`
- **Categoria:** Portas lógicas de 1 bit
- **Dimensões (bbox, relativo à âncora):** x 0..3600, y 0..2400 → 3600 × 2400

## O que faz

Y = A OR B.

## Linha de componente

```
hades.models.gates.Or2 <nome> <x> <y> @N 1001 1.0E-8
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
| `B` | entrada | 1 | (0, 1800) | esquerda |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- Modelo de atraso de transporte; entradas e saída `StdLogic1164` (1 bit).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\ALUCONTROL.hds`

```
hades.models.gates.Or2 i3 20400 8400 @N 1001 1.0E-8
hades.signals.SignalStdLogic1164 n9 2 i1 Y i3 B 1 2 19200 10200 20400 10200 0
```

A segunda linha é um sinal ligado à instância `i3`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
