# Índice

Abrir só o arquivo do componente necessário. Tamanho = bbox (L×A).

## Entradas, saídas e fontes

| Componente | Função | Portas | Tamanho |
|---|---|---|---|
| [ClockGen](components/io/ClockGen.md) | Gerador de clock | clk | 2400×2400 |
| [Constant](components/io/Constant.md) | Constante de n bits | Y | 3600×1800 |
| [Gnd](components/io/Gnd.md) | Terra (constante 0) | GND | 1200×1500 |
| [Ipin](components/io/Ipin.md) | Entrada de 1 bit (chave interativa / porta de subcircuito) | Y | 1200×1200 |
| [IpinVector](components/io/IpinVector.md) | Entrada de n bits (chave interativa / porta de subcircuito) | Y | 4800×1200 |
| [IpinVectorLarge](components/io/IpinVectorLarge.md) | Entrada de n bits (símbolo largo) | Y | 14400×1200 |
| [LED](components/io/LED.md) | LED | A | 1200×1200 |
| [Opin](components/io/Opin.md) | Saída de 1 bit (LED / porta de subcircuito) | A | 1200×1200 |
| [OpinVector](components/io/OpinVector.md) | Saída de n bits (display / porta de subcircuito) | A | 4800×1200 |
| [PulseSwitch](components/io/PulseSwitch.md) | Chave de pulso | Y | 1200×1200 |
| [SmallConstant](components/io/SmallConstant.md) | Constante de n bits (símbolo pequeno) | Y | 1200×1200 |

## Manipulação de barramentos

| Componente | Função | Portas | Tamanho |
|---|---|---|---|
| [Expander](components/barramentos/Expander.md) | Separa um barramento em n bits | A, Y0..Y{n-1} | 3000×1200 |
| [ExpanderVertical](components/barramentos/ExpanderVertical.md) | Separa um barramento em n bits (saídas verticais) | A, Y0..Y{n-1} | 1200×4200 |
| [MergeBits](components/barramentos/MergeBits.md) | Junta n bits em um barramento | Y, A0..A{n-1} | 3000×1200 |
| [Subset](components/barramentos/Subset.md) | Extrai uma faixa de bits | A, Y | 2400×600 |

## Portas lógicas de 1 bit

| Componente | Função | Portas | Tamanho |
|---|---|---|---|
| [And2](components/portas/And2.md) | Porta AND de 2 entradas | Y, A, B | 3600×2400 |
| [And2Vertical](components/portas/And2Vertical.md) | Porta AND de 2 entradas (símbolo vertical) | Y, A, B | 2400×3600 |
| [And3](components/portas/And3.md) | Porta AND de 3 entradas | Y, A, B, C | 3600×2400 |
| [And3Vertical](components/portas/And3Vertical.md) | Porta AND de 3 entradas (símbolo vertical) | Y, A, B, C | 2400×3600 |
| [InvSmall](components/portas/InvSmall.md) | Inversor (símbolo pequeno, horizontal) | A, Y | 1800×1200 |
| [InvVertical](components/portas/InvVertical.md) | Inversor vertical (estilo DIN) | A, Y | 1200×1800 |
| [Nand2](components/portas/Nand2.md) | Porta NAND de 2 entradas | Y, A, B | 3600×2400 |
| [Nor4](components/portas/Nor4.md) | Porta NOR de 4 entradas (estilo DIN) | Y, A, B, C, D | 3600×3000 |
| [Or2](components/portas/Or2.md) | Porta OR de 2 entradas | Y, A, B | 3600×2400 |

## Lógica de redução e comparação

