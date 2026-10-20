# MergeBits — Junta n bits em um barramento

- **Classe HADES:** `hades.models.rtlib.io.MergeBits`
- **Categoria:** Manipulação de barramentos
- **Dimensões (bbox, relativo à âncora):** x 0..3000, y 0..1200 → 3000 × 1200 *(símbolo dinâmico: depende de n_bits, veja Dicas)*

## O que faz

Concatena n entradas de 1 bit (A0..A{n-1}) num vetor Y de n bits. A0 é o bit menos significativo.

## Linha de componente

```
hades.models.rtlib.io.MergeBits <nome> <x> <y> @N 1001 4 1.0E-8
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
| `Y` | saída | n_bits | (600, 1200) | base |
| `A0` | entrada | 1 | (2400, 0) | topo |
| `A1` | entrada | 1 | (1800, 0) | topo |
| `A2` | entrada | 1 | (1200, 0) | topo |
| `A3` | entrada | 1 | (600, 0) | topo |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- Y[i] = Ai.

## Dicas

- Símbolo dinâmico: largura 600·(n+1), altura 1200.
- Posições: `Y` = (600, 1200); `Ai` = (600·(n−i), 0) → A0 fica mais à direita, A{n-1} em x=600.

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\CONTROLLER.hds`

```
hades.models.rtlib.io.MergeBits mg9 36000 38400 @N 1001 9 1.0E-8
hades.signals.SignalStdLogic1164 n35 2 i35 Y mg9 A3 3 2 31800 29400 33600 29400 2 33600 29400 39600 29400 2 39600 29400 39600 38400 0
```

A segunda linha é um sinal ligado à instância `mg9`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
