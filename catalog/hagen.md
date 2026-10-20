# hades.models.hagen

Gerado do hades.jar com parâmetros padrão. ✅ = doc em `components/`. Demais: documentar antes de usar (`ADICIONANDO_COMPONENTES.md`).

## ROM_8x8
`hades.models.hagen.ROM_8x8` — Read-only memory with 8 words of 8 bits each.
- params: `1001 /hades/models/rtl/ROM_1Kx8.rom`; bbox (0,0)..(3600,9000)
- portas: `nCS` in 1b (0,1200), `nOE` in 1b (0,600), `Y0` out 1b (3600,7200), `Y1` out 1b (3600,6600), `Y2` out 1b (3600,6000), `Y3` out 1b (3600,5400), `Y4` out 1b (3600,4800), `Y5` out 1b (3600,4200), `Y6` out 1b (3600,3600), `Y7` out 1b (3600,3000), `A0` in 1b (0,8400), `A1` in 1b (0,7800), `A2` in 1b (0,7200)

## SimpleShiftRegister
`hades.models.hagen.SimpleShiftRegister` — Shift register with reset input.
- params: `1001 8 8.0E-9 UUUUUUUU`; bbox (0,0)..(10800,1200) dinâmico
- portas: `D0` passive_in 1b, `D1` passive_in 1b, `D2` passive_in 1b, `D3` passive_in 1b, `D4` passive_in 1b, `D5` passive_in 1b, `D6` passive_in 1b, `D7` passive_in 1b, `Q0` out 1b (10200,1200), `Q1` out 1b (9000,1200), `Q2` out 1b (7800,1200), `Q3` out 1b (6600,1200), `Q4` out 1b (5400,1200), `Q5` out 1b (4200,1200), `Q6` out 1b (3000,1200), `Q7` out 1b (1800,1200), `C` in 1b (600,0), `NR` in 1b (0,600), `Sin` in 1b (10800,600)
