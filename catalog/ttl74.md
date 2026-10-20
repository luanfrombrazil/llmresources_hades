# Catálogo HADES — pacote `hades.models.ttl74`

Gerado automaticamente a partir do `hades.jar` (parâmetros PADRÃO). Componentes marcados com ✅ têm documentação detalhada em `components/`.
Para os demais: portas, posições e bbox valem para os parâmetros padrão; componentes de largura variável mudam com `n_bits`. Antes de usar um deles pela primeira vez, documente-o (veja `ADICIONANDO_COMPONENTES.md`).

## SN7400

`hades.models.ttl74.SN7400` — cription]

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(7200, 18000)
- Portas: `dummy` <unknown> 1b (sem posição), `A1` in 1b @(0,2400), `B1` in 1b @(0,4800), `Y1` out 1b @(7200,3600), `A2` in 1b @(0,6000), `B2` in 1b @(0,8400), `Y2` out 1b @(7200,7200), `GND` in 1b (sem posição), `A3` in 1b @(0,9600), `B3` in 1b @(0,12000), `Y3` out 1b @(7200,10800), `A4` in 1b @(0,13200), `B4` in 1b @(0,15600), `Y4` out 1b @(7200,14400), `VCC` in 1b (sem posição)

## SN7400_pinout

`hades.models.ttl74.SN7400_pinout` — [description]

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(3600, 9600)
- Portas: `dummy` <unknown> 1b (sem posição), `A1` in 1b @(0,1200), `B1` in 1b @(0,2400), `Y1` out 1b @(0,3600), `A2` in 1b @(0,4800), `B2` in 1b @(0,6000), `Y2` out 1b @(0,7200), `GND` in 1b @(0,8400), `A3` in 1b @(3600,2400), `B3` in 1b @(3600,3600), `Y3` out 1b @(3600,4800), `A4` in 1b @(3600,6000), `B4` in 1b @(3600,7200), `Y4` out 1b @(3600,8400), `VCC` in 1b @(3600,1200)

## SN7405

`hades.models.ttl74.SN7405` — 7405 6x INV gate

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(7200, 18000)
- Portas: `dummy` <unknown> 1b (sem posição), `A1` in 1b @(0,2400), `Y1` out 1b @(7200,2400), `A2` in 1b @(0,4800), `Y2` out 1b @(7200,4800), `A3` in 1b @(0,7200), `Y3` out 1b @(7200,7200), `GND` in 1b (sem posição), `Y6` out 1b @(7200,14400), `A6` in 1b @(0,14400), `Y5` out 1b @(7200,12000), `A5` in 1b @(0,12000), `Y4` out 1b @(7200,9600), `A4` in 1b @(0,9600), `VCC` in 1b (sem posição)

## SN7405_pinout

`hades.models.ttl74.SN7405_pinout` — 7405 6x INV gate

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(3600, 9600)
- Portas: `dummy` <unknown> 1b (sem posição), `A1` in 1b @(0,1200), `Y1` out 1b @(0,2400), `A2` in 1b @(0,3600), `Y2` out 1b @(0,4800), `A3` in 1b @(0,6000), `Y3` out 1b @(0,7200), `GND` in 1b @(0,8400), `Y6` out 1b @(3600,8400), `A6` in 1b @(3600,7200), `Y5` out 1b @(3600,6000), `A5` in 1b @(3600,4800), `Y4` out 1b @(3600,3600), `A4` in 1b @(3600,2400), `VCC` in 1b @(3600,1200)

## SN7408_pinout

`hades.models.ttl74.SN7408_pinout` — 7408 4x AND2 gate

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(3600, 9600)
- Portas: `dummy` <unknown> 1b (sem posição), `A1` in 1b @(0,1200), `B1` in 1b @(0,2400), `Y1` out 1b @(0,3600), `A2` in 1b @(0,4800), `B2` in 1b @(0,6000), `Y2` out 1b @(0,7200), `GND` in 1b @(0,8400), `A3` in 1b @(3600,2400), `B3` in 1b @(3600,3600), `Y3` out 1b @(3600,4800), `A4` in 1b @(3600,6000), `B4` in 1b @(3600,7200), `Y4` out 1b @(3600,8400), `VCC` in 1b @(3600,1200)

## SN74189

`hades.models.ttl74.SN74189` — TTL-series 74189 16x4 bit RAM.

