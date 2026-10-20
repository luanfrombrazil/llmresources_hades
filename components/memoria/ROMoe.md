# ROMoe — ROM com chip-select e output-enable

- **Classe HADES:** `hades.models.rtlib.memory.ROMoe`
- **Categoria:** Memórias e bancos de registradores
- **Dimensões (bbox, relativo à âncora):** x 0..6000, y 0..4800 → 6000 × 4800

## O que faz

Como ROM, com nCS e nOE ativos em nível baixo (saída em Z quando desabilitada).

## Linha de componente

```
hades.models.rtlib.memory.ROMoe <nome> <x> <y> @N 1001 16 16
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_words` | palavras |
| 2 | `n_bits` | bits por palavra |
| 3 | `arquivo` | opcional, `.rom` |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | ceil(log2(n_words)) | (0, 2400) | esquerda |
| `D` | saída | n_bits | (3600, 4800) | base |
| `nCS` | entrada | 1 | (0, 1800) | esquerda |
| `nOE` | entrada | 1 | (0, 3000) | esquerda |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Exemplo

```
hades.models.rtlib.memory.ROMoe i0 6000 6000 @N 1001 16 16
```

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
