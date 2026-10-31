"""Servidor MCP da biblioteca HADES.

Expõe a documentação, o catálogo de componentes, o gerador/validador (tools/gerador/hdslib.py) e um
validador de .hds existentes como ferramentas MCP.

Uso:
  hades-mcp                                   # stdio (Claude Desktop, Claude Code, Cursor...)
  hades-mcp --transport streamable-http --host 0.0.0.0 --port 8000   # HTTP em /mcp
"""
from __future__ import annotations

import argparse
import io
import json
import os
from pathlib import Path
from typing import Any

from mcp.server.mcpserver import Image, MCPServer
from mcp_types import ToolAnnotations

from . import __version__, hdsparse, library, natives, rom, spec as specmod
from .library import hdslib

RO = ToolAnnotations(readOnlyHint=True, idempotentHint=True, openWorldHint=False)
RW = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=True, openWorldHint=False)

INSTRUCTIONS = """\
Biblioteca para gerar e corrigir esquemáticos .hds do simulador HADES (hades.jar) sem inventar portas,
posições ou parâmetros. Documentação em português.

Fluxo recomendado:
1. read_doc("FORMATO_HDS") e read_doc("LAYOUT") antes de escrever qualquer .hds.
2. search_components / get_component para cada componente (portas, larguras, posições relativas, bbox).
3. Projetos novos: list_native_types + build_design (especificação JSON -> .hds/.sym validados pelo hdslib).
   Subcircuitos: read_doc("SUBCIRCUITOS") e read_doc("PORTAS_MISTAS").
4. Memórias: make_rom / validate_rom (read_doc("ARQUIVOS_PARA_MEMORIA")).
5. Arquivos existentes (do editor ou de outra LLM): validate_hds e render_hds; corrigir até errors=[]
   (lint = regras de desenho da biblioteca; idealmente também vazio).
Regras essenciais: grade de 600, y cresce para baixo, porta absoluta = âncora + posição relativa,
uma saída por sinal, largura do sinal = largura das portas, circuito sequencial precisa de reset.
O validador cobre geometria e conectividade, não comportamento: simular no HADES.
"""

mcp = MCPServer('hades', title='HADES .hds library', version=__version__, instructions=INSTRUCTIONS)


# ---------------------------------------------------------------- workspace (pasta montada em /work)
def _workspace() -> Path | None:
    env = os.environ.get('HADES_WORKSPACE')
    if env == '':
        return None
    p = Path(env) if env else Path('/work')
    return p.resolve() if p.is_dir() else None


def _inside(ws: Path, p: Path) -> bool:
    return p == ws or ws in p.parents


def _wpath(rel: str, must_exist: bool = False) -> Path:
    """Caminho no workspace. resolve() segue links simbólicos: um link que aponta para fora é recusado."""
    ws = _workspace()
    if ws is None:
        raise ValueError('sem workspace: monte uma pasta em /work (docker -v "$PWD:/work") ou defina HADES_WORKSPACE')
    p = (ws / rel).resolve()
    if not _inside(ws, p):
        raise ValueError(f'caminho fora do workspace: {rel}')
    if must_exist and not p.exists():
        raise FileNotFoundError(f'{rel} não existe no workspace')
    return p


def _save(files: dict[str, str], save_to: str | None) -> list[str]:
    if not save_to:
        return []
    folder = _wpath(save_to)
    folder.mkdir(parents=True, exist_ok=True)
    targets = {}
    for name in files:
        if Path(name).name != name:
            raise ValueError(f'nome de arquivo inválido: {name}')
        targets[name] = _wpath(str(Path(save_to) / name))   # recusa link simbólico que escape do workspace
    ws = _workspace()
    out = []
    for name, text in files.items():
        targets[name].write_text(text, encoding='utf-8', newline='\n')
        out.append(str(targets[name].relative_to(ws)))
    return out


