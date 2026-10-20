# hades.models.ruge

Gerado do hades.jar com parâmetros padrão. ✅ = doc em `components/`. Demais: documentar antes de usar (`ADICIONANDO_COMPONENTES.md`).

## Adder
`hades.models.ruge.Adder` — XXX
- params: `1001 1.0E-8`; bbox (0,0)..(4800,2400)
- portas: `A` in 1b (1200,2400), `B` in 1b (3600,2400), `SUM` out 1b (2400,0)

## Alu
`hades.models.ruge.Alu` — XXX
- params: `1001 1.0E-8`; bbox (0,0)..(4800,2400)
- portas: `A` in 1b (1200,2400), `B` in 1b (3600,2400), `Y` out 1b (2400,0), `SEL` out 1b (4800,1200)

## Constant
`hades.models.ruge.Constant` — XXX
- params: `1001 0`; bbox (0,0)..(2400,2400)
- portas: `Y` out 1b (1200,0)

## DelayNode
`hades.models.ruge.DelayNode` — XXX
- params: `1001 0.2`; bbox (-150,-150)..(150,150)
- portas: `A` inout 1b (0,-150), `B` inout 1b (-150,0), `C` inout 1b (0,150), `D` inout 1b (150,0)

## Incr
`hades.models.ruge.Incr` — XXX
- params: `1001 1.0E-8`; bbox (0,0)..(2400,2400)
- portas: `A` in 1b (1200,2400), `SUM` out 1b (1200,0)

## Latch
`hades.models.ruge.Latch` — XXX
- params: `1001 0 1.0E-8`; bbox (0,0)..(2400,2400)
- portas: `CLK` in 1b (1800,2400), `D` in 1b (1200,2400), `Q` out 1b (1200,0)

## Mux
`hades.models.ruge.Mux` — XXX
- params: `1001 1.0E-8`; bbox (0,0)..(4800,2400)
- portas: `A0` in 1b (3600,2400), `A1` in 1b (1200,2400), `S` in 1b (4200,2400), `Y` out 1b (2400,0)

## RAM_64K
`hades.models.ruge.RAM_64K` — XXX
- params: `1001 /hades/models/rtl/RAM_64K.rom`; bbox (0,0)..(5400,3600)
- portas: `ADDR` in 1b (0,1800), `DIN` in 1b (3000,3600), `DOUT` out 1b (3000,0), `nME` in 1b (0,1200), `nWE` in 1b (0,2400)

## Register
`hades.models.ruge.Register` — XXX
- params: `1001 0 1.0E-8`; bbox (0,0)..(2400,2400)
- portas: `CLK` in 1b (1800,2400), `ENA` in 1b (600,2400), `D` in 1b (1200,2400), `Q` out 1b (1200,0)

## TriBuf
`hades.models.ruge.TriBuf` — XXX
- params: `1001 1.0E-8`; bbox (0,0)..(1200,1200)
- portas: `A` in 1b (600,1200), `Y` out 1b (600,0), `S` in 1b (1200,600)
