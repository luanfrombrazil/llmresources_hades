# hades.models.microjava

Gerado do hades.jar com parâmetros padrão. ✅ = doc em `components/`. Demais: documentar antes de usar (`ADICIONANDO_COMPONENTES.md`).

## ALU ✅
`hades.models.microjava.ALU` — arithmetic logical unit for the Microjava processor → [components/aritmetica/ALU.md](../components/aritmetica/ALU.md)
- params: `1001 16 1.0E-8 16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15`; bbox (0,0)..(4800,2400)
- portas: `OPC` in 4b (0,1200), `A` in 16b (1200,0), `B` in 16b (3600,0), `Y` out 16b (2400,2400), `CIN` in 1b (600,0), `COUT` out 1b (1200,2400), `ZERO` out 1b (3000,2400), `NEG` out 1b (3600,2400), `EQ` out 1b, `OVF` out 1b

## BuffReg
`hades.models.microjava.BuffReg` — memory read buffer register for Microjava I
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(7200,1800)
- portas: `CLK` in 1b (600,1800), `NR` in 1b (1200,0), `rd` in 1b (7200,1200), `wr` in 1b (0,1200), `D` in 16b (0,600), `Q` out 16b (7200,600), `V` out 16b

## DFF
`hades.models.microjava.DFF` — rising-edge triggered D-type flipflop
- params: `1001 5.0E-9 4.0E-9 3.0E-9 0`; bbox (0,0)..(1200,1200)
- portas: `Q` out 1b (600,0), `NQ` out 1b, `D` in 1b (600,1200), `C` in 1b (0,600)

## DFFE
`hades.models.microjava.DFFE` — rising-edge triggered D-type flipflop with enable input
- params: `1001 5.0E-9 4.0E-9 3.0E-9`; bbox (0,0)..(1200,1200)
- portas: `Q` out 1b (600,0), `NQ` out 1b, `D` in 1b (600,1200), `C` in 1b (0,600), `E` in 1b (1200,600)

## IFU
`hades.models.microjava.IFU` — instruction fetch unit for Microjava 2
- params: `1001 1.0E-8`; bbox (0,0)..(7200,2400)
- portas: `CLK` in 1b (600,2400), `NR` in 1b (1200,0), `s` in 1b (5400,0), `m16` in 1b (6000,0), `m8` in 1b (6600,0), `pcw` in 1b (3000,0), `Q` out 32b (0,1800), `Opc` out 8b (4200,0), `A` out 32b (7200,1200), `nOE` out 1b (7200,600), `D` in 32b (7200,1800), `C` in 32b (0,1200), `mAc` in 1b (1800,0)

## MROM
`hades.models.microjava.MROM` — microcode ROM for Microjava 2
- params: `1001 16 16`; bbox (0,0)..(15000,6000)
- portas: `D0` out 1b (3600,6000), `D1` out 1b (4200,6000), `D2` out 1b (4800,6000), `D3` out 1b (6600,0), `D4` out 1b (7200,0), `D5` out 1b (7800,0), `D6` out 1b (8400,0), `D7` out 1b (9000,0), `D8` out 1b (4800,0), `D9` out 1b (5400,0), `D10` out 1b (10200,0), `D11` out 1b (10800,0), `D12` out 1b (6000,0), `D13` out 1b (9600,0), `D14` out 1b (6000,6000), `D15` out 1b (6600,6000), `D16` out 1b (7200,6000), `D17` out 1b (8400,6000), `D18` out 1b (9000,6000), `X` out 10b (2400,6000), `ALU` out 4b (3600,0), `BusA` out 3b (2400,0), `A` in 10b (0,3000)

## MRR
`hades.models.microjava.MRR` — memory read register for Microjava 2
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(7200,1800)
- portas: `CLK` in 1b (600,1800), `NR` in 1b (1200,0), `rd` in 1b (0,1200), `wr` in 1b (7200,1200), `D` in 16b (7200,600), `Q` out 16b (0,600), `V` out 16b

## PcReg
`hades.models.microjava.PcReg` — program counter register for Microjava 2
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(7200,1800)
- portas: `CLK` in 1b (600,1800), `NR` in 1b (1200,0), `rd` in 1b (7200,1200), `wr` in 1b (0,1200), `D` in 16b (0,600), `Q` out 16b (7200,600), `V` out 16b, `inc` in 1b (6600,0), `inc2` in 1b (6000,0)

## RAMoe
`hades.models.microjava.RAMoe` — main memory for Microjava 2
- params: `1001 16 16`; bbox (0,0)..(6000,4200)
- portas: `A` in 4b (0,1800), `DIN` in 16b (3000,0), `DOUT` out 16b (4200,0), `nWE` in 1b (0,2400), `nCS` in 1b (0,1200), `nOE` in 1b (0,3000)

## ROMoe
`hades.models.microjava.ROMoe` — main program memory for Microjava 2
- params: `1001 16 16`; bbox (0,0)..(6000,4200)
- portas: `A` in 4b (0,1800), `D` out 16b (4200,0), `nCS` in 1b (0,1200), `nOE` in 1b (0,3000)

## RegR
`hades.models.microjava.RegR` — D-type register with asynchronous reset
- params: `1001 16 UUUUUUUUUUUUUUUU_B 1.0E-8`; bbox (0,0)..(3600,2400)
- portas: `CLK` in 1b (0,600), `NR` in 1b (0,1200), `D` in 16b (1800,2400), `Q` out 16b (1800,0)
