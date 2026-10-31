"""Acesso à biblioteca HADES (docs, catálogo, componentes, exemplos) a partir do disco.

A raiz é procurada em: $HADES_LIB_ROOT, depois subindo a partir deste arquivo até achar INDEX.md
(funciona tanto no repositório quanto na imagem Docker, onde a biblioteca fica em /opt/hades-lib).
"""
from __future__ import annotations

import json
import os
import re
import sys
from functools import lru_cache
from pathlib import Path

# Guias da raiz, na ordem de leitura do README.
DOCS = {
    'README': 'Visão geral, ordem de leitura e regras essenciais',
    'FORMATO_HDS': 'Gramática do arquivo .hds (obrigatório)',
    'INDEX': 'Índice dos componentes documentados',
    'LAYOUT': 'Posicionamento, fios, reset, boas práticas de desenho',
    'SUBCIRCUITOS': 'Hierarquia: hades.models.Design e .sym',
    'PORTAS_MISTAS': 'Subcircuitos com portas fora do padrão esquerda/direita',
    'ARQUIVOS_PARA_MEMORIA': 'Formato .rom para ROM/RAM/bancos de registradores',
    'GERADOR': 'Gerador Python (hdslib) e validação automática',
    'ADICIONANDO_COMPONENTES': 'Como documentar um componente novo',
    'TEMPLATE_COMPONENTE': 'Modelo de documentação de componente',
}


def _find_root() -> Path:
    env = os.environ.get('HADES_LIB_ROOT')
    if env:
        p = Path(env).resolve()
        if (p / 'INDEX.md').is_file():
            return p
        raise RuntimeError(f'HADES_LIB_ROOT={env} não contém INDEX.md')
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / 'INDEX.md').is_file() and (parent / 'catalog' / 'components.json').is_file():
            return parent
    raise RuntimeError('biblioteca HADES não encontrada; defina HADES_LIB_ROOT')


ROOT = _find_root()

# hdslib vive em tools/gerador e é importado direto de lá (fonte única de verdade).
_GERADOR = ROOT / 'tools' / 'gerador'
if str(_GERADOR) not in sys.path:
    sys.path.insert(0, str(_GERADOR))
import hdslib  # noqa: E402


def read_text(rel: str) -> str:
    p = (ROOT / rel).resolve()
    if ROOT not in p.parents and p != ROOT:
        raise ValueError(f'caminho fora da biblioteca: {rel}')
    return p.read_text(encoding='utf-8')


def doc(name: str) -> str:
    key = name.upper().removesuffix('.MD')
    if key not in DOCS:
        raise KeyError(f'doc desconhecido: {name}. Disponíveis: {", ".join(DOCS)}')
    return read_text(f'{key}.md')


@lru_cache(maxsize=1)
def catalog() -> dict:
    return json.loads(read_text('catalog/components.json'))


@lru_cache(maxsize=1)
def documented() -> dict[str, dict]:
    """classe Java -> {name, path, category, title} para os componentes de components/."""
    out = {}
    for md in sorted((ROOT / 'components').glob('*/*.md')):
        txt = md.read_text(encoding='utf-8')
        m = re.search(r'^Classe:\s*`([^`]+)`', txt, re.M)
        if not m:
            continue
        title = txt.splitlines()[0].lstrip('# ').strip()
        out[m.group(1)] = dict(name=md.stem, path=str(md.relative_to(ROOT)), category=md.parent.name, title=title)
    return out


def resolve_class(name: str) -> str | None:
    """Aceita classe completa, nome simples ('Mux21') ou nome de doc; devolve a classe Java."""
    cat = catalog()
    if name in cat:
        return name
    low = name.lower()
    for cls, d in documented().items():
        if d['name'].lower() == low:
            return cls
    hits = [c for c in cat if c.rsplit('.', 1)[-1].lower() == low]
    if len(hits) == 1:
        return hits[0]
    if hits:
        # preferir a documentada, depois rtlib
        for c in hits:
            if c in documented():
                return c
        for c in hits:
            if '.rtlib.' in c:
                return c
        return hits[0]
    return None


def search(query: str = '', package: str | None = None, documented_only: bool = False, limit: int = 25) -> list[dict]:
    terms = [t for t in query.lower().split() if t]
    docs = documented()
    res = []
    for cls, e in catalog().items():
        if documented_only and cls not in docs:
            continue
        pkg = cls.removeprefix('hades.models.').rsplit('.', 1)[0]
        if package and not (pkg == package or pkg.startswith(package + '.')):
            continue
        hay = ' '.join([cls.lower(), (e.get('description') or '').lower(),
                        docs.get(cls, {}).get('title', '').lower(), ' '.join(p['name'].lower() for p in e['ports'])])
        if terms and not all(t in hay for t in terms):
            continue
        score = sum(3 if t in cls.lower().rsplit('.', 1)[-1] else 1 for t in terms) + (5 if cls in docs else 0)
        res.append((score, cls, e))
    res.sort(key=lambda r: (-r[0], r[1]))
    return [dict(cls=cls, package=cls.removeprefix('hades.models.').rsplit('.', 1)[0],
                 description=e.get('description'), documented=cls in docs,
                 doc=docs.get(cls, {}).get('path'), ports=[p['name'] for p in e['ports']])
            for _, cls, e in res[:limit]]


def examples() -> dict[str, list[str]]:
    out = {}
    base = ROOT / 'examples'
    for d in sorted(p for p in base.iterdir() if p.is_dir()):
        out[d.name] = sorted(f.name for f in d.iterdir() if f.is_file())
    return out


def example_file(example: str, file: str) -> str:
    ex = examples()
    if example not in ex:
        raise KeyError(f'exemplo desconhecido: {example}. Disponíveis: {", ".join(ex)}')
    if file not in ex[example]:
        raise KeyError(f'{file} não existe em {example}: {", ".join(ex[example])}')
    return read_text(f'examples/{example}/{file}')


def blocks() -> dict[str, str]:
    return {f.name: read_text(f'blocks/{f.name}') for f in sorted((ROOT / 'blocks').iterdir()) if f.is_file()}
