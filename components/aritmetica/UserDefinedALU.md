# UserDefinedALU — ULA com mapeamento de opcodes configurável

Classe: `hades.models.rtlib.arith.UserDefinedALU`  
bbox: (0,0)..(4800,2400)

(Y, flags) = ALU(A, B, CIN, OPC); cada OPC mapeia para um código de operação.

## Linha

```
hades.models.rtlib.arith.UserDefinedALU <nome> <x> <y> @N 1001 32 1.0E-8 16 15 16 9 0 0 0 12 12 0 0 0 0 0 0 0 0
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `delay` | atraso em s (`1.0E-8`) |
| 3 | `n_ops` | nº de opcodes (16 → OPC de 4 bits) |
| 4 | `op_0 … op_{n_ops−1}` | código da operação para OPC = 0, 1, … |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `OPC` | in | log2(n_ops) | (0,1200) | esq |
| `A` | in | n_bits | (1200,0) | topo |
| `B` | in | n_bits | (3600,0) | topo |
| `Y` | out | n_bits | (2400,2400) | base |
| `CIN` | in | 1 | (4200,0) | topo |
| `COUT` | out | 1 | (1800,2400) | base |
| `ZERO` | out | 1 | (3000,2400) | base |
| `NEG` | out | 1 | (3300,2400) | base |
| `EQ` | out | 1 | (3600,2400) | base |
| `OVF` | out | 1 | (3900,2400) | base |

## Comportamento

- Códigos de operação: 0=0, 1=1, 2=−1 (FFFF), 3=A, 4=B, 5=A+1, 6=B+1, 7=A−1, 8=B−1, 9=A+B, 10=A+B+1, 11=A+B+CIN, 12=A−B, 13=NOT A, 14=NOT B, 15=A AND B, 16=A OR B, 17=A XOR B, 18=A XNOR B, 19=SHL A, 20=SRL A, 21=SRA A, 22=ROL A, 23=ROR A, 24=ROL A c/ carry, 25=ROR A c/ carry.
- ULA MIPS: `1001 32 1.0E-8 16 15 16 9 0 0 0 12 12 0 0 0 0 0 0 0 0` → OPC 0=AND, 1=OR, 2=ADD, 6=SUB, 7=SUB.

## Notas

- Flags: ZERO (Y==0), NEG, EQ (A==B), OVF, COUT.
- ZERO/NEG/EQ/OVF em x 3000/3300/3600/3900: fora da grade de 600.

## Exemplo

```
hades.models.rtlib.arith.UserDefinedALU i20 81600 28800 @N 1001 32 1.0E-8 16 15 16 9 0 0 0 12 12 0 0 0 0 0 0 0 0
hades.signals.SignalStdLogic1164 n62 2 i20 ZERO EXMEM ZERO_I 4 2 84600 31200 84600 33000 2 84600 33000 90000 33000 2 90000 33000 90000 24000 2 90000 24000 96600 24000 0
```
