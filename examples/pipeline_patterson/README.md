# MIPS Pipeline — layout da Fig. 4.65 (Patterson & Hennessy)

Abrir `MIPS_PIPELINE.hds` no HADES. Caminhos relativos (mesma pasta). Segue `llmresources_hades` (FORMATO_HDS, LAYOUT, SUBCIRCUITOS, PORTAS_MISTAS, ARQUIVOS_PARA_MEMORIA).

ISA: `lw`, `sw`, tipo R (`add`, `sub`, `and`, `or`), `beq`. Forwarding (EX/MEM e MEM/WB), hazard load-use (bolha), desvio resolvido em ID com IF.Flush.

## Componentes nativos (editáveis no `MIPS_PIPELINE.hds`)

| Instância | Classe | Função |
|---|---|---|
| `PCMUX` | Mux21 32 | A0 = PC+4, A1 = alvo do desvio, S = IF.Flush (PCSrc) |
| `PC` | RegRE 32 | ENA = PCWrite |
| `BYTE2WORD`, `IMEMADDR` | ShiftRightLogic 2, Subset 9..0 | endereço de byte → palavra |
| `IMEM` | ROM 1024×32 `program.rom` | memória de instruções |
| `FOUR`, `ADDPC` | Constant 4, Add 32 | PC+4 |
| `REGS` | MipsRegBank 32×32 | banco de registradores |
| `REGWE`, `REGCS` | Nand2 (RegWrite, CLK invertido), Gnd | escrita na 2ª metade do ciclo |
| `CMP` | CompareEqual 32 | "=" do desvio em ID |
| `SHL2`, `ADDBR` | ShiftLeft 2, Add 32 | alvo do desvio |
| `FWDSELA/B`, `FWDMUXA/B` | ExpanderVertical 2, Mux41 32 | forwarding: A0 = registrador, A1 = write-back, A2 = A3 = EX/MEM |
| `ALUSRCMUX` | Mux21 32 | A0 = rt, A1 = imediato |
| `ALU` | UserDefinedALU 32 | OPC 0 AND, 1 OR, 2 ADD, 6 SUB, 7 SUB |
| `REGDSTMUX` | Mux21 5 | A0 = rt, A1 = rd |
| `DMEMADDR`, `DMEM` | Subset 9..0, RAM 1024×32 `data.rom` | memória de dados (endereço = resultado da ULA) |
| `DMEMWE`, `DMEMCS` | Nand2 (MemWrite, CLK invertido), Gnd | escrita na 2ª metade do ciclo |
| `WBMUX` | Mux21 32 | A0 = resultado da ULA, A1 = dado lido; S = MemtoReg |
| `CLOCK`, `CLKINV` | ClockGen 1 s, InvSmall | clock e clock invertido |
| `RESETGEN`, `RESETINV` | ClockGen, InvSmall | reset automático (NR = 0 nos primeiros 0,25 s) |

## Subcircuitos

| Bloco | Portas (lado) | Interno |
|---|---|---|
| `IFID` | FLUSH, WE, CLK, NR (topo); PC4_I, INSTR_I (esq); campos separados (dir) | FLUSH zera a instrução; saídas: opcode, rs, rt, rd, imediato, com cópias para hazard (topo) e ID/EX (base) |
| `IDEX` | CLK, NR (topo); HZ_MEMREAD, HZ_RT saindo pela esq | EX separado em REGDST, ALUSRC, ALUOP |
| `EXMEM` | CLK, NR (topo); FWD, FW_RD, FW_RW saindo pela esq | M → MEMWRITE |
| `MEMWB` | REGWRITE, CLK, NR (topo); RW, RD (base) | WB → REGWRITE, MEMTOREG |
| `CONTROL` | OPCODE (esq); FLUSH (topo); WB, M, EX (dir); EQ (base) | ROM 64×9 `control.rom`; FLUSH = Branch AND EQ |
| `MUXCTL` | STALL (topo); WB_I, M_I, EX_I (esq); WB, M, EX (dir) | 3× Mux21 com zero (bolha) |
| `HAZARD` | IFIDWRITE, PCWRITE (topo); IFID_RS/RT (esq); IDEX_MEMREAD/RT (dir); STALL (base) | load-use |
| `FORWARD` | FWDA, FWDB (topo); IDEX_RS/RT (esq); EXMEM_RD/RW (dir); MEMWB_RD/RW (base) | FWDx = {EX/MEM, MEM/WB}, rd ≠ 0 |
| `ALUCTL` | IMM, ALUOP (esq); OP (dir) | ALUOp 00 → ADD, 01 → SUB, 1x → `aluctl.rom` (funct) |
| `SIGNEXT` | INPUT (esq); OUTPUT (dir) | extensão 16 → 32 (bloco da biblioteca) |

Registradores de pipeline: altura 36600, portas na altura de quem as usa; um campo pode ter várias saídas (fan-out interno). Campos: WB = {MemtoReg, RegWrite}, M = {MemWrite, MemRead}, EX = {ALUOp1, ALUOp0, ALUSrc, RegDst} (bit 0 à direita).

## Organização do layout

| Faixa | Conteúdo |
|---|---|
| y = 0 / 600 / 1200 | trilhos NR / CLK / CLK invertido |
| y = 2400…5400 | volta superior: RegWrite, alvo do desvio, PCWrite, IF.Flush, IF/IDWrite, PC+4 (ordem com menos cruzamentos) |
| y = 6600…43200 | componentes; registradores de pipeline na altura toda |
| y = 44400…45600 | volta inferior: RegWrite e rd do MEM/WB, dado de write-back |

Componentes nativos têm entradas no topo e saída na base: fio chega de cima e sai por baixo, voltando ao fluxo horizontal (`LAYOUT.md`).

## Simulação

- Clock de período 1 s; primeira borda útil em t = 1 s.
- Banco de registradores e RAM escrevem com CLK = 0 (2ª metade); leitura em ID vê o valor no mesmo ciclo.
- `program.rom`: resultado esperado $1=5, $2=10, $3=20, $4=25, $5=45, $6=20, $7=4, $8=20, $9=10, $10=10, mem[100]=10, $11=10, $12=0, $13=0, $14=15, $15=20; `beq` desviado volta ao endereço 0.

## Pendências

- Topo de `IFID` e `MEMWB`: portas a 1200 (regra: ≥ 2400), rótulos curtos.
- Validar cada subcircuito no HADES (PORTAS_MISTAS, passo 2).
- MemRead não é usado pela RAM (sem habilitação de leitura); continua no campo M para a Hazard Unit.
