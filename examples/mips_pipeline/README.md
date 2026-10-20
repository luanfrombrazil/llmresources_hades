# Exemplo: pipeline MIPS de 5 estágios

`MIPS_PIPELINE.hds`: pipeline com forwarding e detecção de hazard (subconjunto MIPS: lw, sw, tipo R, beq). Usa os blocos abaixo (nesta pasta) e `../../blocks/SIGNAL_EXTENDER.hds`, `../../blocks/SHIFTLEFT2.hds`. ROM de instruções: `program.rom`. Todos os caminhos são relativos.

Reset manual: Ipin `NR` (0 → 1) antes de rodar; `ENABLEWRITE` = 1.

## Padrões usados

| Função | Montagem |
|---|---|
| PC | `RegRE` 32; D ← Mux21(PC+4, alvo); ENA ← And2(ENABLEWRITE, PCWRITE) |
| PC+4 | `Add` 32: B ← PC, A ← `Constant` 4 |
| Busca | PC → `ShiftRightLogic` 32/2 → `Subset` 9..0 → `ROM` 1024×32 |
| Campos | `Subset` 32: 31 26, 25 21, 20 16, 15 11, 15 0, 5 0 |
| Banco de registradores | `MipsRegBank 32 32`; nCS ← Gnd; nWE ← Nand2(REGWRITE, CLK) |
| Memória de dados | `RAM 1024 32`; A ← Subset 9..0 do resultado; nCS ← Gnd; nWE ← InvSmall(MEMWRITE) |
| ULA | `UserDefinedALU 32 … 16 15 16 9 0 0 0 12 12 0…` |
| Desvio em ID | `CompareEqual` 32 entre DR0 e DR1 |
| Forwarding | 2× `Mux41` 32 (FWDA/FWDB) |
| Controle | `ExpanderVertical` do opcode → `InvVertical` → `And3Vertical` → `MergeBits` |
| Roteamento | mão dupla (`LAYOUT.md`): clock/reset/enable no topo; write-back e forwarding pela faixa de volta acima; progressão entre estágios por baixo |

## Blocos específicos

### IFID

Registrador IF/ID: PC+4 e instrução.

Símbolo 4800×3600.

| Porta | Dir | Largura | Pos (x,y) |
|---|---|---|---|
| `ENA` | in | 1 | (0,600) |
| `CLK` | in | 1 | (0,1200) |
| `PC4_I` | in | 32 | (0,1800) |
| `NR` | in | 1 | (0,2400) |
| `INSTRUCTION_I` | in | 32 | (0,3000) |
| `PC4_O` | out | 32 | (4800,600) |
| `INSTRUCTION_O` | out | 32 | (4800,1200) |

### IDEX

Registrador ID/EX: controle, PC+4, dados lidos, imediato, rs/rt/rd.

Símbolo 4800×12000.

| Porta | Dir | Largura | Pos (x,y) |
|---|---|---|---|
| `ENABLEWRITE` | in | 1 | (0,600) |
| `NOTRESET` | in | 1 | (0,1200) |
| `CLK` | in | 1 | (0,1800) |
| `CTL` | in | 9 | (0,2400) |
| `PCPLUS4` | in | 32 | (0,7800) |
| `DATA1` | in | 32 | (0,8400) |
| `DATA2` | in | 32 | (0,9000) |
| `IMEDIATE` | in | 32 | (0,9600) |
| `RT` | in | 5 | (0,10200) |
| `RD` | in | 5 | (0,10800) |
| `RS` | in | 5 | (0,11400) |
| `WB` | out | 2 | (4800,600) |
| `MEM` | out | 3 | (4800,1200) |
| `REGDST` | out | 1 | (4800,1800) |
| `ALUOP1` | out | 1 | (4800,2400) |
| `ALUOP2` | out | 1 | (4800,3000) |
| `ALUSRC` | out | 1 | (4800,3600) |
| `PC_PLUS_4` | out | 32 | (4800,4200) |
| `DATA1O` | out | 32 | (4800,4800) |
| `DATA2O` | out | 32 | (4800,5400) |
| `IMEDIATEO` | out | 32 | (4800,6000) |
| `RTO` | out | 5 | (4800,6600) |
| `RDO` | out | 5 | (4800,7200) |
| `RSO` | out | 5 | (4800,7800) |

### EXMEM

Registrador EX/MEM.

Símbolo 4800×6600.

