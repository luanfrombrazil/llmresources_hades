# Formato do arquivo `.hds`

Um `.hds` é texto puro, uma entrada por linha, com tokens separados por espaço. Esta especificação foi conferida contra o leitor do `hades.jar` e contra os 1.100 sinais e 1.391 componentes dos seus arquivos: todos seguem exatamente as regras abaixo.

## 1. Estrutura geral

```
# hades.models.Design file
#  
[name] NOME_DO_CIRCUITO
[components]
<linha de componente>
...
[end components]
[signals]
<linha de sinal>
...
[end signals]
[end]
```

- As linhas que começam com `#` são comentários. Mantenha as duas primeiras como o HADES grava.
- `[name]` é o nome do design. Em subcircuitos, é o nome que aparece no símbolo. Use sem espaços (ex.: `HAZARDUNIT`).
- A ordem das linhas dentro de cada seção é livre. O HADES grava em ordem inversa de criação, então não estranhe.
- Toda instância citada em `[signals]` precisa existir em `[components]`.

## 2. Linha de componente

```
<classe> <instância> <x> <y> @N <parâmetros...>
```

| Campo | Significado |
|---|---|
| `<classe>` | nome Java completo, ex.: `hades.models.rtlib.muxes.Mux21` |
| `<instância>` | nome único no arquivo, sem espaços; use só `[A-Za-z0-9_]`. Com outros caracteres o HADES escapa o nome na linha de componente (`Add_PC\u002b4`), mas não nas linhas de sinal (`Add_PC+4`). Evite. Em `Ipin`/`Opin`/`IpinVector`/`OpinVector` de um subcircuito, **é o nome da porta** que o bloco terá |
| `<x> <y>` | âncora da instância em unidades HADES; use múltiplos de 600. **y cresce para baixo** |
| `@N` | orientação normal. É a única usada nos seus arquivos. O HADES aceita `@X`/`@Y` (espelhamento), mas não aceita rotação; **use sempre `@N`** |
| `<parâmetros>` | começam sempre por `1001` (versão do modelo). O restante depende da classe: veja o arquivo do componente em `components/` |

Exemplo:

```
hades.models.rtlib.muxes.Mux21 MUXALU 21600 13200 @N 1001 32 00000000000000000000000000000000_B 1.0E-8
```

### Valores comuns nos parâmetros

| Tipo | Formato | Exemplo |
|---|---|---|
| atraso | segundos, notação Java | `1.0E-8` (portas e RTLIB), `5.0E-9` (inversores, Opin), `1.0E-9` (IpinVector/OpinVector) |
| vetor | bits do MSB ao LSB + `_B`, **exatamente n_bits caracteres**; cada bit em `0 1 X U Z` | `00100_B` |
| bit (StdLogic) | um caractere | `0`, `1`, `U`, `X` |
| caminho de arquivo | absoluto, com `/`, espaço = `\u0020`, caracteres não-ASCII = `\uXXXX` | `C:/Users/Luan/Documents/CEFET/2026.2/HACKING\u0020AOC/Claude_Hades/IFID.hds` |

Escapes já vistos nos seus arquivos: espaço `\u0020`, `ç` `\u00e7`, `ã` `\u00e3`. Para outros acentos, use o código Unicode em hexadecimal com 4 dígitos (`á` = `\u00e1`, `é` = `\u00e9`, `õ` = `\u00f5`).

## 3. Linha de sinal (fio)

Um sinal liga uma saída a uma ou mais entradas e carrega o desenho do fio.

**1 bit:**
```
hades.signals.SignalStdLogic1164 <nome> <nC> <inst₁> <porta₁> … <instₙ> <portaₙ> <nS> <segmento>… <nD> <x y>…
```

**n bits:**
```
hades.signals.SignalStdLogicVector <nome> <largura> <nC> <inst₁> <porta₁> … <nS> <segmento>… <nD> <x y>…
```

