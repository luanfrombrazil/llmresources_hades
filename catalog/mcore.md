# Catálogo HADES — pacote `hades.models.mcore`

Gerado automaticamente a partir do `hades.jar` (parâmetros PADRÃO). Componentes marcados com ✅ têm documentação detalhada em `components/`.
Para os demais: portas, posições e bbox valem para os parâmetros padrão; componentes de largura variável mudam com `n_bits`. Antes de usar um deles pela primeira vez, documente-o (veja `ADICIONANDO_COMPONENTES.md`).

## DcoreRAM

`hades.models.mcore.DcoreRAM` — random-access memory for the D*CORE processor.

- Parâmetros padrão: `1001 16 16 0`
- bbox: (0, 0)..(6000, 4800)
- Portas: `A` in 5b @(0,2400), `DIN` in 16b @(3600,0), `DOUT` out 16b @(3600,4800), `nWE` in 1b @(0,3000), `nCS` in 1b @(0,1800), `nOE` in 1b @(0,3600)

## DcoreROM

`hades.models.mcore.DcoreROM` — read-only memory for the D*CORE processor.

- Parâmetros padrão: `1001 16 16 0`
- bbox: (0, 0)..(6000, 4800)
- Portas: `A` in 5b @(0,2400), `DOUT` out 16b @(3600,4800), `nCS` in 1b @(0,1800), `nOE` in 1b @(0,3000)
