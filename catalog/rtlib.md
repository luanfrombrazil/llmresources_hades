# hades.models.rtlib

Gerado do hades.jar com parâmetros padrão. ✅ = doc em `components/`. Demais: documentar antes de usar (`ADICIONANDO_COMPONENTES.md`).

## Add ✅
`hades.models.rtlib.arith.Add` — n-bit adder. → [components/aritmetica/Add.md](../components/aritmetica/Add.md)
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(4800,2400)
- portas: `A` in 16b (1200,0), `B` in 16b (3600,0), `SUM` out 16b (2400,2400)

## Addc
`hades.models.rtlib.arith.Addc` — n-bit adder with carry input and output.
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(4800,2400)
- portas: `A` in 16b (1200,0), `B` in 16b (3600,0), `CIN` in 1b (4200,0), `SUM` out 16b (2400,2400), `COUT` out 1b (1800,2400)

## DcoreALU ✅
`hades.models.rtlib.arith.DcoreALU` — RTLIB n-bit ALU for the D*CORE processor. → [components/aritmetica/DcoreALU.md](../components/aritmetica/DcoreALU.md)
- params: `1001 16 1.0E-8 24 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23`; bbox (0,0)..(4800,2400)
- portas: `OPC` in 5b (0,1200), `A` in 16b (3600,0), `B` in 16b (1200,0), `Y` out 16b (2400,2400), `CIN` in 1b (4200,0), `COUT` out 1b (1800,2400), `IMM` in 4b (600,0)

## DcoreALU2
`hades.models.rtlib.arith.DcoreALU2` — RTLIB n-bit ALU for the D*CORE processor.
- params: `1001 16 1.0E-8 28 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27`; bbox (0,0)..(4800,2400)
- portas: `OPC` in 5b (0,1200), `A` in 16b (3600,0), `B` in 16b (1200,0), `Y` out 16b (2400,2400), `CIN` in 1b (4200,0), `COUT` out 1b (1800,2400), `IMM` in 4b (600,0)

## Decr
`hades.models.rtlib.arith.Decr` — n-bit decrementer.
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 16b (1800,0), `Y` out 16b (1800,1800)

## Incr
`hades.models.rtlib.arith.Incr` — n-bit incrementer.
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 16b (1800,0), `Y` out 16b (1800,1800)

## Incr2
`hades.models.rtlib.arith.Incr2` — n-bit incrementer (by two)
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 16b (1800,0), `Y` out 16b (1800,1800)

## RotateLeft
`hades.models.rtlib.arith.RotateLeft` — n-bit left rotation
- params: `1001 16 1 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (-1800,0)..(1800,1800)
- portas: `A` in 16b (0,0), `Y` out 16b (0,1800)

## RotateRight
`hades.models.rtlib.arith.RotateRight` — n-bit right rotation
- params: `1001 16 1 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (-1800,0)..(1800,1800)
- portas: `A` in 16b (0,0), `Y` out 16b (0,1800)

## ShiftLeft ✅
`hades.models.rtlib.arith.ShiftLeft` — n-bit left shift → [components/aritmetica/ShiftLeft.md](../components/aritmetica/ShiftLeft.md)
- params: `1001 16 1 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (-1800,0)..(1800,1800)
- portas: `A` in 16b (0,0), `Y` out 16b (0,1800)

## ShiftRightArith
`hades.models.rtlib.arith.ShiftRightArith` — n-bit arithmetic right shift
- params: `1001 16 1 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (-1800,0)..(1800,1800)
- portas: `A` in 16b (0,0), `Y` out 16b (0,1800)

