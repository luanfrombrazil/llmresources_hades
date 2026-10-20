# RAMoe — RAM assíncrona com output-enable

Classe: `hades.models.rtlib.memory.RAMoe`  
bbox: (0,0)..(6000,4800)

RAM com nOE na saída.

## Linha

```
hades.models.rtlib.memory.RAMoe <nome> <x> <y> @N 1001 256 32
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_words` | palavras |
| 2 | `n_bits` | bits |
| 3 | `arquivo` | opcional |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | ceil(log2(n_words)) | (0,2400) | esq |
| `DIN` | in | n_bits | (3600,0) | topo |
| `DOUT` | out | n_bits | (3600,4800) | base |
| `nWE` | in | 1 | (0,3000) | esq |
| `nCS` | in | 1 | (0,1800) | esq |
| `nOE` | in | 1 | (0,3600) | esq |

## Exemplo

```
hades.models.rtlib.memory.RAMoe RAM 61800 15600 @N 1001 256 32 RAMTesting.rom
hades.signals.SignalStdLogicVector n29_0 8 2 Address Y RAM A 6 2 49800 29400 49800 30000 2 49800 30000 57000 30000 2 61200 23400 61200 18000 2 61200 18000 61800 18000 2 57000 30000 61200 30000 2 61200 30000 61200 23400 0
```
