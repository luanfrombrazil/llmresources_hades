# RegBank — Banco de registradores D*CORE

- **Classe HADES:** `hades.models.rtlib.memory.RegBank`
- **Categoria:** Memórias e bancos de registradores
- **Dimensões (bbox, relativo à âncora):** x 0..7200, y 0..6000 → 7200 × 6000

## O que faz

Duas leituras (AX→DX, AY→DY) e uma escrita síncrona (AZ←DZ).

## Linha de componente

```
hades.models.rtlib.memory.RegBank <nome> <x> <y> @N 1001 32 32
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_words` | registradores |
| 2 | `n_bits` | bits |
| 3 | `arquivo` | opcional, `.rom` |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `AX` | entrada | ceil(log2(n_words)) | (0, 3000) | esquerda |
| `AY` | entrada | ceil(log2(n_words)) | (0, 3600) | esquerda |
| `AZ` | entrada | ceil(log2(n_words)) | (0, 4200) | esquerda |
| `DX` | saída | n_bits | (4800, 6000) | base |
| `DY` | saída | n_bits | (2400, 6000) | base |
| `DZ` | entrada | n_bits | (4800, 0) | topo |
| `nWE` | entrada | 1 | (0, 2400) | esquerda |
| `CLK` | entrada | 1 | (0, 1800) | esquerda |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- Escrita na borda de subida de CLK com nWE='0'.

## Dicas

- Para MIPS, prefira MipsRegBank.

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.1\Arquitetura e Organização de Computadores I\TP_Test\Testing.hds`

```
hades.models.rtlib.memory.RegBank RegBank 63000 7800 @N 1001 32 32 C:/Users/wilma/OneDrive/Documentos/papaLeaoXIV/Testing/RegBankTesting.rom
hades.signals.SignalStdLogicVector n26 5 3 Rt Y RegDst A0 RegBank AY 8 2 26400 18600 26400 19200 2 26400 19200 43200 19200 2 43200 19200 43200 11400 2 43200 11400 63000 11400 2 43200 19200 43200 22800 2 43200 22800 40200 22800 2 40200 22800 40200 23400 2 63000 11400 63000 11400 1 43200 19200
```

A segunda linha é um sinal ligado à instância `RegBank`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