## ShiftRightLogic ✅
`hades.models.rtlib.arith.ShiftRightLogic` — n-bit logical right shift → [components/aritmetica/ShiftRightLogic.md](../components/aritmetica/ShiftRightLogic.md)
- params: `1001 16 1 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (-1800,0)..(1800,1800)
- portas: `A` in 16b (0,0), `Y` out 16b (0,1800)

## Sub
`hades.models.rtlib.arith.Sub` — n-bit subtraction
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(4800,2400)
- portas: `A` in 16b (1200,0), `B` in 16b (3600,0), `SUM` out 16b (2400,2400)

## TwosComplement
`hades.models.rtlib.arith.TwosComplement` — n-bit two's complement
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 16b (1800,0), `Y` out 16b (1800,1800)

## UserDefinedALU ✅
`hades.models.rtlib.arith.UserDefinedALU` — n-bit user-defined arithmetic logical unit → [components/aritmetica/UserDefinedALU.md](../components/aritmetica/UserDefinedALU.md)
- params: `1001 16 1.0E-8 16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15`; bbox (0,0)..(4800,2400)
- portas: `OPC` in 4b (0,1200), `A` in 16b (1200,0), `B` in 16b (3600,0), `Y` out 16b (2400,2400), `CIN` in 1b (4200,0), `COUT` out 1b (1800,2400), `ZERO` out 1b (3000,2400), `NEG` out 1b (3300,2400), `EQ` out 1b (3600,2400), `OVF` out 1b (3900,2400)

## CompareAll
`hades.models.rtlib.compare.CompareAll` — n-bit unsigned comparison.
- params: `1001 16 U 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 1b (1200,0), `B` in 1b (2400,0), `LT` out 1b (600,1800), `LE` out 1b (1200,1800), `EQ` out 1b (1800,1800), `GE` out 1b (2400,1800), `GT` out 1b (3000,1800)

## CompareEqual ✅
`hades.models.rtlib.compare.CompareEqual` — n-bit test for equality → [components/logica-vetorial/CompareEqual.md](../components/logica-vetorial/CompareEqual.md)
- params: `1001 16 U 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 1b (1200,0), `B` in 1b (2400,0), `Y` out 1b (1800,1800)

## CompareGreater
`hades.models.rtlib.compare.CompareGreater` — n-bit test for unsigned greater-than.
- params: `1001 16 U 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 1b (1200,0), `B` in 1b (2400,0), `Y` out 1b (1800,1800)

## CompareLess
`hades.models.rtlib.compare.CompareLess` — n-bit test for unsigned less-than.
- params: `1001 16 U 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 1b (1200,0), `B` in 1b (2400,0), `Y` out 1b (1800,1800)

## CompareNotEqual
`hades.models.rtlib.compare.CompareNotEqual` — n-bit test for not-equal.
- params: `1001 16 U 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 1b (1200,0), `B` in 1b (2400,0), `Y` out 1b (1800,1800)

## BusTapBottom
`hades.models.rtlib.io.BusTapBottom` — A bus-tap oriented top-down.
- params: `1001 16 3 0 U_B 1.0E-8`; bbox (-600,-600)..(600,600)
- portas: `A` in 1b (0,0), `Y` out 1b (0,600)

## BusTapRight
`hades.models.rtlib.io.BusTapRight` — A bus-tap oriented left-right.
- params: `1001 16 3 0 U_B 1.0E-8`; bbox (-600,-600)..(600,600)
- portas: `A` in 1b (0,0), `Y` out 1b (600,0)

## Constant ✅
`hades.models.rtlib.io.Constant` — constant. → [components/io/Constant.md](../components/io/Constant.md)
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `Y` out 1b (1800,1800)

## ExpandBit
`hades.models.rtlib.io.ExpandBit` — expand a 1-bit input to n-bits (clone).
- params: `1001 16 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 1b (1800,0), `Y` out 16b (1800,1800)

## Expander ✅
`hades.models.rtlib.io.Expander` — expand an n-bit bus input to n single-bits. → [components/barramentos/Expander.md](../components/barramentos/Expander.md)
- params: `1001 16 1.0E-8`; bbox (0,0)..(10200,1200) dinâmico
- portas: `A` in 16b (600,0), `Y0` out 1b (9600,1200), `Y1` out 1b (9000,1200), `Y2` out 1b (8400,1200), `Y3` out 1b (7800,1200), `Y4` out 1b (7200,1200), `Y5` out 1b (6600,1200), `Y6` out 1b (6000,1200), `Y7` out 1b (5400,1200), `Y8` out 1b (4800,1200), `Y9` out 1b (4200,1200), `Y10` out 1b (3600,1200), `Y11` out 1b (3000,1200), `Y12` out 1b (2400,1200), `Y13` out 1b (1800,1200), `Y14` out 1b (1200,1200), `Y15` out 1b (600,1200)

## ExpanderVertical ✅
`hades.models.rtlib.io.ExpanderVertical` — expand a n-bit bus input into n single bits; the symbol's → [components/barramentos/ExpanderVertical.md](../components/barramentos/ExpanderVertical.md)
- params: `1001 16 1.0E-8`; bbox (0,0)..(1200,10200) dinâmico
- portas: `A` in 16b (600,0), `Y0` out 1b (1200,9600), `Y1` out 1b (1200,9000), `Y2` out 1b (1200,8400), `Y3` out 1b (1200,7800), `Y4` out 1b (1200,7200), `Y5` out 1b (1200,6600), `Y6` out 1b (1200,6000), `Y7` out 1b (1200,5400), `Y8` out 1b (1200,4800), `Y9` out 1b (1200,4200), `Y10` out 1b (1200,3600), `Y11` out 1b (1200,3000), `Y12` out 1b (1200,2400), `Y13` out 1b (1200,1800), `Y14` out 1b (1200,1200), `Y15` out 1b (1200,600)

## IpinVector ✅
`hades.models.rtlib.io.IpinVector` — n-bit input (interactive switch). → [components/io/IpinVector.md](../components/io/IpinVector.md)
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-9 0`; bbox (-4800,-600)..(0,600)
- portas: `Y` out 1b (0,0)

