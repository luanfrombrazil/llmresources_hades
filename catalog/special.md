# hades.models.special

Gerado do hades.jar com parâmetros padrão. ✅ = doc em `components/`. Demais: documentar antes de usar (`ADICIONANDO_COMPONENTES.md`).

## Counter
`hades.models.special.Counter` — XXX
- params: `1001 0`; bbox (0,0)..(6000,2400)
- portas: `D` in 1b (0,1200), `C` in 1b (0,1800)

## EdgeTrigger
`hades.models.special.EdgeTrigger` — XXX
- params: `1001 0 0 false true true`; bbox (0,0)..(3600,1200)
- portas: `A` in 1b (0,600), `Q` out 1b (3600,600)

## HazardTrigger
`hades.models.special.HazardTrigger` — XXX
- params: `1001 0 1.0E-9 false true true`; bbox (0,0)..(3600,1200)
- portas: `A` in 1b (0,600), `Q` out 1b (3600,600)

## MidiReceiver
`hades.models.special.MidiReceiver` — XXX
- params: ``; bbox (0,0)..(3600,2400)
- portas: `RX` in 1b (0,1200)

## ValueTrigger
`hades.models.special.ValueTrigger` — XXX
- params: `1001 0 false true true`; bbox (0,0)..(3600,1200)
- portas: `A` in 1b (0,600), `Q` out 1b (3600,600)
