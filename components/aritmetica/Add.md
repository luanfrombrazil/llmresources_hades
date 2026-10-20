# Add — Somador de n bits

- **Classe HADES:** `hades.models.rtlib.arith.Add`
- **Categoria:** Aritmética e ULAs
- **Dimensões (bbox, relativo à âncora):** x 0..4800, y 0..2400 → 4800 × 2400

## O que faz

SUM = A + B (sem carry in/out). Usado para PC+4 e cálculo do alvo de desvio.

## Linha de componente

```
hades.models.rtlib.arith.Add <nome> <x> <y> @N 1001 32 UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU_B 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `valor` | valor atual de SUM em binário `..._B` |
| 3 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | n_bits | (1200, 0) | topo |
| `B` | entrada | n_bits | (3600, 0) | topo |
| `SUM` | saída | n_bits | (2400, 2400) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Dicas

- Saída chama-se `SUM` (não `Y`).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\PIPELINE.hds`

```
hades.models.rtlib.arith.Add i19 75600 19200 @N 1001 32 00000000000000000000000011110110_B 1.0E-8
hades.signals.SignalStdLogicVector n53 32 2 SHIFT4 Y i19 A 5 2 67200 21000 67200 21600 2 67200 21600 75000 21600 2 75000 21600 75000 18600 2 75000 18600 76800 18600 2 76800 18600 76800 19200 0
```

A segunda linha é um sinal ligado à instância `i19`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
