# Catálogo HADES — pacote `hades.models.rtlib`

Gerado automaticamente a partir do `hades.jar` (parâmetros PADRÃO). Componentes marcados com ✅ têm documentação detalhada em `components/`.
Para os demais: portas, posições e bbox valem para os parâmetros padrão; componentes de largura variável mudam com `n_bits`. Antes de usar um deles pela primeira vez, documente-o (veja `ADICIONANDO_COMPONENTES.md`).

## Add ✅

`hades.models.rtlib.arith.Add` — n-bit adder.

Doc detalhada: [components/aritmetica/Add.md](../components/aritmetica/Add.md)

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(4800, 2400)
- Portas: `A` in 16b @(1200,0), `B` in 16b @(3600,0), `SUM` out 16b @(2400,2400)

## Addc

`hades.models.rtlib.arith.Addc` — n-bit adder with carry input and output.

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(4800, 2400)
- Portas: `A` in 16b @(1200,0), `B` in 16b @(3600,0), `CIN` in 1b @(4200,0), `SUM` out 16b @(2400,2400), `COUT` out 1b @(1800,2400)

## DcoreALU ✅

`hades.models.rtlib.arith.DcoreALU` — RTLIB n-bit ALU for the D*CORE processor.

Doc detalhada: [components/aritmetica/DcoreALU.md](../components/aritmetica/DcoreALU.md)

- Parâmetros padrão: `1001 16 1.0E-8 24 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23`
- bbox: (0, 0)..(4800, 2400)
- Portas: `OPC` in 5b @(0,1200), `A` in 16b @(3600,0), `B` in 16b @(1200,0), `Y` out 16b @(2400,2400), `CIN` in 1b @(4200,0), `COUT` out 1b @(1800,2400), `IMM` in 4b @(600,0)

## DcoreALU2

`hades.models.rtlib.arith.DcoreALU2` — RTLIB n-bit ALU for the D*CORE processor.

- Parâmetros padrão: `1001 16 1.0E-8 28 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27`
- bbox: (0, 0)..(4800, 2400)
- Portas: `OPC` in 5b @(0,1200), `A` in 16b @(3600,0), `B` in 16b @(1200,0), `Y` out 16b @(2400,2400), `CIN` in 1b @(4200,0), `COUT` out 1b @(1800,2400), `IMM` in 4b @(600,0)

## Decr

`hades.models.rtlib.arith.Decr` — n-bit decrementer.

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 16b @(1800,0), `Y` out 16b @(1800,1800)

## Incr

`hades.models.rtlib.arith.Incr` — n-bit incrementer.

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 16b @(1800,0), `Y` out 16b @(1800,1800)

## Incr2

`hades.models.rtlib.arith.Incr2` — n-bit incrementer (by two)

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 16b @(1800,0), `Y` out 16b @(1800,1800)

## RotateLeft

`hades.models.rtlib.arith.RotateLeft` — n-bit left rotation

- Parâmetros padrão: `1001 16 1 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (-1800, 0)..(1800, 1800)
- Portas: `A` in 16b @(0,0), `Y` out 16b @(0,1800)

## RotateRight

`hades.models.rtlib.arith.RotateRight` — n-bit right rotation

- Parâmetros padrão: `1001 16 1 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (-1800, 0)..(1800, 1800)
- Portas: `A` in 16b @(0,0), `Y` out 16b @(0,1800)

## ShiftLeft ✅

`hades.models.rtlib.arith.ShiftLeft` — n-bit left shift

Doc detalhada: [components/aritmetica/ShiftLeft.md](../components/aritmetica/ShiftLeft.md)

- Parâmetros padrão: `1001 16 1 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (-1800, 0)..(1800, 1800)
- Portas: `A` in 16b @(0,0), `Y` out 16b @(0,1800)

## ShiftRightArith

`hades.models.rtlib.arith.ShiftRightArith` — n-bit arithmetic right shift

- Parâmetros padrão: `1001 16 1 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (-1800, 0)..(1800, 1800)
- Portas: `A` in 16b @(0,0), `Y` out 16b @(0,1800)

## ShiftRightLogic ✅

