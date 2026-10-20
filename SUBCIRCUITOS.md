# Subcircuitos (hierarquia) e arquivos `.sym`

O HADES monta hierarquia instanciando um `.hds` dentro de outro com a classe `hades.models.Design`. É assim que o seu pipeline usa IFID, IDEX, EXMEM, MEMWB, CONTROLLER, ALUCONTROL, FORWARDING UNIT e HAZARD UNIT. A documentação de cada bloco está em `subdesigns/`.

## 1. Criando um bloco

Um bloco é um `.hds` comum em que:

- cada **entrada** do bloco é um `hades.models.io.Ipin` (1 bit) ou `hades.models.rtlib.io.IpinVector` (n bits);
- cada **saída** é um `hades.models.io.Opin` (1 bit) ou `hades.models.rtlib.io.OpinVector` (n bits);
- o **nome da instância** desses pinos é o nome da porta do bloco (ex.: `IpinVector PC4_I …` cria a porta `PC4_I` de 32 bits).

A largura da porta é o `n_bits` do IpinVector/OpinVector.

## 2. Usando o bloco em outro circuito

```
hades.models.Design <instância> <x> <y> @N 1001 <caminho_do_hds>
```

Exemplo real (PIPELINEPOSHAZ.hds):

```
hades.models.Design IFID 9000 28800 @N 1001 C:/Users/Luan/Documents/CEFET/2026.2/HACKING\u0020AOC/Claude_Hades/IFID.hds
```

- **Caminho:** absoluto, com `/`, espaço como `\u0020` e acentos como `\uXXXX`. É o que os seus arquivos usam e o mais seguro. Caminho **relativo à pasta do `.hds` pai** também funciona (testado com o leitor do hades.jar), mas o editor regrava como absoluto ao salvar.
- **Sinais:** referencie as portas pelo nome do pino interno: `IFID PC4_I`, `IFID INSTRUCTION_O`.
- Posição absoluta da porta = âncora da instância + posição da porta no `.sym` do bloco.

## 3. O arquivo `.sym`

O símbolo de um bloco fica num arquivo com **o mesmo nome do `.hds` e extensão `.sym`, na mesma pasta** (`IFID.hds` → `IFID.sym`). É o `.sym` que define o tamanho do retângulo e onde cada porta aparece. Ao criar um bloco novo, **gere o `.sym` junto**, para não depender do editor.

### Formato

```
hades.symbols.BboxRectangle  0 0 <L> <A>
hades.symbols.Rectangle  0 0 <L> <A>
hades.symbols.PortLabel <L-150> <y+150> 3 <SAIDA>
hades.symbols.PortSymbol <L> <y> <SAIDA>
hades.symbols.PortLabel 150 <y+150> <ENTRADA>
hades.symbols.PortSymbol 0 <y> <ENTRADA>
hades.symbols.InstanceLabel 150 <A-150> <NOME>
hades.symbols.ClassLabel 150 450 <NOME>
```

| Linha | Função |
|---|---|
| `BboxRectangle 0 0 L A` | caixa de seleção (largura L, altura A) |
| `Rectangle 0 0 L A` | retângulo desenhado |
| `PortSymbol x y NOME` | **posição da porta**; o `NOME` tem de ser igual ao nome do Ipin/Opin interno |
| `PortLabel x y [alinh] texto` | rótulo; `3` = alinhado à direita (usado nas saídas); sem número = à esquerda |
| `InstanceLabel` / `ClassLabel` | rótulos do nome da instância e do bloco |

### Regra de layout (a mesma de todos os seus `.sym`)

- Largura **L = 4800**.
- Entradas em **x = 0**, saídas em **x = L**.
- Portas em **y = 600, 1200, 1800, …** (passo 600). Pode haver lacunas para agrupar portas (o IDEX tem).
- Altura **A = 600 × (máx(nº entradas, nº saídas) + 1)**, ou mais, se houver lacunas: A = maior y de porta + 600.
- Rótulo de entrada: `PortLabel 150 (y+150) NOME`. Rótulo de saída: `PortLabel (L−150) (y+150) 3 NOME`.

Exemplo completo (`SHIFTLEFT2.sym`, 1 entrada e 1 saída):

```
hades.symbols.BboxRectangle  0 0 4800 1200
hades.symbols.Rectangle  0 0 4800 1200
hades.symbols.PortLabel 4650 750 3 OUTPUT
hades.symbols.PortSymbol 4800 600 OUTPUT
hades.symbols.PortLabel 150 750 INPUT
hades.symbols.PortSymbol 0 600 INPUT
hades.symbols.InstanceLabel 150 1050 SHIFTLEFT2
hades.symbols.ClassLabel 150 450 SHIFTLEFT2
```

## 4. Checklist de um bloco novo

- [ ] `.hds` do bloco com um Ipin/IpinVector por entrada e um Opin/OpinVector por saída, com nomes únicos e sem espaço.
- [ ] `.sym` com o mesmo nome base, na mesma pasta, com um `PortSymbol` para cada pino e nomes idênticos.
- [ ] Larguras dos sinais no circuito pai iguais às larguras dos IpinVector/OpinVector do bloco.
- [ ] Caminho absoluto e escapado na linha `hades.models.Design`.
- [ ] Novo `subdesigns/<NOME>.md` documentando o bloco (portas, larguras, posições), como os existentes.
