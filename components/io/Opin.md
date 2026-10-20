# Opin — Saída de 1 bit (LED / porta de subcircuito)

- **Classe HADES:** `hades.models.io.Opin`
- **Categoria:** Entradas, saídas e fontes
- **Dimensões (bbox, relativo à âncora):** x 0..1200, y -600..600 → 1200 × 1200

## O que faz

Mostra um sinal de 1 bit. Também é o conector de SAÍDA de um subdesign: cada Opin vira uma porta de saída com o nome da instância.

## Linha de componente

```
hades.models.io.Opin <nome> <x> <y> @N 1001 5.0E-9
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `t_delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | 1 | (0, 0) | esquerda |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- A porta extra com o nome da instância é interna (hierarquia); conecte só `A`.

## Dicas

- Âncora = posição da porta A; o desenho fica à direita (bbox 0..1200).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\ALUCONTROL.hds`

```
hades.models.io.Opin OP0 25200 12000 @N 1001 5.0E-9
hades.signals.SignalStdLogic1164 n14 2 i2 Y OP0 A 2 2 18600 18000 25200 18000 2 25200 18000 25200 12000 0
```

A segunda linha é um sinal ligado à instância `OP0`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
