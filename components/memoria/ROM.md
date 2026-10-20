# ROM — ROM (memória só de leitura)

Classe: `hades.models.rtlib.memory.ROM`  
bbox: (0,0)..(6000,4800)

D = mem[A], leitura assíncrona.

## Linha

```
hades.models.rtlib.memory.ROM <nome> <x> <y> @N 1001 1024 32
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_words` | palavras |
| 2 | `n_bits` | bits por palavra |
| 3 | `arquivo` | opcional: `.rom` de inicialização (caminho relativo ao .hds ou absoluto escapado) |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | ceil(log2(n_words)) | (0,2400) | esq |
| `D` | out | n_bits | (3600,4800) | base |

## Comportamento

- Endereço por palavra.

## Notas

- Formato `.rom`: uma linha por palavra, `addr_hex:dado_hex` (`0000:8C010003`).

## Exemplo

```
hades.models.rtlib.memory.ROM INSTRUCTION_MEMORY 600 24000 @N 1001 1024 32 ROMDATA.rom
hades.signals.SignalStdLogicVector n5 32 2 INSTRUCTION_MEMORY D IFID INSTRUCTION_I 2 2 4200 28800 4200 31800 2 4200 31800 9000 31800 0
```
