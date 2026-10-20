# Catálogo HADES — pacote `hades.models.dsp`

Gerado automaticamente a partir do `hades.jar` (parâmetros PADRÃO). Componentes marcados com ✅ têm documentação detalhada em `components/`.
Para os demais: portas, posições e bbox valem para os parâmetros padrão; componentes de largura variável mudam com `n_bits`. Antes de usar um deles pela primeira vez, documente-o (veja `ADICIONANDO_COMPONENTES.md`).

## Acos

`hades.models.dsp.Acos` — inverse cosinus operator (arccos function, radians).

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## Add

`hades.models.dsp.Add` — two-inputs addition operator, Y = A + B.

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `B` in 1b @(1200,0), `Y` out 1b @(2400,1200)

## Asin

`hades.models.dsp.Asin` — inverse sinus operator (arcsin function, radians).

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## Atan

`hades.models.dsp.Atan` — inverse tangens operator (arctan function, radians).

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## Clip

`hades.models.dsp.Clip` — hard-clipping operator with user-specified lower and upper bounds:

- Parâmetros padrão: `1001 1.0E-8 0.0 5.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `X` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## Constant

`hades.models.dsp.Constant` — constant generator, Y = constant.

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `Y` out 1b @(2400,1200)

## Cos

`hades.models.dsp.Cos` — cosinus operator, Y = cos( X )    (radians)

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## Counter

`hades.models.dsp.Counter` — an operator to count clock events.  On a rising-edge of the 

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `C` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## Div

`hades.models.dsp.Div` — two-inputs division operator, Y = A / B.

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `B` in 1b @(1200,0), `Y` out 1b @(2400,1200)

## DoubleToInteger

`hades.models.dsp.DoubleToInteger` — converter from double to integer values. 

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## DoubleToStdLogic1164

`hades.models.dsp.DoubleToStdLogic1164` — converter from double values to StdLogic1164. 

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## DoubleToStdLogicVector

`hades.models.dsp.DoubleToStdLogicVector` — converter from double values to StdLogicVector.

- Parâmetros padrão: `1001 16 1.0E-8 0.0 1.0`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 16b @(2400,1200)

## Exp

`hades.models.dsp.Exp` — exponential function operator, Y = exp( X )

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## Function

`hades.models.dsp.Function` — general arithmetic function operator. 

- Parâmetros padrão: `1001 5.0E-9 1 x null`
- bbox: (0, 0)..(4800, 3000) (dinâmico)
- Portas: `x` in 1b @(0,1200), `FUNC` out 1b @(4800,1200)

## IntegerToDouble

`hades.models.dsp.IntegerToDouble` — converter from integer to double values.

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## LevelTrigger

`hades.models.dsp.LevelTrigger` — generates a StdLogic1164 0-1 transition when the input value

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b (sem posição)

## Log

`hades.models.dsp.Log` — natural logarithm operator, Y = log( X )

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## Log10

`hades.models.dsp.Log10` — base-10 logarithm operator, Y = log_10( X )

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## Log2

`hades.models.dsp.Log2` — base-2 logarithm operator, Y = log_2( X )

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## Max

`hades.models.dsp.Max` — two-inputs maximum operator, Y = max( A, B )

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1800), `Y` out 1b @(2400,1200)

## Max3

`hades.models.dsp.Max3` — three-inputs maximum operator, Y = max( A, B, C )

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1200), `C` in 1b @(0,1800), `Y` out 1b @(2400,1200)

## Min

`hades.models.dsp.Min` — two-inputs minimum operator, Y = min( A, B )

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1800), `Y` out 1b @(2400,1200)

## Min3

`hades.models.dsp.Min3` — three-inputs minimum operator, Y = min( A, B, C )

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1200), `C` in 1b @(0,1800), `Y` out 1b @(2400,1200)

## Mult

`hades.models.dsp.Mult` — two-inputs multiplication operator, Y = A * B.

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `B` in 1b @(1200,0), `Y` out 1b @(2400,1200)

## Mux21

`hades.models.dsp.Mux21` — two-inputs multiplexer, Y = ( S ? A : B )

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1800), `S` in 1b @(1200,2400), `Y` out 1b @(2400,1200)

## Mux41

`hades.models.dsp.Mux41` — four-inputs multiplexer.

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 3000)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1200), `C` in 1b @(0,1800), `D` in 1b @(0,2400), `S0` in 1b @(1800,3000), `S1` in 1b @(1200,3000), `Y` out 1b @(2400,1200)

## Neg

`hades.models.dsp.Neg` — arithmetic negation operator, Y = - X

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## Oscilloscope

`hades.models.dsp.Oscilloscope` — basic two-channel oscilloscope. 

- Parâmetros padrão: `1001 256 0.001 0.1 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(3600, 3000)
- Portas: `T` in 1b @(0,2400), `A` passive_in 1b @(0,600), `B` passive_in 1b @(0,1200)

## Printf

`hades.models.dsp.Printf` — the printf operator converts its double-precision input value

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## Random

`hades.models.dsp.Random` — random number generator with uniform distribution and user-settable

- Parâmetros padrão: `1001 1.0E-8 0.0 1.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `C` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## Reciprocal

`hades.models.dsp.Reciprocal` — reciprocal operator, Y = 1.0 / X.

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## Register

`hades.models.dsp.Register` — rising-edge triggered register for double-precision values.

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `D` in 1b @(0,1200), `C` in 1b @(1200,2400), `Q` out 1b @(2400,1200)

## Scale

`hades.models.dsp.Scale` — linear transformation operator (scaling), Y = a*X + b.

- Parâmetros padrão: `1001 1.0E-8 1.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `X` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## SimTime

`hades.models.dsp.SimTime` — an operator to access the current simulation time.

- Parâmetros padrão: `1001 0.0 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `C` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## Sin

`hades.models.dsp.Sin` — sinus function operator, Y = sin( X )    (radians)

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## StdLogicVectorToDouble

`hades.models.dsp.StdLogicVectorToDouble` — converter from StdLogicVector (unsigned) to double values.

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 0b @(0,1200), `Y` out 1b @(2400,1200)

## Sub

`hades.models.dsp.Sub` — two-inputs subtraction operator, Y = A - B.

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `B` in 1b @(1200,0), `Y` out 1b @(2400,1200)

## Tan

`hades.models.dsp.Tan` — tangens function operator, Y = tan( X )    (radians)

- Parâmetros padrão: `1001 1.0E-8 0.0 0.0 0.0 0.0 0 0 0 0 null null null null`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(2400,1200)
