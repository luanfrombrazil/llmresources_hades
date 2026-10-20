# Índice de componentes

Leia este índice primeiro e abra **só** o arquivo do componente que for usar. Cada arquivo traz: classe Java, parâmetros da linha, portas (direção, largura, posição relativa), dimensões, comportamento e um exemplo real.

Notação: largura `n_bits` = parâmetro do componente; dimensões = largura × altura do bbox em unidades HADES.

## Entradas, saídas e fontes

Pinos de E/S (também usados como portas de subcircuitos), clock, constantes.

| Componente | Classe | Função | Portas | Tamanho | Doc |
|---|---|---|---|---|---|
| **ClockGen** | `io.ClockGen` | Gerador de clock | clk | 2400×2400 | [ClockGen.md](components/io/ClockGen.md) |
| **Constant** | `rtlib.io.Constant` | Constante de n bits | Y | 3600×1800 | [Constant.md](components/io/Constant.md) |
| **Gnd** | `io.Gnd` | Terra (constante 0) | GND | 1200×1500 | [Gnd.md](components/io/Gnd.md) |
| **Ipin** | `io.Ipin` | Entrada de 1 bit (chave interativa / porta de subcircuito) | Y | 1200×1200 | [Ipin.md](components/io/Ipin.md) |
| **IpinVector** | `rtlib.io.IpinVector` | Entrada de n bits (chave interativa / porta de subcircuito) | Y | 4800×1200 | [IpinVector.md](components/io/IpinVector.md) |
| **IpinVectorLarge** | `rtlib.io.IpinVectorLarge` | Entrada de n bits (símbolo largo) | Y | 14400×1200 | [IpinVectorLarge.md](components/io/IpinVectorLarge.md) |
| **LED** | `io.LED` | LED | A | 1200×1200 | [LED.md](components/io/LED.md) |
| **Opin** | `io.Opin` | Saída de 1 bit (LED / porta de subcircuito) | A | 1200×1200 | [Opin.md](components/io/Opin.md) |
| **OpinVector** | `rtlib.io.OpinVector` | Saída de n bits (display / porta de subcircuito) | A | 4800×1200 | [OpinVector.md](components/io/OpinVector.md) |
| **PulseSwitch** | `io.PulseSwitch` | Chave de pulso | Y | 1200×1200 | [PulseSwitch.md](components/io/PulseSwitch.md) |
| **SmallConstant** | `rtlib.io.SmallConstant` | Constante de n bits (símbolo pequeno) | Y | 1200×1200 | [SmallConstant.md](components/io/SmallConstant.md) |

## Manipulação de barramentos

Juntar, separar e fatiar vetores.

| Componente | Classe | Função | Portas | Tamanho | Doc |
|---|---|---|---|---|---|
| **Expander** | `rtlib.io.Expander` | Separa um barramento em n bits | A, Y0..Y{n-1} | 3000×1200 | [Expander.md](components/barramentos/Expander.md) |
| **ExpanderVertical** | `rtlib.io.ExpanderVertical` | Separa um barramento em n bits (saídas verticais) | A, Y0..Y{n-1} | 1200×4200 | [ExpanderVertical.md](components/barramentos/ExpanderVertical.md) |
| **MergeBits** | `rtlib.io.MergeBits` | Junta n bits em um barramento | Y, A0..A{n-1} | 3000×1200 | [MergeBits.md](components/barramentos/MergeBits.md) |
| **Subset** | `rtlib.io.Subset` | Extrai uma faixa de bits | A, Y | 2400×600 | [Subset.md](components/barramentos/Subset.md) |

## Portas lógicas de 1 bit

AND/OR/NAND/NOR/NOT com sinais StdLogic1164.

| Componente | Classe | Função | Portas | Tamanho | Doc |
|---|---|---|---|---|---|
| **And2** | `gates.And2` | Porta AND de 2 entradas | Y, A, B | 3600×2400 | [And2.md](components/portas/And2.md) |
| **And2Vertical** | `gates.And2Vertical` | Porta AND de 2 entradas (símbolo vertical) | Y, A, B | 2400×3600 | [And2Vertical.md](components/portas/And2Vertical.md) |
| **And3** | `gates.And3` | Porta AND de 3 entradas | Y, A, B, C | 3600×2400 | [And3.md](components/portas/And3.md) |
| **And3Vertical** | `gates.And3Vertical` | Porta AND de 3 entradas (símbolo vertical) | Y, A, B, C | 2400×3600 | [And3Vertical.md](components/portas/And3Vertical.md) |
| **InvSmall** | `gates.InvSmall` | Inversor (símbolo pequeno, horizontal) | A, Y | 1800×1200 | [InvSmall.md](components/portas/InvSmall.md) |
| **InvVertical** | `gatter.InvVertical` | Inversor vertical (estilo DIN) | A, Y | 1200×1800 | [InvVertical.md](components/portas/InvVertical.md) |
| **Nand2** | `gates.Nand2` | Porta NAND de 2 entradas | Y, A, B | 3600×2400 | [Nand2.md](components/portas/Nand2.md) |
| **Nor4** | `gatter.Nor4` | Porta NOR de 4 entradas (estilo DIN) | Y, A, B, C, D | 3600×3000 | [Nor4.md](components/portas/Nor4.md) |
| **Or2** | `gates.Or2` | Porta OR de 2 entradas | Y, A, B | 3600×2400 | [Or2.md](components/portas/Or2.md) |