## IpinVectorLarge ✅
`hades.models.rtlib.io.IpinVectorLarge` — n-bit input (interactive switch, large symbol). → [components/io/IpinVectorLarge.md](../components/io/IpinVectorLarge.md)
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-9 0`; bbox (-14400,-600)..(0,600)
- portas: `Y` out 1b (0,0)

## Merge
`hades.models.rtlib.io.Merge` — merge two n-bit and m-bit buses into a (n+m) bit bus.
- params: `1001 16 8 8 _B 1.0E-8`; bbox (-1200,0)..(1200,600)
- portas: `A` in 1b (-600,0), `B` in 1b (600,0), `Y` out 1b (0,600)

## Merge3
`hades.models.rtlib.io.Merge3` — merge three n-bit, m-bit, k-bit buses into one (n+m+k)-bit bus.
- params: `1001 24 8 8 8 UUU_B 1.0E-8`; bbox (-1200,0)..(1200,600)
- portas: `A` in 1b (-600,0), `B` in 1b (0,0), `C` in 1b (600,0), `Y` out 3b (0,600)

## MergeBits ✅
`hades.models.rtlib.io.MergeBits` — merge n single-bit inputs into one n-bit output bus. → [components/barramentos/MergeBits.md](../components/barramentos/MergeBits.md)
- params: `1001 16 1.0E-8`; bbox (0,0)..(10200,1200) dinâmico
- portas: `Y` out 16b (600,1200), `A0` in 1b (9600,0), `A1` in 1b (9000,0), `A2` in 1b (8400,0), `A3` in 1b (7800,0), `A4` in 1b (7200,0), `A5` in 1b (6600,0), `A6` in 1b (6000,0), `A7` in 1b (5400,0), `A8` in 1b (4800,0), `A9` in 1b (4200,0), `A10` in 1b (3600,0), `A11` in 1b (3000,0), `A12` in 1b (2400,0), `A13` in 1b (1800,0), `A14` in 1b (1200,0), `A15` in 1b (600,0)

## OpinVector ✅
`hades.models.rtlib.io.OpinVector` — n-bit output connector (with display).  → [components/io/OpinVector.md](../components/io/OpinVector.md)
- params: `1001 16 1.0E-9 0`; bbox (0,-600)..(4800,600)
- portas: `A` in 1b (0,0), `i0` out 1b

## OpinVectorLarge
`hades.models.rtlib.io.OpinVectorLarge` — n-bit output connector (with display, large symbol).
- params: `1001 16 1.0E-9 0`; bbox (0,-600)..(14400,600)
- portas: `A` in 1b (0,0), `i0` out 1b

## SelectBit
`hades.models.rtlib.io.SelectBit` — select one bit from an n-bit bus.
- params: `1001 16 0 1.0E-8`; bbox (-1200,0)..(1200,600)
- portas: `A` in 1b (0,0), `Y` out 1b (0,600)

## SmallConstant ✅
`hades.models.rtlib.io.SmallConstant` — constant (small symbol). → [components/io/SmallConstant.md](../components/io/SmallConstant.md)
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(1200,1200)
- portas: `Y` out 1b (600,1200)

## Subset ✅
`hades.models.rtlib.io.Subset` — extract a subset of m-bits from an n-bit input bus. → [components/barramentos/Subset.md](../components/barramentos/Subset.md)
- params: `1001 16 3 0 U_B 1.0E-8`; bbox (-1200,0)..(1200,600)
- portas: `A` in 1b (0,0), `Y` out 1b (0,600)

## SubsetFlip
`hades.models.rtlib.io.SubsetFlip` — extract a subset of m-bits from an n-bit input bus;
- params: `1001 16 3 0 U_B 1.0E-8`; bbox (-1200,0)..(1200,600)
- portas: `A` in 1b (0,0), `Y` out 1b (0,600)

## And ✅
`hades.models.rtlib.logic.And` — n-bit to 1-bit logical AND. → [components/logica-vetorial/And.md](../components/logica-vetorial/And.md)
- params: `1001 16 U 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 1b (1800,0), `Y` out 1b (1800,1800)

