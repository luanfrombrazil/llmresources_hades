# hades.models.register

Gerado do hades.jar com parâmetros padrão. ✅ = doc em `components/`. Demais: documentar antes de usar (`ADICIONANDO_COMPONENTES.md`).

## CounterRE16
`hades.models.register.CounterRE16` — edge-triggered 16-bit parallel output synchronous counter 
- params: `1001 1.0E-8 0 65535`; bbox (0,0)..(6000,11400)
- portas: `Q0` out 1b (6000,10800), `Q1` out 1b (6000,10200), `Q2` out 1b (6000,9600), `Q3` out 1b (6000,9000), `Q4` out 1b (6000,8400), `Q5` out 1b (6000,7800), `Q6` out 1b (6000,7200), `Q7` out 1b (6000,6600), `Q8` out 1b (6000,6000), `Q9` out 1b (6000,5400), `Q10` out 1b (6000,4800), `Q11` out 1b (6000,4200), `Q12` out 1b (6000,3600), `Q13` out 1b (6000,3000), `Q14` out 1b (6000,2400), `Q15` out 1b (6000,1800), `clk` in 1b (0,10200), `nreset` in 1b (0,10800), `enable` in 1b (0,600), `cout` out 1b (6000,600)

## CounterRE8
`hades.models.register.CounterRE8` — edge-triggered 8-bit parallel output synchronous counter
- params: `1001 1.0E-8 0 255`; bbox (0,0)..(6000,6600)
- portas: `Q0` out 1b (6000,6000), `Q1` out 1b (6000,5400), `Q2` out 1b (6000,4800), `Q3` out 1b (6000,4200), `Q4` out 1b (6000,3600), `Q5` out 1b (6000,3000), `Q6` out 1b (6000,2400), `Q7` out 1b (6000,1800), `clk` in 1b (0,5400), `nreset` in 1b (0,6000), `enable` in 1b (0,600), `cout` out 1b (6000,600)

## LFSRAnalyzer16
`hades.models.register.LFSRAnalyzer16` — 16-bit parallel input LFSR signature analysis register.
- params: `1001 1.0E-8 13534451 0`; bbox (0,0)..(6000,11400)
- portas: `D0` in 1b (0,10800), `D1` in 1b (0,10200), `D2` in 1b (0,9600), `D3` in 1b (0,9000), `D4` in 1b (0,8400), `D5` in 1b (0,7800), `D6` in 1b (0,7200), `D7` in 1b (0,6600), `D8` in 1b (0,6000), `D9` in 1b (0,5400), `D10` in 1b (0,4800), `D11` in 1b (0,4200), `D12` in 1b (0,3600), `D13` in 1b (0,3000), `D14` in 1b (0,2400), `D15` in 1b (0,1800), `CLK` in 1b (0,600), `NRESET` in 1b (0,1200)

## LFSRAnalyzer24
`hades.models.register.LFSRAnalyzer24` — 24-bit parallel input LFSR signature analysis register.
- params: `1001 1.0E-8 13534451 0`; bbox (0,0)..(6000,16200)
- portas: `D0` in 1b (0,15600), `D1` in 1b (0,15000), `D2` in 1b (0,14400), `D3` in 1b (0,13800), `D4` in 1b (0,13200), `D5` in 1b (0,12600), `D6` in 1b (0,12000), `D7` in 1b (0,11400), `D8` in 1b (0,10800), `D9` in 1b (0,10200), `D10` in 1b (0,9600), `D11` in 1b (0,9000), `D12` in 1b (0,8400), `D13` in 1b (0,7800), `D14` in 1b (0,7200), `D15` in 1b (0,6600), `D16` in 1b (0,6000), `D17` in 1b (0,5400), `D18` in 1b (0,4800), `D19` in 1b (0,4200), `D20` in 1b (0,3600), `D21` in 1b (0,3000), `D22` in 1b (0,2400), `D23` in 1b (0,1800), `CLK` in 1b (0,600), `NRESET` in 1b (0,1200)

