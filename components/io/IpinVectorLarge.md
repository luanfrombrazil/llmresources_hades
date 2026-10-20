# IpinVectorLarge — Entrada de n bits (símbolo largo)

- **Classe HADES:** `hades.models.rtlib.io.IpinVectorLarge`
- **Categoria:** Entradas, saídas e fontes
- **Dimensões (bbox, relativo à âncora):** x -14400..0, y -600..600 → 14400 × 1200

## O que faz

Igual ao IpinVector, com símbolo bem mais largo (bbox -14400..0).

## Linha de componente

```
hades.models.rtlib.io.IpinVectorLarge <nome> <x> <y> @N 1001 6 000000_B 1.0E-9 2
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `valor_inicial` | binário `..._B` |
| 3 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |
| 4 | `formato` | 0=dec, 1=hex, 2=bin |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `Y` | saída | n_bits | (0, 0) | direita |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Dicas

- Prefira IpinVector; este ocupa muito espaço.

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.1\Arquitetura e Organização de Computadores I\TP_Test\MainControlTesting.hds`

```
hades.models.rtlib.io.IpinVectorLarge Funct 21600 -12600 @N 1001 6 101010_B 1.0E-9 2
hades.signals.SignalStdLogicVector n28 6 2 Funct Y ExpanderFunct A 2 2 22200 -11400 22200 -12600 2 22200 -12600 21600 -12600 0
```

A segunda linha é um sinal ligado à instância `Funct`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