## BitwiseAnd
`hades.models.rtlib.logic.BitwiseAnd` — n-bit bitwise logical AND.
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 16b (1200,0), `B` in 16b (2400,0), `Y` out 16b (1800,1800)

## BitwiseOr
`hades.models.rtlib.logic.BitwiseOr` — n-bit bitwise logical OR.
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 16b (1200,0), `B` in 16b (2400,0), `Y` out 16b (1800,1800)

## BitwiseXor
`hades.models.rtlib.logic.BitwiseXor` — n-bit bitwise logical XOR.
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 16b (1200,0), `B` in 16b (2400,0), `Y` out 16b (1800,1800)

## N1And
`hades.models.rtlib.logic.N1And` — n-bit logical AND with 1-bit signal.
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 1b (1200,0), `B` in 16b (2400,0), `Y` out 16b (1800,1800)

## N1Or
`hades.models.rtlib.logic.N1Or` — n-bit logical OR with 1-bit signal.
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(1200,1800)
- portas: `A` in 1b (0,600), `B` in 16b (600,0), `Y` out 16b (600,1800)

## Nand
`hades.models.rtlib.logic.Nand` — NOT-AND of n-bit input.
- params: `1001 16 U 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 1b (1800,0), `Y` out 1b (1800,1800)

## Nor ✅
`hades.models.rtlib.logic.Nor` — NOT-OR of n-bit input. → [components/logica-vetorial/Nor.md](../components/logica-vetorial/Nor.md)
- params: `1001 16 U 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 1b (1800,0), `Y` out 1b (1800,1800)

## Or ✅
`hades.models.rtlib.logic.Or` — OR of n-bit input. → [components/logica-vetorial/Or.md](../components/logica-vetorial/Or.md)
- params: `1001 16 U 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 1b (1800,0), `Y` out 1b (1800,1800)

## Xnor
`hades.models.rtlib.logic.Xnor` — NOT-XOR of n-bit input (parity).
- params: `1001 16 U 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 1b (1800,0), `Y` out 1b (1800,1800)

