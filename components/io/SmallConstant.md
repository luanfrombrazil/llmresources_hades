# SmallConstant — Constante de n bits (símbolo pequeno)

- **Classe HADES:** `hades.models.rtlib.io.SmallConstant`
- **Categoria:** Entradas, saídas e fontes
- **Dimensões (bbox, relativo à âncora):** x 0..1200, y 0..1200 → 1200 × 1200

## O que faz

Igual a Constant, com símbolo 1200×1200.

## Linha de componente

```
hades.models.rtlib.io.SmallConstant <nome> <x> <y> @N 1001 5 11111_B 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `valor` | binário `..._B` |
| 3 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `Y` | saída | n_bits | (600, 1200) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.1\Arquitetura e Organização de Computadores I\TP_Test\Testing.hds`

```
hades.models.rtlib.io.SmallConstant C31 37800 12600 @N 1001 5 11111_B 1.0E-8
hades.signals.SignalStdLogicVector n16 5 2 C31 Y MuxJAL A1 1 2 38400 13800 38400 20400 0
```

A segunda linha é um sinal ligado à instância `C31`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
