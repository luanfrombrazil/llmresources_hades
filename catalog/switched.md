# Catálogo HADES — pacote `hades.models.switched`

Gerado automaticamente a partir do `hades.jar` (parâmetros PADRÃO). Componentes marcados com ✅ têm documentação detalhada em `components/`.
Para os demais: portas, posições e bbox valem para os parâmetros padrão; componentes de largura variável mudam com `n_bits`. Antes de usar um deles pela primeira vez, documente-o (veja `ADICIONANDO_COMPONENTES.md`).

## AnimatedTgate

`hades.models.switched.AnimatedTgate` — simplified switch-level simulation model of transmission-gate

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` inout 1b @(0,1200), `B` inout 1b @(2400,1200), `C` in 1b @(1200,0)

## Bulb

`hades.models.switched.Bulb` — animated switch-level simulation model of a lightbulb.

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1200, 1200)
- Portas: `A` in 1b @(0,600), `B` in 1b @(1200,600)

## BulbBig

`hades.models.switched.BulbBig` — animated switch-level simulation model of a lightbulb.

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `B` in 1b @(2400,1200)

## ISwitch

`hades.models.switched.ISwitch` — interactive switch.

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(3600, 3000)
- Portas: `A` inout 1b @(0,1800), `A0` inout 1b @(3600,2400), `A1` inout 1b @(3600,1200)

## ISwitch2

`hades.models.switched.ISwitch2` — interactive switch (two separate changeover switches).

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(3600, 5400)
- Portas: `A` inout 1b @(0,1800), `A0` inout 1b @(3600,2400), `A1` inout 1b @(3600,1200), `B` inout 1b @(0,4200), `B0` inout 1b @(3600,4800), `B1` inout 1b @(3600,3600)

## NTRAN

`hades.models.switched.NTRAN` — simplified switch-level simulation model of n-channel transistor.

- Parâmetros padrão: `1001 6.0E-9`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` inout 1b @(1800,0), `B` inout 1b @(1800,2400), `C` in 1b @(0,1200)

## NTRANh

`hades.models.switched.NTRANh` — simplified switch-level simulation model of n-channel transistor.

- Parâmetros padrão: `1001 6.0E-9`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` inout 1b @(0,1800), `B` inout 1b @(2400,1800), `C` in 1b @(1200,0)

## PTRAN

`hades.models.switched.PTRAN` — simplified switch-level simulation model of p-channel transistor.

- Parâmetros padrão: `1001 6.0E-9`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` inout 1b @(1800,0), `B` inout 1b @(1800,2400), `C` in 1b @(0,1200)

## Relay1

`hades.models.switched.Relay1` — switch-level simulation model of a relay with 

- Parâmetros padrão: `1001 6.0E-9`
- bbox: (0, 0)..(3600, 4200)
- Portas: `A` inout 1b @(0,3000), `A0` inout 1b @(3600,3600), `A1` inout 1b @(3600,2400), `X` in 1b @(0,1200), `Y` in 1b @(3600,1200)

## Relay2

`hades.models.switched.Relay2` — switch-level simulation model of a relay with 

- Parâmetros padrão: `1001 6.0E-9`
- bbox: (0, 0)..(3600, 6600)
- Portas: `A` inout 1b @(0,3000), `A0` inout 1b @(3600,3600), `A1` inout 1b @(3600,2400), `B` inout 1b @(0,5400), `B0` inout 1b @(3600,6000), `B1` inout 1b @(3600,4800), `X` in 1b @(0,1200), `Y` in 1b @(3600,1200)

## Relay4

`hades.models.switched.Relay4` — switch-level simulation model of a relay with 

- Parâmetros padrão: `1001 6.0E-9`
- bbox: (0, 0)..(3600, 11400)
- Portas: `A` inout 1b @(0,3000), `A0` inout 1b @(3600,3600), `A1` inout 1b @(3600,2400), `B` inout 1b @(0,5400), `B0` inout 1b @(3600,6000), `B1` inout 1b @(3600,4800), `C` inout 1b @(0,7800), `C0` inout 1b @(3600,8400), `C1` inout 1b @(3600,7200), `D` inout 1b @(0,10200), `D0` inout 1b @(3600,10800), `D1` inout 1b @(3600,9600), `X` in 1b @(0,1200), `Y` in 1b @(3600,1200)

## Switch

`hades.models.switched.Switch` — transmission-gate switch

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(3600, 2400)
- Portas: `A` inout 1b @(0,1200), `B` inout 1b @(3600,1200), `C` in 1b @(1800,0)

## TGATE

`hades.models.switched.TGATE` — simplified switch-level simulation model of transmission-gate

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` inout 1b @(0,1200), `B` inout 1b @(2400,1200), `C` in 1b @(1200,0)
