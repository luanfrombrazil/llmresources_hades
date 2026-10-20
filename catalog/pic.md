# Catálogo HADES — pacote `hades.models.pic`

Gerado automaticamente a partir do `hades.jar` (parâmetros PADRÃO). Componentes marcados com ✅ têm documentação detalhada em `components/`.
Para os demais: portas, posições e bbox valem para os parâmetros padrão; componentes de largura variável mudam com `n_bits`. Antes de usar um deles pela primeira vez, documente-o (veja `ADICIONANDO_COMPONENTES.md`).

## TurboPic16C84

`hades.models.pic.TurboPic16C84` — "Turbo" PIC16C84

- Parâmetros padrão: `1001 4000000.0 null`
- bbox: (0, 0)..(3000, 10200)
- Portas: `CLKIN` in 1b @(3000,1800), `CLKOUT` out 1b @(3000,2400), `/MCLR` in 1b @(0,2400), `A0` inout 1b @(3000,1200), `A1` inout 1b @(3000,600), `A2` inout 1b @(0,600), `A3` inout 1b @(0,1200), `A4` inout 1b @(0,1800), `B0` inout 1b @(0,3600), `B1` inout 1b @(0,4200), `B2` inout 1b @(0,4800), `B3` inout 1b @(0,5400), `B4` inout 1b @(3000,5400), `B5` inout 1b @(3000,4800), `B6` inout 1b @(3000,4200), `B7` inout 1b @(3000,3600), `PC` out 1b @(3000,6600), `W` out 1b @(3000,7200), `STATUS` out 1b @(3000,7800), `INTCON` out 1b @(3000,8400), `INSTR` out 1b @(3000,9000)