`hades.models.rtlib.arith.ShiftRightLogic` — n-bit logical right shift

Doc detalhada: [components/aritmetica/ShiftRightLogic.md](../components/aritmetica/ShiftRightLogic.md)

- Parâmetros padrão: `1001 16 1 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (-1800, 0)..(1800, 1800)
- Portas: `A` in 16b @(0,0), `Y` out 16b @(0,1800)

## Sub

`hades.models.rtlib.arith.Sub` — n-bit subtraction

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(4800, 2400)
- Portas: `A` in 16b @(1200,0), `B` in 16b @(3600,0), `SUM` out 16b @(2400,2400)

## TwosComplement

`hades.models.rtlib.arith.TwosComplement` — n-bit two's complement

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 16b @(1800,0), `Y` out 16b @(1800,1800)

## UserDefinedALU ✅

`hades.models.rtlib.arith.UserDefinedALU` — n-bit user-defined arithmetic logical unit

Doc detalhada: [components/aritmetica/UserDefinedALU.md](../components/aritmetica/UserDefinedALU.md)

- Parâmetros padrão: `1001 16 1.0E-8 16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15`
- bbox: (0, 0)..(4800, 2400)
- Portas: `OPC` in 4b @(0,1200), `A` in 16b @(1200,0), `B` in 16b @(3600,0), `Y` out 16b @(2400,2400), `CIN` in 1b @(4200,0), `COUT` out 1b @(1800,2400), `ZERO` out 1b @(3000,2400), `NEG` out 1b @(3300,2400), `EQ` out 1b @(3600,2400), `OVF` out 1b @(3900,2400)

## CompareAll

`hades.models.rtlib.compare.CompareAll` — n-bit unsigned comparison.

- Parâmetros padrão: `1001 16 U 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 1b @(1200,0), `B` in 1b @(2400,0), `LT` out 1b @(600,1800), `LE` out 1b @(1200,1800), `EQ` out 1b @(1800,1800), `GE` out 1b @(2400,1800), `GT` out 1b @(3000,1800)

## CompareEqual ✅

`hades.models.rtlib.compare.CompareEqual` — n-bit test for equality

Doc detalhada: [components/logica-vetorial/CompareEqual.md](../components/logica-vetorial/CompareEqual.md)

- Parâmetros padrão: `1001 16 U 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 1b @(1200,0), `B` in 1b @(2400,0), `Y` out 1b @(1800,1800)

## CompareGreater

`hades.models.rtlib.compare.CompareGreater` — n-bit test for unsigned greater-than.

- Parâmetros padrão: `1001 16 U 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 1b @(1200,0), `B` in 1b @(2400,0), `Y` out 1b @(1800,1800)

## CompareLess

`hades.models.rtlib.compare.CompareLess` — n-bit test for unsigned less-than.

- Parâmetros padrão: `1001 16 U 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 1b @(1200,0), `B` in 1b @(2400,0), `Y` out 1b @(1800,1800)

## CompareNotEqual

`hades.models.rtlib.compare.CompareNotEqual` — n-bit test for not-equal.

- Parâmetros padrão: `1001 16 U 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 1b @(1200,0), `B` in 1b @(2400,0), `Y` out 1b @(1800,1800)

## BusTapBottom

`hades.models.rtlib.io.BusTapBottom` — A bus-tap oriented top-down.

- Parâmetros padrão: `1001 16 3 0 U_B 1.0E-8`
- bbox: (-600, -600)..(600, 600)
- Portas: `A` in 1b @(0,0), `Y` out 1b @(0,600)

## BusTapRight

`hades.models.rtlib.io.BusTapRight` — A bus-tap oriented left-right.

- Parâmetros padrão: `1001 16 3 0 U_B 1.0E-8`
- bbox: (-600, -600)..(600, 600)
- Portas: `A` in 1b @(0,0), `Y` out 1b @(600,0)

## Constant ✅

`hades.models.rtlib.io.Constant` — constant.

Doc detalhada: [components/io/Constant.md](../components/io/Constant.md)

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `Y` out 1b @(1800,1800)

## ExpandBit

