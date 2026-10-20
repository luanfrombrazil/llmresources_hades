# Nor — NOR de redução (n bits → 1 bit)

- **Classe HADES:** `hades.models.rtlib.logic.Nor`
- **Categoria:** Lógica de redução e comparação
- **Dimensões (bbox, relativo à âncora):** x 0..3600, y 0..1800 → 3600 × 1800

## O que faz

Y = NOT(A[0] OR … OR A[n−1]). Detecta vetor zero.

## Linha de componente

```
hades.models.rtlib.logic.Nor <nome> <x> <y> @N 1001 5 1 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `valor` | valor atual da saída |
| 3 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | n_bits | (1800, 0) | topo |
| `Y` | saída | 1 | (1800, 1800) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.1\Arquitetura e Organização de Computadores I\TP_Test\Testing.hds`

```
hades.models.rtlib.logic.Nor NorRegD 73200 22800 @N 1001 5 1 1.0E-8
hades.signals.SignalStdLogicVector n43_0 5 3 RegDst Y RegBank AZ NorRegD A 10 2 39600 25200 39600 25800 2 39600 25800 43800 25800 2 43800 25800 43800 24600 2 43800 24600 43800 12000 2 54600 12000 63000 12000 2 43800 12000 54600 12000 2 54600 12000 54600 22200 2 54600 22200 71400 22200 2 71400 22200 75000 22200 2 75000 22200 75000 22800 1 54600 12000
```

A segunda linha é um sinal ligado à instância `NorRegD`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
