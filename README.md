# Biblioteca HADES para LLMs

Documentação estruturada para que uma LLM consiga **ler um pedido de circuito e escrever um arquivo `.hds` válido** para o simulador HADES (versão do `hades.jar` usado na disciplina de AOC do CEFET), consultando os componentes, portas, larguras e dimensões aqui descritos.

Tudo aqui foi extraído de duas fontes, e nada foi inventado:

1. **O próprio `hades.jar`**: cada componente foi instanciado em Java e teve lidos as portas, a direção, as posições no símbolo, o bbox e o formato exato de parâmetros que o HADES grava.
2. **Os seus `.hds` reais** (AOC I, Lab AOC I, Lab AOC II, HACKING AOC): os exemplos de linhas, os padrões de projeto e os subcircuitos vêm deles.

## Como uma LLM deve usar esta pasta

Siga esta ordem e abra só o necessário:

1. **`FORMATO_HDS.md`**: leia sempre. É a gramática do arquivo: cabeçalho, linha de componente, linha de sinal (fios) e regras.
2. **`INDEX.md`**: tabela de todos os componentes documentados, com função, portas e tamanho. Escolha os componentes aqui.
3. **`components/<categoria>/<Componente>.md`**: abra um arquivo por componente escolhido para pegar parâmetros, larguras e posições das portas.
4. **`LAYOUT.md`**: como posicionar componentes e traçar fios na grade, e os padrões de projeto que você já usa (PC+4, banco de registradores, memórias, fatiamento da instrução etc.).
5. **`SUBCIRCUITOS.md`** + **`subdesigns/`**: se o circuito usar ou criar blocos hierárquicos (`hades.models.Design`) e os arquivos `.sym`.
6. **`examples/`**: arquivos `.hds` reais e comentados, para conferir o formato.

Para um componente que não está em `components/`, consulte `catalog/` (todos os 384 componentes do `hades.jar`, com parâmetros padrão) e documente-o antes de usar (`ADICIONANDO_COMPONENTES.md`).

## Estrutura

```
llmresources_hades/
├── README.md                  ← você está aqui
├── INDEX.md                   ← índice dos componentes documentados + subcircuitos
├── FORMATO_HDS.md             ← especificação do formato .hds
├── LAYOUT.md                  ← grade, posicionamento, fios, padrões de projeto
├── SUBCIRCUITOS.md            ← hierarquia: hades.models.Design e arquivos .sym
├── ADICIONANDO_COMPONENTES.md ← como documentar um componente novo
├── TEMPLATE_COMPONENTE.md     ← modelo de arquivo de componente
├── components/                ← 44 componentes usados nos seus circuitos (doc detalhada)
│   ├── io/  barramentos/  portas/  logica-vetorial/
│   └── aritmetica/  mux/  registradores/  memoria/
├── subdesigns/                ← seus blocos do pipeline MIPS (IFID, IDEX, CONTROLLER…)
├── catalog/                   ← catálogo automático de todo o hades.jar (+ components.json)
├── examples/                  ← .hds reais comentados
└── tools/                     ← script Java que extrai portas/posições de qualquer componente
```

## Regras de ouro (resumo)

- Coordenadas em **unidades HADES**; componentes e fios na **grade de 600**.
- Posição absoluta de uma porta = **(x, y) da instância + (x, y) relativo** da tabela de portas.
- A **conectividade** é definida pela lista `(instância, porta)` de cada sinal. Os segmentos de fio são só desenho, mas devem terminar exatamente nas portas para o circuito ficar legível e editável.
- A largura de um `SignalStdLogicVector` tem de ser igual à largura de **todas** as portas que ele liga; portas de 1 bit usam `SignalStdLogic1164`.
- Cada sinal tem **exatamente uma** saída que o dirige.
- Nomes de instância e de sinal são **únicos** no arquivo e **sem espaços**.
