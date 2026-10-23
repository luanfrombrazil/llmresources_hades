# Biblioteca HADES para LLMs

Referência para gerar arquivos `.hds` (esquemáticos do simulador HADES, `hades.jar`). Portas, posições, bbox e formato de parâmetros extraídos do próprio `hades.jar`.

## Ordem de leitura

1. `FORMATO_HDS.md`: gramática do `.hds` (obrigatório).
2. `INDEX.md`: escolher componentes.
3. `components/<cat>/<Componente>.md`: parâmetros, portas, larguras, posições.
4. `LAYOUT.md`: posicionamento, fios, reset.
5. `SUBCIRCUITOS.md` + `blocks/`: hierarquia (`hades.models.Design`, `.sym`). Portas fora do padrão esq/dir: `PORTAS_MISTAS.md`.
6. `ARQUIVOS_PARA_MEMORIA.md`: conteúdo de ROM/RAM/bancos de registradores (`.rom`).
7. `GERADOR.md`: gerar projetos grandes em Python (`tools/gerador/`), com validação automática.
8. `examples/`: arquivos completos e validados.

Componente fora de `components/`: ver `catalog/` e documentar antes (`ADICIONANDO_COMPONENTES.md`).

## Estrutura

```
FORMATO_HDS.md  LAYOUT.md  SUBCIRCUITOS.md  PORTAS_MISTAS.md  ARQUIVOS_PARA_MEMORIA.md  GERADOR.md  INDEX.md
ADICIONANDO_COMPONENTES.md  TEMPLATE_COMPONENTE.md
components/   45 componentes documentados, por categoria
blocks/       subcircuitos genéricos reutilizáveis
catalog/      384 componentes do hades.jar (md + components.json)
examples/     mux4, contador4, portas_mistas, mips_pipeline, pipeline_patterson, monociclo_patterson
tools/        HadesIntro.java (extrai dados de qualquer componente); gerador/ (hdslib.py + scripts)
```

## Regras essenciais

- Unidades HADES, grade de 600, y cresce para baixo.
- Porta absoluta = âncora da instância + posição relativa da porta.
- Conectividade = lista `(instância, porta)` do sinal; segmentos são só desenho, mas devem terminar nas portas.
- Largura do sinal = largura de todas as portas ligadas. 1 bit: `SignalStdLogic1164`.
- Uma saída por sinal. Nomes únicos, `[A-Za-z0-9_]`.
- Circuito sequencial precisa de reset (registradores começam em X).


## Sobre esta biblioteca: ganhos e riscos

*Seção para leitores humanos (alunos, professores, monitores).*

### Por que essa bilbioteca existe?

As frustações encontradas ao utilizar o software Hades nas disciplinas que cursei são diversas e compartilhadas por todos os alunos que tive contato. Alguns alunos perceberam problemas do Hades vinculados à maneira que os arquivos .hds são gerados e solucionavam esses problemas manualmente. Ou se criava protocolos estranhos para mitigar os problemas: salvamento constante, fechar e abrir o programa, fechar e abrir o arquivo em edição, mudar uma ação; e os mais frustantes: deletar um fio completo conectado a diversas portas porque parou de funcionar, recriar um subcomponente ou no pior caso, começar o projeto do zero. Desses alunos, alguns perceberam que talvez fosse possível usar uma LLM para identificar os problemas do circuito - ou bugs do proprio Hades - e ser acertivo nas modificações. Entretanto, modelos de linguagem erram muito ao editar os arquivos do HADES: inventam portas, posições e parâmetros, tentam importar componentes que não existem, entre outros problemas. 

O que é essa bibliotcae? 
Esta biblioteca entrega a esses modelos de linguagem como funciona um arquivo do Hades, o funcionamento do software em sí além dos dados de componentes extraídos do binário do próprio hades, regras de desenho e boas práticas que desenvolvi durante as disciplinas que utilizei o software. O resultado são arquivos `.hds` que carregam e funcionam, em vez de arquivos que só parecem certos.

Além disso, essa biblioteca é parte de um esforço pessoal para desenvolver ferramentas, padrões de escrita e soluções utilizando as tecnologias atuais de modelos e agentes.

### Ganhos educacionais

- **Tutor:** pedir explicação de um circuito existente, perguntar por que deve-se usar uma porta lógica e não outra, explicações de código assembly e como o código percorre os caminhos de dados, por exemplo.
- **Experimentação:** levantar uma hipótese ("e se o sistema de forwarding não existisse?"), alterar instantâneamente e simular em seguida.
- **Conceito:** depois que a montagem manual já foi dominada, automatizar a parte mecânica libera tempo para desenvolvimento de outros conceitos. Imagine o tempo perdido ao construir uma simulação de cache, copiar e conectar repedidamente 32+ componentes de memória. E o tempo perdido para se conectar dezenas de portas lógicas e no meio obter problemas nos fios. 
- **Especificação:** aprender a descrever um circuito com precisão suficiente para outra pessoa construí-lo - nesse caso um modelo linguistico -  também é uma competência de engenharia!

