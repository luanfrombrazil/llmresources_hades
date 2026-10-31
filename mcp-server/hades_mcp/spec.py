"""Monta um projeto a partir de uma especificação JSON usando hdslib (Design/Block) e devolve os arquivos.

Especificação (todas as coordenadas em unidades HADES, grade de 600):

{
  "name": "TOPO",
  "components": [ {"type": "Ipin", "name": "A", "x": 1200, "y": 1200, "params": {"v": "0"}}, ... ],
  "instances":  [ {"block": "SUB", "name": "U1", "x": 9600, "y": 1200}, ... ],
  "wires": [ {"name": "n0", "paths": [["A.Y", [3600, 1200], "AND.A"], [[3600, 1200], "OR.A"]], "auto_elbow": false} ],
  "expansions": [[x, y]],            # pontas soltas permitidas (LAYOUT.md)
  "allow_open": ["ALU.CIN"],         # entradas que podem ficar abertas
  "subcircuits": {                   # subcircuitos usados em "instances" (mesmo formato, recursivo)
     "SUB": { ...mesmo formato..., "symbol": "standard" | {"width": 4800, "height": 1200,
                                    "ports": [["A", "T", 1200], ["Y", "R", 600]], "label": "SUB"} }
  }
}

Pontos de um caminho: "INST.PORTA" (posição absoluta da porta) ou [x, y].
"auto_elbow": insere um canto (x do destino, y da origem) entre pontos não alinhados.
"""
from __future__ import annotations

import os
import tempfile

from .library import hdslib


class SpecError(ValueError):
    pass


def _pt(d, p):
    if isinstance(p, str):
        if '.' not in p:
            raise SpecError(f'ponto "{p}": use "INSTANCIA.PORTA" ou [x, y]')
        inst, port = p.rsplit('.', 1)
        if inst not in d.comps:
            raise SpecError(f'ponto "{p}": instância {inst} não existe')
        if port not in d.comps[inst].rports:
            raise SpecError(f'ponto "{p}": {inst} não tem porta {port}; portas: {", ".join(d.comps[inst].rports)}')
        return d.P(inst, port)
    if isinstance(p, (list, tuple)) and len(p) == 2:
        return (int(p[0]), int(p[1]))
    raise SpecError(f'ponto inválido: {p!r}')


def _elbow(poly):
    out = [poly[0]]
    for b in poly[1:]:
        a = out[-1]
        if a[0] != b[0] and a[1] != b[1]:
            out.append((b[0], a[1]))
        out.append(b)
    return out


def _design(spec: dict, blocks: dict) -> hdslib.Design:
    name = spec.get('name')
    if not name:
        raise SpecError('"name" obrigatório')
    d = hdslib.Design(name)
    for c in spec.get('components', []):
        try:
            if c['x'] % 600 or c['y'] % 600:
                raise SpecError(f'{c["name"]}: âncora ({c["x"]},{c["y"]}) fora da grade de 600')
            if c['name'] in d.comps:
                raise SpecError(f'instância duplicada {c["name"]}')
            d.add(c['type'], c['name'], c['x'], c['y'], **(c.get('params') or {}))
        except KeyError as e:
            raise SpecError(f'componente {c.get("name")}: tipo/campo desconhecido {e}; ver list_native_types') from None
    for inst in spec.get('instances', []):
        blk = blocks.get(inst['block'])
        if blk is None:
            raise SpecError(f'instância {inst.get("name")}: subcircuito {inst.get("block")} não definido em "subcircuits"')
        if inst['name'] in d.comps:
            raise SpecError(f'instância duplicada {inst["name"]}')
        d.addblock(blk, inst['name'], inst['x'], inst['y'])
    for w in spec.get('wires', []):
        polys = []
        for path in w['paths']:
            poly = [_pt(d, p) for p in path]
            polys.append(_elbow(poly) if w.get('auto_elbow') else poly)
        d.wire(w['name'], *polys)
    d.expansion(*[tuple(p) for p in spec.get('expansions', [])])
    for ap in spec.get('allow_open', []):
        inst, port = ap.rsplit('.', 1)
        d.allow_open.add((inst, port))
    return d


def _block(name: str, spec: dict, blocks: dict) -> hdslib.Block:
    spec = dict(spec); spec.setdefault('name', name)
    d = _design(spec, blocks)
    sym = spec.get('symbol', 'standard')
    if sym == 'standard':
        return hdslib.Block.standard(d, label=None)
    try:
        ports = [tuple(p) for p in sym['ports']]
        return hdslib.Block(d, sym['width'], sym['height'], ports, label=sym.get('label'))
    except AssertionError as e:
        raise SpecError(f'{name}: portas do símbolo não batem com Ipin/Opin do subcircuito: {e}') from None


def build(spec: dict) -> dict:
    """Valida e gera. Retorna {ok, files{nome: texto}, designs{nome: {errors, warnings, notes, crossings}}}."""
    blocks: dict[str, hdslib.Block] = {}
    subs = spec.get('subcircuits') or {}
    # ordem: dependências primeiro (subcircuitos podem instanciar outros)
    pending = dict(subs)
    while pending:
        progressed = False
        for bname, bspec in list(pending.items()):
            deps = {i['block'] for i in bspec.get('instances', [])}
            if deps <= set(blocks):
                blocks[bname] = _block(bname, bspec, blocks)
                del pending[bname]; progressed = True
        if not progressed:
            raise SpecError(f'dependência circular ou subcircuito ausente entre: {", ".join(pending)}')
    top = _design(spec, blocks)
    report, files, ok = {}, {}, True
    with tempfile.TemporaryDirectory() as tmp:
        for bname, blk in blocks.items():
            e, w = blk.d.build()
            report[bname] = dict(errors=e, warnings=w, notes=list(blk.d.notes), crossings=blk.d.crossings() if not e else None)
            ok &= not e and not w
            blk.write(tmp)
        e, w = top.build()
        report[top.name] = dict(errors=e, warnings=w, notes=list(top.notes), crossings=top.crossings() if not e else None)
        ok &= not e and not w
        top.write(os.path.join(tmp, top.name + '.hds'))
        for f in sorted(os.listdir(tmp)):
            with open(os.path.join(tmp, f), encoding='utf-8') as fh:
                files[f] = fh.read()
    return dict(ok=ok, files=files, designs=report, _top=top)
