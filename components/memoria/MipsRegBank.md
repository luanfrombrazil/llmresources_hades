# MipsRegBank — Banco de registradores MIPS (32×32)

Classe: `hades.models.rtlib.memory.MipsRegBank`  
bbox: (0,0)..(7200,4800)

2 leituras (AR0→DR0, AR1→DR1), 1 escrita (AW0←DW0).

## Linha

```
hades.models.rtlib.memory.MipsRegBank <nome> <x> <y> @N 1001 32 32 [arquivo]
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_words` | 32 |
| 2 | `n_bits` | 32 |
| 3 | `arquivo` | opcional, `.rom` |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `AR0` | in | 5 | (0,3000) | esq |
| `AR1` | in | 5 | (0,3600) | esq |
| `AW0` | in | 5 | (0,2400) | esq |
| `DR0` | out | n_bits | (2400,4800) | base |
| `DR1` | out | n_bits | (4800,4800) | base |
| `DW0` | in | n_bits | (2400,0) | topo |
| `nWE` | in | 1 | (0,1800) | esq |
| `nCS` | in | 1 | (0,1200) | esq |

## Comportamento

- nCS=1 → DR0/DR1=Z.
- nCS=0, nWE=0 → mem[AW0]=DW0 (por nível).
- DRi = mem[ARi] (assíncrono).

## Notas

- Sem clock: nWE = NAND(RegWrite, CLK); nCS ← Gnd.
- Valor do arquivo para o registrador 0 é ignorado (fica 0).
- Arquivo de inicialização: ver `ARQUIVOS_PARA_MEMORIA.md`.

## Exemplo

```
hades.models.rtlib.memory.MipsRegBank i7 24000 23400 @N 1001 32 32 
hades.signals.SignalStdLogicVector n31 5 2 i8 Y i7 AR0 2 2 21600 25800 21600 26400 2 21600 26400 24000 26400 0
```
