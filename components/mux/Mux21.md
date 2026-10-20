# Mux21 — Multiplexador 2:1 de n bits

- **Classe HADES:** `hades.models.rtlib.muxes.Mux21`
- **Categoria:** Multiplexadores
- **Dimensões (bbox, relativo à âncora):** x 0..3600, y 0..1800 → 3600 × 1800

## O que faz

Y = S ? A1 : A0.

## Linha de componente

```
hades.models.rtlib.muxes.Mux21 <nome> <x> <y> @N 1001 32 00000000000000000000000000000000_B 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `valor` | valor atual de Y em binário `..._B` |
| 3 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `S` | entrada | 1 | (0, 1200) | esquerda |
| `A1` | entrada | n_bits | (1200, 0) | topo |
| `A0` | entrada | n_bits | (2400, 0) | topo |
| `Y` | saída | n_bits | (1800, 1800) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- S=0 → A0; S=1 → A1; S indefinido → X.

## Dicas

- Atenção: A1 fica à ESQUERDA (x=1200) e A0 à DIREITA (x=2400) no topo do símbolo.

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\PIPELINE.hds`

```
hades.models.rtlib.muxes.Mux21 i6 -1800 13800 @N 1001 32 00000000000000000000000011111110_B 1.0E-8
hades.signals.SignalStdLogic1164 n83 2 i30 Y i6 S 1 2 -2400 15000 -1800 15000 0
```

A segunda linha é um sinal ligado à instância `i6`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
