# RegRE — Registrador de n bits com enable e reset

- **Classe HADES:** `hades.models.rtlib.register.RegRE`
- **Categoria:** Registradores
- **Dimensões (bbox, relativo à âncora):** x 0..3600, y 0..2400 → 3600 × 2400

## O que faz

Q ← D na borda de subida de CLK quando ENA=1; NR=0 zera de forma assíncrona. É o bloco básico dos registradores de pipeline (IFID, IDEX, EXMEM, MEMWB) e do PC.

## Linha de componente

```
hades.models.rtlib.register.RegRE <nome> <x> <y> @N 1001 32 00000000000000000000000000000000_B 1.0E-8
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | largura do barramento em bits (1..63; nos seus arquivos: 2–32) |
| 2 | `valor` | conteúdo atual/inicial em binário `..._B` |
| 3 | `delay` | atraso de propagação em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `CLK` | entrada | 1 | (0, 1200) | esquerda |
| `NR` | entrada | 1 | (0, 1800) | esquerda |
| `ENA` | entrada | 1 | (0, 600) | esquerda |
| `D` | entrada | n_bits | (1800, 0) | topo |
| `Q` | saída | n_bits | (1800, 2400) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- NR='0' → Q=0 imediatamente (reset ativo em nível baixo).
- Borda de subida em CLK com ENA='1' → Q=D (após `delay`).
- CLK/ENA/NR indefinidos → Q=X.

## Dicas

- O registrador começa em X (o `valor` da linha é só o que o editor mostra). Sem um pulso de NR='0' no início, um contador ou PC fica em X para sempre. Use o Ipin de reset (clique 0→1) ou o truque do ClockGen descrito em ClockGen.md.
- Para um registrador sempre habilitado, ligue ENA a um Ipin com valor 1.

## Exemplo real (dos seus arquivos)

Arquivo: `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\EXMEM.hds`

```
hades.models.rtlib.register.RegRE DATA -9600 16800 @N 1001 32 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX_B 1.0E-8
hades.signals.SignalStdLogicVector n9 32 2 DATA_I Y DATA D 2 2 -9600 16200 -7800 16200 2 -7800 16200 -7800 16800 0
```

A segunda linha é um sinal ligado à instância `DATA`.

---
Fonte: introspecção do `hades.jar` (portas, posições, bbox, formato de `write()`) + uso real nos seus `.hds`.
