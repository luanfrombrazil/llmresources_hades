# Nor4 — Porta NOR de 4 entradas (estilo DIN)

- **Classe HADES:** `hades.models.gatter.Nor4`
- **Categoria:** Portas lógicas de 1 bit
- **Dimensões (bbox, relativo à âncora):** x 0..3600, y 0..3000 → 3600 × 3000

## O que faz

Y = NOT(A OR B OR C OR D). Pacote `gatter`.

## Linha de componente

```
hades.models.gatter.Nor4 <nome> <x> <y> @N 1001 1.0E-8
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
| `D` | entrada | 1 | (0, 2400) | esquerda |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- Modelo de atraso de transporte; entradas e saída `StdLogic1164` (1 bit).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.1\Arquitetura e Organização de Computadores I\TP_Test\Testing.hds`

```
hades.models.gatter.Nor4 AUX -11400 4200 @N 1001 0.0
hades.signals.SignalStdLogic1164 n55_0_1_1 2 AUX Y AND_CLK B 4 2 -7200 2400 -7200 1800 2 -7200 2400 -7200 5400 2 -7800 5400 -7200 5400 2 -7200 1800 -6000 1800 0
```

A segunda linha é um sinal ligado à instância `AUX`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
