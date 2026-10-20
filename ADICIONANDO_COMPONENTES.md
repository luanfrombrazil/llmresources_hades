# Documentar componente novo

1. Achar a classe em `catalog/<pacote>.md` ou `catalog/components.json` (busca pela descrição).
2. Extrair dados com `tools/HadesIntro.java` na pasta do `hades.jar` (Windows: `;` no classpath; Linux/macOS: `:`):
   ```
   javac -encoding UTF-8 -cp hades.jar HadesIntro.java
   java -Djava.awt.headless=true -cp "hades.jar;." HadesIntro --md "<classe> | 1001 <parâmetros>" > <Classe>.md
   ```
   - Após `|`: parâmetros como após `@N` no `.hds`. Sem `|`: padrão.
   - Símbolo dinâmico: rodar com 2–3 valores de n_bits e escrever a fórmula das posições.
   - Larguras de alguns RTLIB aparecem como 1 até a simulação: deduzir de n_bits.
3. Completar conforme `TEMPLATE_COMPONENTE.md`. Significado dos parâmetros = ordem gravada por `write()`; descrição em inglês no `catalog/`.
4. Validar num circuito mínimo no HADES.
5. Salvar em `components/<cat>/<Classe>.md` e adicionar linha em `INDEX.md`.
