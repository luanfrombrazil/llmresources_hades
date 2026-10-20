# Xor — XOR de redução / paridade (n bits → 1 bit)

- **Classe HADES:** `hades.models.rtlib.logic.Xor`
- **Categoria:** Lógica de redução e comparação
- **Dimensões (bbox, relativo à âncora):** x 0..3600, y 0..1800 → 3600 × 1800

## O que faz

Y = A[0] XOR … XOR A[n−1].

## Linha de componente

```
hades.models.rtlib.logic.Xor <nome> <x> <y> @N 1001 2 0 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `valor` | valor atual da saída |
| 3 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | n_bits | (1800, 0) | topo |
| `Y` | saída | 1 | (1800, 1800) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.1\Arquitetura e Organização de Computadores I\TP_Test\MainControlTesting.hds`

```
hades.models.rtlib.logic.Xor Exclude 66000 34800 @N 1001 2 0 1.0E-8
hades.signals.SignalStdLogic1164 n63 2 Exclude Y MergeOP A1 3 2 67800 36600 67800 40800 2 67800 40800 75000 40800 2 75000 40800 75000 43800 0
```

A segunda linha é um sinal ligado à instância `Exclude`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
