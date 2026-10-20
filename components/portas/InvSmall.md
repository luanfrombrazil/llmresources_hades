# InvSmall — Inversor (símbolo pequeno, horizontal)

- **Classe HADES:** `hades.models.gates.InvSmall`
- **Categoria:** Portas lógicas de 1 bit
- **Dimensões (bbox, relativo à âncora):** x 0..1800, y 0..1200 → 1800 × 1200

## O que faz

Y = NOT A. Entrada à esquerda, saída à direita.

## Linha de componente

```
hades.models.gates.InvSmall <nome> <x> <y> @N 1001 5.0E-9
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `t_delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | 1 | (0, 600) | esquerda |
| `Y` | saída | 1 | (1800, 600) | direita |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- Modelo de atraso de transporte; entradas e saída `StdLogic1164` (1 bit).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\ALUCONTROL.hds`

```
hades.models.gates.InvSmall i9 18000 12600 @N 1001 5.0E-9
hades.signals.SignalStdLogic1164 n7 4 ALUOP1 Y i2 A i9 A i1 A 9 2 10800 4800 11400 8400 2 11400 8400 14400 8400 2 14400 12600 14400 17400 2 14400 17400 15000 17400 2 14400 9600 14400 12600 2 14400 12600 18000 12600 2 18000 12600 18000 13200 2 14400 8400 14400 9600 2 14400 9600 15600 9600 2 14400 9600 14400 12600
```

A segunda linha é um sinal ligado à instância `i9`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