### Ganhos de produtividade

- **Trabalho repetitivo:** registradores de pipeline, vias de cache, decodificadores e barramentos largos são montados em segundos. 
- **Ganho de biblioteca:** componentes simples como extensores de sinais, Mux sem decodificação etc não existem por padrão no Hades, e são gerados em segundos sem quebrar o fluxo de trabalho, que é pensar macro no circuito.
- **Modificações de escala** mover uma porção grande de componentes juntos. Como não há no software uma maneira de selecionar multiplos componentes, as capacidades de uso são ampliadas de forma indireta.
- **Variações rápidas:** mudar uma cache de 4 para 8 vias, trocar a codificação do controle ou testar outra organização do caminho de dados. Preenchimento da RAM, ROM e Banco de Registradores com valores desejados em larga escala.
- **Verificação:** simular um programa de teste e comparar registradores e memória com o esperado. Foi assim que encontrei um erro de temporização no monociclo de exemplo, que passei tempo procurando um problema no circuito em sí.
- **Flexibilização estética:** o hades por padrão gera automaticamente os arquivos .sym, que são usados para gerar subcomponentes de um circuito. O problema é que não há maneira de customizar esse componente, posição das portas, o tamanho e a escala dos componentes no circuito onde vai ser usado etc. O aluno já não gerava o .sym, agora há a possibilidade de se gerar um .sym com uma estética desejada.
- **Docência:** preparar exemplos, gabaritos, variações de exercícios, ferramentas de correção, imagens para avaliações, modelos práticos para simular em sala de aula entre outros.

### Uso indevido e prejuízos

Usar esta biblioteca para **delegar trabalhos avaliativos** a um modelo e entregar o resultado como próprio é fraude acadêmica.

- **O aprendizado está no processo.** Montar o caminho de dados, depurar um hazard e entender por que o registrador ficou em X é o que forma o raciocínio de arquitetura de computadores, por exemplo. Quem pula essa etapa não desenvolve a competência que a disciplina existe para ensinar.
- **Ilusão de competência.** Um circuito que funciona não prova que você sabe fazê-lo. 
- **Erros que não se percebe.** Circuitos gerados podem estar sutilmente errados. Mesmo que certos, podem ser reduntantes e exagerados. Um exemplo é o um dos caminho de dados monociclo deste repositório, que foi gerado por um modelo com menor capacidade computacional, passou no validador e executava errado até ser simulado. Quem não entende o circuito não perceberia o erro.
- **Dependência.** Sem fundamentos, o aluno não consegue avaliar, corrigir nem adaptar o que o modelo produzir.

### Uso responsável

**Alunos:**
- Siga as regras da sua disciplina; na dúvida, pergunte ao professor.
- Faça primeiro e use a ferramenta para revisar, explicar ou explorar.
- Declare o uso. Por exemplo: usar o modelo para mover um conjunto de componentes por você não vai invalidar seus esforços do que construiu até ali.
- Só entregue o que você consegue explicar, fio por fio.
- No geral, use com tudo isso em mente e tenha **bom senso**. 
- Não me responsabilizo pelo uso indevido e seus prejuizos. Afinal, usou porque quis, então o problema é seu, não meu.

**Docentes:**
- Incentive o uso de ferramentas de versionamento para acompanhar o progresso. Os arquivos são texto puro e são fáceis de visualizar no git, por exemplo.
- Deixe explícito no plano de ensino o que é permitido.
- Avalie também o processo: defesa oral, versões intermediárias, perguntas sobre o próprio circuito.
- Aproveite a ferramenta para gerar material e explorar variações em aula.

### Detecção e FLAGS.

- Os arquivos gerados dessa maneira têm características estruturais distintas dos feitos manualmente no editor. Portanto, as detecções de se o arquivo é legitimo e feito por humano é trivial. 
- O Hades quando usado manualmente gera alguns artefatos e padrões que podem ser usados de FLAGS para detecção de uso de "ia".
- Estou ciente de todas as diferenças e **não é do meu interesse** criar nenhum tipo de documentação para evitar que elas aconteçam visto que essas diferenças não mudam a performance e não geram bugs no editor.

# 
"-- Se um homem criar uma máquina para calcular, que mal há nisso?

-- Você pensa que o perigo estava nas engrenagens e nos circuitos, garoto? O problema nunca foram as máquinas superarem os homens em malícia. O perigo real foi que os homens entregaram sua capacidade de pensar às máquinas.

-- Eles se tornaram preguiçosos?

-- Pior do que isso. Eles se tornaram escravos por escolha própria. Ao permitirem que as máquinas decidissem, que as máquinas calculassem o futuro e removessem o peso das escolhas, os seres humanos abdicaram de sua própria alma. Quem tinha as máquinas mais complexas governava os outros. A mente humana decaiu, atrofiou. Nós nos transformamos em rebanhos dependentes de metal e silício." Dune, Frank Herbert.
