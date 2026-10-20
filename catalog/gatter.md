# hades.models.gatter

Gerado do hades.jar com parâmetros padrão. ✅ = doc em `components/`. Demais: documentar antes de usar (`ADICIONANDO_COMPONENTES.md`).

## And2
`hades.models.gatter.And2` — 2-input AND gate with DIN-style symbol.
- params: `1001 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `Y` out 1b (3600,1200), `A` in 1b (0,600), `B` in 1b (0,1800)

## And3
`hades.models.gatter.And3` — 3-input AND gate with DIN-style symbol.
- params: `1001 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `Y` out 1b (3600,1200), `A` in 1b (0,600), `B` in 1b (0,1200), `C` in 1b (0,1800)

## And4
`hades.models.gatter.And4` — 4-input AND gate with DIN-style symbol.
- params: `1001 1.0E-8`; bbox (0,0)..(3600,3000)
- portas: `Y` out 1b (3600,1200), `A` in 1b (0,600), `B` in 1b (0,1200), `C` in 1b (0,1800), `D` in 1b (0,2400)

## And4Neg2
`hades.models.gatter.And4Neg2` — AND-gate with 2 positive and 2 inverted inputs 
- params: `1001 1.0E-8`; bbox (0,0)..(3600,3000)
- portas: `Y` out 1b (3600,1200), `A` in 1b (0,600), `B` in 1b (0,1200), `C` in 1b (0,1800), `D` in 1b (0,2400)

## Buffer
`hades.models.gatter.Buffer` — Simple non-inverting buffer with DIN-style symbol.
- params: `1001 1.0E-8`; bbox (0,0)..(1800,1200)
- portas: `Y` out 1b (1800,600), `A` in 1b (0,600)

## Demux14
`hades.models.gatter.Demux14` — Simple 1-to-4 demultiplexer.
- params: `1001 1.5E-8`; bbox (0,0)..(3000,3000)
- portas: `Y0` out 1b (3000,2400), `Y1` out 1b (3000,1800), `Y2` out 1b (3000,1200), `Y3` out 1b (3000,600), `S0` in 1b (1800,3000), `S1` in 1b (1200,3000), `A` in 1b (0,1200)

## Inv
`hades.models.gatter.Inv` — Simple inverter gate, DIN-style symbol.
- params: `1001 5.0E-9`; bbox (0,0)..(1800,1200)
- portas: `A` in 1b (0,600), `Y` out 1b (1800,600)

## InvVertical ✅
`hades.models.gatter.InvVertical` — Simple inverter gate with vertically oriented DIN-style symbol. → [components/portas/InvVertical.md](../components/portas/InvVertical.md)
- params: `1001 5.0E-9`; bbox (0,0)..(1200,1800)
- portas: `A` in 1b (600,0), `Y` out 1b (600,1800)

## Mux21
`hades.models.gatter.Mux21` — 2-to-1 multiplexer gate, DIN-style symbol.
- params: `1001 1.0E-8`; bbox (0,0)..(2400,2400)
- portas: `Y` out 1b (2400,1200), `A0` in 1b (0,1800), `A1` in 1b (0,600), `S` in 1b (1200,2400)

## Mux41
`hades.models.gatter.Mux41` — 4-to-1 multiplexer gate.
- params: `1001 1.5E-8`; bbox (0,0)..(3000,3600)
- portas: `Y` out 1b (3000,1800), `A0` in 1b (0,2400), `A1` in 1b (0,1800), `A2` in 1b (0,1200), `A3` in 1b (0,600), `S0` in 1b (1800,3600), `S1` in 1b (1200,3600)

## Mux41DIN
`hades.models.gatter.Mux41DIN` — 4-to-1 multiplexer gate, DIN-style symbol.
- params: `1001 1.5E-8`; bbox (0,0)..(3600,4800)
- portas: `Y` out 1b (3600,2400), `A0` in 1b (0,4200), `A1` in 1b (0,3600), `A2` in 1b (0,3000), `A3` in 1b (0,2400), `S0` in 1b (0,1200), `S1` in 1b (0,600)

