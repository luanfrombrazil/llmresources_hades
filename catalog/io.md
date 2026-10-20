# hades.models.io

Gerado do hades.jar com parâmetros padrão. ✅ = doc em `components/`. Demais: documentar antes de usar (`ADICIONANDO_COMPONENTES.md`).

## AsciiDisplay
`hades.models.io.AsciiDisplay` — 20-segment ASCII LED display
- params: `1001`; bbox (0,0)..(3000,4200)
- portas: `D7` in 1b (300,0), `D6` in 1b (600,0), `D5` in 1b (900,0), `D4` in 1b (1200,0), `D3` in 1b (1500,0), `D2` in 1b (1800,0), `D1` in 1b (2100,0), `D0` in 1b (2400,0)

## BitReg6
`hades.models.io.BitReg6` — directly editable 6-bit D-register
- params: `1001`; bbox (0,0)..(8400,1200)
- portas: `C` in 1b (600,0), `NR` in 1b (0,900), `D0` passive_in 1b (7800,0), `D1` passive_in 1b (6600,0), `D2` passive_in 1b (5400,0), `D3` passive_in 1b (4200,0), `D4` passive_in 1b (3000,0), `D5` passive_in 1b (1800,0), `Q0` out 1b (7800,1200), `Q1` out 1b (6600,1200), `Q2` out 1b (5400,1200), `Q3` out 1b (4200,1200), `Q4` out 1b (3000,1200), `Q5` out 1b (1800,1200)

## ClockGen ✅
`hades.models.io.ClockGen` — Clock generator  → [components/io/ClockGen.md](../components/io/ClockGen.md)
- params: `1001 1.0 0.5 0.0 null`; bbox (0,0)..(2400,2400)
- portas: `clk` out 1b (2400,1200)

## ClockGenWithAutoStop
`hades.models.io.ClockGenWithAutoStop` — Clock generator with auto-stop.
- params: `1001 1.0 0.5 0.0 1000`; bbox (0,0)..(2400,2400)
- portas: `clk` out 1b (2400,1200)

## Constant0
`hades.models.io.Constant0` — constant 0
- params: `1001`; bbox (0,0)..(1200,1200)
- portas: `Y` inout 1b (1200,600)

## Constant1
`hades.models.io.Constant1` — constant 1
- params: `1001`; bbox (0,0)..(1200,1200)
- portas: `Y` inout 1b (1200,600)

## ConstantH
`hades.models.io.ConstantH` — constant H
- params: `1001`; bbox (0,0)..(1200,1200)
- portas: `Y` inout 1b (1200,600)

## ConstantL
`hades.models.io.ConstantL` — constant L
- params: `1001`; bbox (0,0)..(1200,1200)
- portas: `Y` inout 1b (1200,600)

## ConstantU
`hades.models.io.ConstantU` — constant U
- params: `1001`; bbox (0,0)..(1200,1200)
- portas: `Y` inout 1b (1200,600)

## ConstantW
`hades.models.io.ConstantW` — constant W
- params: `1001`; bbox (0,0)..(1200,1200)
- portas: `Y` inout 1b (1200,600)

## ConstantX
`hades.models.io.ConstantX` — constant X
- params: `1001`; bbox (0,0)..(1200,1200)
- portas: `Y` inout 1b (1200,600)

## ConstantZ
`hades.models.io.ConstantZ` — constant Z
- params: `1001`; bbox (0,0)..(1200,1200)
- portas: `Y` inout 1b (1200,600)

## DiodeSwitch
`hades.models.io.DiodeSwitch` — Interactive switch with series diode
- params: `1001 U`; bbox (0,0)..(1800,1200)
- portas: `Y` out 1b (1800,600), `A` in 1b (0,600)

## GalFuse
`hades.models.io.GalFuse` — Interactive switch (with builtin diode)
- params: `1001 5.0E-9 0`; bbox (0,0)..(900,900)
- portas: `A` in 1b (0,0), `Y` out 1b (900,900)

## Gnd ✅
`hades.models.io.Gnd` — GND connection → [components/io/Gnd.md](../components/io/Gnd.md)
- params: `1001`; bbox (-600,0)..(600,1500)
- portas: `GND` inout 1b (0,0)

## HexDisplay
`hades.models.io.HexDisplay` — HEX LED display
- params: `1001`; bbox (0,0)..(2700,4200)
- portas: `A3` in 1b (0,1200), `A2` in 1b (0,1800), `A1` in 1b (0,2400), `A0` in 1b (0,3000)

## HexDisplaySmall
`hades.models.io.HexDisplaySmall` — HEX LED display  (small symbol)
- params: `1001`; bbox (0,0)..(1500,1800)
- portas: `A3` in 1b (0,0), `A2` in 1b (0,600), `A1` in 1b (0,1200), `A0` in 1b (0,1800)