## Xor ✅
`hades.models.rtlib.logic.Xor` — XOR of n-bit input (parity). → [components/logica-vetorial/Xor.md](../components/logica-vetorial/Xor.md)
- params: `1001 16 U 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 1b (1800,0), `Y` out 1b (1800,1800)

## AddressDecoder4
`hades.models.rtlib.memory.AddressDecoder4` — generic address decoder with four user-defined address ranges.
- params: `1001 16 1.0E-8 0 0 0 0 0 0 0 0`; bbox (0,0)..(3600,1800)
- portas: `A` in 16b (1800,0), `nCS0` out 1b (600,1800), `nCS1` out 1b (1200,1800), `nCS2` out 1b (1800,1800), `nCS3` out 1b (2400,1800)

## DPRAM
`hades.models.rtlib.memory.DPRAM` — dual-port memory with one write and two read ports.
- params: `1001 16 16`; bbox (0,0)..(7200,4800)
- portas: `A0` in 4b (0,2400), `A1` in 4b (7200,2400), `DI0` in 16b (2400,0), `DO0` out 16b (2400,4800), `DO1` out 16b (4800,4800), `nWE` in 1b (0,3000), `nCS` in 1b (0,1800)

## MR
`hades.models.rtlib.memory.MR` — microcode-rom with 256 words of 8+8+2+16 outputs.
- params: `1001 16 16`; bbox (0,0)..(18000,6000)
- portas: `D0` out 1b (15600,6000), `D1` out 1b (15000,6000), `D2` out 1b (14400,6000), `D3` out 1b (13800,6000), `D4` out 1b (13200,6000), `D5` out 1b (12600,6000), `D6` out 1b (12000,6000), `D7` out 1b (11400,6000), `D8` out 1b (10200,6000), `D9` out 1b (9600,6000), `D10` out 1b (9000,6000), `D11` out 1b (8400,6000), `D12` out 1b (7800,6000), `D13` out 1b (7200,6000), `D14` out 1b (6600,6000), `D15` out 1b (6000,6000), `X` out 8b (4200,6000), `Y` out 8b (4800,6000), `S1` out 1b (2400,6000), `S0` out 1b (3000,6000), `A` in 8b (0,3000), `STATE` out 1b (16800,6000)

## MR20
`hades.models.rtlib.memory.MR20` — microcode-rom with 256 words of 8+8+2+20 outputs.
- params: `1001 16 16`; bbox (0,0)..(21000,6000)
- portas: `D0` out 1b (18600,6000), `D1` out 1b (18000,6000), `D2` out 1b (17400,6000), `D3` out 1b (16800,6000), `D4` out 1b (16200,6000), `D5` out 1b (15600,6000), `D6` out 1b (15000,6000), `D7` out 1b (14400,6000), `D8` out 1b (13200,6000), `D9` out 1b (12600,6000), `D10` out 1b (12000,6000), `D11` out 1b (11400,6000), `D12` out 1b (10800,6000), `D13` out 1b (10200,6000), `D14` out 1b (9600,6000), `D15` out 1b (9000,6000), `D16` out 1b (7800,6000), `D17` out 1b (7200,6000), `D18` out 1b (6600,6000), `D19` out 1b (6000,6000), `X` out 8b (4200,6000), `Y` out 8b (4800,6000), `S1` out 1b (2400,6000), `S0` out 1b (3000,6000), `A` in 8b (0,3000), `STATE` out 1b (19800,6000)

## MicroROM
`hades.models.rtlib.memory.MicroROM` — microcode-rom with 1024 words of 12+4+4+4+4+16 outputs.
- params: `1001 4096 44`; bbox (0,0)..(18000,4800)
- portas: `D0` out 1b (17400,4800), `D1` out 1b (16800,4800), `D2` out 1b (16200,4800), `D3` out 1b (15600,4800), `D4` out 1b (15000,4800), `D5` out 1b (14400,4800), `D6` out 1b (13800,4800), `D7` out 1b (13200,4800), `D8` out 1b (12000,4800), `D9` out 1b (11400,4800), `D10` out 1b (10800,4800), `D11` out 1b (10200,4800), `D12` out 1b (9600,4800), `D13` out 1b (9000,4800), `D14` out 1b (8400,4800), `D15` out 1b (7800,4800), `E` out 4b (6000,4800), `F` out 4b (5400,4800), `G` out 4b (4800,4800), `H` out 4b (4200,4800), `X` out 12b (2400,4800), `A` in 12b (0,2400)

## MipsRegBank ✅
`hades.models.rtlib.memory.MipsRegBank` — register bank of the MIPS R2K/R3K processors. → [components/memoria/MipsRegBank.md](../components/memoria/MipsRegBank.md)
- params: `1001 32 32`; bbox (0,0)..(7200,4800)
- portas: `AR0` in 5b (0,3000), `AR1` in 5b (0,3600), `AW0` in 5b (0,2400), `DR0` out 32b (2400,4800), `DR1` out 32b (4800,4800), `DW0` in 32b (2400,0), `nWE` in 1b (0,1800), `nCS` in 1b (0,1200)

## RAM ✅
`hades.models.rtlib.memory.RAM` — random-access memory with separate read and write ports. → [components/memoria/RAM.md](../components/memoria/RAM.md)
- params: `1001 16 16`; bbox (0,0)..(6000,4800)
- portas: `A` in 4b (0,2400), `DIN` in 16b (3600,0), `DOUT` out 16b (3600,4800), `nWE` in 1b (0,3000), `nCS` in 1b (0,1800)

## RAMoe ✅
`hades.models.rtlib.memory.RAMoe` — random-access memory with separate read and write ports. → [components/memoria/RAMoe.md](../components/memoria/RAMoe.md)
- params: `1001 16 16`; bbox (0,0)..(6000,4800)
- portas: `A` in 4b (0,2400), `DIN` in 16b (3600,0), `DOUT` out 16b (3600,4800), `nWE` in 1b (0,3000), `nCS` in 1b (0,1800), `nOE` in 1b (0,3600)

## ROM ✅
`hades.models.rtlib.memory.ROM` — read-only memory. → [components/memoria/ROM.md](../components/memoria/ROM.md)
- params: `1001 16 16`; bbox (0,0)..(6000,4800)
- portas: `A` in 4b (0,2400), `D` out 16b (3600,4800)

## ROMcs
`hades.models.rtlib.memory.ROMcs` — read-only memory with tri-state output.
- params: `1001 16 16`; bbox (0,0)..(6000,4800)
- portas: `A` in 4b (0,2400), `D` out 16b (3600,4800), `nCS` in 1b (0,1800)

## ROMoe ✅
`hades.models.rtlib.memory.ROMoe` — read-only memory with output-enable input. → [components/memoria/ROMoe.md](../components/memoria/ROMoe.md)
- params: `1001 16 16`; bbox (0,0)..(6000,4800)
- portas: `A` in 4b (0,2400), `D` out 16b (3600,4800), `nCS` in 1b (0,1800), `nOE` in 1b (0,3000)

## RealTimeClock
`hades.models.rtlib.memory.RealTimeClock` — RealTimeClock - a generic real-time clock with RAM-like addressing
- params: `1001 8 16`; bbox (0,0)..(6000,3000)
- portas: `A` in 3b (0,1200), `DIN` in 16b (3000,0), `DOUT` out 16b (3000,3000), `nWE` in 1b (0,1800), `nCS` in 1b (0,600), `nOE` in 1b (0,2400)

## RegBank ✅
`hades.models.rtlib.memory.RegBank` — register bank for the D*CORE processor. → [components/memoria/RegBank.md](../components/memoria/RegBank.md)
- params: `1001 16 16`; bbox (0,0)..(7200,6000)
- portas: `AX` in 4b (0,3000), `AY` in 4b (0,3600), `AZ` in 4b (0,4200), `DX` out 16b (4800,6000), `DY` out 16b (2400,6000), `DZ` in 16b (4800,0), `nWE` in 1b (0,2400), `CLK` in 1b (0,1800)

## BitDecoder
`hades.models.rtlib.muxes.BitDecoder` — n-to-2^n decoder. 
- params: `1001 5 1.0E-8`; bbox (0,0)..(19800,1200) dinâmico
- portas: `A` in 5b (600,0), `Y0` out 1b (19200,1200), `Y1` out 1b (18600,1200), `Y2` out 1b (18000,1200), `Y3` out 1b (17400,1200), `Y4` out 1b (16800,1200), `Y5` out 1b (16200,1200), `Y6` out 1b (15600,1200), `Y7` out 1b (15000,1200), `Y8` out 1b (14400,1200), `Y9` out 1b (13800,1200), `Y10` out 1b (13200,1200), `Y11` out 1b (12600,1200), `Y12` out 1b (12000,1200), `Y13` out 1b (11400,1200), `Y14` out 1b (10800,1200), `Y15` out 1b (10200,1200), `Y16` out 1b (9600,1200), `Y17` out 1b (9000,1200), `Y18` out 1b (8400,1200), `Y19` out 1b (7800,1200), `Y20` out 1b (7200,1200), `Y21` out 1b (6600,1200), `Y22` out 1b (6000,1200), `Y23` out 1b (5400,1200), `Y24` out 1b (4800,1200), `Y25` out 1b (4200,1200), `Y26` out 1b (3600,1200), `Y27` out 1b (3000,1200), `Y28` out 1b (2400,1200), `Y29` out 1b (1800,1200), `Y30` out 1b (1200,1200), `Y31` out 1b (600,1200)

## Decoder
`hades.models.rtlib.muxes.Decoder` — n-to-2^n decoder. 
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `A` in 16b (1800,0), `Y` out 65536b (1800,1800)

## Mux21 ✅
`hades.models.rtlib.muxes.Mux21` — 2:1 n-bit multiplexer (with animation). → [components/mux/Mux21.md](../components/mux/Mux21.md)
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,1800)
- portas: `S` in 1b (0,1200), `A1` in 16b (1200,0), `A0` in 16b (2400,0), `Y` out 16b (1800,1800)

## Mux41 ✅
`hades.models.rtlib.muxes.Mux41` — 4:1 n-bit multiplexer. → [components/mux/Mux41.md](../components/mux/Mux41.md)
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(4800,1800)
- portas: `S1` in 1b (0,600), `S0` in 1b (0,1200), `A3` in 16b (600,0), `A2` in 16b (1800,0), `A1` in 16b (3000,0), `A0` in 16b (4200,0), `Y` out 16b (2400,1800)

## TriBuf
`hades.models.rtlib.muxes.TriBuf` — n-bit tri-state buffer.
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(1200,1200)
- portas: `A` in 16b (600,0), `S` in 1b (0,600), `Y` out 16b (600,1200)

## TriBufBig
`hades.models.rtlib.muxes.TriBufBig` — n-bit tri-state buffer (big symbol).
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(1800,1800)
- portas: `A` in 16b (900,0), `S` in 1b (0,1200), `Y` out 16b (900,1800)

## CounterRE
`hades.models.rtlib.register.CounterRE` — n-bit positive edge-triggered counter with reset and enable.
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `CLK` in 1b (0,1200), `NR` in 1b (0,1800), `ENA` in 1b (0,600), `Q` out 16b (1800,2400)

## LFSR
`hades.models.rtlib.register.LFSR` — positive edge-triggered linear feedback shift register,
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8 13755891`; bbox (0,0)..(3600,2400)
- portas: `CLK` in 1b (0,1200), `NR` in 1b (0,1800), `Q` out 16b (1800,2400)

