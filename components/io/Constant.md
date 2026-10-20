# Constant — Constante de n bits

- **Classe HADES:** `hades.models.rtlib.io.Constant`
- **Categoria:** Entradas, saídas e fontes
- **Dimensões (bbox, relativo à âncora):** x 0..3600, y 0..1800 → 3600 × 1800

## O que faz

Saída fixa de n bits.

## Linha de componente

```
hades.models.rtlib.io.Constant <nome> <x> <y> @N 1001 32 00000000000000000000000000000100_B 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `valor` | a constante em binário `..._B` com n caracteres |
| 3 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `Y` | saída | n_bits | (1800, 1800) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Dicas

- Ex.: constante 4 de 32 bits: `1001 32 00000000000000000000000000000100_B 1.0E-8`.

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\PIPELINE.hds`

```
hades.models.rtlib.io.Constant MAIS4 -8400 24000 @N 1001 32 00000000000000000000000000000100_B 1.0E-8
hades.signals.SignalStdLogicVector n7 32 2 MAIS4 Y i3 A 1 2 -6600 25800 -6600 26400 0
```

A segunda linha é um sinal ligado à instância `MAIS4`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
