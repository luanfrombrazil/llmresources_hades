# hades.models.flipflops

Gerado do hades.jar com parâmetros padrão. ✅ = doc em `components/`. Demais: documentar antes de usar (`ADICIONANDO_COMPONENTES.md`).

## Dff
`hades.models.flipflops.Dff` — DFF: D-type flipflop
- params: `1001 5.0E-9 4.0E-9 3.0E-9`; bbox (0,0)..(3600,2400)
- portas: `Q` out 1b (3600,600), `NQ` out 1b (3600,1800), `D` in 1b (0,600), `C` in 1b (0,1800)

## DffMetastable
`hades.models.flipflops.DffMetastable` — "real, metastable" D-type flipflop
- params: `1001 5.0E-9 4.0E-9 3.0E-9`; bbox (0,0)..(3600,2400)
- portas: `Q` out 1b (3600,600), `NQ` out 1b (3600,1800), `D` in 1b (0,600), `C` in 1b (0,1800)

## DffRtlib
`hades.models.flipflops.DffRtlib` — D-type flipflop with RTLIB symbol
- params: `1001 5.0E-9 4.0E-9 3.0E-9`; bbox (0,0)..(3600,2400)
- portas: `Q` out 1b (3600,600), `NQ` out 1b (3600,1800), `D` in 1b (0,600), `C` in 1b (0,1800)

## Dffe
`hades.models.flipflops.Dffe` — DFFE: D-type flipflop with enable
- params: `1001 5.0E-9 4.0E-9 3.0E-9`; bbox (0,0)..(3600,2400)
- portas: `Q` out 1b (3600,600), `NQ` out 1b (3600,1800), `D` in 1b (0,600), `C` in 1b (0,1800), `E` in 1b (0,1200)

## Dffr
`hades.models.flipflops.Dffr` — D-type flipflop with asynchronous reset.
- params: `1001 5.0E-9 4.0E-9 3.0E-9`; bbox (0,0)..(3600,4800)
- portas: `Q` out 1b (3600,1800), `NQ` out 1b (3600,3000), `D` in 1b (0,1800), `C` in 1b (0,3000), `NR` in 1b (0,4200)

## DffrMetastable
`hades.models.flipflops.DffrMetastable` — "metastable" D-type flipflop with reset
- params: `1001 5.0E-9 4.0E-9 3.0E-9`; bbox (0,0)..(3600,4800)
- portas: `Q` out 1b (3600,1800), `NQ` out 1b (3600,3000), `D` in 1b (0,1800), `C` in 1b (0,3000), `NR` in 1b (0,4200)

## Dffre
`hades.models.flipflops.Dffre` — D-type flipflop with asynchronous reset and enable
- params: `1001 5.0E-9 4.0E-9 3.0E-9`; bbox (0,0)..(3600,4800)
- portas: `D` passive_in 1b (0,1800), `C` in 1b (0,3000), `Q` out 1b (3600,1800), `NQ` out 1b (3600,3000), `NR` in 1b (0,4200), `E` in 1b (0,600)

## DffreRtlib
`hades.models.flipflops.DffreRtlib` — D-type flipflop with asynchronous reset and enable
- params: `1001 5.0E-9 4.0E-9 3.0E-9`; bbox (0,0)..(2400,2400)
- portas: `D` passive_in 1b (1200,0), `C` in 1b (0,1200), `Q` out 1b (1200,2400), `NQ` out 1b (1800,2400), `NR` in 1b (0,1800), `E` in 1b (0,600)

## Dffrs
`hades.models.flipflops.Dffrs` — D-type flipflop with asynchronous set and reset inputs
- params: `1001 5.0E-9 4.0E-9 3.0E-9`; bbox (0,0)..(3600,4800)
- portas: `Q` out 1b (3600,1800), `NQ` out 1b (3600,3000), `D` in 1b (0,1800), `C` in 1b (0,3000), `NR` in 1b (0,4200), `NS` in 1b (0,600)

## Jkff
`hades.models.flipflops.Jkff` — JK-type flipflop
- params: `1001 5.0E-9 4.0E-9 3.0E-9`; bbox (0,0)..(3600,4800)
- portas: `Q` out 1b (3600,1800), `NQ` out 1b (3600,3000), `NC` in 1b (0,1800), `J` in 1b (0,600), `K` in 1b (0,3000), `NR` in 1b (0,4200)

## JkffMetastable
`hades.models.flipflops.JkffMetastable` — "metastable" JK-type flipflop
- params: `1001 5.0E-9 4.0E-9 3.0E-9`; bbox (0,0)..(3600,4800)
- portas: `Q` out 1b (3600,1800), `NQ` out 1b (3600,3000), `NC` in 1b (0,1800), `J` in 1b (0,600), `K` in 1b (0,3000), `NR` in 1b (0,4200)

## Latch
`hades.models.flipflops.Latch` — D-Latch 
- params: `1001 5.0E-9 4.0E-9 3.0E-9`; bbox (0,0)..(3600,2400)
- portas: `Q` out 1b (3600,600), `NQ` out 1b (3600,1800), `D` in 1b (0,600), `C` in 1b (0,1800)

## LatchMetastable
`hades.models.flipflops.LatchMetastable` — "metastable" D-Latch
- params: `1001 5.0E-9 4.0E-9 3.0E-9`; bbox (0,0)..(3600,2400)
- portas: `Q` out 1b (3600,600), `NQ` out 1b (3600,1800), `D` in 1b (0,600), `C` in 1b (0,1800)

## Latchr
`hades.models.flipflops.Latchr` — D-latch with asynchronous reset input
- params: `1001 5.0E-9 4.0E-9 3.0E-9`; bbox (0,0)..(3600,4800)
- portas: `Q` out 1b (3600,1800), `NQ` out 1b (3600,3000), `D` in 1b (0,1800), `C` in 1b (0,3000), `NR` in 1b (0,4200)

## Srff
`hades.models.flipflops.Srff` — basic SR flipflop.
- params: `1001 5.0E-9 4.0E-9 3.0E-9`; bbox (0,0)..(3600,2400)
- portas: `Q` out 1b (3600,600), `NQ` out 1b (3600,1800), `S` in 1b (0,600), `R` in 1b (0,1800)

## SrffRtlib
`hades.models.flipflops.SrffRtlib` — basic SR flipflop with RTLIB-style symbol.
- params: `1001 5.0E-9 4.0E-9 3.0E-9`; bbox (0,0)..(3600,2400)
- portas: `Q` out 1b (3600,600), `NQ` out 1b (3600,1800), `S` in 1b (0,600), `R` in 1b (0,1800)
