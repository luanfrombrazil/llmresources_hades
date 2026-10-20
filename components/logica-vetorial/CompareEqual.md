# CompareEqual — Comparador de igualdade

- **Classe HADES:** `hades.models.rtlib.compare.CompareEqual`
- **Categoria:** Lógica de redução e comparação
- **Dimensões (bbox, relativo à âncora):** x 0..3600, y 0..1800 → 3600 × 1800

## O que faz

Y = 1 se A == B. Usado na Forwarding Unit e na Hazard Unit (comparar registradores de 5 bits).

## Linha de componente

```
hades.models.rtlib.compare.CompareEqual <nome> <x> <y> @N 1001 5 0 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `valor` | valor atual da saída (0/1/X) |
| 3 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | n_bits | (1200, 0) | topo |
| `B` | entrada | n_bits | (2400, 0) | topo |
| `Y` | saída | 1 | (1800, 1800) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\FOWARDING UNIT.hds`

```
hades.models.rtlib.compare.CompareEqual i9 13200 7200 @N 1001 5 0 1.0E-8
hades.signals.SignalStdLogic1164 n9 2 i9 Y FORWARDB C 3 2 15000 9000 15000 11400 2 15000 11400 11400 11400 2 11400 11400 11400 12600 0
```

A segunda linha é um sinal ligado à instância `i9`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