## Latch
`hades.models.rtlib.register.Latch` — n-bit latch.
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `CLK` in 1b (0,1200), `D` in 16b (1800,0), `Q` out 16b (1800,2400)

## LatchR
`hades.models.rtlib.register.LatchR` — n-bit latch with asynchronous reset.
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `CLK` in 1b (0,1200), `NR` in 1b (0,1800), `D` in 16b (1800,0), `Q` out 16b (1800,2400)

## Reg
`hades.models.rtlib.register.Reg` — n-bit positive edge-triggered D-type register.
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `CLK` in 1b (0,1200), `D` in 16b (1800,0), `Q` out 16b (1800,2400)

## RegE
`hades.models.rtlib.register.RegE` — n-bit positive edge-triggered D-type register with enable.
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `CLK` in 1b (0,1200), `ENA` in 1b (0,600), `D` in 16b (1800,0), `Q` out 16b (1800,2400)

## RegR
`hades.models.rtlib.register.RegR` — n-bit positive edge-triggered D-type register with reset.
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `CLK` in 1b (0,1200), `NR` in 1b (0,1800), `D` in 16b (1800,0), `Q` out 16b (1800,2400)

## RegRE ✅
`hades.models.rtlib.register.RegRE` — n-bit positive edge-triggered D-type register with reset → [components/registradores/RegRE.md](../components/registradores/RegRE.md)
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `CLK` in 1b (0,1200), `NR` in 1b (0,1800), `ENA` in 1b (0,600), `D` in 16b (1800,0), `Q` out 16b (1800,2400)

## RegWithInitialValue
`hades.models.rtlib.register.RegWithInitialValue` — n-bit positive edge-triggered D-type register with
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `CLK` in 1b (0,1200), `D` in 16b (1800,0), `Q` out 16b (1800,2400)

## ShiftRegR
`hades.models.rtlib.register.ShiftRegR` — n-bit positive edge-triggered D-type or shift register.
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(4800,2400)
- portas: `CLK` in 1b (0,1200), `NR` in 1b (0,1800), `ENA` in 1b (0,600), `SIN` in 1b (1200,0), `SOUT` out 1b (3600,2400), `D` in 16b (2400,0), `Q` out 16b (2400,2400)
