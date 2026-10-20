# DcoreALU — ULA do processador D*CORE

- **Classe HADES:** `hades.models.rtlib.arith.DcoreALU`
- **Categoria:** Aritmética e ULAs
- **Dimensões (bbox, relativo à âncora):** x 0..4800, y 0..2400 → 4800 × 2400

## O que faz

(COUT, Y) = ALU(A, B, CIN, IMM, OPC) com 24 operações D*CORE.

## Linha de componente

```
hades.models.rtlib.arith.DcoreALU <nome> <x> <y> @N 1001 16 1.0E-8 24 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |
| 3 | `n_ops` | 24 |
| 4 | `op_i` | mapeamento de opcodes (0..23) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `OPC` | entrada | 5 | (0, 1200) | esquerda |
| `A` | entrada | n_bits | (3600, 0) | topo |
| `B` | entrada | n_bits | (1200, 0) | topo |
| `Y` | saída | n_bits | (2400, 2400) | base |
| `CIN` | entrada | 1 | (4200, 0) | topo |
| `COUT` | saída | 1 | (1800, 2400) | base |
| `IMM` | entrada | 4 | (600, 0) | topo |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Dicas

- Usada só em um arquivo de teste antigo.

## Exemplo

```
hades.models.rtlib.arith.DcoreALU i0 6000 6000 @N 1001 16 1.0E-8 24 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
```

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
