# Ipin — Entrada de 1 bit (chave interativa / porta de subcircuito)

- **Classe HADES:** `hades.models.io.Ipin`
- **Categoria:** Entradas, saídas e fontes
- **Dimensões (bbox, relativo à âncora):** x -1200..0, y -600..600 → 1200 × 1200

## O que faz

Chave que gera um sinal de 1 bit. Também é o conector de ENTRADA de um subdesign: cada Ipin vira uma porta de entrada com o nome da instância.

## Linha de componente

```
hades.models.io.Ipin <nome> <x> <y> @N 1001 null U
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `bindkey` | tecla de atalho ou `null` (o editor às vezes grava vazio, gerando dois espaços: `1001  U`) |
| 2 | `valor_inicial` | `0`, `1` ou `U` |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `Y` | saída | 1 | (0, 0) | direita |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- Clique alterna 0/1; shift-clique percorre 0-1-U-Z.
- A porta `i0`/nome-da-instância listada pelo HADES é interna (conexão hierárquica) — não conecte fios nela; use só `Y`.

## Dicas

- Forma recomendada ao gerar: `1001 null 0` (ou `1001 null U`).
- O ponto de âncora (x,y) É a posição da porta Y; o desenho fica à esquerda (bbox -1200..0).

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\ALUCONTROL.hds`

```
hades.models.io.Ipin ALUOP1 10800 4800 @N 1001  U
hades.signals.SignalStdLogic1164 n7 4 ALUOP1 Y i2 A i9 A i1 A 9 2 10800 4800 11400 8400 2 11400 8400 14400 8400 2 14400 12600 14400 17400 2 14400 17400 15000 17400 2 14400 9600 14400 12600 2 14400 12600 18000 12600 2 18000 12600 18000 13200 2 14400 8400 14400 9600 2 14400 9600 15600 9600 2 14400 9600 14400 12600
```

A segunda linha é um sinal ligado à instância `ALUOP1`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