`hades.models.rtlib.io.ExpandBit` — expand a 1-bit input to n-bits (clone).

- Parâmetros padrão: `1001 16 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 1b @(1800,0), `Y` out 16b @(1800,1800)

## Expander ✅

`hades.models.rtlib.io.Expander` — expand an n-bit bus input to n single-bits.

Doc detalhada: [components/barramentos/Expander.md](../components/barramentos/Expander.md)

- Parâmetros padrão: `1001 16 1.0E-8`
- bbox: (0, 0)..(10200, 1200) (dinâmico)
- Portas: `A` in 16b @(600,0), `Y0` out 1b @(9600,1200), `Y1` out 1b @(9000,1200), `Y2` out 1b @(8400,1200), `Y3` out 1b @(7800,1200), `Y4` out 1b @(7200,1200), `Y5` out 1b @(6600,1200), `Y6` out 1b @(6000,1200), `Y7` out 1b @(5400,1200), `Y8` out 1b @(4800,1200), `Y9` out 1b @(4200,1200), `Y10` out 1b @(3600,1200), `Y11` out 1b @(3000,1200), `Y12` out 1b @(2400,1200), `Y13` out 1b @(1800,1200), `Y14` out 1b @(1200,1200), `Y15` out 1b @(600,1200)

## ExpanderVertical ✅

`hades.models.rtlib.io.ExpanderVertical` — expand a n-bit bus input into n single bits; the symbol's

Doc detalhada: [components/barramentos/ExpanderVertical.md](../components/barramentos/ExpanderVertical.md)

- Parâmetros padrão: `1001 16 1.0E-8`
- bbox: (0, 0)..(1200, 10200) (dinâmico)
- Portas: `A` in 16b @(600,0), `Y0` out 1b @(1200,9600), `Y1` out 1b @(1200,9000), `Y2` out 1b @(1200,8400), `Y3` out 1b @(1200,7800), `Y4` out 1b @(1200,7200), `Y5` out 1b @(1200,6600), `Y6` out 1b @(1200,6000), `Y7` out 1b @(1200,5400), `Y8` out 1b @(1200,4800), `Y9` out 1b @(1200,4200), `Y10` out 1b @(1200,3600), `Y11` out 1b @(1200,3000), `Y12` out 1b @(1200,2400), `Y13` out 1b @(1200,1800), `Y14` out 1b @(1200,1200), `Y15` out 1b @(1200,600)

## IpinVector ✅

`hades.models.rtlib.io.IpinVector` — n-bit input (interactive switch).

Doc detalhada: [components/io/IpinVector.md](../components/io/IpinVector.md)

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-9 0`
- bbox: (-4800, -600)..(0, 600)
- Portas: `Y` out 1b @(0,0)

## IpinVectorLarge ✅

`hades.models.rtlib.io.IpinVectorLarge` — n-bit input (interactive switch, large symbol).

