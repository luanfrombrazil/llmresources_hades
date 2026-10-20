# Catálogo HADES — pacote `hades.models.special`

Gerado automaticamente a partir do `hades.jar` (parâmetros PADRÃO). Componentes marcados com ✅ têm documentação detalhada em `components/`.
Para os demais: portas, posições e bbox valem para os parâmetros padrão; componentes de largura variável mudam com `n_bits`. Antes de usar um deles pela primeira vez, documente-o (veja `ADICIONANDO_COMPONENTES.md`).

## Counter

`hades.models.special.Counter` — XXX

- Parâmetros padrão: `1001 0`
- bbox: (0, 0)..(6000, 2400)
- Portas: `D` in 1b @(0,1200), `C` in 1b @(0,1800)

## EdgeTrigger

`hades.models.special.EdgeTrigger` — XXX

- Parâmetros padrão: `1001 0 0 false true true`
- bbox: (0, 0)..(3600, 1200)
- Portas: `A` in 1b @(0,600), `Q` out 1b @(3600,600)

## HazardTrigger

`hades.models.special.HazardTrigger` — XXX

- Parâmetros padrão: `1001 0 1.0E-9 false true true`
- bbox: (0, 0)..(3600, 1200)
- Portas: `A` in 1b @(0,600), `Q` out 1b @(3600,600)

## MidiReceiver

`hades.models.special.MidiReceiver` — XXX

- Parâmetros padrão: ``
- bbox: (0, 0)..(3600, 2400)
- Portas: `RX` in 1b @(0,1200)

## ValueTrigger

`hades.models.special.ValueTrigger` — XXX

- Parâmetros padrão: `1001 0 false true true`
- bbox: (0, 0)..(3600, 1200)
- Portas: `A` in 1b @(0,600), `Q` out 1b @(3600,600)
