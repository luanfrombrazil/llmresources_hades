# MIPS monociclo com `j` — Fig. 4.24 (Patterson & Hennessy)

Abrir `MONOCICLO.hds` no HADES (caminhos relativos: manter tudo na mesma pasta).

ISA: `lw`, `sw`, tipo R (`add`, `sub`, `and`, `or`), `beq`, `j`.

## Tudo editável no topo

Três subcircuitos: `SIGNEXT` (16→32 bits) e `JUMPADDR` (INSTR[25:0] << 2 concatenado com PC+4[31:28]) são só fiação; `WBREG` é o registrador de write-back (explicado abaixo). O resto é nativo, inclusive o controle e o controle da ULA:

| Instância | Classe | Função |
|---|---|---|
| `PC`, `PCEN` | RegRE 32, Ipin = 1 | contador de programa (sempre habilitado) |
| `ADDPC`, `FOUR` | Add, Constant 4 | PC + 4 |
| `IMEMADDR`, `IMEM` | Subset 11..2, ROM 1024×32 `program.rom` | memória de instruções |
| `S_OPCODE`, `CTRLROM`, `CTRLX` | Subset, ROM 64×10 `control.rom`, Expander 10 | controle principal e separação dos 10 sinais |
| `S_RS`, `S_RT`, `S_RD`, `REGDSTMUX`, `REGS` | Subset, Mux21 5, MipsRegBank | banco de registradores |
| `WBREG`, `REGCS` | bloco (3 × RegRE + SelectBit + 2 × InvSmall + Nand2), Gnd | captura dado/endereço/RegWrite e comanda a escrita do banco |
| `S_IMM`, `SIGNEXT`, `SHL2`, `ADDBR` | Subset, bloco, ShiftLeft 2, Add | imediato e alvo do desvio |
| `S_FUNCT`, `FUNCTX`, `ALUCTLADDR`, `ALUCTLROM` | Subset, Expander 6, MergeBits 8, ROM 256×4 `aluctl.rom` | controle da ULA: endereço = {ALUOp, funct} |
| `ALUSRCMUX`, `ALU` | Mux21, UserDefinedALU | ULA (OPC 0 AND, 1 OR, 2 ADD, 6 SUB) |
| `BRANCHAND`, `BRMUX`, `JUMPADDR`, `JMUX` | And2, Mux21, bloco, Mux21 | PCSrc = Branch AND Zero; escolha desvio / jump |
| `DMEMADDR`, `DMEM`, `MEMOR`, `MEMNCS`, `DMEMWE` | Subset 11..2, RAM 1024×32 `data.rom`, Or2, InvSmall, Nand2 | memória de dados; nCS = NOT(MemRead OR MemWrite); nWE = NAND(MemWrite, CLK invertido) |
| `WBMUX` | Mux21 | MemtoReg |
| `CLOCK`, `RESETGEN`, `RESETINV` | ClockGen | clock (1 s) e reset automático (NR = 0 por 0,25 s) |
| `CLKINV` | InvSmall | clock invertido (só para a escrita da RAM) |

## Por que existe o `WBREG`

`MipsRegBank` e `RAM` escrevem **por nível** (nWE = 0). No banco de registradores isso cria um laço: em `add $1,$1,$1` a escrita muda `$1`, que muda a ULA, que muda o dado escrito, e o valor dobraria sem parar enquanto nWE = 0.

Solução: o `WBREG` captura, na **borda de subida** do clock (a mesma em que o PC avança), o dado de write-back, o número do registrador destino e a palavra de controle (de onde sai RegWrite). O banco escreve a partir das saídas dele com `nWE = NAND(RegWrite_capturado, CLK atrasado)`: o clock passa por 2 × InvSmall de 20 ns, então a escrita começa 40 ns após a borda de subida (dado, endereço e RegWrite já estáveis) e termina 40 ns após a descida. O fim da escrita força o `MipsRegBank` a reler as saídas, e a instrução *i+1* enxerga o valor escrito por *i* na 2ª metade do ciclo.

Versão anterior (`nWE = NOT RegWrite_capturado`) tinha corrida na borda: dado/endereço novos chegavam antes do enable novo e o `sw $3` sobrescrevia `$3`.

A RAM não tem laço (`sw` não altera endereço nem dado), então escreve na segunda metade do ciclo: `nWE = NAND(MemWrite, CLK invertido)`.

## Faixas de fios

| Faixa | Conteúdo |
|---|---|
| y = -600 / 600 | NR e CLK (globais) |
| y = 3600…6000 | volta superior: write-back, Branch/PCSrc, alvo do desvio, PC+4, Jump |
| y = 14400…20400 | faixas dos sinais de controle (saem do `CTRLX`) e do clock invertido |

A ordem das faixas foi escolhida por busca (`choose_lanes` em `top_mono.py`) para minimizar cruzamentos; o resultado está fixo em `LANES`.

## Programa de teste (`program.rom`)

Resultado (conferido no simulador do hades.jar): `$1=5 $2=10 $3=15 $4=5 $5=0 $6=15 $7=15 $9=20 $11=20`, `mem[byte 100] = 15`. O `beq` pula a instrução 9 e o `j 13` pula a 12 (`$8` e `$10` não são escritos). O último `j 0` reinicia o programa.

## Pendências

- Simulado no hades.jar (motor de simulação, sem o editor gráfico).
- `slt` não é suportado pela ULA (cai em SUB).
- `ALU.CIN` fica aberto de propósito.
