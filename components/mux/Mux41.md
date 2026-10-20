# Mux41 — Multiplexador 4:1 de n bits

- **Classe HADES:** `hades.models.rtlib.muxes.Mux41`
- **Categoria:** Multiplexadores
- **Dimensões (bbox, relativo à âncora):** x 0..4800, y 0..1800 → 4800 × 1800

## O que faz

Y = A[S1S0].

## Linha de componente

```
hades.models.rtlib.muxes.Mux41 <nome> <x> <y> @N 1001 32 00000000000000000000000000000000_B 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `valor` | valor atual de Y |
| 3 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `S1` | entrada | 1 | (0, 600) | esquerda |
| `S0` | entrada | 1 | (0, 1200) | esquerda |
| `A3` | entrada | n_bits | (600, 0) | topo |
| `A2` | entrada | n_bits | (1800, 0) | topo |
| `A1` | entrada | n_bits | (3000, 0) | topo |
| `A0` | entrada | n_bits | (4200, 0) | topo |
| `Y` | saída | n_bits | (2400, 1800) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- S1S0=00 → A0, 01 → A1, 10 → A2, 11 → A3.

## Dicas

- Entradas no topo em ordem A3, A2, A1, A0 da esquerda para a direita; S1 acima de S0 no lado esquerdo.

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\MUX4.hds`

```
hades.models.rtlib.muxes.Mux41 i2 8400 6600 @N 1001 16 0000000000000011_B 1.0E-8
hades.signals.SignalStdLogicVector n6 16 2 i2 Y i1 A 2 2 10800 8400 10800 10800 2 10800 10800 18600 10800 0
```

A segunda linha é um sinal ligado à instância `i2`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
