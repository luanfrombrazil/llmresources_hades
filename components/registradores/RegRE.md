# RegRE — Registrador de n bits com enable e reset

Classe: `hades.models.rtlib.register.RegRE`  
bbox: (0,0)..(3600,2400)

Q ← D na subida de CLK se ENA=1; NR=0 zera (assíncrono).

## Linha

```
hades.models.rtlib.register.RegRE <nome> <x> <y> @N 1001 32 00000000000000000000000000000000_B 1.0E-8
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits (1..63) |
| 2 | `valor` | exibido; binário `_B`; não define o estado inicial |
| 3 | `delay` | atraso em s (`1.0E-8`) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `CLK` | in | 1 | (0,1200) | esq |
| `NR` | in | 1 | (0,1800) | esq |
| `ENA` | in | 1 | (0,600) | esq |
| `D` | in | n_bits | (1800,0) | topo |
| `Q` | out | n_bits | (1800,2400) | base |

## Comportamento

- NR=0 → Q=0 (ativo baixo).
- Subida de CLK com ENA=1 → Q=D.
- CLK/ENA/NR indefinidos → Q=X.
- Estado inicial X até o primeiro NR=0.

## Notas

- Sempre prever reset (Ipin manual ou ClockGen, ver ClockGen.md).
- Sempre habilitado: ENA ← Ipin valor 1.

## Exemplo

```
hades.models.rtlib.register.RegRE DATA -9600 16800 @N 1001 32 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX_B 1.0E-8
hades.signals.SignalStdLogicVector n9 32 2 DATA_I Y DATA D 2 2 -9600 16200 -7800 16200 2 -7800 16200 -7800 16800 0
```
