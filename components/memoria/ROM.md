# ROM — ROM (memória só de leitura)

- **Classe HADES:** `hades.models.rtlib.memory.ROM`
- **Categoria:** Memórias e bancos de registradores
- **Dimensões (bbox, relativo à âncora):** x 0..6000, y 0..4800 → 6000 × 4800

## O que faz

D = mem[A], leitura assíncrona. É a memória de instruções do seu pipeline.

## Linha de componente

```
hades.models.rtlib.memory.ROM <nome> <x> <y> @N 1001 1024 32
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_words` | número de palavras (ex.: 1024) |
| 2 | `n_bits` | bits por palavra (ex.: 32) |
| 3 | `arquivo` | opcional: caminho absoluto do `.rom` de inicialização (espaços como `\u0020`, acentos como `\u00e7` etc.) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | ceil(log2(n_words)) | (0, 2400) | esquerda |
| `D` | saída | n_bits | (3600, 4800) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- Endereço por PALAVRA (não por byte): por isso o PC passa por um ShiftRightLogic de 2 antes de A.

## Dicas

- Formato `.rom`: uma linha por palavra, `endereço_hex:dado_hex` (ex.: `0000:8C010003`).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\PIPELINE.hds`

```
hades.models.rtlib.memory.ROM INSTRUCTION_MEMORY 600 24000 @N 1001 1024 32 C:/Users/Luan/Documents/CEFET/2026.2/HACKING\u0020AOC/Claude_Hades/ROMDATA.rom
hades.signals.SignalStdLogicVector n5 32 2 INSTRUCTION_MEMORY D IFID INSTRUCTION_I 2 2 4200 28800 4200 31800 2 4200 31800 9000 31800 0
```

A segunda linha é um sinal ligado à instância `INSTRUCTION_MEMORY`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