def _png(design) -> Image:
    import tempfile
    with tempfile.NamedTemporaryFile(suffix='.png') as f:
        hdslib.render(design, f.name)
        return Image(data=Path(f.name).read_bytes(), format='png')


# ---------------------------------------------------------------- documentação e catálogo
@mcp.tool(annotations=RO)
def list_docs() -> dict:
    """Lista os guias da biblioteca (nome -> conteúdo), na ordem de leitura recomendada."""
    return library.DOCS


@mcp.tool(annotations=RO)
def read_doc(name: str) -> str:
    """Lê um guia da biblioteca. name: README, FORMATO_HDS, INDEX, LAYOUT, SUBCIRCUITOS, PORTAS_MISTAS,
    ARQUIVOS_PARA_MEMORIA, GERADOR, ADICIONANDO_COMPONENTES, TEMPLATE_COMPONENTE."""
    return library.doc(name)


@mcp.tool(annotations=RO)
def search_components(query: str = '', package: str | None = None, documented_only: bool = False,
                      limit: int = 25) -> list[dict]:
    """Busca nos 384 componentes do hades.jar (classe, descrição, nomes de portas).
    package: ex. 'gates', 'rtlib.muxes', 'flipflops'. documented_only: só os de components/ (preferíveis:
    parâmetros e comportamento conferidos). Use get_component para os detalhes."""
    return library.search(query, package, documented_only, max(1, min(limit, 200)))


@mcp.tool(annotations=RO)
def get_component(name: str) -> dict:
    """Detalhes de um componente: classe completa ou nome simples ('Mux21', 'RegRE', 'And2').
    Retorna a documentação de components/ (quando existe) e a entrada do catálogo: portas
    (direção, largura padrão, posição relativa à âncora), bbox e parâmetros padrão."""
    cls = library.resolve_class(name)
    if not cls:
        hits = library.search(name, limit=10)
        raise ValueError(f'componente {name!r} não encontrado. Parecidos: {", ".join(h["cls"] for h in hits) or "nenhum"}')
    out = dict(cls=cls, catalog=library.catalog()[cls])
    d = library.documented().get(cls)
    if d:
        out['doc_path'] = d['path']
        out['doc'] = library.read_text(d['path'])
    else:
        out['note'] = ('Não documentado em components/: posições valem para os parâmetros padrão; '
                       'conferir no HADES antes de usar (ADICIONANDO_COMPONENTES.md).')
    types = natives.CLASS_TO_TYPES.get(cls)
    if types:
        out['build_design_types'] = types
    return out


@mcp.tool(annotations=RO)
def list_native_types() -> list[dict]:
    """Tipos aceitos em build_design (hdslib.native): classe, kwargs, linha .hds, bbox e portas com
    posição relativa, direção e largura (para os kwargs de exemplo)."""
    return natives.table()


@mcp.tool(annotations=RO)
def describe_native_type(type: str, params: dict[str, Any] | None = None) -> dict:
    """Portas/bbox de um tipo de build_design com parâmetros específicos (ex. type='Expander',
    params={'n': 8}) — útil para símbolos dinâmicos e para calcular posições antes de ligar fios."""
    if type not in natives.NATIVE:
        raise ValueError(f'tipo desconhecido {type}; ver list_native_types')
    return natives.describe(type, **(params or {}))


@mcp.tool(annotations=RO)
def list_library(folder: str = '') -> dict:
    """Lista arquivos da biblioteca. folder: '', 'components', 'components/mux', 'catalog', 'examples',
    'examples/mux4', 'blocks', 'tools/gerador'..."""
    base = (library.ROOT / folder).resolve()
    if base != library.ROOT and library.ROOT not in base.parents or not base.is_dir():
        raise ValueError(f'pasta inválida: {folder}')
    dirs, files = [], []
    for p in sorted(base.iterdir()):
        if p.name.startswith('.') or p.name in ('mcp-server', '__pycache__'):
            continue
        (dirs if p.is_dir() else files).append(p.name)
    return dict(folder=folder or '.', dirs=dirs, files=files)


