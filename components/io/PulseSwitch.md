# PulseSwitch — Chave de pulso

- **Classe HADES:** `hades.models.io.PulseSwitch`
- **Categoria:** Entradas, saídas e fontes
- **Dimensões (bbox, relativo à âncora):** x -1200..0, y -600..600 → 1200 × 1200

## O que faz

Ao clicar, gera um pulso 0-1-0 de duração fixa.

## Linha de componente

```
hades.models.io.PulseSwitch <nome> <x> <y> @N 1001 0.1
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `t_pulse` | duração do pulso em segundos (ex.: `0.1`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `Y` | saída | 1 | (0, 0) | direita |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Dicas

- Útil como clock manual (um passo por clique).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.1\Arquitetura e Organização de Computadores I\TP_Test\Testing.hds`

```
hades.models.io.PulseSwitch Pulse -15000 -600 @N 1001 0.2 
hades.signals.SignalStdLogic1164 n69 2 Pulse Y OR_CLK1 B 4 2 -6000 -600 -6000 -600 2 -10800 -600 -6600 -600 2 -6600 -600 -6000 -600 2 -15000 -600 -10800 -600 0
```

A segunda linha é um sinal ligado à instância `Pulse`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
