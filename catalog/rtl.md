# Catálogo HADES — pacote `hades.models.rtl`

Gerado automaticamente a partir do `hades.jar` (parâmetros PADRÃO). Componentes marcados com ✅ têm documentação detalhada em `components/`.
Para os demais: portas, posições e bbox valem para os parâmetros padrão; componentes de largura variável mudam com `n_bits`. Antes de usar um deles pela primeira vez, documente-o (veja `ADICIONANDO_COMPONENTES.md`).

## IDT6116

`hades.models.rtl.IDT6116` — static CMOS RAM of 2Kx8 bits.

- Parâmetros padrão: `1001 /hades/models/rtl/empty.rom`
- bbox: (0, 0)..(6600, 10200)
- Portas: `A0` in 1b @(0,9000), `A1` in 1b @(0,8400), `A2` in 1b @(0,7800), `A3` in 1b @(0,7200), `A4` in 1b @(0,6600), `A5` in 1b @(0,6000), `A6` in 1b @(0,5400), `A7` in 1b @(0,4800), `A8` in 1b @(0,4200), `A9` in 1b @(0,3600), `A10` in 1b @(0,3000), `D0` inout 1b @(5400,10200), `D1` inout 1b @(4800,10200), `D2` inout 1b @(4200,10200), `D3` inout 1b @(3600,10200), `D4` inout 1b @(3000,10200), `D5` inout 1b @(2400,10200), `D6` inout 1b @(1800,10200), `D7` inout 1b @(1200,10200), `nCS` in 1b @(0,600), `nOE` in 1b @(0,1800), `nWE` in 1b @(0,1200)

## IDT6164

`hades.models.rtl.IDT6164` — static CMOS RAM of 2Kx8 bits.

- Parâmetros padrão: `1001 /hades/models/rtl/empty.rom`
- bbox: (0, 0)..(6600, 11400)
- Portas: `A0` in 1b @(0,10200), `A1` in 1b @(0,9600), `A2` in 1b @(0,9000), `A3` in 1b @(0,8400), `A4` in 1b @(0,7800), `A5` in 1b @(0,7200), `A6` in 1b @(0,6600), `A7` in 1b @(0,6000), `A8` in 1b @(0,5400), `A9` in 1b @(0,4800), `A10` in 1b @(0,4200), `A11` in 1b @(0,3600), `A12` in 1b @(0,3000), `D0` inout 1b @(5400,11400), `D1` inout 1b @(4800,11400), `D2` inout 1b @(4200,11400), `D3` inout 1b @(3600,11400), `D4` inout 1b @(3000,11400), `D5` inout 1b @(2400,11400), `D6` inout 1b @(1800,11400), `D7` inout 1b @(1200,11400), `nCS` in 1b @(0,600), `nOE` in 1b @(0,1800), `nWE` in 1b @(0,1200)

## RAM_256x8

`hades.models.rtl.RAM_256x8` — random-access memory cell with 256x8 bits.

- Parâmetros padrão: `1001 /hades/models/rtl/RAM_256x8.rom`
- bbox: (0, 0)..(3600, 13800)
- Portas: `A0` passive_in 1b @(0,7200), `A1` passive_in 1b @(0,6600), `A2` passive_in 1b @(0,6000), `A3` passive_in 1b @(0,5400), `A4` passive_in 1b @(0,4800), `A5` passive_in 1b @(0,4200), `A6` passive_in 1b @(0,3600), `A7` passive_in 1b @(0,3000), `DI0` passive_in 1b @(0,13200), `DI1` passive_in 1b @(0,12600), `DI2` passive_in 1b @(0,12000), `DI3` passive_in 1b @(0,11400), `DI4` passive_in 1b @(0,10800), `DI5` passive_in 1b @(0,10200), `DI6` passive_in 1b @(0,9600), `DI7` passive_in 1b @(0,9000), `DO0` out 1b @(3600,13200), `DO1` out 1b @(3600,12600), `DO2` out 1b @(3600,12000), `DO3` out 1b @(3600,11400), `DO4` out 1b @(3600,10800), `DO5` out 1b @(3600,10200), `DO6` out 1b @(3600,9600), `DO7` out 1b @(3600,9000), `nCS` in 1b @(0,600), `nME` in 1b @(0,1800), `nWE` in 1b @(0,1200)

## ROM_1Kx8

`hades.models.rtl.ROM_1Kx8` — static read-only memory of 1024 words of 8 bit.

- Parâmetros padrão: `1001 /hades/models/rtl/ROM_1Kx8.rom`
- bbox: (0, 0)..(3600, 9000)
- Portas: `nCS` in 1b @(0,1200), `nOE` in 1b @(0,600), `Y0` out 1b @(3600,7200), `Y1` out 1b @(3600,6600), `Y2` out 1b @(3600,6000), `Y3` out 1b @(3600,5400), `Y4` out 1b @(3600,4800), `Y5` out 1b @(3600,4200), `Y6` out 1b @(3600,3600), `Y7` out 1b @(3600,3000), `A0` in 1b @(0,8400), `A1` in 1b @(0,7800), `A2` in 1b @(0,7200), `A3` in 1b @(0,6600), `A4` in 1b @(0,6000), `A5` in 1b @(0,5400), `A6` in 1b @(0,4800), `A7` in 1b @(0,4200), `A8` in 1b @(0,3600), `A9` in 1b @(0,3000)

