# RAM — RAM assíncrona

Classe: `hades.models.rtlib.memory.RAM`  
bbox: (0,0)..(6000,4800)

Memória assíncrona; endereço A, entrada DIN, saída DOUT.

## Linha

```
hades.models.rtlib.memory.RAM <nome> <x> <y> @N 1001 1024 32
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_words` | palavras |
| 2 | `n_bits` | bits por palavra |
| 3 | `arquivo` | opcional, `.rom` de inicialização |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | ceil(log2(n_words)) | (0,2400) | esq |
| `DIN` | in | n_bits | (3600,0) | topo |
| `DOUT` | out | n_bits | (3600,4800) | base |
| `nWE` | in | 1 | (0,3000) | esq |
| `nCS` | in | 1 | (0,1800) | esq |

## Comportamento

- nCS=1 → DOUT=Z.
- nCS=0, nWE=0 → mem[A]=DIN (por nível).
- nCS=0, nWE=1 → DOUT=mem[A].

## Notas

- Escrita síncrona: nWE = NAND(MemWrite, CLK).
- Endereço por palavra.

## Exemplo

```
hades.models.rtlib.memory.RAM i25 103800 27600 @N 1001 1024 32 
hades.signals.SignalStdLogicVector n81 32 2 i25 DOUT MEMWB MEMDATA_I 6 2 107400 32400 107400 33600 2 107400 33600 111000 33600 2 111000 33600 111000 26400 2 111000 26400 108600 26400 2 108600 26400 108600 21000 2 108600 21000 109800 21000 0
```