| Campo | Significado |
|---|---|
| `<nome>` | nome único do sinal; o HADES usa `n0`, `n1`, … (também aceita nomes como `n21_0`) |
| `<largura>` | só em `SignalStdLogicVector`: número de bits; igual à largura de todas as portas ligadas |
| `<nC>` | número de conexões, seguido de `nC` pares `instância porta` |
| `<nS>` | número de segmentos de fio, seguido de `nS` segmentos |
| `<segmento>` | sempre `2 x1 y1 x2 y2` (o `2` é o número de pontos; nos seus 1.100 sinais ele é sempre 2) |
| `<nD>` | número de pontos de solda (junções em T), seguido de `nD` pares `x y` |

Exemplo (de `IFID.hds`): o clock ligado a dois registradores, com 4 segmentos e 1 ponto de solda:

```
hades.signals.SignalStdLogic1164 n1 3 CLK Y INSTRUCTION CLK PC4 CLK 4 2 1200 12000 1200 17400 2 1200 17400 13200 17400 2 1200 9000 1200 12000 2 1200 12000 13200 12000 1 1200 12000
```

Leitura: sinal `n1`; 3 conexões (`CLK.Y`, `INSTRUCTION.CLK`, `PC4.CLK`); 4 segmentos; 1 ponto de solda em (1200, 12000).

### Regras dos sinais

1. **Conectividade:** é a lista de pares `(instância, porta)` que liga as portas. Os segmentos são só desenho.
2. **Desenho:** cada porta conectada deve coincidir com a extremidade de algum segmento, na posição absoluta da porta (âncora da instância + posição relativa da tabela de portas). Use segmentos horizontais e verticais na grade de 600.
3. **Junções:** quando três ou mais segmentos se encontram num ponto, declare um ponto de solda nele.
4. **Tipo e largura:** portas de 1 bit usam `SignalStdLogic1164`. Portas vetoriais usam `SignalStdLogicVector` com `<largura>` igual à da porta. Um `MergeBits`/`Expander`/`Subset` é o jeito de mudar de largura; nunca ligue larguras diferentes no mesmo sinal.
5. **Uma fonte:** cada sinal tem exatamente uma porta de saída (Y, Q, SUM, D da ROM, DOUT, `Y` de Ipin…); as demais são entradas.
6. **Uma ligação por porta:** cada porta de cada instância aparece em no máximo um sinal.
7. Um sinal com `0` segmentos e `0` pontos de solda (`... 0 0`) é aceito pelo leitor e funciona, mas fica invisível no editor. Evite.

## 4. Conexões com subcircuitos

Uma instância `hades.models.Design` tem como portas os nomes das instâncias `Ipin`/`IpinVector` (entradas) e `Opin`/`OpinVector` (saídas) dentro do `.hds` dela. Num sinal, use `<instância_do_bloco> <nome_da_porta>`:

```
hades.signals.SignalStdLogicVector n44 32 2 IFID INSTRUCTION_O i8 A 2 2 ...
```

As posições das portas de um bloco vêm do arquivo `.sym` dele. Veja `SUBCIRCUITOS.md`.

## 5. Checklist antes de entregar um `.hds`

- [ ] Cabeçalho, `[name]` e as 3 marcações de fim (`[end components]`, `[end signals]`, `[end]`).
- [ ] Todas as linhas de componente com `@N 1001` e os parâmetros na ordem do arquivo do componente.
- [ ] Vetores `_B` com exatamente n caracteres.
- [ ] Nomes de instância e de sinal únicos, sem espaços.
- [ ] Toda porta citada existe naquela classe (atenção a maiúsculas: `clk` do ClockGen, `SUM` do Add, `nWE`).
- [ ] Larguras consistentes em todos os sinais.
- [ ] Cada sinal com uma única saída.
- [ ] Extremidades dos fios exatamente nas posições absolutas das portas.
- [ ] Caminhos de subcircuitos absolutos e escapados (`\u0020`).
