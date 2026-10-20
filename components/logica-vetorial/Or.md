# Or — OR de redução (n bits → 1 bit)

- **Classe HADES:** `hades.models.rtlib.logic.Or`
- **Categoria:** Lógica de redução e comparação
- **Dimensões (bbox, relativo à âncora):** x 0..3600, y 0..1800 → 3600 × 1800

## O que faz

Y = A[0] OR … OR A[n−1].

## Linha de componente

```
hades.models.rtlib.logic.Or <nome> <x> <y> @N 1001 3 0 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `valor` | valor atual da saída; use 0 |
| 3 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | n_bits | (1800, 0) | topo |
| `Y` | saída | 1 | (1800, 1800) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\FOWARDING UNIT.hds`

```
hades.models.rtlib.logic.Or i16 39000 8400 @N 1001 5 1 1.0E-8
hades.signals.SignalStdLogic1164 n6 2 i16 Y FORWARDB2 B 1 2 40800 10200 40800 13200 0
```

A segunda linha é um sinal ligado à instância `i16`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
