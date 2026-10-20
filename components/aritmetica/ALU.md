# ALU — ULA do processador MicroJava

- **Classe HADES:** `hades.models.microjava.ALU`
- **Categoria:** Aritmética e ULAs
- **Dimensões (bbox, relativo à âncora):** x 0..4800, y 0..2400 → 4800 × 2400

## O que faz

Subclasse de UserDefinedALU com outro símbolo; mesmos parâmetros e tabela de operações.

## Linha de componente

```
hades.models.microjava.ALU <nome> <x> <y> @N 1001 32 1.0E-8 16 15 16 9 3 4 5 12 6 8 9 10 11 12 13 14 15
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |
| 3 | `n_ops` | número de opcodes |
| 4 | `op_i` | código da operação para cada OPC (tabela da UserDefinedALU) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `OPC` | entrada | log2(n_ops) | (0, 1200) | esquerda |
| `A` | entrada | n_bits | (1200, 0) | topo |
| `B` | entrada | n_bits | (3600, 0) | topo |
| `Y` | saída | n_bits | (2400, 2400) | base |
| `CIN` | entrada | 1 | (600, 0) | topo |
| `COUT` | saída | 1 | (1200, 2400) | base |
| `ZERO` | saída | 1 | (3000, 2400) | base |
| `NEG` | saída | 1 | (3600, 2400) | base |
| `EQ` | saída | 1 | — (sem posição no símbolo) | — |
| `OVF` | saída | 1 | — (sem posição no símbolo) | — |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- O símbolo NÃO desenha as portas EQ e OVF (elas existem no modelo mas não têm posição).

## Dicas

- Prefira UserDefinedALU.

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.1\Arquitetura e Organização de Computadores I\TP_Test\Testing.hds`

```
hades.models.microjava.ALU ALU 47400 24000 @N 1001 32 1.0E-8 16 15 16 9 3 4 5 12 6 8 9 10 11 12 13 14 15
hades.signals.SignalStdLogic1164 n54_0_1_0 3 ALU ZERO MergeBEQ A1 NOT_Zero A 12 2 50400 26400 50400 27000 2 50400 27000 45600 27000 2 45600 5400 45600 3000 2 45600 3000 45600 600 2 45600 600 45600 -7200 2 45600 -7200 45600 -8400 2 45600 -8400 30600 -8400 2 30600 -8400 22200 -8400 2 22200 -8400 22200 -7200 2 22200 -8400 22200 -9600 2 22200 -9600 24600 -9600 2 45600 5400 45600 27000 1 22200 -8400
```

A segunda linha é um sinal ligado à instância `ALU`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
