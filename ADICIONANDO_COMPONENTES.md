# Adicionando componentes à biblioteca

`components/` documenta os 44 componentes que você já usou. O HADES tem 384 (todos listados em `catalog/`). Quando um circuito precisar de um componente novo, documente-o **antes** de usá-lo, para a próxima LLM encontrar tudo pronto.

## Passo a passo

1. **Ache a classe** em `catalog/<pacote>.md` ou `catalog/components.json` (busque pela descrição, ex.: "adder with carry" → `hades.models.rtlib.arith.Addc`).
2. **Extraia os dados reais** com a ferramenta `tools/HadesIntro.java`, rodando-a na pasta do `hades.jar`:
   ```
   javac -encoding UTF-8 -cp hades.jar HadesIntro.java
   java -Djava.awt.headless=true -cp "hades.jar;." HadesIntro --md "hades.models.rtlib.arith.Addc | 1001 32 UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU_B 1.0E-8" > Addc.md
   ```
   - Depois de `|` vão os parâmetros exatamente como ficariam depois de `@N` no `.hds`. Sem `|`, ele usa os parâmetros padrão.
   - A saída já traz a classe, o bbox, a linha de componente e a tabela de portas com as posições.
   - Para componentes de símbolo dinâmico (como MergeBits), rode com 2 ou 3 valores de `n_bits` e escreva a fórmula das posições.
3. **Complete o esqueleto** seguindo `TEMPLATE_COMPONENTE.md`: título, categoria, o que faz, significado de cada parâmetro (na ordem da linha), larguras em função dos parâmetros, comportamento e dicas. A descrição em inglês do `catalog/` ajuda.
4. **Confira no HADES:** monte um circuito mínimo com o componente, abra no editor e veja se as portas e os fios batem.
5. **Salve** em `components/<categoria>/<Classe>.md` e **adicione uma linha** na tabela da categoria em `INDEX.md`.

## Subcircuitos novos

Ao criar um bloco `.hds` reutilizável, documente-o em `subdesigns/<NOME>.md` (veja `SUBCIRCUITOS.md`): caminho, portas com largura e posição no `.sym`, e função.

## Como esta biblioteca foi gerada

- As **portas, posições, bbox e o formato de parâmetros** vieram da instanciação de cada classe do `hades.jar` (a mesma lógica do `HadesIntro.java`).
- As **descrições** de `catalog/` vêm dos arquivos `.clb` dentro do `hades.jar`.
- O **significado dos parâmetros** veio da ordem em que o método `write()` de cada classe grava os campos.
- Os **exemplos e padrões** vieram dos seus `.hds` em AOC I, Lab AOC I, Lab AOC II e HACKING AOC.