## HexSwitch
`hades.models.io.HexSwitch` — HEX switch
- params: `1001 0 null`; bbox (0,0)..(3000,3900)
- portas: `Y0` out 1b (3000,2400), `Y1` out 1b (3000,1800), `Y2` out 1b (3000,1200), `Y3` out 1b (3000,600)

## Ipin ✅
`hades.models.io.Ipin` — Interactive switch → [components/io/Ipin.md](../components/io/Ipin.md)
- params: `1001 null U`; bbox (-1200,-600)..(0,600)
- portas: `Y` out 1b (0,0)

## IpinLarge
`hades.models.io.IpinLarge` — Interactive switch  (large symbol)
- params: `1001 null U`; bbox (-2400,-1200)..(0,1200)
- portas: `Y` out 1b (0,0)

## IpinStdLogic1164
`hades.models.io.IpinStdLogic1164` — Interactive switch for all StdLogic1164 levels.
- params: `1001 null U`; bbox (0,0)..(3600,2400)
- portas: `Y` out 1b (3600,1200)

## Iso8859Display
`hades.models.io.Iso8859Display` — LED-matrix display with integrated decoder.
- params: `1001`; bbox (0,0)..(3000,4200)
- portas: `D7` in 1b (300,0), `D6` in 1b (600,0), `D5` in 1b (900,0), `D4` in 1b (1200,0), `D3` in 1b (1500,0), `D2` in 1b (1800,0), `D1` in 1b (2100,0), `D0` in 1b (2400,0)

## LED ✅
`hades.models.io.LED` — Simple LED  → [components/io/LED.md](../components/io/LED.md)
- params: `1001 0`; bbox (0,-600)..(1200,600)
- portas: `A` in 1b (0,0)

## Opin ✅
`hades.models.io.Opin` — Output Pin with LED → [components/io/Opin.md](../components/io/Opin.md)
- params: `1001 5.0E-9`; bbox (0,-600)..(1200,600)
- portas: `A` in 1b (0,0), `i0` out 1b

## OpinLarge
`hades.models.io.OpinLarge` — Output Pin with LED  (large symbol)
- params: `1001 5.0E-9`; bbox (0,-1200)..(2400,1200)
- portas: `A` in 1b (0,0), `i0` out 1b

## OpinWithLabel
`hades.models.io.OpinWithLabel` — Output Pin with LED
- params: `1001 5.0E-9`; bbox (0,-600)..(1200,600)
- portas: `A` in 1b (0,0), `i0` out 1b

## PowerOnReset
`hades.models.io.PowerOnReset` — Power-on reset 
- params: `1001 0.005 0.005 null`; bbox (-2400,-1200)..(0,600)
- portas: `nreset` out 1b (0,0)

## Pullup
`hades.models.io.Pullup` — Pullup
- params: `1001`; bbox (-600,-1200)..(600,0)
- portas: `H` inout 1b (0,0)

## PulseSwitch ✅
`hades.models.io.PulseSwitch` — Interactive pulse switch → [components/io/PulseSwitch.md](../components/io/PulseSwitch.md)
- params: `1001 0.1 null`; bbox (-1200,-600)..(0,600)
- portas: `Y` out 1b (0,0)

## RandomBitGenerator
`hades.models.io.RandomBitGenerator` — RandomBitGenerator: a simulation model which generates a new random 0/1 
- params: `1001 5.0E-9 1235678942131 0.5`; bbox (0,0)..(3600,2400)
- portas: `C` in 1b (0,1800), `Y` out 1b (3600,600)

## RemoteIpin
`hades.models.io.RemoteIpin` — RemoteIpin - read N bits of data from a remote server and generate the
- params: `1001 http://tech-www.informatik.uni-hamburg.de/cgi-bin/dummy 0815`; bbox (0,0)..(6000,17400)
- portas: `YA0` out 1b (6000,16800), `YA1` out 1b (6000,16200), `YA2` out 1b (6000,15600), `YA3` out 1b (6000,15000), `YA4` out 1b (6000,14400), `YA5` out 1b (6000,13800), `YA6` out 1b (6000,13200), `YA7` out 1b (6000,12600), `YB0` out 1b (6000,11400), `YB1` out 1b (6000,10800), `YB2` out 1b (6000,10200), `YB3` out 1b (6000,9600), `YB4` out 1b (6000,9000), `YB5` out 1b (6000,8400), `YB6` out 1b (6000,7800), `YB7` out 1b (6000,7200), `YC0` out 1b (6000,6000), `YC1` out 1b (6000,5400), `YC2` out 1b (6000,4800), `YC3` out 1b (6000,4200), `YC4` out 1b (6000,3600), `YC5` out 1b (6000,3000), `YC6` out 1b (6000,2400), `YC7` out 1b (6000,1800), `error` out 1b (6000,600), `sample` in 1b (0,600)

