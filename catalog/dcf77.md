# hades.models.dcf77

Gerado do hades.jar com parâmetros padrão. ✅ = doc em `components/`. Demais: documentar antes de usar (`ADICIONANDO_COMPONENTES.md`).

## Dcf77Clock
`hades.models.dcf77.Dcf77Clock` — DCF77 time signal decoder / digital clock.
- params: `1001`; bbox (0,0)..(4800,3600) dinâmico
- portas: `dcf_in` in 1b (0,3000)

## Dcf77Sender
`hades.models.dcf77.Dcf77Sender` — DCF77 time signal sender.
- params: `1001 17 45 9 20 10 26 3 0.0`; bbox (0,0)..(3600,2400)
- portas: `dcf77` out 1b (3600,1200)
