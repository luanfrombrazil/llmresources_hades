# Formato `.hds`

Texto, uma entrada por linha, tokens separados por espaço.

## Estrutura

```
# hades.models.Design file
#  
[name] NOME
[components]
<componente>...
[end components]
[signals]
<sinal>...
[end signals]
[end]
```

- `#` = comentário. Manter as duas linhas iniciais.
- `[name]`: nome do design (rótulo em subcircuitos), sem espaços.
- Ordem livre dentro das seções. Instâncias citadas em sinais devem existir.

## Componente

```
<classe> <instância> <x> <y> @N 1001 <parâmetros>
```

| Campo | Regra |
|---|---|
| classe | nome Java completo |
| instância | único, `[A-Za-z0-9_]`. Em Ipin/Opin/IpinVector/OpinVector de subcircuito = nome da porta do bloco. Outros caracteres são escapados (`+`) na linha de componente mas não nos sinais: evitar |
| x y | âncora, múltiplos de 600 |
| `@N` | orientação normal. Usar sempre (`@X`/`@Y` espelham; rotação não suportada) |
| `1001` | versão do modelo, sempre |
| parâmetros | por classe, ver `components/` |

Valores:

| Tipo | Formato | Exemplo |
|---|---|---|
| atraso | segundos | `1.0E-8` (padrão), `5.0E-9` (InvSmall, Opin), `1.0E-9` (IpinVector, OpinVector) |
| vetor | MSB…LSB + `_B`, exatamente n caracteres de `01XUZ` | `00100_B` |
| bit | 1 caractere | `0` `1` `U` `X` |
| caminho | relativo ao `.hds` (preferido) ou absoluto; `/`; espaço ` `; não-ASCII `\uXXXX` | `../../blocks/SHIFTLEFT2.hds` |

## Sinal

```
hades.signals.SignalStdLogic1164   <nome> <nC> (<inst> <porta>)×nC <nS> (2 x1 y1 x2 y2)×nS <nD> (x y)×nD
hades.signals.SignalStdLogicVector <nome> <largura> <nC> (<inst> <porta>)×nC <nS> (2 x1 y1 x2 y2)×nS <nD> (x y)×nD
```

- `nC` conexões, `nS` segmentos (cada um começa com `2` = nº de pontos), `nD` pontos de solda.
- Nomes de sinal únicos (`n0`, `n1`, …).

Exemplo (clock para 2 registradores; 4 segmentos, 1 solda):

```
hades.signals.SignalStdLogic1164 n1 3 CLK Y INSTRUCTION CLK PC4 CLK 4 2 1200 12000 1200 17400 2 1200 17400 13200 17400 2 1200 9000 1200 12000 2 1200 12000 13200 12000 1 1200 12000
```

## Regras

1. Conectividade = pares `(instância, porta)`. Segmentos são desenho.
2. Cada porta conectada coincide com uma extremidade de segmento (posição absoluta).
3. Segmentos ortogonais na grade de 600. Junção de 3+ segmentos: ponto de solda; dividir segmentos na junção.
4. 1 bit → `SignalStdLogic1164`; vetor → `SignalStdLogicVector` com largura = largura das portas. Mudar largura só via MergeBits/Expander/Subset.
5. Exatamente uma saída por sinal.
6. Cada porta em no máximo um sinal.
7. `... 0 0` (sem segmentos) é aceito, mas invisível no editor: evitar.

Porta de subcircuito: `<instância_do_bloco> <nome_do_pino_interno>`.

## Checklist

- [ ] Cabeçalho, `[name]`, `[end components]`, `[end signals]`, `[end]`.
- [ ] `@N 1001` + parâmetros na ordem do doc.
- [ ] Vetores `_B` com n caracteres.
- [ ] Nomes únicos, sem espaço.
- [ ] Portas existem na classe (maiúsculas: `clk`, `SUM`, `nWE`).
- [ ] Larguras consistentes.
- [ ] Uma saída por sinal.
- [ ] Extremidades nas posições absolutas das portas.
- [ ] Caminhos de subcircuitos/ROM corretos.
- [ ] Reset previsto em circuitos sequenciais.