## RemoteIpin8
`hades.models.io.RemoteIpin8` — RemoteIpin - read 8 bits of data from a remote server and generate the
- params: `1001 http://tech-www.informatik.uni-hamburg.de/cgi-bin/dummy 0815`; bbox (0,0)..(6000,6600)
- portas: `Y0` out 1b (6000,6000), `Y1` out 1b (6000,5400), `Y2` out 1b (6000,4800), `Y3` out 1b (6000,4200), `Y4` out 1b (6000,3600), `Y5` out 1b (6000,3000), `Y6` out 1b (6000,2400), `Y7` out 1b (6000,1800), `error` out 1b (6000,600), `sample` in 1b (0,600)

## RemoteOpin
`hades.models.io.RemoteOpin` — RemoteOpin - transfer input events to a remote server using
- params: `1001 http://tech-www.informatik.uni-hamburg.de/cgi-bin/dummy 0815`; bbox (0,0)..(6000,17400)
- portas: `A0` in 1b (0,16800), `A1` in 1b (0,16200), `A2` in 1b (0,15600), `A3` in 1b (0,15000), `A4` in 1b (0,14400), `A5` in 1b (0,13800), `A6` in 1b (0,13200), `A7` in 1b (0,12600), `B0` in 1b (0,11400), `B1` in 1b (0,10800), `B2` in 1b (0,10200), `B3` in 1b (0,9600), `B4` in 1b (0,9000), `B5` in 1b (0,8400), `B6` in 1b (0,7800), `B7` in 1b (0,7200), `C0` in 1b (0,6000), `C1` in 1b (0,5400), `C2` in 1b (0,4800), `C3` in 1b (0,4200), `C4` in 1b (0,3600), `C5` in 1b (0,3000), `C6` in 1b (0,2400), `C7` in 1b (0,1800), `trigger` out 1b (6000,1200), `error` out 1b (6000,600)

## RemoteOpin8
`hades.models.io.RemoteOpin8` — RemoteOpin - transfer input events to a remote server using
- params: `1001 http://tech-www.informatik.uni-hamburg.de/cgi-bin/dummy 0815`; bbox (0,0)..(6000,6600)
- portas: `D0` in 1b (0,6000), `D1` in 1b (0,5400), `D2` in 1b (0,4800), `D3` in 1b (0,4200), `D4` in 1b (0,3600), `D5` in 1b (0,3000), `D6` in 1b (0,2400), `D7` in 1b (0,1800), `trigger` out 1b (6000,1200), `error` out 1b (6000,600)

## RomDiode
`hades.models.io.RomDiode` — RomDiode: a faked diode useful for demonstrating ROM or PLA arrays.
- params: `1001 5.0E-9`; bbox (0,0)..(1200,1200)
- portas: `A` in 1b (0,0), `Y` out 1b (1200,1200)

## SevenSegment
`hades.models.io.SevenSegment` — Seven-segment LED display
- params: `1001`; bbox (0,0)..(2700,4200)
- portas: `A` in 1b (300,0), `B` in 1b (600,0), `C` in 1b (900,0), `D` in 1b (1200,0), `E` in 1b (1500,0), `F` in 1b (1800,0), `G` in 1b (2100,0), `P` in 1b (2400,0), `K` in 1b (2400,4200)

## SevenSegmentMultiplexed
`hades.models.io.SevenSegmentMultiplexed` — Seven-segment LED display.
- params: `1001 0.02 2.0E-4`; bbox (0,0)..(2700,4200) dinâmico
- portas: `A` in 1b (300,0), `B` in 1b (600,0), `C` in 1b (900,0), `D` in 1b (1200,0), `E` in 1b (1500,0), `F` in 1b (1800,0), `G` in 1b (2100,0), `P` in 1b (2400,0), `K` in 1b (2400,4200)

## Stimulus
`hades.models.io.Stimulus` — Stimulus generator
- params: `1001 /hades/models/io/Stimulus.hst`; bbox (0,0)..(3000,5400)
- portas: `Y0` out 1b (3000,4800), `Y1` out 1b (3000,4200), `Y2` out 1b (3000,3600), `Y3` out 1b (3000,3000), `Y4` out 1b (3000,2400), `Y5` out 1b (3000,1800), `Y6` out 1b (3000,1200), `Y7` out 1b (3000,600)

## Swatch
`hades.models.io.Swatch` — "Swatch"
- params: `1001`; bbox (0,0)..(12000,12000)
- portas: `m_time` in 1b (0,9600), `m_min` in 1b (0,10200), `m_sec` in 1b (0,10800), `m_1/10` in 1b (0,11400), `startstop` out 1b (12000,3000), `resetpause` out 1b (12000,9000), `z_min` out 1b (12000,10200), `z_sec` out 1b (12000,10800), `z_1/10` out 1b (12000,11400)

## Vcc
`hades.models.io.Vcc` — VCC connection
- params: `1001`; bbox (-600,-1500)..(600,0)
- portas: `VCC` inout 1b (0,0)