## Lógica de redução e comparação

Operações n bits → 1 bit.

| Componente | Classe | Função | Portas | Tamanho | Doc |
|---|---|---|---|---|---|
| **And** | `rtlib.logic.And` | AND de redução (n bits → 1 bit) | A, Y | 3600×1800 | [And.md](components/logica-vetorial/And.md) |
| **CompareEqual** | `rtlib.compare.CompareEqual` | Comparador de igualdade | A, B, Y | 3600×1800 | [CompareEqual.md](components/logica-vetorial/CompareEqual.md) |
| **Nor** | `rtlib.logic.Nor` | NOR de redução (n bits → 1 bit) | A, Y | 3600×1800 | [Nor.md](components/logica-vetorial/Nor.md) |
| **Or** | `rtlib.logic.Or` | OR de redução (n bits → 1 bit) | A, Y | 3600×1800 | [Or.md](components/logica-vetorial/Or.md) |
| **Xor** | `rtlib.logic.Xor` | XOR de redução / paridade (n bits → 1 bit) | A, Y | 3600×1800 | [Xor.md](components/logica-vetorial/Xor.md) |

## Aritmética e ULAs

Somadores, deslocadores e ULAs.

| Componente | Classe | Função | Portas | Tamanho | Doc |
|---|---|---|---|---|---|
| **ALU** | `microjava.ALU` | ULA do processador MicroJava | OPC, A, B, Y, CIN, COUT, ZERO, NEG, EQ, OVF | 4800×2400 | [ALU.md](components/aritmetica/ALU.md) |
| **Add** | `rtlib.arith.Add` | Somador de n bits | A, B, SUM | 4800×2400 | [Add.md](components/aritmetica/Add.md) |
| **DcoreALU** | `rtlib.arith.DcoreALU` | ULA do processador D*CORE | OPC, A, B, Y, CIN, COUT, IMM | 4800×2400 | [DcoreALU.md](components/aritmetica/DcoreALU.md) |
| **ShiftLeft** | `rtlib.arith.ShiftLeft` | Deslocamento lógico à esquerda (quantidade fixa) | A, Y | 3600×1800 | [ShiftLeft.md](components/aritmetica/ShiftLeft.md) |
| **ShiftRightLogic** | `rtlib.arith.ShiftRightLogic` | Deslocamento lógico à direita (quantidade fixa) | A, Y | 3600×1800 | [ShiftRightLogic.md](components/aritmetica/ShiftRightLogic.md) |
| **UserDefinedALU** | `rtlib.arith.UserDefinedALU` | ULA com mapeamento de opcodes configurável | OPC, A, B, Y, CIN, COUT, ZERO, NEG, EQ, OVF | 4800×2400 | [UserDefinedALU.md](components/aritmetica/UserDefinedALU.md) |

## Multiplexadores

Seleção de barramentos.

| Componente | Classe | Função | Portas | Tamanho | Doc |
|---|---|---|---|---|---|
| **Mux21** | `rtlib.muxes.Mux21` | Multiplexador 2:1 de n bits | S, A1, A0, Y | 3600×1800 | [Mux21.md](components/mux/Mux21.md) |
| **Mux41** | `rtlib.muxes.Mux41` | Multiplexador 4:1 de n bits | S1, S0, A3, A2, A1, A0, Y | 4800×1800 | [Mux41.md](components/mux/Mux41.md) |

## Registradores

Elementos de estado sincronizados por clock.

| Componente | Classe | Função | Portas | Tamanho | Doc |
|---|---|---|---|---|---|
| **RegRE** | `rtlib.register.RegRE` | Registrador de n bits com enable e reset | CLK, NR, ENA, D, Q | 3600×2400 | [RegRE.md](components/registradores/RegRE.md) |

## Memórias e bancos de registradores

ROM, RAM e bancos de registradores.