Doc detalhada: [components/io/IpinVectorLarge.md](../components/io/IpinVectorLarge.md)

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-9 0`
- bbox: (-14400, -600)..(0, 600)
- Portas: `Y` out 1b @(0,0)

## Merge

`hades.models.rtlib.io.Merge` — merge two n-bit and m-bit buses into a (n+m) bit bus.

- Parâmetros padrão: `1001 16 8 8 _B 1.0E-8`
- bbox: (-1200, 0)..(1200, 600)
- Portas: `A` in 1b @(-600,0), `B` in 1b @(600,0), `Y` out 1b @(0,600)

## Merge3

`hades.models.rtlib.io.Merge3` — merge three n-bit, m-bit, k-bit buses into one (n+m+k)-bit bus.

- Parâmetros padrão: `1001 24 8 8 8 UUU_B 1.0E-8`
- bbox: (-1200, 0)..(1200, 600)
- Portas: `A` in 1b @(-600,0), `B` in 1b @(0,0), `C` in 1b @(600,0), `Y` out 3b @(0,600)

## MergeBits ✅

`hades.models.rtlib.io.MergeBits` — merge n single-bit inputs into one n-bit output bus.

Doc detalhada: [components/barramentos/MergeBits.md](../components/barramentos/MergeBits.md)

- Parâmetros padrão: `1001 16 1.0E-8`
- bbox: (0, 0)..(10200, 1200) (dinâmico)
- Portas: `Y` out 16b @(600,1200), `A0` in 1b @(9600,0), `A1` in 1b @(9000,0), `A2` in 1b @(8400,0), `A3` in 1b @(7800,0), `A4` in 1b @(7200,0), `A5` in 1b @(6600,0), `A6` in 1b @(6000,0), `A7` in 1b @(5400,0), `A8` in 1b @(4800,0), `A9` in 1b @(4200,0), `A10` in 1b @(3600,0), `A11` in 1b @(3000,0), `A12` in 1b @(2400,0), `A13` in 1b @(1800,0), `A14` in 1b @(1200,0), `A15` in 1b @(600,0)

## OpinVector ✅

`hades.models.rtlib.io.OpinVector` — n-bit output connector (with display). 

Doc detalhada: [components/io/OpinVector.md](../components/io/OpinVector.md)

- Parâmetros padrão: `1001 16 1.0E-9 0`
- bbox: (0, -600)..(4800, 600)
- Portas: `A` in 1b @(0,0), `i0` out 1b (sem posição)

## OpinVectorLarge

`hades.models.rtlib.io.OpinVectorLarge` — n-bit output connector (with display, large symbol).

- Parâmetros padrão: `1001 16 1.0E-9 0`
- bbox: (0, -600)..(14400, 600)
- Portas: `A` in 1b @(0,0), `i0` out 1b (sem posição)

## SelectBit

`hades.models.rtlib.io.SelectBit` — select one bit from an n-bit bus.

- Parâmetros padrão: `1001 16 0 1.0E-8`
- bbox: (-1200, 0)..(1200, 600)
- Portas: `A` in 1b @(0,0), `Y` out 1b @(0,600)

## SmallConstant ✅

`hades.models.rtlib.io.SmallConstant` — constant (small symbol).

Doc detalhada: [components/io/SmallConstant.md](../components/io/SmallConstant.md)

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(1200, 1200)
- Portas: `Y` out 1b @(600,1200)

## Subset ✅

`hades.models.rtlib.io.Subset` — extract a subset of m-bits from an n-bit input bus.

Doc detalhada: [components/barramentos/Subset.md](../components/barramentos/Subset.md)

- Parâmetros padrão: `1001 16 3 0 U_B 1.0E-8`
- bbox: (-1200, 0)..(1200, 600)
- Portas: `A` in 1b @(0,0), `Y` out 1b @(0,600)

## SubsetFlip

`hades.models.rtlib.io.SubsetFlip` — extract a subset of m-bits from an n-bit input bus;

- Parâmetros padrão: `1001 16 3 0 U_B 1.0E-8`
- bbox: (-1200, 0)..(1200, 600)
- Portas: `A` in 1b @(0,0), `Y` out 1b @(0,600)

## And ✅

`hades.models.rtlib.logic.And` — n-bit to 1-bit logical AND.

Doc detalhada: [components/logica-vetorial/And.md](../components/logica-vetorial/And.md)

- Parâmetros padrão: `1001 16 U 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 1b @(1800,0), `Y` out 1b @(1800,1800)

## BitwiseAnd

`hades.models.rtlib.logic.BitwiseAnd` — n-bit bitwise logical AND.

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 16b @(1200,0), `B` in 16b @(2400,0), `Y` out 16b @(1800,1800)

## BitwiseOr

`hades.models.rtlib.logic.BitwiseOr` — n-bit bitwise logical OR.

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 16b @(1200,0), `B` in 16b @(2400,0), `Y` out 16b @(1800,1800)

## BitwiseXor

`hades.models.rtlib.logic.BitwiseXor` — n-bit bitwise logical XOR.

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 16b @(1200,0), `B` in 16b @(2400,0), `Y` out 16b @(1800,1800)

## N1And

`hades.models.rtlib.logic.N1And` — n-bit logical AND with 1-bit signal.

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 1b @(1200,0), `B` in 16b @(2400,0), `Y` out 16b @(1800,1800)

## N1Or

