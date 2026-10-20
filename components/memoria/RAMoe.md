# RAMoe — RAM assíncrona com output-enable

- **Classe HADES:** `hades.models.rtlib.memory.RAMoe`
- **Categoria:** Memórias e bancos de registradores
- **Dimensões (bbox, relativo à âncora):** x 0..6000, y 0..4800 → 6000 × 4800

## O que faz

Como RAM, com nOE controlando a saída.

## Linha de componente

```
hades.models.rtlib.memory.RAMoe <nome> <x> <y> @N 1001 256 32
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_words` | palavras |
| 2 | `n_bits` | bits |
| 3 | `arquivo` | opcional |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | ceil(log2(n_words)) | (0, 2400) | esquerda |
| `DIN` | entrada | n_bits | (3600, 0) | topo |
| `DOUT` | saída | n_bits | (3600, 4800) | base |
| `nWE` | entrada | 1 | (0, 3000) | esquerda |
| `nCS` | entrada | 1 | (0, 1800) | esquerda |
| `nOE` | entrada | 1 | (0, 3600) | esquerda |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.1\Arquitetura e Organização de Computadores I\TP_Test\Testing.hds`

```
hades.models.rtlib.memory.RAMoe RAM 61800 15600 @N 1001 256 32 C:/Users/wilma/OneDrive/Documentos/papaLeaoXIV/Testing/RAMTesting.rom
hades.signals.SignalStdLogicVector n29_0 8 2 Address Y RAM A 6 2 49800 29400 49800 30000 2 49800 30000 57000 30000 2 61200 23400 61200 18000 2 61200 18000 61800 18000 2 57000 30000 61200 30000 2 61200 30000 61200 23400 0
```

A segunda linha é um sinal ligado à instância `RAM`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