@mcp.tool(annotations=RO)
def read_library_file(path: str) -> str:
    """Lê um arquivo de texto da biblioteca (ex. 'examples/contador4/CONTADOR4.hds',
    'blocks/SHIFTLEFT2.sym', 'catalog/rtlib.md', 'tools/gerador/mips/top_mono.py')."""
    return library.read_text(path)


# ---------------------------------------------------------------- geração
@mcp.tool(annotations=RW, structured_output=False)
def build_design(spec: dict[str, Any], save_to: str | None = None, preview: bool = False):
    """Gera .hds (e .sym dos subcircuitos) a partir de uma especificação JSON, validando com o hdslib.

    spec = {
      "name": "TOPO",
      "components": [{"type": "Ipin", "name": "A", "x": 1200, "y": 1200, "params": {"v": "0"}}, ...],
      "instances": [{"block": "SUB", "name": "U1", "x": 9600, "y": 1200}],
      "wires": [{"name": "n0", "paths": [["A.Y", [3600, 1200], "AND.A"], [[3600, 1200], "OR.A"]]}],
      "expansions": [[x, y]], "allow_open": ["ALU.CIN"],
      "subcircuits": {"SUB": {<mesmo formato>, "symbol": "standard" |
                      {"width": 4800, "height": 1200, "ports": [["A", "T", 1200], ["Y", "R", 600]]}}}
    }
    Tipos e kwargs: list_native_types. Pontos: "INST.PORTA" ou [x, y]; cada caminho = polilinha ortogonal;
    vários caminhos = derivações (solda automática). "auto_elbow": true insere cantos automaticamente.
    ok=true só sem erros e sem avisos. save_to: pasta relativa no workspace (/work) para gravar os arquivos.
    preview: inclui PNG do circuito principal."""
    try:
        res = specmod.build(spec)
    except (specmod.SpecError, AssertionError, KeyError, TypeError, ValueError) as e:
        raise ValueError(f'especificação inválida: {e}') from None
    top = res.pop('_top')
    if save_to and res['ok']:
        res['saved'] = _save(res['files'], save_to)
    elif save_to:
        res['saved'] = []
        res['note'] = 'não gravado: corrigir erros/avisos primeiro'
    img = None
    if preview and not res['designs'][top.name]['errors']:
        try:
            img = _png(top)
        except Exception as e:  # prévia é opcional: não perder os arquivos gerados
            res['preview_error'] = f'{type(e).__name__}: {e}'
    out = [json.dumps(res, ensure_ascii=False, indent=1)]
    return out + [img] if img else out


@mcp.tool(annotations=RW)
def make_rom(entries: list[dict[str, Any]], bits: int = 32, words: int | None = None,
             header: str | None = None, save_to: str | None = None) -> dict:
    """Gera conteúdo .rom no padrão da biblioteca (endereço 4 dígitos, dado bits/4 dígitos, comentários).
    entries: [{"addr": 0, "data": "8C010003", "comment": "lw $1, 3($0)"}]; strings são sempre hex
    (prefixo 0x opcional), inteiros JSON são decimais.
    Endereço = índice de PALAVRA (byte/4 se o circuito usa ShiftRightLogic 2).
    save_to: caminho do arquivo no workspace (ex. 'meu_proj/program.rom')."""
    text = rom.make(entries, bits, words, header)
    out = dict(text=text)
    if save_to:
        p = _wpath(save_to); p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding='utf-8', newline='\n')
        out['saved'] = save_to
    return out


@mcp.tool(annotations=RO)
def validate_rom(text: str | None = None, path: str | None = None, bits: int | None = None,
                 words: int | None = None) -> dict:
    """Confere um .rom (texto ou caminho no workspace): formato <endereço_hex>:<dado_hex>, limites."""
    if text is None:
        if not path:
            raise ValueError('informe text ou path')
        text = _wpath(path, True).read_text(encoding='utf-8')
    return rom.validate(text, bits, words)