`hades.models.rtlib.logic.N1Or` — n-bit logical OR with 1-bit signal.

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(1200, 1800)
- Portas: `A` in 1b @(0,600), `B` in 16b @(600,0), `Y` out 16b @(600,1800)

## Nand

`hades.models.rtlib.logic.Nand` — NOT-AND of n-bit input.

- Parâmetros padrão: `1001 16 U 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 1b @(1800,0), `Y` out 1b @(1800,1800)

## Nor ✅

`hades.models.rtlib.logic.Nor` — NOT-OR of n-bit input.

Doc detalhada: [components/logica-vetorial/Nor.md](../components/logica-vetorial/Nor.md)

- Parâmetros padrão: `1001 16 U 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 1b @(1800,0), `Y` out 1b @(1800,1800)

## Or ✅

`hades.models.rtlib.logic.Or` — OR of n-bit input.

Doc detalhada: [components/logica-vetorial/Or.md](../components/logica-vetorial/Or.md)

- Parâmetros padrão: `1001 16 U 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 1b @(1800,0), `Y` out 1b @(1800,1800)

## Xnor

`hades.models.rtlib.logic.Xnor` — NOT-XOR of n-bit input (parity).

- Parâmetros padrão: `1001 16 U 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 1b @(1800,0), `Y` out 1b @(1800,1800)

## Xor ✅

`hades.models.rtlib.logic.Xor` — XOR of n-bit input (parity).

Doc detalhada: [components/logica-vetorial/Xor.md](../components/logica-vetorial/Xor.md)

