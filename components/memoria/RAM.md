# RAM — RAM assíncrona

- **Classe HADES:** `hades.models.rtlib.memory.RAM`
- **Categoria:** Memórias e bancos de registradores
- **Dimensões (bbox, relativo à âncora):** x 0..6000, y 0..4800 → 6000 × 4800

## O que faz

Memória de dados do pipeline. Uma porta de endereço A, entrada DIN e saída DOUT.

## Linha de componente

```
hades.models.rtlib.memory.RAM <nome> <x> <y> @N 1001 1024 32
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_words` | palavras |
| 2 | `n_bits` | bits por palavra |
| 3 | `arquivo` | opcional, `.rom` de inicialização |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | ceil(log2(n_words)) | (0, 2400) | esquerda |
| `DIN` | entrada | n_bits | (3600, 0) | topo |
| `DOUT` | saída | n_bits | (3600, 4800) | base |
| `nWE` | entrada | 1 | (0, 3000) | esquerda |
| `nCS` | entrada | 1 | (0, 1800) | esquerda |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- nCS='1' → DOUT em Z.
- nCS='0' e nWE='0' → escreve DIN em mem[A] (por nível, sem clock).
- nCS='0' e nWE='1' → DOUT = mem[A].

## Dicas

- Escrita é assíncrona: gere nWE combinando MemWrite com o clock se precisar de escrita síncrona.
- Endereço por palavra (use ShiftRightLogic 2 no endereço em bytes).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\PIPELINE.hds`

```
hades.models.rtlib.memory.RAM i25 103800 27600 @N 1001 1024 32 
hades.signals.SignalStdLogicVector n81 32 2 i25 DOUT MEMWB MEMDATA_I 6 2 107400 32400 107400 33600 2 107400 33600 111000 33600 2 111000 33600 111000 26400 2 111000 26400 108600 26400 2 108600 26400 108600 21000 2 108600 21000 109800 21000 0
```

A segunda linha é um sinal ligado à instância `i25`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
