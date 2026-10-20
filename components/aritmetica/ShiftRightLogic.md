# ShiftRightLogic — Deslocamento lógico à direita (quantidade fixa)

- **Classe HADES:** `hades.models.rtlib.arith.ShiftRightLogic`
- **Categoria:** Aritmética e ULAs
- **Dimensões (bbox, relativo à âncora):** x -1800..1800, y 0..1800 → 3600 × 1800

## O que faz

Y = A >> shiftcount (entra 0 à esquerda). Nos seus pipelines aparece com shiftcount 2 (endereço de palavra da ROM/RAM).

## Linha de componente

```
hades.models.rtlib.arith.ShiftRightLogic <nome> <x> <y> @N 1001 32 2 00000000000000000000000000000000_B 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `shiftcount` | quantidade fixa |
| 3 | `valor` | valor atual de Y |
| 4 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | n_bits | (0, 0) | topo |
| `Y` | saída | n_bits | (0, 1800) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Dicas

- Mesmo símbolo do ShiftLeft.

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\PIPELINE.hds`

```
hades.models.rtlib.arith.ShiftRightLogic SHIFT4 67200 19200 @N 1001 32 1 00000000000000000000000000000000_B 1.0E-8
hades.signals.SignalStdLogicVector n53 32 2 SHIFT4 Y i19 A 5 2 67200 21000 67200 21600 2 67200 21600 75000 21600 2 75000 21600 75000 18600 2 75000 18600 76800 18600 2 76800 18600 76800 19200 0
```

A segunda linha é um sinal ligado à instância `SHIFT4`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