# ---------------------------------------------------------------- validação de .hds existentes
def _load(hds: str | None, path: str | None, symbols, subdesigns):
    symbols = dict(symbols or {}); subdesigns = dict(subdesigns or {})
    base = None
    if hds is None:
        if not path:
            raise ValueError('informe hds (texto) ou path (arquivo no workspace)')
        p = _wpath(path, True); base = p.parent
        hds = p.read_text(encoding='utf-8', errors='replace')
    ws = _workspace()
    P0 = hdsparse.parse(hds)
    refs = hdsparse.referenced_files(P0)
    missing, outside = [], []
    for sub in refs['subcircuits']:
        stem = (sub[:-4] if sub.endswith('.hds') else sub).replace('\\', '/')
        found_sym = hdsparse._lookup(symbols, stem + '.sym', '.sym') is not None
        if base is not None:
            for ext, store in (('.sym', symbols), ('.hds', subdesigns)):
                f = (base / (stem + ext)).resolve()
                if not _inside(ws, f):          # nunca ler fora do workspace (../, links simbólicos)
                    outside.append(stem + ext)
                elif f.is_file():
                    # chave = caminho como escrito no .hds: a/X e b/X não colidem
                    store.setdefault(stem + ext, f.read_text(encoding='utf-8', errors='replace'))
                    if ext == '.sym':
                        found_sym = True
                elif ext == '.sym' and not found_sym:
                    missing.append(stem + ext)
        # blocos genéricos da biblioteca (blocks/)
        lib = library.ROOT / 'blocks' / (Path(stem).name + '.sym')
        if not found_sym and lib.is_file():
            symbols.setdefault(lib.name, lib.read_text(encoding='utf-8'))
    if base is not None:
        for r in refs['roms']:
            f = (base / r).resolve()
            if not _inside(ws, f):
                outside.append(r)
            elif not f.is_file():
                missing.append(r)
    return hds, symbols, subdesigns, refs, missing, outside


@mcp.tool(annotations=RO)
def validate_hds(hds: str | None = None, path: str | None = None, symbols: dict[str, str] | None = None,
                 subdesigns: dict[str, str] | None = None) -> dict:
    """Valida um .hds existente contra as regras da biblioteca (FORMATO_HDS.md, LAYOUT.md).

    hds: texto do arquivo, ou path: arquivo no workspace (.sym/.hds/.rom vizinhos são lidos sozinhos).
    symbols: {"BLOCO.sym": texto} dos subcircuitos usados; subdesigns: {"BLOCO.hds": texto} (opcional,
    dá direção/largura dos pinos). Retorno: errors (quebram carga/simulação), lint (regras de desenho
    da biblioteca: pontas soltas, diagonais, solda, portas no meio de fio, toques entre sinais),
    warnings (entradas abertas, componentes não documentados...), referenced_files, missing_files,
    outside_workspace (referências fora do workspace: não lidas; passe o .sym em symbols)."""
    hds, symbols, subdesigns, refs, missing, outside = _load(hds, path, symbols, subdesigns)
    P = hdsparse.check(hds, symbols, subdesigns)
    return dict(ok=not P.errors, clean=not P.errors and not P.lint, name=P.name,
                components=len(P.comps), signals=len(P.sigs), errors=P.errors, lint=P.lint,
                warnings=P.warnings, referenced_files=refs, missing_files=missing,
                outside_workspace=outside)