| Componente | Função | Portas | Tamanho |
|---|---|---|---|
| [And](components/logica-vetorial/And.md) | AND de redução (n bits → 1 bit) | A, Y | 3600×1800 |
| [CompareEqual](components/logica-vetorial/CompareEqual.md) | Comparador de igualdade | A, B, Y | 3600×1800 |
| [Nor](components/logica-vetorial/Nor.md) | NOR de redução (n bits → 1 bit) | A, Y | 3600×1800 |
| [Or](components/logica-vetorial/Or.md) | OR de redução (n bits → 1 bit) | A, Y | 3600×1800 |
| [Xor](components/logica-vetorial/Xor.md) | XOR de redução / paridade (n bits → 1 bit) | A, Y | 3600×1800 |

## Aritmética e ULAs

| Componente | Função | Portas | Tamanho |
|---|---|---|---|
| [ALU](components/aritmetica/ALU.md) | ULA do processador MicroJava | OPC, A, B, Y, CIN, COUT, ZERO, NEG, EQ, OVF | 4800×2400 |
| [Add](components/aritmetica/Add.md) | Somador de n bits | A, B, SUM | 4800×2400 |
| [DcoreALU](components/aritmetica/DcoreALU.md) | ULA do processador D*CORE | OPC, A, B, Y, CIN, COUT, IMM | 4800×2400 |
| [ShiftLeft](components/aritmetica/ShiftLeft.md) | Deslocamento lógico à esquerda (quantidade fixa) | A, Y | 3600×1800 |
| [ShiftRightLogic](components/aritmetica/ShiftRightLogic.md) | Deslocamento lógico à direita (quantidade fixa) | A, Y | 3600×1800 |
| [UserDefinedALU](components/aritmetica/UserDefinedALU.md) | ULA com mapeamento de opcodes configurável | OPC, A, B, Y, CIN, COUT, ZERO, NEG, EQ, OVF | 4800×2400 |

## Multiplexadores

| Componente | Função | Portas | Tamanho |
|---|---|---|---|
| [Mux21](components/mux/Mux21.md) | Multiplexador 2:1 de n bits | S, A1, A0, Y | 3600×1800 |
| [Mux41](components/mux/Mux41.md) | Multiplexador 4:1 de n bits | S1, S0, A3, A2, A1, A0, Y | 4800×1800 |

## Registradores

| Componente | Função | Portas | Tamanho |
|---|---|---|---|
| [RegRE](components/registradores/RegRE.md) | Registrador de n bits com enable e reset | CLK, NR, ENA, D, Q | 3600×2400 |

## Memórias e bancos de registradores

| Componente | Função | Portas | Tamanho |
|---|---|---|---|
| [MipsRegBank](components/memoria/MipsRegBank.md) | Banco de registradores MIPS (32×32) | AR0, AR1, AW0, DR0, DR1, DW0, nWE, nCS | 7200×4800 |
| [RAM](components/memoria/RAM.md) | RAM assíncrona | A, DIN, DOUT, nWE, nCS | 6000×4800 |
| [RAMoe](components/memoria/RAMoe.md) | RAM assíncrona com output-enable | A, DIN, DOUT, nWE, nCS, nOE | 6000×4800 |
| [ROM](components/memoria/ROM.md) | ROM (memória só de leitura) | A, D | 6000×4800 |
| [ROMoe](components/memoria/ROMoe.md) | ROM com chip-select e output-enable | A, D, nCS, nOE | 6000×4800 |
| [RegBank](components/memoria/RegBank.md) | Banco de registradores D*CORE | AX, AY, AZ, DX, DY, DZ, nWE, CLK | 7200×6000 |

## Blocos (subcircuitos genéricos)

| Bloco | Função |
|---|---|
| [SIGNAL_EXTENDER](blocks/README.md#signal_extender) | Extensão de sinal 16 → 32 bits: OUTPUT[15:0] = INPUT, OUTPUT[31:16] = INPUT[15]. |
| [SHIFTLEFT2](blocks/README.md#shiftleft2) | Deslocamento fixo de 2 à esquerda, 32 bits: OUTPUT = INPUT << 2. |

## Demais componentes

[`catalog/`](catalog/README.md): 384 componentes do hades.jar, parâmetros padrão.
