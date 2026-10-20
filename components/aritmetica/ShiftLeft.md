# ShiftLeft — Deslocamento lógico à esquerda (quantidade fixa)

- **Classe HADES:** `hades.models.rtlib.arith.ShiftLeft`
- **Categoria:** Aritmética e ULAs
- **Dimensões (bbox, relativo à âncora):** x -1800..1800, y 0..1800 → 3600 × 1800

## O que faz

Y = A << shiftcount.

## Linha de componente

```
hades.models.rtlib.arith.ShiftLeft <nome> <x> <y> @N 1001 32 2 00000000000000000000000000000000_B 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `shiftcount` | quantidade fixa de bits deslocados |
| 3 | `valor` | valor atual de Y |
| 4 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | n_bits | (0, 0) | topo |
| `Y` | saída | n_bits | (0, 1800) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Dicas

- Símbolo centrado na âncora: A em (0,0), Y em (0,1800), bbox −1800..1800.

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.1\Arquitetura e Organização de Computadores I\TP_Test\Testing.hds`

```
hades.models.rtlib.arith.ShiftLeft ShiftL_2b 56400 -600 @N 1001 32 2 00000000000000000000000000000000_B 1.0E-8
hades.signals.SignalStdLogicVector n20 32 3 ExtendSignal1 SignalExtended ShiftL_2b A ALUSrc A1 9 2 36600 26400 45000 26400 2 45000 26400 45000 25200 2 45000 14400 45000 -2400 2 45000 -2400 56400 -2400 2 56400 -2400 56400 -600 2 45000 20400 45000 14400 2 45000 14400 48600 14400 2 48600 14400 48600 15000 2 45000 20400 45000 25200 1 45000 14400
```

A segunda linha é um sinal ligado à instância `ShiftL_2b`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
