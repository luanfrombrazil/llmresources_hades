# ClockGen — Gerador de clock

- **Classe HADES:** `hades.models.io.ClockGen`
- **Categoria:** Entradas, saídas e fontes
- **Dimensões (bbox, relativo à âncora):** x 0..2400, y 0..2400 → 2400 × 2400

## O que faz

Gera um clock periódico de 1 bit.

## Linha de componente

```
hades.models.io.ClockGen <nome> <x> <y> @N 1001 1.0 0.5 0.0
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `periodo` | período em segundos (ex.: `1.0`) |
| 2 | `duty` | ciclo de trabalho 0..1 (ex.: `0.5`) |
| 3 | `offset` | atraso inicial em segundos |
| 4 | `bindkey` | tecla ou `null` (pode ser omitido) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `clk` | saída | 1 | (2400, 1200) | direita |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- Antes de `offset` a saída é `U`. A partir de `offset`: fica em '1' durante `duty × periodo`, depois em '0' até completar o período, e repete (verificado em simulação).

## Dicas

- Porta de saída chama-se `clk` (minúsculo).
- Truque para RESET automático no início: `ClockGen` com período enorme e duty minúsculo (ex.: `1001 1000.0 5.0E-4 0.0 null`, que fica em 1 só por 0,5 s) seguido de um `InvSmall` → sinal 0 no começo e 1 depois, ideal para o `NR` dos registradores.

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.1\Arquitetura e Organização de Computadores I\TP_Test\Testing.hds`

```
hades.models.io.ClockGen CLK -17400 600 @N 1001 1.0 0.5 0.0 a
hades.signals.SignalStdLogic1164 n57 2 CLK clk i0 B 1 2 -15000 1800 -11400 1800 0
```

A segunda linha é um sinal ligado à instância `CLK`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