- Parâmetros padrão: `1001 /hades/models/rtl/empty.rom`
- bbox: (0, 0)..(2400, 6600)
- Portas: `A0` in 1b @(0,4800), `A1` in 1b @(0,4200), `A2` in 1b @(0,3600), `A3` in 1b @(0,3000), `D0` in 1b @(0,2400), `D1` in 1b @(0,1800), `D2` in 1b @(0,1200), `D3` in 1b @(0,600), `Q0` out 1b @(2400,2400), `Q1` out 1b @(2400,1800), `Q2` out 1b @(2400,1200), `Q3` out 1b @(2400,600), `NCS` in 1b @(0,5400), `R/NW` in 1b @(0,6000)

## SN74219

`hades.models.ttl74.SN74219` — TTL-series 74219 16x4 bit RAM.

- Parâmetros padrão: `1001 /hades/models/rtl/empty.rom`
- bbox: (0, 0)..(2400, 6600)
- Portas: `A0` in 1b @(0,4800), `A1` in 1b @(0,4200), `A2` in 1b @(0,3600), `A3` in 1b @(0,3000), `D0` in 1b @(0,2400), `D1` in 1b @(0,1800), `D2` in 1b @(0,1200), `D3` in 1b @(0,600), `Q0` out 1b @(2400,2400), `Q1` out 1b @(2400,1800), `Q2` out 1b @(2400,1200), `Q3` out 1b @(2400,600), `nCE` in 1b @(0,5400), `nWE` in 1b @(0,6000)

## SN7432_pinout

`hades.models.ttl74.SN7432_pinout` — 7432 4x OR2 gate

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(3600, 9600)
- Portas: `dummy` <unknown> 1b (sem posição), `A1` in 1b @(0,1200), `B1` in 1b @(0,2400), `Y1` out 1b @(0,3600), `A2` in 1b @(0,4800), `B2` in 1b @(0,6000), `Y2` out 1b @(0,7200), `GND` in 1b @(0,8400), `A3` in 1b @(3600,2400), `B3` in 1b @(3600,3600), `Y3` out 1b @(3600,4800), `A4` in 1b @(3600,6000), `B4` in 1b @(3600,7200), `Y4` out 1b @(3600,8400), `VCC` in 1b @(3600,1200)

## SN7449

`hades.models.ttl74.SN7449` — 7449 seven-segment decoder circuit.

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 6000)
- Portas: `dummy` <unknown> 1b (sem posição), `B` in 1b @(0,4200), `C` in 1b @(0,3600), `Ndark` in 1b @(0,600), `D` in 1b @(0,3000), `A` in 1b @(0,4800), `e` out 1b @(1800,3000), `GND` in 1b (sem posição), `d` out 1b @(1800,3600), `c` out 1b @(1800,4200), `b` out 1b @(1800,4800), `a` out 1b @(1800,5400), `g` out 1b @(1800,1800), `f` out 1b @(1800,2400), `VCC` in 1b (sem posição)

## SN7449_pinout

`hades.models.ttl74.SN7449_pinout` — TTL-series 7449 seven-segment decoder circuit.

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(3600, 9600)
- Portas: `dummy` <unknown> 1b (sem posição), `B` in 1b @(0,1200), `C` in 1b @(0,2400), `Ndark` in 1b @(0,3600), `D` in 1b @(0,4800), `A` in 1b @(0,6000), `e` out 1b @(0,7200), `GND` in 1b @(0,8400), `d` out 1b @(3600,8400), `c` out 1b @(3600,7200), `b` out 1b @(3600,6000), `a` out 1b @(3600,4800), `g` out 1b @(3600,3600), `f` out 1b @(3600,2400), `VCC` in 1b @(3600,1200)

## SN7486_pinout

`hades.models.ttl74.SN7486_pinout` — 7486 4x XOR2 gate

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(3600, 9600)
- Portas: `dummy` <unknown> 1b (sem posição), `A1` in 1b @(0,1200), `B1` in 1b @(0,2400), `Y1` out 1b @(0,3600), `A2` in 1b @(0,4800), `B2` in 1b @(0,6000), `Y2` out 1b @(0,7200), `GND` in 1b @(0,8400), `A3` in 1b @(3600,2400), `B3` in 1b @(3600,3600), `Y3` out 1b @(3600,4800), `A4` in 1b @(3600,6000), `B4` in 1b @(3600,7200), `Y4` out 1b @(3600,8400), `VCC` in 1b @(3600,1200)