## LFSRAnalyzer32
`hades.models.register.LFSRAnalyzer32` — 32-bit parallel input LFSR signature analysis register.
- params: `1001 1.0E-8 13534451 0`; bbox (0,0)..(6000,21000)
- portas: `D0` in 1b (0,20400), `D1` in 1b (0,19800), `D2` in 1b (0,19200), `D3` in 1b (0,18600), `D4` in 1b (0,18000), `D5` in 1b (0,17400), `D6` in 1b (0,16800), `D7` in 1b (0,16200), `D8` in 1b (0,15600), `D9` in 1b (0,15000), `D10` in 1b (0,14400), `D11` in 1b (0,13800), `D12` in 1b (0,13200), `D13` in 1b (0,12600), `D14` in 1b (0,12000), `D15` in 1b (0,11400), `D16` in 1b (0,10800), `D17` in 1b (0,10200), `D18` in 1b (0,9600), `D19` in 1b (0,9000), `D20` in 1b (0,8400), `D21` in 1b (0,7800), `D22` in 1b (0,7200), `D23` in 1b (0,6600), `D24` in 1b (0,6000), `D25` in 1b (0,5400), `D26` in 1b (0,4800), `D27` in 1b (0,4200), `D28` in 1b (0,3600), `D29` in 1b (0,3000), `D30` in 1b (0,2400), `D31` in 1b (0,1800), `CLK` in 1b (0,600), `NRESET` in 1b (0,1200)

## LFSRAnalyzer8
`hades.models.register.LFSRAnalyzer8` — 8-bit parallel input LFSR signature analysis register.
- params: `1001 1.0E-8 13534451 0`; bbox (0,0)..(6000,6600)
- portas: `D0` in 1b (0,6000), `D1` in 1b (0,5400), `D2` in 1b (0,4800), `D3` in 1b (0,4200), `D4` in 1b (0,3600), `D5` in 1b (0,3000), `D6` in 1b (0,2400), `D7` in 1b (0,1800), `CLK` in 1b (0,600), `NRESET` in 1b (0,1200)

## LFSRGenerator16
`hades.models.register.LFSRGenerator16` — 16-bit parallel output LFSR register.
- params: `1001 1.0E-8 13534451`; bbox (0,0)..(6000,10200)
- portas: `Q0` out 1b (6000,9600), `Q1` out 1b (6000,9000), `Q2` out 1b (6000,8400), `Q3` out 1b (6000,7800), `Q4` out 1b (6000,7200), `Q5` out 1b (6000,6600), `Q6` out 1b (6000,6000), `Q7` out 1b (6000,5400), `Q8` out 1b (6000,4800), `Q9` out 1b (6000,4200), `Q10` out 1b (6000,3600), `Q11` out 1b (6000,3000), `Q12` out 1b (6000,2400), `Q13` out 1b (6000,1800), `Q14` out 1b (6000,1200), `Q15` out 1b (6000,600), `CLK` in 1b (0,600), `NRESET` in 1b (0,1200)

## LFSRGenerator24
`hades.models.register.LFSRGenerator24` — 24-bit parallel output LFSR register.
- params: `1001 1.0E-8 13534451`; bbox (0,0)..(6000,15000)
- portas: `Q0` out 1b (6000,14400), `Q1` out 1b (6000,13800), `Q2` out 1b (6000,13200), `Q3` out 1b (6000,12600), `Q4` out 1b (6000,12000), `Q5` out 1b (6000,11400), `Q6` out 1b (6000,10800), `Q7` out 1b (6000,10200), `Q8` out 1b (6000,9600), `Q9` out 1b (6000,9000), `Q10` out 1b (6000,8400), `Q11` out 1b (6000,7800), `Q12` out 1b (6000,7200), `Q13` out 1b (6000,6600), `Q14` out 1b (6000,6000), `Q15` out 1b (6000,5400), `Q16` out 1b (6000,4800), `Q17` out 1b (6000,4200), `Q18` out 1b (6000,3600), `Q19` out 1b (6000,3000), `Q20` out 1b (6000,2400), `Q21` out 1b (6000,1800), `Q22` out 1b (6000,1200), `Q23` out 1b (6000,600), `CLK` in 1b (0,600), `NRESET` in 1b (0,1200)

