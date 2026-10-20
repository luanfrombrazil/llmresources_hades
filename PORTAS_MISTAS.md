# Subcircuitos com portas mistas

Bloco com portas em lados não padrão (ex.: entrada no topo, saída no topo). Só o `.sym` muda; o `.hds` do bloco segue o padrão de `SUBCIRCUITOS.md`.

## Procedimento obrigatório

1. Criar o bloco no padrão HADES: `.hds` com Ipin/Opin e `.sym` com entradas em x=0, saídas em x=L.
2. Validar o bloco pronto (carregar/simular num circuito de teste).
3. Só então reposicionar portas no `.sym`: mover `PortSymbol` e `PortLabel` correspondentes; ajustar `BboxRectangle`/`Rectangle` se preciso.
4. Não alterar o `.hds` do bloco (nomes de pinos, lógica). Direção da porta continua definida pelo pino (Ipin = entrada, Opin = saída), não pelo lado.
5. Nos circuitos pais: conectividade não muda; refazer só os segmentos dos fios ligados às portas movidas.

## Regras de posicionamento

| Regra | Valor |
|---|---|
| Porta na borda | x=0 (esq), x=L (dir), y=0 (topo), y=A (base) |
| Grade | múltiplos de 600 |
| Distância entre portas na mesma borda (topo/base) | ≥ 2400 |
| Distância do canto | ≥ 1200 |
| Largura mínima com n portas no topo | L ≥ 1200 + 2400·(n−1) + 1200 |

## Rótulos

| Lado | Linha |
|---|---|
| esquerda | `PortLabel 150 <y+150> NOME` |
| direita | `PortLabel <L-150> <y+150> 3 NOME` |
| topo | `PortLabel <x> 450 2 NOME` (centralizado, abaixo da porta) |
| base | `PortLabel <x> <A-150> 2 NOME` |

`ClassLabel`/`InstanceLabel` centralizados (`2`) para não colidir com rótulos do topo:
`ClassLabel <L/2> <A-150> 2 NOME`, `InstanceLabel <L/2> <A+450> 2 NOME` (abaixo da caixa).

## Fios no circuito pai

- Porta no topo: fio chega/sai verticalmente por cima.
- Porta na base: verticalmente por baixo.
- Manter a horizontalidade do restante do fluxo (`LAYOUT.md`).

## Exemplo

`examples/portas_mistas/`: `PORTAS_MISTAS` (Y = A AND B, Z = A OR B). Entrada A e saída Z no topo, entrada B à esquerda, saída Y à direita.

```
hades.symbols.BboxRectangle  0 0 4800 2400
hades.symbols.Rectangle  0 0 4800 2400
hades.symbols.PortSymbol 1200 0 A
hades.symbols.PortLabel 1200 450 2 A
hades.symbols.PortSymbol 3600 0 Z
hades.symbols.PortLabel 3600 450 2 Z
hades.symbols.PortSymbol 0 1200 B
hades.symbols.PortLabel 150 1350 B
hades.symbols.PortSymbol 4800 1200 Y
hades.symbols.PortLabel 4650 1350 3 Y
hades.symbols.ClassLabel 2400 2250 2 PORTAS_MISTAS
hades.symbols.InstanceLabel 2400 2850 2 PORTAS_MISTAS
```

Uso: `TESTE_PORTAS_MISTAS.hds` (A desce de cima, Z sobe e segue à direita).