## Nand2
`hades.models.gatter.Nand2` — 2-input NAND gate, DIN-style symbol.
- params: `1001 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `Y` out 1b (3600,1200), `A` in 1b (0,600), `B` in 1b (0,1800)

## Nand3
`hades.models.gatter.Nand3` — 3-input NAND gate, DIN-style symbol.
- params: `1001 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `Y` out 1b (3600,1200), `A` in 1b (0,600), `B` in 1b (0,1200), `C` in 1b (0,1800)

## Nand4
`hades.models.gatter.Nand4` — 4-input NAND gate, DIN-style symbol.
- params: `1001 1.0E-8`; bbox (0,0)..(3600,3000)
- portas: `Y` out 1b (3600,1200), `A` in 1b (0,600), `B` in 1b (0,1200), `C` in 1b (0,1800), `D` in 1b (0,2400)

## Nor2
`hades.models.gatter.Nor2` — 2-input NOR gate, DIN-style symbol.
- params: `1001 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `Y` out 1b (3600,1200), `A` in 1b (0,600), `B` in 1b (0,1800)

## Nor3
`hades.models.gatter.Nor3` — 3-input NOR gate, DIN-style symbol.
- params: `1001 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `Y` out 1b (3600,1200), `A` in 1b (0,600), `B` in 1b (0,1200), `C` in 1b (0,1800)

## Nor4 ✅
`hades.models.gatter.Nor4` — 4-input NOR gate, DIN-style symbol. → [components/portas/Nor4.md](../components/portas/Nor4.md)
- params: `1001 1.0E-8`; bbox (0,0)..(3600,3000)
- portas: `Y` out 1b (3600,1200), `A` in 1b (0,600), `B` in 1b (0,1200), `C` in 1b (0,1800), `D` in 1b (0,2400)

## Or2
`hades.models.gatter.Or2` — 2-input OR gate, DIN-style symbol.
- params: `1001 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `Y` out 1b (3600,1200), `A` in 1b (0,600), `B` in 1b (0,1800)

## Or3
`hades.models.gatter.Or3` — 3-input OR gate, DIN-style symbol.
- params: `1001 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `Y` out 1b (3600,1200), `A` in 1b (0,600), `B` in 1b (0,1200), `C` in 1b (0,1800)

## Or4
`hades.models.gatter.Or4` — 4-input OR gate, DIN-style symbol.
- params: `1001 1.0E-8`; bbox (0,0)..(3600,3000)
- portas: `Y` out 1b (3600,1200), `A` in 1b (0,600), `B` in 1b (0,1200), `C` in 1b (0,1800), `D` in 1b (0,2400)

## Or6
`hades.models.gatter.Or6` — 6-input OR gate, DIN-style symbol.
- params: `1001 1.0E-8`; bbox (0,0)..(3600,4200)
- portas: `Y` out 1b (3600,1200), `A` in 1b (0,600), `B` in 1b (0,1200), `C` in 1b (0,1800), `D` in 1b (0,2400), `E` in 1b (0,3000), `F` in 1b (0,3600)

## Tri
`hades.models.gatter.Tri` — Inverting buffer with tr-state output, DIN-style symbol.
- params: `1001 5.0E-9`; bbox (0,0)..(2400,2400)
- portas: `Y` out 1b (2400,1200), `A` in 1b (0,1200), `S` in 1b (1200,2400)

## Xnor2
`hades.models.gatter.Xnor2` — 2-input XNOR gate, DIN-style symbol.
- params: `1001 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `Y` out 1b (3600,1200), `A` in 1b (0,600), `B` in 1b (0,1800)

## Xor2
`hades.models.gatter.Xor2` — 2-input XOR gate, DIN-style symbol.
- params: `1001 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `Y` out 1b (3600,1200), `A` in 1b (0,600), `B` in 1b (0,1800)