| Componente | Classe | Função | Portas | Tamanho | Doc |
|---|---|---|---|---|---|
| **MipsRegBank** | `rtlib.memory.MipsRegBank` | Banco de registradores MIPS (32×32) | AR0, AR1, AW0, DR0, DR1, DW0, nWE, nCS | 7200×4800 | [MipsRegBank.md](components/memoria/MipsRegBank.md) |
| **RAM** | `rtlib.memory.RAM` | RAM assíncrona | A, DIN, DOUT, nWE, nCS | 6000×4800 | [RAM.md](components/memoria/RAM.md) |
| **RAMoe** | `rtlib.memory.RAMoe` | RAM assíncrona com output-enable | A, DIN, DOUT, nWE, nCS, nOE | 6000×4800 | [RAMoe.md](components/memoria/RAMoe.md) |
| **ROM** | `rtlib.memory.ROM` | ROM (memória só de leitura) | A, D | 6000×4800 | [ROM.md](components/memoria/ROM.md) |
| **ROMoe** | `rtlib.memory.ROMoe` | ROM com chip-select e output-enable | A, D, nCS, nOE | 6000×4800 | [ROMoe.md](components/memoria/ROMoe.md) |
| **RegBank** | `rtlib.memory.RegBank` | Banco de registradores D*CORE | AX, AY, AZ, DX, DY, DZ, nWE, CLK | 7200×6000 | [RegBank.md](components/memoria/RegBank.md) |

## Seus subcircuitos (subdesigns)

Blocos `.hds` seus, instanciados com `hades.models.Design`. Detalhes em `subdesigns/`.

| Bloco | Função | Nº portas | Doc |
|---|---|---|---|
| **ALUCONTROL** | Controle da ULA: ALUOp + funct → código de operação da ULA. | 12 | [ALUCONTROL.md](subdesigns/ALUCONTROL.md) |
| **CONTROLLER** | Unidade de controle principal: opcode (6 bits) → barramento de controle CTL (9 bits) + BRANCH. | 3 | [CONTROLLER.md](subdesigns/CONTROLLER.md) |
| **CONTROLLERV1** | Versão anterior do CONTROLLER (saídas separadas). Usada por PIPELINE.hds. | 15 | [CONTROLLERV1.md](subdesigns/CONTROLLERV1.md) |
| **EXMEM** | Registrador de pipeline EX/MEM. | 19 | [EXMEM.md](subdesigns/EXMEM.md) |
| **FOWARDING UNIT** | Unidade de forwarding (adiantamento): compara registradores destino de EX/MEM e MEM/WB com rs/rt de ID/EX e gera os seletores dos Mux41. | 8 | [FOWARDING_UNIT.md](subdesigns/FOWARDING_UNIT.md) |
| **HAZARD UNIT** | Unidade de detecção de hazard load-use: gera PCWRITE, IFIDWRITE, NOBUBBLE e STALL. | 8 | [HAZARD_UNIT.md](subdesigns/HAZARD_UNIT.md) |
| **IDEX** | Registrador de pipeline ID/EX: sinais de controle, PC+4, dados lidos, imediato e campos rs/rt/rd. | 24 | [IDEX.md](subdesigns/IDEX.md) |
| **IDEXV1** | Versão anterior do IDEX. Usada por PIPELINE.hds. | 32 | [IDEXV1.md](subdesigns/IDEXV1.md) |
| **IFID** | Registrador de pipeline IF/ID: guarda PC+4 e a instrução. | 7 | [IFID.md](subdesigns/IFID.md) |
| **JUMP CONTROLLER** | Controle de jump do monociclo (TP02, AOC I). | 7 | [JUMP_CONTROLLER.md](subdesigns/JUMP_CONTROLLER.md) |
| **MEM INDEXER FIX** | Ajuste do endereço de memória (bloco auxiliar). | 2 | [MEM_INDEXER_FIX.md](subdesigns/MEM_INDEXER_FIX.md) |
| **MEMWB** | Registrador de pipeline MEM/WB. | 13 | [MEMWB.md](subdesigns/MEMWB.md) |
| **SHIFTLEFT2** | Deslocamento de 2 bits à esquerda (32 bits), para o alvo de desvio. | 2 | [SHIFTLEFT2.md](subdesigns/SHIFTLEFT2.md) |
| **SIGNAL EXTENDER** | Extensor de sinal 16 → 32 bits. | 2 | [SIGNAL_EXTENDER.md](subdesigns/SIGNAL_EXTENDER.md) |

## Outros componentes do HADES

O `hades.jar` tem 384 componentes. Os que ainda não foram usados estão em [`catalog/`](catalog/README.md), com portas e posições para os parâmetros padrão. Ao usar um pela primeira vez, documente-o em `components/` seguindo [`ADICIONANDO_COMPONENTES.md`](ADICIONANDO_COMPONENTES.md).
