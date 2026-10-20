# Catálogo HADES — pacote `hades.models.fsm`

Gerado automaticamente a partir do `hades.jar` (parâmetros PADRÃO). Componentes marcados com ✅ têm documentação detalhada em `components/`.
Para os demais: portas, posições e bbox valem para os parâmetros padrão; componentes de largura variável mudam com `n_bits`. Antes de usar um deles pela primeira vez, documente-o (veja `ADICIONANDO_COMPONENTES.md`).

## FsmWrapper

`hades.models.fsm.FsmWrapper` — Embedded finite-state machine.

- Parâmetros padrão: `1001 /hades/models/fsm/default.fsm`
- bbox: (0, 0)..(4800, 6600) (dinâmico)
- Portas: `nreset` in 1b @(0,600), `clk` in 1b @(0,1200), `state` out 1b @(4800,1200)
