# IpinVector — Entrada de n bits (chave interativa / porta de subcircuito)

- **Classe HADES:** `hades.models.rtlib.io.IpinVector`
- **Categoria:** Entradas, saídas e fontes
- **Dimensões (bbox, relativo à âncora):** x -4800..0, y -600..600 → 4800 × 1200

## O que faz

Gera um vetor de n bits. Em subdesigns, é a porta de ENTRADA de barramento (nome = nome da instância).

## Linha de componente

```
hades.models.rtlib.io.IpinVector <nome> <x> <y> @N 1001 32 00000000000000000000000000000000_B 1.0E-9 0
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `valor_inicial` | valor de saída inicial em binário `..._B` com n caracteres |
| 3 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |
| 4 | `formato` | formato de exibição: 0=decimal, 1=hex, 2=binário |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `Y` | saída | n_bits | (0, 0) | direita |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- Clique incrementa, shift-clique decrementa, ctrl-clique alterna X/U/Z.

## Dicas

- Âncora = porta Y; desenho à esquerda (bbox -4800..0, independente de n).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\CONTROLLER.hds`

```
hades.models.rtlib.io.IpinVector OPCODE -24000 600 @N 1001 6 000000_B 1.0E-9 0
hades.signals.SignalStdLogicVector nOPC 6 2 OPCODE Y ex6 A 1 2 -24000 600 -24000 2400 0
```

A segunda linha é um sinal ligado à instância `OPCODE`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
