# UserDefinedALU — ULA com mapeamento de opcodes configurável

- **Classe HADES:** `hades.models.rtlib.arith.UserDefinedALU`
- **Categoria:** Aritmética e ULAs
- **Dimensões (bbox, relativo à âncora):** x 0..4800, y 0..2400 → 4800 × 2400

## O que faz

(Y, flags) = ALU(A, B, CIN, OPC). Cada valor de OPC é mapeado para uma operação da tabela abaixo. É a ULA do seu pipeline MIPS.

## Linha de componente

```
hades.models.rtlib.arith.UserDefinedALU <nome> <x> <y> @N 1001 32 1.0E-8 16 15 16 9 0 0 0 12 12 0 0 0 0 0 0 0 0
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |
| 3 | `n_ops` | número de opcodes (16 → OPC de 4 bits) |
| 4 | `op_0 … op_{n_ops−1}` | código da operação executada para OPC = 0, 1, 2 … |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `OPC` | entrada | log2(n_ops) | (0, 1200) | esquerda |
| `A` | entrada | n_bits | (1200, 0) | topo |
| `B` | entrada | n_bits | (3600, 0) | topo |
| `Y` | saída | n_bits | (2400, 2400) | base |
| `CIN` | entrada | 1 | (4200, 0) | topo |
| `COUT` | saída | 1 | (1800, 2400) | base |
| `ZERO` | saída | 1 | (3000, 2400) | base |
| `NEG` | saída | 1 | (3300, 2400) | base |
| `EQ` | saída | 1 | (3600, 2400) | base |
| `OVF` | saída | 1 | (3900, 2400) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- Códigos de operação: 0=0, 1=1, 2=−1 (FFFF), 3=A, 4=B, 5=A+1, 6=B+1, 7=A−1, 8=B−1, 9=A+B, 10=A+B+1, 11=A+B+CIN, 12=A−B, 13=NOT A, 14=NOT B, 15=A AND B, 16=A OR B, 17=A XOR B, 18=A XNOR B, 19=SHL A, 20=SRL A, 21=SRA A, 22=ROL A, 23=ROR A, 24=ROL A c/ carry, 25=ROR A c/ carry.
- Seu pipeline usa `1001 32 1.0E-8 16 15 16 9 0 0 0 12 12 0 0 0 0 0 0 0 0` → OPC 0=AND, 1=OR, 2=ADD, 6=SUB, 7=SUB (demais = 0).

## Dicas

- Flags: ZERO (Y==0), NEG, EQ (A==B), OVF, COUT.
- ZERO, NEG, EQ e OVF ficam em x = 3000, 3300, 3600, 3900: múltiplos de 300, fora da grade de 600. O fio precisa terminar exatamente nesses pontos.

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\PIPELINE.hds`

```
hades.models.rtlib.arith.UserDefinedALU i20 81600 28800 @N 1001 32 1.0E-8 16 15 16 9 0 0 0 12 12 0 0 0 0 0 0 0 0
hades.signals.SignalStdLogic1164 n62 2 i20 ZERO EXMEM ZERO_I 4 2 84600 31200 84600 33000 2 84600 33000 90000 33000 2 90000 33000 90000 24000 2 90000 24000 96600 24000 0
```

A segunda linha é um sinal ligado à instância `i20`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
