# Subset — Extrai uma faixa de bits

- **Classe HADES:** `hades.models.rtlib.io.Subset`
- **Categoria:** Manipulação de barramentos
- **Dimensões (bbox, relativo à âncora):** x -1200..1200, y 0..600 → 2400 × 600

## O que faz

Y = A[upper:lower]. Usado para fatiar a instrução MIPS (opcode 31..26, rs 25..21, rt 20..16, rd 15..11, imediato 15..0).

## Linha de componente

```
hades.models.rtlib.io.Subset <nome> <x> <y> @N 1001 32 25 21 00000_B 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura da entrada A |
| 2 | `upper` | bit mais alto (inclusivo) |
| 3 | `lower` | bit mais baixo (inclusivo) |
| 4 | `valor` | valor atual de Y em binário `..._B` com (upper−lower+1) caracteres |
| 5 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | n_bits | (0, 0) | topo |
| `Y` | saída | upper − lower + 1 | (0, 600) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Dicas

- Símbolo pequeno: A em (0,0) e Y em (0,600) — entrada em cima, saída logo abaixo.
- Ex.: campo rs: `1001 32 25 21 00000_B 1.0E-8`.

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\PIPELINE.hds`

```
hades.models.rtlib.io.Subset i9 16800 31800 @N 1001 32 15 11 00000_B 1.0E-8
hades.signals.SignalStdLogicVector n32 5 2 i9 Y IDEX RD 1 2 16800 32400 53400 32400 0
```

A segunda linha é um sinal ligado à instância `i9`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
