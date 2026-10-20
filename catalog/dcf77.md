# Catálogo HADES — pacote `hades.models.dcf77`

Gerado automaticamente a partir do `hades.jar` (parâmetros PADRÃO). Componentes marcados com ✅ têm documentação detalhada em `components/`.
Para os demais: portas, posições e bbox valem para os parâmetros padrão; componentes de largura variável mudam com `n_bits`. Antes de usar um deles pela primeira vez, documente-o (veja `ADICIONANDO_COMPONENTES.md`).

## Dcf77Clock

`hades.models.dcf77.Dcf77Clock` — DCF77 time signal decoder / digital clock.

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(4800, 3600) (dinâmico)
- Portas: `dcf_in` in 1b @(0,3000)

## Dcf77Sender

`hades.models.dcf77.Dcf77Sender` — DCF77 time signal sender.

- Parâmetros padrão: `1001 17 45 9 20 10 26 3 0.0`
- bbox: (0, 0)..(3600, 2400)
- Portas: `dcf77` out 1b @(3600,1200)
