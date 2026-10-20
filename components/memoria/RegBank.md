# RegBank — Banco de registradores D*CORE

Classe: `hades.models.rtlib.memory.RegBank`  
bbox: (0,0)..(7200,6000)

2 leituras (AX→DX, AY→DY), 1 escrita síncrona (AZ←DZ).

## Linha

```
hades.models.rtlib.memory.RegBank <nome> <x> <y> @N 1001 32 32
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_words` | registradores |
| 2 | `n_bits` | bits |
| 3 | `arquivo` | opcional, `.rom` |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `AX` | in | ceil(log2(n_words)) | (0,3000) | esq |
| `AY` | in | ceil(log2(n_words)) | (0,3600) | esq |
| `AZ` | in | ceil(log2(n_words)) | (0,4200) | esq |
| `DX` | out | n_bits | (4800,6000) | base |
| `DY` | out | n_bits | (2400,6000) | base |
| `DZ` | in | n_bits | (4800,0) | topo |
| `nWE` | in | 1 | (0,2400) | esq |
| `CLK` | in | 1 | (0,1800) | esq |

## Comportamento

- Escrita na subida de CLK com nWE=0.

## Notas

- Para MIPS: MipsRegBank.

## Exemplo

```
hades.models.rtlib.memory.RegBank RegBank 63000 7800 @N 1001 32 32 RegBankTesting.rom
hades.signals.SignalStdLogicVector n26 5 3 Rt Y RegDst A0 RegBank AY 8 2 26400 18600 26400 19200 2 26400 19200 43200 19200 2 43200 19200 43200 11400 2 43200 11400 63000 11400 2 43200 19200 43200 22800 2 43200 22800 40200 22800 2 40200 22800 40200 23400 2 63000 11400 63000 11400 1 43200 19200
```