## LFSRGenerator32
`hades.models.register.LFSRGenerator32` — 32-bit parallel output LFSR register.
- params: `1001 1.0E-8 13534451`; bbox (0,0)..(6000,19800)
- portas: `Q0` out 1b (6000,19200), `Q1` out 1b (6000,18600), `Q2` out 1b (6000,18000), `Q3` out 1b (6000,17400), `Q4` out 1b (6000,16800), `Q5` out 1b (6000,16200), `Q6` out 1b (6000,15600), `Q7` out 1b (6000,15000), `Q8` out 1b (6000,14400), `Q9` out 1b (6000,13800), `Q10` out 1b (6000,13200), `Q11` out 1b (6000,12600), `Q12` out 1b (6000,12000), `Q13` out 1b (6000,11400), `Q14` out 1b (6000,10800), `Q15` out 1b (6000,10200), `Q16` out 1b (6000,9600), `Q17` out 1b (6000,9000), `Q18` out 1b (6000,8400), `Q19` out 1b (6000,7800), `Q20` out 1b (6000,7200), `Q21` out 1b (6000,6600), `Q22` out 1b (6000,6000), `Q23` out 1b (6000,5400), `Q24` out 1b (6000,4800), `Q25` out 1b (6000,4200), `Q26` out 1b (6000,3600), `Q27` out 1b (6000,3000), `Q28` out 1b (6000,2400), `Q29` out 1b (6000,1800), `Q30` out 1b (6000,1200), `Q31` out 1b (6000,600), `CLK` in 1b (0,600), `NRESET` in 1b (0,1200)

## LFSRGenerator8
`hades.models.register.LFSRGenerator8` — 8-bit parallel output LFSR register.
- params: `1001 1.0E-8 13534451`; bbox (0,0)..(6000,5400)
- portas: `Q0` out 1b (6000,4800), `Q1` out 1b (6000,4200), `Q2` out 1b (6000,3600), `Q3` out 1b (6000,3000), `Q4` out 1b (6000,2400), `Q5` out 1b (6000,1800), `Q6` out 1b (6000,1200), `Q7` out 1b (6000,600), `CLK` in 1b (0,600), `NRESET` in 1b (0,1200)

## Register
`hades.models.register.Register` — n-bit D-type register with visualization.
- params: `1001 4 8.0E-9`; bbox (0,0)..(6000,1200) dinâmico
- portas: `D0` passive_in 1b (5400,0), `D1` passive_in 1b (4200,0), `D2` passive_in 1b (3000,0), `D3` passive_in 1b (1800,0), `Q0` out 1b (5400,1200), `Q1` out 1b (4200,1200), `Q2` out 1b (3000,1200), `Q3` out 1b (1800,1200), `C` in 1b (600,0)

## RegisterR
`hades.models.register.RegisterR` — n-bit D-type register with visualization.
- params: `1001 4 8.0E-9`; bbox (0,0)..(6000,1200) dinâmico
- portas: `D0` passive_in 1b (5400,0), `D1` passive_in 1b (4200,0), `D2` passive_in 1b (3000,0), `D3` passive_in 1b (1800,0), `Q0` out 1b (5400,1200), `Q1` out 1b (4200,1200), `Q2` out 1b (3000,1200), `Q3` out 1b (1800,1200), `C` in 1b (600,0), `NR` in 1b (0,900)

## RegisterRE
`hades.models.register.RegisterRE` — n-bit D-type register with visualization.
- params: `1001 4 8.0E-9`; bbox (0,0)..(6000,1200) dinâmico
- portas: `D0` passive_in 1b (5400,0), `D1` passive_in 1b (4200,0), `D2` passive_in 1b (3000,0), `D3` passive_in 1b (1800,0), `Q0` out 1b (5400,1200), `Q1` out 1b (4200,1200), `Q2` out 1b (3000,1200), `Q3` out 1b (1800,1200), `C` in 1b (600,0), `NR` in 1b (0,900), `EN` in 1b (0,300)

## ShiftRegister
`hades.models.register.ShiftRegister` — n-bit D-type shift-register with visualization.
- params: `1001 4 8.0E-9`; bbox (0,0)..(6000,1200) dinâmico
- portas: `D0` passive_in 1b (5400,0), `D1` passive_in 1b (4200,0), `D2` passive_in 1b (3000,0), `D3` passive_in 1b (1800,0), `Q0` out 1b (5400,1200), `Q1` out 1b (4200,1200), `Q2` out 1b (3000,1200), `Q3` out 1b (1800,1200), `C` in 1b (600,0), `NR` in 1b (0,900), `SE` in 1b (0,600), `Sin` in 1b (1200,0), `Sout` out 1b
