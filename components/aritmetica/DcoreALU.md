# DcoreALU — ULA do processador D*CORE

Classe: `hades.models.rtlib.arith.DcoreALU`  
bbox: (0,0)..(4800,2400)

(COUT, Y) = ALU(A, B, CIN, IMM, OPC) com 24 operações D*CORE.

## Linha

```
hades.models.rtlib.arith.DcoreALU <nome> <x> <y> @N 1001 16 1.0E-8 24 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `delay` | atraso em s (`1.0E-8`) |
| 3 | `n_ops` | 24 |
| 4 | `op_i` | mapeamento de opcodes (0..23) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `OPC` | in | 5 | (0,1200) | esq |
| `A` | in | n_bits | (3600,0) | topo |
| `B` | in | n_bits | (1200,0) | topo |
| `Y` | out | n_bits | (2400,2400) | base |
| `CIN` | in | 1 | (4200,0) | topo |
| `COUT` | out | 1 | (1800,2400) | base |
| `IMM` | in | 4 | (600,0) | topo |
