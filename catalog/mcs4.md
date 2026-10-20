# Catálogo HADES — pacote `hades.models.mcs4`

Gerado automaticamente a partir do `hades.jar` (parâmetros PADRÃO). Componentes marcados com ✅ têm documentação detalhada em `components/`.
Para os demais: portas, posições e bbox valem para os parâmetros padrão; componentes de largura variável mudam com `n_bits`. Antes de usar um deles pela primeira vez, documente-o (veja `ADICIONANDO_COMPONENTES.md`).

## i4001

`hades.models.mcs4.i4001` — Intel i4001 programmable ROM and I/O port.

- Parâmetros padrão: `1001 0 out out out out`
- bbox: (0, 0)..(4800, 19200)
- Portas: `D0` inout 1b @(0,1200), `D1` inout 1b @(0,3600), `D2` inout 1b @(0,6000), `D3` inout 1b @(0,8400), `Vss` in 1b @(0,10800), `phi1` in 1b @(0,13200), `phi2` in 1b @(0,15600), `SYNC` in 1b @(0,18000), `IO0` inout 1b @(4800,1200), `IO1` inout 1b @(4800,3600), `IO2` inout 1b @(4800,6000), `IO3` inout 1b @(4800,8400), `Vdd` in 1b @(4800,10800), `CM` in 1b @(4800,13200), `CL` in 1b @(4800,15600), `RESET` in 1b @(4800,18000)

## i4002

`hades.models.mcs4.i4002` — Intel i4002 20x4 bit RAM and 4 bit output port.

- Parâmetros padrão: `1001 4002-1`
- bbox: (0, 0)..(4800, 19200)
- Portas: `D0` inout 1b @(0,1200), `D1` inout 1b @(0,3600), `D2` inout 1b @(0,6000), `D3` inout 1b @(0,8400), `Vss` in 1b @(0,10800), `phi1` in 1b @(0,13200), `phi2` in 1b @(0,15600), `SYNC` in 1b @(0,18000), `O0` out 1b @(4800,1200), `O1` out 1b @(4800,3600), `O2` out 1b @(4800,6000), `O3` out 1b @(4800,8400), `Vdd` in 1b @(4800,10800), `CM` in 1b @(4800,13200), `P0` in 1b @(4800,15600), `RESET` in 1b @(4800,18000)

## i4003

`hades.models.mcs4.i4003` — Intel i4003 10 bit shift register and output expander.

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(4800, 19200)
- Portas: `CP` in 1b @(0,1200), `DataIn` in 1b @(0,3600), `Vss` in 1b @(0,10800), `E` in 1b @(4800,1200), `SerialOut` out 1b @(4800,3600), `Vdd` in 1b @(4800,6000), `Q0` out 1b @(0,6000), `Q1` out 1b @(0,8400), `Q2` out 1b @(0,13200), `Q3` out 1b @(0,15600), `Q4` out 1b @(0,18000), `Q5` out 1b @(4800,18000), `Q6` out 1b @(4800,15600), `Q7` out 1b @(4800,13200), `Q8` out 1b @(4800,10800), `Q9` out 1b @(4800,8400)