| Porta | Dir | Largura | Pos (x,y) |
|---|---|---|---|
| `ENA` | in | 1 | (0,600) |
| `CLK` | in | 1 | (0,1200) |
| `NR` | in | 1 | (0,1800) |
| `WB_I` | in | 2 | (0,2400) |
| `MEM_I` | in | 3 | (0,3000) |
| `JUMPADDRESS_I` | in | 32 | (0,3600) |
| `ZERO_I` | in | 1 | (0,4200) |
| `ALUR_I` | in | 32 | (0,4800) |
| `DATA_I` | in | 32 | (0,5400) |
| `REGDEST_I` | in | 5 | (0,6000) |
| `WB_O` | out | 2 | (4800,600) |
| `BRANCH` | out | 1 | (4800,1200) |
| `MEMREAD` | out | 1 | (4800,1800) |
| `MEMWRITE` | out | 1 | (4800,2400) |
| `JUMPADDRESS_O` | out | 32 | (4800,3000) |
| `ZERO_O` | out | 1 | (4800,3600) |
| `ALUR_O` | out | 32 | (4800,4200) |
| `DATA_O` | out | 32 | (4800,4800) |
| `REGDEST_O` | out | 5 | (4800,5400) |

### MEMWB

Registrador MEM/WB.

Símbolo 4800×5400.

| Porta | Dir | Largura | Pos (x,y) |
|---|---|---|---|
| `ENA` | in | 1 | (0,600) |
| `CLK` | in | 1 | (0,1200) |
| `NR` | in | 1 | (0,1800) |
| `WB_I` | in | 2 | (0,2400) |
| `MEMDATA_I` | in | 32 | (0,3000) |
| `ALURESULT_I` | in | 32 | (0,3600) |
| `REGDEST_I` | in | 5 | (0,4200) |
| `REGWRITE` | out | 1 | (4800,600) |
| `MEMTOREG` | out | 1 | (4800,1200) |
| `MEMDATA_O` | out | 32 | (4800,1800) |
| `ALURESULT_O` | out | 32 | (4800,2400) |
| `REGDEST_O` | out | 5 | (4800,3000) |
| `WB_O` | out | 2 | (4800,3600) |

### CONTROLLER

Controle principal: OPCODE (6) → CTL (9) + BRANCH.

Símbolo 4800×1800.

| Porta | Dir | Largura | Pos (x,y) |
|---|---|---|---|
| `OPCODE` | in | 6 | (0,600) |
| `CTL` | out | 9 | (4800,600) |
| `BRANCH` | out | 1 | (4800,1200) |

### ALUCONTROL

Controle da ULA: ALUOp + funct → OPC da UserDefinedALU.

Símbolo 4800×5400.

| Porta | Dir | Largura | Pos (x,y) |
|---|---|---|---|
| `ALUOP0` | in | 1 | (0,600) |
| `ALUOP1` | in | 1 | (0,1200) |
| `f5` | in | 1 | (0,1800) |
| `f4` | in | 1 | (0,2400) |
| `f3` | in | 1 | (0,3000) |
| `f2` | in | 1 | (0,3600) |
| `f1` | in | 1 | (0,4200) |
| `f0` | in | 1 | (0,4800) |
| `OP3` | out | 1 | (4800,600) |
| `OP2` | out | 1 | (4800,1200) |
| `OP1` | out | 1 | (4800,1800) |
| `OP0` | out | 1 | (4800,2400) |

### FORWARDING_UNIT

Forwarding: seletores dos Mux41 de operandos.

Símbolo 4800×4200.

| Porta | Dir | Largura | Pos (x,y) |
|---|---|---|---|
| `RS` | in | 5 | (0,600) |
| `RT` | in | 5 | (0,1200) |
| `RDMEM` | in | 5 | (0,1800) |
| `EXMEM` | in | 2 | (0,2400) |
| `RDWB1` | in | 5 | (0,3000) |
| `MEMWB` | in | 2 | (0,3600) |
| `FORWARD_A` | out | 2 | (4800,600) |
| `FORWARD_B` | out | 2 | (4800,1200) |

### HAZARD_UNIT

Hazard load-use: PCWRITE, IFIDWRITE, NOBUBBLE, STALL.

Símbolo 4800×3000.

| Porta | Dir | Largura | Pos (x,y) |
|---|---|---|---|
| `MEMREAD` | in | 1 | (0,600) |
| `IDEX_RT` | in | 5 | (0,1200) |
| `IFID_RS` | in | 5 | (0,1800) |
| `IFID_RT` | in | 5 | (0,2400) |
| `PCWRITE` | out | 1 | (4800,600) |
| `IFIDWRITE` | out | 1 | (4800,1200) |
| `NOBUBBLE` | out | 1 | (4800,1800) |
| `STALL` | out | 1 | (4800,2400) |