- Parâmetros padrão: `1001 16 U 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 1b @(1800,0), `Y` out 1b @(1800,1800)

## AddressDecoder4

`hades.models.rtlib.memory.AddressDecoder4` — generic address decoder with four user-defined address ranges.

- Parâmetros padrão: `1001 16 1.0E-8 0 0 0 0 0 0 0 0`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 16b @(1800,0), `nCS0` out 1b @(600,1800), `nCS1` out 1b @(1200,1800), `nCS2` out 1b @(1800,1800), `nCS3` out 1b @(2400,1800)

## DPRAM

`hades.models.rtlib.memory.DPRAM` — dual-port memory with one write and two read ports.

- Parâmetros padrão: `1001 16 16`
- bbox: (0, 0)..(7200, 4800)
- Portas: `A0` in 4b @(0,2400), `A1` in 4b @(7200,2400), `DI0` in 16b @(2400,0), `DO0` out 16b @(2400,4800), `DO1` out 16b @(4800,4800), `nWE` in 1b @(0,3000), `nCS` in 1b @(0,1800)

## MR

`hades.models.rtlib.memory.MR` — microcode-rom with 256 words of 8+8+2+16 outputs.

- Parâmetros padrão: `1001 16 16`
- bbox: (0, 0)..(18000, 6000)
- Portas: `D0` out 1b @(15600,6000), `D1` out 1b @(15000,6000), `D2` out 1b @(14400,6000), `D3` out 1b @(13800,6000), `D4` out 1b @(13200,6000), `D5` out 1b @(12600,6000), `D6` out 1b @(12000,6000), `D7` out 1b @(11400,6000), `D8` out 1b @(10200,6000), `D9` out 1b @(9600,6000), `D10` out 1b @(9000,6000), `D11` out 1b @(8400,6000), `D12` out 1b @(7800,6000), `D13` out 1b @(7200,6000), `D14` out 1b @(6600,6000), `D15` out 1b @(6000,6000), `X` out 8b @(4200,6000), `Y` out 8b @(4800,6000), `S1` out 1b @(2400,6000), `S0` out 1b @(3000,6000), `A` in 8b @(0,3000), `STATE` out 1b @(16800,6000)

## MR20

`hades.models.rtlib.memory.MR20` — microcode-rom with 256 words of 8+8+2+20 outputs.

- Parâmetros padrão: `1001 16 16`
- bbox: (0, 0)..(21000, 6000)
- Portas: `D0` out 1b @(18600,6000), `D1` out 1b @(18000,6000), `D2` out 1b @(17400,6000), `D3` out 1b @(16800,6000), `D4` out 1b @(16200,6000), `D5` out 1b @(15600,6000), `D6` out 1b @(15000,6000), `D7` out 1b @(14400,6000), `D8` out 1b @(13200,6000), `D9` out 1b @(12600,6000), `D10` out 1b @(12000,6000), `D11` out 1b @(11400,6000), `D12` out 1b @(10800,6000), `D13` out 1b @(10200,6000), `D14` out 1b @(9600,6000), `D15` out 1b @(9000,6000), `D16` out 1b @(7800,6000), `D17` out 1b @(7200,6000), `D18` out 1b @(6600,6000), `D19` out 1b @(6000,6000), `X` out 8b @(4200,6000), `Y` out 8b @(4800,6000), `S1` out 1b @(2400,6000), `S0` out 1b @(3000,6000), `A` in 8b @(0,3000), `STATE` out 1b @(19800,6000)

## MicroROM

`hades.models.rtlib.memory.MicroROM` — microcode-rom with 1024 words of 12+4+4+4+4+16 outputs.

- Parâmetros padrão: `1001 4096 44`
- bbox: (0, 0)..(18000, 4800)
- Portas: `D0` out 1b @(17400,4800), `D1` out 1b @(16800,4800), `D2` out 1b @(16200,4800), `D3` out 1b @(15600,4800), `D4` out 1b @(15000,4800), `D5` out 1b @(14400,4800), `D6` out 1b @(13800,4800), `D7` out 1b @(13200,4800), `D8` out 1b @(12000,4800), `D9` out 1b @(11400,4800), `D10` out 1b @(10800,4800), `D11` out 1b @(10200,4800), `D12` out 1b @(9600,4800), `D13` out 1b @(9000,4800), `D14` out 1b @(8400,4800), `D15` out 1b @(7800,4800), `E` out 4b @(6000,4800), `F` out 4b @(5400,4800), `G` out 4b @(4800,4800), `H` out 4b @(4200,4800), `X` out 12b @(2400,4800), `A` in 12b @(0,2400)

## MipsRegBank ✅

`hades.models.rtlib.memory.MipsRegBank` — register bank of the MIPS R2K/R3K processors.

Doc detalhada: [components/memoria/MipsRegBank.md](../components/memoria/MipsRegBank.md)

- Parâmetros padrão: `1001 32 32`
- bbox: (0, 0)..(7200, 4800)
- Portas: `AR0` in 5b @(0,3000), `AR1` in 5b @(0,3600), `AW0` in 5b @(0,2400), `DR0` out 32b @(2400,4800), `DR1` out 32b @(4800,4800), `DW0` in 32b @(2400,0), `nWE` in 1b @(0,1800), `nCS` in 1b @(0,1200)

## RAM ✅

`hades.models.rtlib.memory.RAM` — random-access memory with separate read and write ports.

Doc detalhada: [components/memoria/RAM.md](../components/memoria/RAM.md)

- Parâmetros padrão: `1001 16 16`
- bbox: (0, 0)..(6000, 4800)
- Portas: `A` in 4b @(0,2400), `DIN` in 16b @(3600,0), `DOUT` out 16b @(3600,4800), `nWE` in 1b @(0,3000), `nCS` in 1b @(0,1800)

## RAMoe ✅

`hades.models.rtlib.memory.RAMoe` — random-access memory with separate read and write ports.

Doc detalhada: [components/memoria/RAMoe.md](../components/memoria/RAMoe.md)

- Parâmetros padrão: `1001 16 16`
- bbox: (0, 0)..(6000, 4800)
- Portas: `A` in 4b @(0,2400), `DIN` in 16b @(3600,0), `DOUT` out 16b @(3600,4800), `nWE` in 1b @(0,3000), `nCS` in 1b @(0,1800), `nOE` in 1b @(0,3600)

## ROM ✅

`hades.models.rtlib.memory.ROM` — read-only memory.

Doc detalhada: [components/memoria/ROM.md](../components/memoria/ROM.md)

- Parâmetros padrão: `1001 16 16`
- bbox: (0, 0)..(6000, 4800)
- Portas: `A` in 4b @(0,2400), `D` out 16b @(3600,4800)

## ROMcs

`hades.models.rtlib.memory.ROMcs` — read-only memory with tri-state output.

- Parâmetros padrão: `1001 16 16`
- bbox: (0, 0)..(6000, 4800)
- Portas: `A` in 4b @(0,2400), `D` out 16b @(3600,4800), `nCS` in 1b @(0,1800)

## ROMoe ✅

`hades.models.rtlib.memory.ROMoe` — read-only memory with output-enable input.

Doc detalhada: [components/memoria/ROMoe.md](../components/memoria/ROMoe.md)

- Parâmetros padrão: `1001 16 16`
- bbox: (0, 0)..(6000, 4800)
- Portas: `A` in 4b @(0,2400), `D` out 16b @(3600,4800), `nCS` in 1b @(0,1800), `nOE` in 1b @(0,3000)

## RealTimeClock

`hades.models.rtlib.memory.RealTimeClock` — RealTimeClock - a generic real-time clock with RAM-like addressing

- Parâmetros padrão: `1001 8 16`
- bbox: (0, 0)..(6000, 3000)
- Portas: `A` in 3b @(0,1200), `DIN` in 16b @(3000,0), `DOUT` out 16b @(3000,3000), `nWE` in 1b @(0,1800), `nCS` in 1b @(0,600), `nOE` in 1b @(0,2400)

## RegBank ✅

`hades.models.rtlib.memory.RegBank` — register bank for the D*CORE processor.

Doc detalhada: [components/memoria/RegBank.md](../components/memoria/RegBank.md)

- Parâmetros padrão: `1001 16 16`
- bbox: (0, 0)..(7200, 6000)
- Portas: `AX` in 4b @(0,3000), `AY` in 4b @(0,3600), `AZ` in 4b @(0,4200), `DX` out 16b @(4800,6000), `DY` out 16b @(2400,6000), `DZ` in 16b @(4800,0), `nWE` in 1b @(0,2400), `CLK` in 1b @(0,1800)

## BitDecoder

`hades.models.rtlib.muxes.BitDecoder` — n-to-2^n decoder. 

- Parâmetros padrão: `1001 5 1.0E-8`
- bbox: (0, 0)..(19800, 1200) (dinâmico)
- Portas: `A` in 5b @(600,0), `Y0` out 1b @(19200,1200), `Y1` out 1b @(18600,1200), `Y2` out 1b @(18000,1200), `Y3` out 1b @(17400,1200), `Y4` out 1b @(16800,1200), `Y5` out 1b @(16200,1200), `Y6` out 1b @(15600,1200), `Y7` out 1b @(15000,1200), `Y8` out 1b @(14400,1200), `Y9` out 1b @(13800,1200), `Y10` out 1b @(13200,1200), `Y11` out 1b @(12600,1200), `Y12` out 1b @(12000,1200), `Y13` out 1b @(11400,1200), `Y14` out 1b @(10800,1200), `Y15` out 1b @(10200,1200), `Y16` out 1b @(9600,1200), `Y17` out 1b @(9000,1200), `Y18` out 1b @(8400,1200), `Y19` out 1b @(7800,1200), `Y20` out 1b @(7200,1200), `Y21` out 1b @(6600,1200), `Y22` out 1b @(6000,1200), `Y23` out 1b @(5400,1200), `Y24` out 1b @(4800,1200), `Y25` out 1b @(4200,1200), `Y26` out 1b @(3600,1200), `Y27` out 1b @(3000,1200), `Y28` out 1b @(2400,1200), `Y29` out 1b @(1800,1200), `Y30` out 1b @(1200,1200), `Y31` out 1b @(600,1200)

## Decoder

`hades.models.rtlib.muxes.Decoder` — n-to-2^n decoder. 

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `A` in 16b @(1800,0), `Y` out 65536b @(1800,1800)

## Mux21 ✅

`hades.models.rtlib.muxes.Mux21` — 2:1 n-bit multiplexer (with animation).

Doc detalhada: [components/mux/Mux21.md](../components/mux/Mux21.md)

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 1800)
- Portas: `S` in 1b @(0,1200), `A1` in 16b @(1200,0), `A0` in 16b @(2400,0), `Y` out 16b @(1800,1800)

## Mux41 ✅

`hades.models.rtlib.muxes.Mux41` — 4:1 n-bit multiplexer.

Doc detalhada: [components/mux/Mux41.md](../components/mux/Mux41.md)

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(4800, 1800)
- Portas: `S1` in 1b @(0,600), `S0` in 1b @(0,1200), `A3` in 16b @(600,0), `A2` in 16b @(1800,0), `A1` in 16b @(3000,0), `A0` in 16b @(4200,0), `Y` out 16b @(2400,1800)

## TriBuf

`hades.models.rtlib.muxes.TriBuf` — n-bit tri-state buffer.

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(1200, 1200)
- Portas: `A` in 16b @(600,0), `S` in 1b @(0,600), `Y` out 16b @(600,1200)

## TriBufBig

`hades.models.rtlib.muxes.TriBufBig` — n-bit tri-state buffer (big symbol).

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(1800, 1800)
- Portas: `A` in 16b @(900,0), `S` in 1b @(0,1200), `Y` out 16b @(900,1800)

## CounterRE

`hades.models.rtlib.register.CounterRE` — n-bit positive edge-triggered counter with reset and enable.

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `CLK` in 1b @(0,1200), `NR` in 1b @(0,1800), `ENA` in 1b @(0,600), `Q` out 16b @(1800,2400)

## LFSR

`hades.models.rtlib.register.LFSR` — positive edge-triggered linear feedback shift register,

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8 13755891`
- bbox: (0, 0)..(3600, 2400)
- Portas: `CLK` in 1b @(0,1200), `NR` in 1b @(0,1800), `Q` out 16b @(1800,2400)

