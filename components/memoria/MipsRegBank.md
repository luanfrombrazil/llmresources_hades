# MipsRegBank — Banco de registradores MIPS (32×32)

- **Classe HADES:** `hades.models.rtlib.memory.MipsRegBank`
- **Categoria:** Memórias e bancos de registradores
- **Dimensões (bbox, relativo à âncora):** x 0..7200, y 0..4800 → 7200 × 4800

## O que faz

Duas leituras (AR0→DR0, AR1→DR1) e uma escrita (AW0←DW0). Banco de registradores do seu pipeline.

## Linha de componente

```
hades.models.rtlib.memory.MipsRegBank <nome> <x> <y> @N 1001 32 32
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_words` | 32 |
| 2 | `n_bits` | 32 |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `AR0` | entrada | 5 | (0, 3000) | esquerda |
| `AR1` | entrada | 5 | (0, 3600) | esquerda |
| `AW0` | entrada | 5 | (0, 2400) | esquerda |
| `DR0` | saída | n_bits | (2400, 4800) | base |
| `DR1` | saída | n_bits | (4800, 4800) | base |
| `DW0` | entrada | n_bits | (2400, 0) | topo |
| `nWE` | entrada | 1 | (0, 1800) | esquerda |
| `nCS` | entrada | 1 | (0, 1200) | esquerda |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- nCS='1' → DR0/DR1 em Z.
- nCS='0' e nWE='0' → mem[AW0] = DW0 (escrita por nível, sem clock).
- Leituras assíncronas: DRi = mem[ARi].

## Dicas

- Não tem porta de clock: o sinal RegWrite (ativo alto) precisa ser invertido para nWE, e normalmente combinado com o clock (Nand2) para escrever só numa fase.
- Sem arquivo de inicialização na linha (só `1001 32 32`).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\PIPELINE.hds`

```
hades.models.rtlib.memory.MipsRegBank i7 24000 23400 @N 1001 32 32 
hades.signals.SignalStdLogicVector n31 5 2 i8 Y i7 AR0 2 2 21600 25800 21600 26400 2 21600 26400 24000 26400 0
```

A segunda linha é um sinal ligado à instância `i7`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