@mcp.tool(annotations=RO, structured_output=False)
def render_hds(hds: str | None = None, path: str | None = None, symbols: dict[str, str] | None = None):
    """Prévia PNG de um .hds (caixas dos componentes, portas, fios coloridos por sinal, pontos de solda).
    Mesmos parâmetros de validate_hds. Bom para conferir layout sem abrir o HADES."""
    hds, symbols, *_ = _load(hds, path, symbols, None)
    P = hdsparse.parse(hds, symbols)
    return _png(hdsparse.to_render_design(P))


# ---------------------------------------------------------------- workspace
@mcp.tool(annotations=RO)
def list_workspace(folder: str = '') -> dict:
    """Lista arquivos do workspace (pasta montada em /work no Docker)."""
    p = _wpath(folder, True)
    if not p.is_dir():
        raise ValueError(f'{folder} não é pasta')
    items = sorted(p.iterdir())
    return dict(folder=folder or '.', dirs=[i.name for i in items if i.is_dir()],
                files=[i.name for i in items if i.is_file()])


@mcp.tool(annotations=RO)
def read_workspace_file(path: str) -> str:
    """Lê um arquivo de texto do workspace (.hds, .sym, .rom...)."""
    return _wpath(path, True).read_text(encoding='utf-8', errors='replace')


@mcp.tool(annotations=RW)
def write_workspace_file(path: str, content: str) -> dict:
    """Grava (ou substitui) um arquivo de texto no workspace — ex. um .hds corrigido. Validar antes."""
    p = _wpath(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding='utf-8', newline='\n')
    return dict(saved=path, bytes=len(content.encode('utf-8')))


# ---------------------------------------------------------------- recursos e prompts
for _name, _desc in library.DOCS.items():
    def _mk(n):
        def _r() -> str:
            return library.doc(n)
        return _r
    mcp.resource(f'hades://docs/{_name}', name=_name, description=_desc, mime_type='text/markdown')(_mk(_name))


@mcp.prompt()
def novo_circuito(descricao: str) -> str:
    """Roteiro para criar um circuito HADES novo a partir de uma descrição."""
    return (f'Crie um circuito HADES: {descricao}\n\n'
            '1. Leia FORMATO_HDS e LAYOUT (read_doc).\n'
            '2. Escolha componentes com search_components/get_component (prefira documented_only).\n'
            '3. Monte a especificação e chame build_design com preview=true; corrija até ok=true.\n'
            '4. Para memórias use make_rom. 5. Explique como simular no HADES e o que esperar.')


@mcp.prompt()
def corrigir_hds(arquivo: str) -> str:
    """Roteiro para diagnosticar e corrigir um .hds existente."""
    return (f'Diagnostique e corrija o arquivo HADES {arquivo}.\n\n'
            '1. validate_hds (path ou texto) e render_hds.\n'
            '2. Para cada erro/lint, consulte get_component e LAYOUT/FORMATO_HDS; não invente portas.\n'
            '3. Corrija preservando nomes de instâncias e sinais; revalide até errors=[] e lint=[].\n'
            '4. Grave com write_workspace_file e resuma o que mudou.')


def main(argv=None):
    ap = argparse.ArgumentParser(prog='hades-mcp', description='Servidor MCP da biblioteca HADES')
    ap.add_argument('--transport', choices=['stdio', 'streamable-http', 'sse'],
                    default=os.environ.get('HADES_MCP_TRANSPORT', 'stdio'))
    ap.add_argument('--host', default=os.environ.get('HADES_MCP_HOST', '127.0.0.1'))
    ap.add_argument('--port', type=int, default=int(os.environ.get('HADES_MCP_PORT', '8000')))
    ap.add_argument('--path', default=os.environ.get('HADES_MCP_PATH', '/mcp'))
    a = ap.parse_args(argv)
    if a.transport == 'stdio':
        mcp.run('stdio')
    elif a.transport == 'sse':
        mcp.run('sse', host=a.host, port=a.port)
    else:
        mcp.run('streamable-http', host=a.host, port=a.port, streamable_http_path=a.path, stateless_http=True)


if __name__ == '__main__':
    main()
