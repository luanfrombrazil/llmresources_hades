// HadesIntro — extrai portas, larguras, posições e bbox de componentes do HADES.
//
// Uso (na pasta onde está o hades.jar; no Windows o separador do classpath é ';'):
//   javac -encoding UTF-8 -cp hades.jar HadesIntro.java
//   java -Djava.awt.headless=true -cp "hades.jar;." HadesIntro "hades.models.rtlib.arith.Addc"
//   java -Djava.awt.headless=true -cp "hades.jar;." HadesIntro "hades.models.rtlib.arith.Addc | 1001 32 UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU_B 1.0E-8"
//   java -Djava.awt.headless=true -cp "hades.jar;." HadesIntro --md "hades.models.rtlib.arith.Addc | 1001 32 ..."  > Addc.md
//
// Sem argumentos de componente, lê linhas "classe [| parâmetros]" da entrada padrão.
// O texto depois de '|' é exatamente o que vem depois de '@N' numa linha de componente do .hds.
// --md gera um esqueleto de documentação no formato de components/ (as seções de significado ficam com TODO).
import hades.simulator.*; import hades.symbols.*; import hades.models.*;
import java.io.*; import java.util.*; import java.awt.Point;

public class HadesIntro {
  static boolean md = false;

  public static void main(String[] args) throws Exception {
    System.setOut(new PrintStream(new FileOutputStream(FileDescriptor.out), true, "UTF-8"));
    List<String> items = new ArrayList<>();
    for (String a : args) { if (a.equals("--md")) md = true; else items.add(a); }
    if (items.isEmpty()) {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      String l; while ((l = br.readLine()) != null) if (!l.trim().isEmpty()) items.add(l.trim());
    }
    for (String it : items) describe(it);
  }

  static void describe(String line) {
    String cls = line, init = null; int k = line.indexOf('|');
    if (k >= 0) { cls = line.substring(0, k).trim(); init = line.substring(k + 1).trim(); }
    try {
      SimObject o = (SimObject) Class.forName(cls).getDeclaredConstructor().newInstance();
      o.setName("i0");
      if (init != null) o.initialize(init);
      StringWriter sw = new StringWriter(); PrintWriter pw = new PrintWriter(sw); o.write(pw); pw.flush();
      String params = sw.toString().trim();
      Symbol s;
      if (o.needsDynamicSymbol()) { o.constructDynamicSymbol(); s = o.getSymbol(); }
      else { s = new Symbol(); s.setParent(o); s.initializeFromResource(o); }
      int[] bb = null;
      for (Enumeration e = s.elements(); e.hasMoreElements();) {
        Object m = e.nextElement();
        if (m instanceof BboxRectangle) { jfig.objects.FigBbox b = ((jfig.objects.FigObject) m).getBbox(); bb = new int[]{b.getXl(), b.getYt(), b.getXr(), b.getYb()}; }
      }
      Port[] ps = o.getPorts();
      if (md) {
        String simple = cls.substring(cls.lastIndexOf('.') + 1);
        System.out.println("# " + simple + " — TODO título em português\n");
        System.out.println("- **Classe HADES:** `" + cls + "`");
        System.out.println("- **Categoria:** TODO");
        if (bb != null) System.out.println("- **Dimensões (bbox, relativo à âncora):** x " + bb[0] + ".." + bb[2] + ", y " + bb[1] + ".." + bb[3] + " → " + (bb[2]-bb[0]) + " × " + (bb[3]-bb[1]) + (o.needsDynamicSymbol() ? " *(símbolo dinâmico)*" : ""));
        System.out.println("\n## O que faz\n\nTODO\n\n## Linha de componente\n\n```\n" + cls + " <nome> <x> <y> @N " + params + "\n```\n");
        System.out.println("| # | Parâmetro | Significado |\n|---|---|---|\n| 1 | TODO | TODO |\n");
        System.out.println("## Portas\n\n| Porta | Direção | Largura (bits) | Posição relativa (x, y) |\n|---|---|---|---|");
      } else {
        System.out.println("### " + cls + (init != null ? " | " + init : ""));
        System.out.println("params: " + params);
        if (bb != null) System.out.println("bbox: " + bb[0] + " " + bb[1] + " " + bb[2] + " " + bb[3] + (o.needsDynamicSymbol() ? " (dinamico)" : ""));
      }
      if (ps != null) for (Port p : ps) {
        if (p.getType() == Port.TOPLEVEL_IN) continue;
        String w = (p instanceof PortStdLogicVector) ? "" + ((PortStdLogicVector) p).getWidth() : "1";
        Point pos = null; try { pos = s.getPortPosition(p.getName()); } catch (Exception ex) {}
        String ps2 = pos == null ? "—" : "(" + pos.x + ", " + pos.y + ")";
        if (md) System.out.println("| `" + p.getName() + "` | " + p.getTypeString() + " | " + w + " | " + ps2 + " |");
        else System.out.println("port: " + p.getName() + " " + p.getTypeString() + " width=" + w + " pos=" + ps2);
      }
      if (md) System.out.println("\n> Largura lida pelo modelo; em alguns componentes RTLIB ela só é ajustada na simulação — confira com n_bits.\n\n## Comportamento\n\n- TODO\n\n## Dicas\n\n- TODO\n");
      System.out.println();
    } catch (Throwable t) {
      System.out.println("### " + cls + " -> ERRO: " + t);
    }
  }
}
