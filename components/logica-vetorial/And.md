# And — AND de redução (n bits → 1 bit)

- **Classe HADES:** `hades.models.rtlib.logic.And`
- **Categoria:** Lógica de redução e comparação
- **Dimensões (bbox, relativo à âncora):** x 0..3600, y 0..1800 → 3600 × 1800

## O que faz

Y = A[0] AND A[1] AND … AND A[n−1].

## Linha de componente

```
hades.models.rtlib.logic.And <nome> <x> <y> @N 1001 6 0 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `valor` | valor atual da saída (0/1/X/U); use 0 |
| 3 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | n_bits | (1800, 0) | topo |
| `Y` | saída | 1 | (1800, 1800) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Dicas

- Útil como decodificador: junte bits com MergeBits (invertendo os que devem ser 0) e reduza com And.

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.1\Arquitetura e Organização de Computadores I\TP_Test\FunctControl.hds`

```
hades.models.rtlib.logic.And Addi 27000 18000 @N 1001 6 0 1.0E-8
hades.signals.SignalStdLogic1164 n15 2 Addi Y MUX A 4 2 43800 21600 42600 21600 2 28800 19800 28800 21600 2 28800 21600 38400 21600 2 38400 21600 42600 21600 0
```

A segunda linha é um sinal ligado à instância `Addi`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
