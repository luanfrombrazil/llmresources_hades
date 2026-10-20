# Expander — Separa um barramento em n bits

- **Classe HADES:** `hades.models.rtlib.io.Expander`
- **Categoria:** Manipulação de barramentos
- **Dimensões (bbox, relativo à âncora):** x 0..3000, y 0..1200 → 3000 × 1200 *(símbolo dinâmico: depende de n_bits, veja Dicas)*

## O que faz

Entrada A de n bits → saídas Y0..Y{n-1} de 1 bit. Y0 é o bit menos significativo.

## Linha de componente

```
hades.models.rtlib.io.Expander <nome> <x> <y> @N 1001 4 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

Exemplo abaixo para **n_bits = 4** (`1001 4 1.0E-8`). Para outros n, use as fórmulas em Dicas.

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | n_bits | (600, 0) | topo |
| `Y0` | saída | 1 | (2400, 1200) | base |
| `Y1` | saída | 1 | (1800, 1200) | base |
| `Y2` | saída | 1 | (1200, 1200) | base |
| `Y3` | saída | 1 | (600, 1200) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- Yi = A[i].

## Dicas

- Símbolo dinâmico: largura 600·(n+1), altura 1200.
- Posições: `A` = (600, 0); `Yi` = (600·(n−i), 1200) → Y0 mais à direita.

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\EXMEM.hds`

```
hades.models.rtlib.io.Expander i2 -5400 9000 @N 1001 1 1.0E-8
hades.signals.SignalStdLogic1164 n18 2 i2 Y0 ZERO_O A 2 2 -4800 10200 -4800 11400 2 -4800 11400 -4200 11400 0
```

A segunda linha é um sinal ligado à instância `i2`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