## Latch

`hades.models.rtlib.register.Latch` — n-bit latch.

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `CLK` in 1b @(0,1200), `D` in 16b @(1800,0), `Q` out 16b @(1800,2400)

## LatchR

`hades.models.rtlib.register.LatchR` — n-bit latch with asynchronous reset.

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `CLK` in 1b @(0,1200), `NR` in 1b @(0,1800), `D` in 16b @(1800,0), `Q` out 16b @(1800,2400)

## Reg

`hades.models.rtlib.register.Reg` — n-bit positive edge-triggered D-type register.

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `CLK` in 1b @(0,1200), `D` in 16b @(1800,0), `Q` out 16b @(1800,2400)

## RegE

`hades.models.rtlib.register.RegE` — n-bit positive edge-triggered D-type register with enable.

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `CLK` in 1b @(0,1200), `ENA` in 1b @(0,600), `D` in 16b @(1800,0), `Q` out 16b @(1800,2400)

## RegR

`hades.models.rtlib.register.RegR` — n-bit positive edge-triggered D-type register with reset.

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `CLK` in 1b @(0,1200), `NR` in 1b @(0,1800), `D` in 16b @(1800,0), `Q` out 16b @(1800,2400)

## RegRE ✅

`hades.models.rtlib.register.RegRE` — n-bit positive edge-triggered D-type register with reset

Doc detalhada: [components/registradores/RegRE.md](../components/registradores/RegRE.md)

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `CLK` in 1b @(0,1200), `NR` in 1b @(0,1800), `ENA` in 1b @(0,600), `D` in 16b @(1800,0), `Q` out 16b @(1800,2400)

## RegWithInitialValue

`hades.models.rtlib.register.RegWithInitialValue` — n-bit positive edge-triggered D-type register with

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `CLK` in 1b @(0,1200), `D` in 16b @(1800,0), `Q` out 16b @(1800,2400)

## ShiftRegR

`hades.models.rtlib.register.ShiftRegR` — n-bit positive edge-triggered D-type or shift register.

- Parâmetros padrão: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`
- bbox: (0, 0)..(4800, 2400)
- Portas: `CLK` in 1b @(0,1200), `NR` in 1b @(0,1800), `ENA` in 1b @(0,600), `SIN` in 1b @(1200,0), `SOUT` out 1b @(3600,2400), `D` in 16b @(2400,0), `Q` out 16b @(2400,2400)