## ROM_256x8

`hades.models.rtl.ROM_256x8` — static read-only memory of 256 words of 8 bit.

- Parâmetros padrão: `1001 /hades/models/rtl/ROM_1Kx8.rom`
- bbox: (0, 0)..(3600, 9000)
- Portas: `nCS` in 1b @(0,1200), `nOE` in 1b @(0,600), `Y0` out 1b @(3600,7200), `Y1` out 1b @(3600,6600), `Y2` out 1b @(3600,6000), `Y3` out 1b @(3600,5400), `Y4` out 1b @(3600,4800), `Y5` out 1b @(3600,4200), `Y6` out 1b @(3600,3600), `Y7` out 1b @(3600,3000), `A0` in 1b @(0,8400), `A1` in 1b @(0,7800), `A2` in 1b @(0,7200), `A3` in 1b @(0,6600), `A4` in 1b @(0,6000), `A5` in 1b @(0,5400), `A6` in 1b @(0,4800), `A7` in 1b @(0,4200)

## ROM_64Kx8

`hades.models.rtl.ROM_64Kx8` — static read-only memory of 64K words of 8 bit.

- Parâmetros padrão: `1001 /hades/models/rtl/ROM_1Kx8.rom`
- bbox: (0, 0)..(3600, 13200)
- Portas: `nCS` in 1b @(0,1200), `nOE` in 1b @(0,600), `Y0` out 1b @(3600,7200), `Y1` out 1b @(3600,6600), `Y2` out 1b @(3600,6000), `Y3` out 1b @(3600,5400), `Y4` out 1b @(3600,4800), `Y5` out 1b @(3600,4200), `Y6` out 1b @(3600,3600), `Y7` out 1b @(3600,3000), `A0` in 1b @(0,12000), `A1` in 1b @(0,11400), `A2` in 1b @(0,10800), `A3` in 1b @(0,10200), `A4` in 1b @(0,9600), `A5` in 1b @(0,9000), `A6` in 1b @(0,8400), `A7` in 1b @(0,7800), `A8` in 1b @(0,7200), `A9` in 1b @(0,6600), `A10` in 1b @(0,6000), `A11` in 1b @(0,5400), `A12` in 1b @(0,4800), `A13` in 1b @(0,4200), `A14` in 1b @(0,3600), `A15` in 1b @(0,3000)

## ROM_64x8

`hades.models.rtl.ROM_64x8` — static read-only memory of 64 words of 8 bit.

- Parâmetros padrão: `1001 /hades/models/rtl/ROM_1Kx8.rom`
- bbox: (0, 0)..(3600, 9000)
- Portas: `nCS` in 1b @(0,1200), `nOE` in 1b @(0,600), `Y0` out 1b @(3600,7200), `Y1` out 1b @(3600,6600), `Y2` out 1b @(3600,6000), `Y3` out 1b @(3600,5400), `Y4` out 1b @(3600,4800), `Y5` out 1b @(3600,4200), `Y6` out 1b @(3600,3600), `Y7` out 1b @(3600,3000), `A0` in 1b @(0,8400), `A1` in 1b @(0,7800), `A2` in 1b @(0,7200), `A3` in 1b @(0,6600), `A4` in 1b @(0,6000), `A5` in 1b @(0,5400)

## ROM_8Kx8

`hades.models.rtl.ROM_8Kx8` — static read-only memory of 8K words of 8 bit.

- Parâmetros padrão: `1001 /hades/models/rtl/ROM_1Kx8.rom`
- bbox: (0, 0)..(3600, 10800)
- Portas: `nCS` in 1b @(0,1200), `nOE` in 1b @(0,600), `Y0` out 1b @(3600,7200), `Y1` out 1b @(3600,6600), `Y2` out 1b @(3600,6000), `Y3` out 1b @(3600,5400), `Y4` out 1b @(3600,4800), `Y5` out 1b @(3600,4200), `Y6` out 1b @(3600,3600), `Y7` out 1b @(3600,3000), `A0` in 1b @(0,10200), `A1` in 1b @(0,9600), `A2` in 1b @(0,9000), `A3` in 1b @(0,8400), `A4` in 1b @(0,7800), `A5` in 1b @(0,7200), `A6` in 1b @(0,6600), `A7` in 1b @(0,6000), `A8` in 1b @(0,5400), `A9` in 1b @(0,4800), `A10` in 1b @(0,4200), `A11` in 1b @(0,3600), `A12` in 1b @(0,3000)
