# OpinVector — Saída de n bits (display / porta de subcircuito)

- **Classe HADES:** `hades.models.rtlib.io.OpinVector`
- **Categoria:** Entradas, saídas e fontes
- **Dimensões (bbox, relativo à âncora):** x 0..4800, y -600..600 → 4800 × 1200

## O que faz

Mostra um vetor de n bits. Em subdesigns, é a porta de SAÍDA de barramento (nome = nome da instância).

## Linha de componente

```
hades.models.rtlib.io.OpinVector <nome> <x> <y> @N 1001 32 1.0E-9 0
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |
| 3 | `formato` | 0=decimal, 1=hex, 2=binário |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | n_bits | (0, 0) | esquerda |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Dicas

- Âncora = porta A; desenho à direita (bbox 0..4800).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\CONTROLLER.hds`

```
hades.models.rtlib.io.OpinVector CTL 44400 40800 @N 1001 9 1.0E-9 0
hades.signals.SignalStdLogicVector nCTL 9 2 mg9 Y CTL A 2 2 36600 39600 36600 40800 2 36600 40800 44400 40800 0
```

A segunda linha é um sinal ligado à instância `CTL`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
