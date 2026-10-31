"""Leitura e validação de arquivos .hds/.sym existentes (escritos à mão, pelo editor ou por LLM).

O validador do hdslib (Design.build) trabalha sobre projetos descritos em Python. Aqui o caminho é o
inverso: parte do texto .hds, reconstrói componentes/portas (hdslib.native(), catalog/components.json
ou o .sym do subcircuito) e aplica as mesmas regras de FORMATO_HDS.md e LAYOUT.md.

Níveis do relatório:
- errors:   quebram carga/simulação (porta inexistente, largura errada, 2 saídas, linha malformada...)
- lint:     regras de desenho da biblioteca (geometria) — o HADES até carrega, mas o editor se perde
- warnings: avisos (entrada aberta, caixas sobrepostas, posição não verificável...)
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import PurePosixPath

from . import library
from .library import hdslib
from .natives import BadParams, kwargs_from_line

G = 600
NAME_RE = re.compile(r'^[A-Za-z0-9_]+$')
SECTIONS = ['[components]', '[end components]', '[signals]', '[end signals]', '[end]']
DIRMAP = {'IN': 'in', 'OUT': 'out', 'INOUT': 'inout', 'PASSIVE_IN': 'in'}


@dataclass
class PComp:
    cls: str
    name: str
    x: int
    y: int
    orient: str
    params: list[str]
    lineno: int
    ports: dict | None = None      # porta -> (rx, ry, dir|None, largura|None, 's'|'v'|None)
    bbox: tuple | None = None      # relativo à âncora
    exact: bool = True             # posições confiáveis para os parâmetros usados
    block: object = None

    def p(self, port):
        r = self.ports[port]
        return (self.x + r[0], self.y + r[1])

    @property
    def abbox(self):
        b = self.bbox or (0, 0, 0, 0)
        return (self.x + b[0], self.y + b[1], self.x + b[2], self.y + b[3])


@dataclass
class PSig:
    name: str
    kind: str          # 's' | 'v'
    width: int
    conns: list
    segs: list
    dots: list
    lineno: int


@dataclass
class Parsed:
    name: str | None = None
    comps: dict = field(default_factory=dict)
    sigs: list = field(default_factory=list)
    errors: list = field(default_factory=list)
    lint: list = field(default_factory=list)
    warnings: list = field(default_factory=list)


def parse_sym(text: str) -> dict:
    ports, bbox = {}, None
    for ln in text.splitlines():
        t = ln.split()
        if len(t) >= 4 and t[0] == 'hades.symbols.PortSymbol':
            ports[t[3]] = (int(t[1]), int(t[2]))
        elif len(t) >= 5 and t[0] == 'hades.symbols.BboxRectangle':
            bbox = tuple(int(v) for v in t[1:5])
    return dict(ports=ports, bbox=bbox)


def subdesign_pins(text: str) -> dict:
    """Pinos de um .hds de subcircuito: nome -> (dir vista de fora, largura, tipo)."""
    out = {}
    for ln in text.splitlines():
        t = ln.split()
        if len(t) < 6 or t[4][:1] != '@':
            continue
        cls, name, params = t[0], t[1], t[6:]
        if cls == 'hades.models.io.Ipin':
            out[name] = ('in', 1, 's')
        elif cls == 'hades.models.io.Opin':
            out[name] = ('out', 1, 's')
        elif cls == 'hades.models.rtlib.io.IpinVector' and params:
            out[name] = ('in', int(params[0]), 'v')
        elif cls == 'hades.models.rtlib.io.OpinVector' and params:
            out[name] = ('out', int(params[0]), 'v')
    return out


def _stem(path: str) -> str:
    return PurePosixPath(path.replace('\\', '/')).stem


def _lookup(d: dict | None, path: str, ext: str):
    if not d:
        return None
    norm = path.replace('\\', '/')
    for cand in (norm, norm.rsplit('/', 1)[-1], _stem(norm) + ext, _stem(norm)):
        if cand in d:
            return d[cand]
    return None


def _resolve_ports(c: PComp, P: Parsed, symbols, subdesigns):
    if c.cls == 'hades.models.Design':
        if not c.params:
            P.errors.append(f'linha {c.lineno}: {c.name}: subcircuito sem caminho do .hds'); return
        path = c.params[0]
        sym = _lookup(symbols, path[:-4] + '.sym' if path.endswith('.hds') else path, '.sym')
        if sym is None:
            P.warnings.append(f'{c.name}: .sym de {path} não fornecido; conexões do subcircuito não verificadas')
            return
        s = parse_sym(sym)
        pins = subdesign_pins(_lookup(subdesigns, path, '.hds') or '')
        if pins and set(pins) != set(s['ports']):
            P.errors.append(f'{c.name}: pinos do .sym {sorted(s["ports"])} != Ipin/Opin do .hds {sorted(pins)}')
        c.ports = {pn: (x, y) + (pins.get(pn) or (None, None, None)) for pn, (x, y) in s['ports'].items()}
        c.bbox = s['bbox'] or (0, 0, 0, 0)
        c.block = s
        return
    try:
        nk = kwargs_from_line(c.cls, c.params)
    except BadParams as e:
        P.errors.append(f'linha {c.lineno}: {c.name}: {e} (ver get_component)')
        return
    if nk:
        t, kw = nk
        try:
            _, params, ports, bbox = hdslib.native(t, **kw)
            c.ports, c.bbox = dict(ports), bbox
            _check_vector_literals(c, t, kw, P)
            return
        except Exception as e:  # parâmetros incoerentes
            P.errors.append(f'linha {c.lineno}: {c.name}: parâmetros inválidos para {c.cls}: {e}')
            return
    e = library.catalog().get(c.cls)
    if not e:
        P.errors.append(f'linha {c.lineno}: classe desconhecida {c.cls} (não está em catalog/components.json)')
        return
    c.ports = {}
    for p in e['ports']:
        if p['pos'] is None:
            continue
        w = None if p['vector'] else p['default_width']
        c.ports[p['name']] = (p['pos'][0], p['pos'][1], DIRMAP.get(p['dir']), w, 'v' if p['vector'] else 's')
    c.bbox = tuple(e['bbox']) if e['bbox'] else (0, 0, 0, 0)
    if e['dynamic_symbol']:
        c.exact = False
        P.warnings.append(f'{c.name}: {c.cls.rsplit(".", 1)[-1]} tem símbolo dinâmico; posições conferidas só para '
                          f'os parâmetros padrão ({e["default_params"]})')
    if c.cls not in library.documented():
        P.warnings.append(f'{c.name}: {c.cls} não documentado em components/ (ADICIONANDO_COMPONENTES.md)')


def _check_vector_literals(c: PComp, t, kw, P: Parsed):
    exp = None
    if t == 'Subset':
        exp = kw['u'] - kw['l'] + 1
    elif 'n' in kw:
        exp = kw['n']
    if exp is None:
        return
    for tok in c.params:
        if tok.endswith('_B'):
            bits = tok[:-2]
            if len(bits) != exp or set(bits) - set('01XUZ'):
                P.errors.append(f'linha {c.lineno}: {c.name}: vetor {tok} deve ter exatamente {exp} caracteres de 01XUZ')


def parse(text: str, symbols: dict | None = None, subdesigns: dict | None = None) -> Parsed:
    P = Parsed()
    lines = text.splitlines()
    seen = [ln.strip() for ln in lines if ln.strip().startswith('[')]
    heads = [s.split()[0] if not s.startswith('[end') else s for s in seen]
    for s in ['[name]'] + SECTIONS:
        if s not in heads:
            P.errors.append(f'seção ausente: {s}')
    if lines[:1] != ['# hades.models.Design file']:
        P.lint.append('cabeçalho: a 1ª linha deve ser "# hades.models.Design file" (FORMATO_HDS.md)')
    sec = None
    for i, raw in enumerate(lines, 1):
        ln = raw.strip()
        if not ln or ln.startswith('#'):
            continue
        if ln.startswith('[name]'):
            P.name = ln[6:].strip() or None
            if P.name and ' ' in P.name:
                P.errors.append(f'linha {i}: [name] com espaço')
            continue
        if ln in ('[components]', '[signals]'):
            sec = ln; continue
        if ln.startswith('[end'):
            sec = None; continue
        t = ln.split()
        if sec == '[components]':
            _parse_comp(t, i, P)
        elif sec == '[signals]':
            _parse_sig(t, i, P)
        else:
            P.errors.append(f'linha {i}: conteúdo fora de seção: {ln[:60]}')
    for c in P.comps.values():
        _resolve_ports(c, P, symbols, subdesigns)
    return P


def _parse_comp(t, i, P: Parsed):
    if len(t) < 6:
        P.errors.append(f'linha {i}: componente malformado'); return
    cls, name = t[0], t[1]
    try:
        x, y = int(t[2]), int(t[3])
    except ValueError:
        P.errors.append(f'linha {i}: coordenadas inválidas'); return
    orient, ver = t[4], t[5]
    if orient not in ('@N', '@X', '@Y'):
        P.errors.append(f'linha {i}: orientação {orient} inválida (use @N)')
    elif orient != '@N':
        P.lint.append(f'linha {i}: {name} espelhado ({orient}); posições das portas não conferidas')
    if ver != '1001':
        P.errors.append(f'linha {i}: versão {ver} (deve ser 1001)')
    if name in P.comps:
        P.errors.append(f'linha {i}: instância duplicada {name}')
    if not NAME_RE.match(name):
        P.lint.append(f'linha {i}: nome de instância {name} fora de [A-Za-z0-9_]')
    if x % G or y % G:
        P.lint.append(f'linha {i}: {name} fora da grade de 600 ({x},{y})')
    P.comps[name] = PComp(cls, name, x, y, orient, t[6:], i)


def _parse_sig(t, i, P: Parsed):
    try:
        cls, name = t[0], t[1]
        k = 2
        if cls == 'hades.signals.SignalStdLogicVector':
            kind, width = 'v', int(t[2]); k = 3
        elif cls == 'hades.signals.SignalStdLogic1164':
            kind, width = 's', 1
        else:
            P.errors.append(f'linha {i}: classe de sinal desconhecida {cls}'); return
        nc = int(t[k]); k += 1
        conns = [(t[k + 2 * j], t[k + 2 * j + 1]) for j in range(nc)]; k += 2 * nc
        ns = int(t[k]); k += 1
        segs = []
        for _ in range(ns):
            npt = int(t[k]); k += 1
            pts = [(int(t[k + 2 * j]), int(t[k + 2 * j + 1])) for j in range(npt)]; k += 2 * npt
            segs += list(zip(pts, pts[1:]))
        nd = int(t[k]); k += 1
        dots = [(int(t[k + 2 * j]), int(t[k + 2 * j + 1])) for j in range(nd)]; k += 2 * nd
        if k != len(t):
            P.errors.append(f'linha {i}: {name}: {len(t) - k} tokens sobrando no fim do sinal')
    except (IndexError, ValueError):
        P.errors.append(f'linha {i}: sinal malformado ({" ".join(t[:2])})'); return
    if any(s.name == name for s in P.sigs):
        P.errors.append(f'linha {i}: sinal duplicado {name}')
    if not NAME_RE.match(name):
        P.lint.append(f'linha {i}: nome de sinal {name} fora de [A-Za-z0-9_]')
    P.sigs.append(PSig(name, kind, width, conns, segs, dots, i))


# ---------------------------------------------------------------- validação
def validate(P: Parsed) -> Parsed:
    E, L, W = P.errors, P.lint, P.warnings
    on_seg, on_int, overlap = hdslib.on_seg, hdslib.on_interior, hdslib.overlap
    portat = {}
    for c in P.comps.values():
        if c.ports is None or c.orient != '@N':
            continue
        for pn in c.ports:
            portat.setdefault(c.p(pn), []).append((c.name, pn))
    for pos, lst in portat.items():
        if len(lst) > 1:
            L.append(f'portas coincidentes em {pos}: {lst}')
    used = {}
    for s in P.sigs:
        # conexões declaradas
        drivers, unknown_dir = [], False
        for inst, pn in s.conns:
            c = P.comps.get(inst)
            if c is None:
                E.append(f'{s.name}: instância inexistente {inst}'); continue
            key = (inst, pn)
            if key in used:
                E.append(f'porta {inst}.{pn} em dois sinais: {used[key]} e {s.name}')
            used[key] = s.name
            if c.ports is None:
                unknown_dir = True; continue
            if pn not in c.ports:
                E.append(f'{s.name}: {inst} ({c.cls.rsplit(".", 1)[-1]}) não tem porta {pn}; portas: {", ".join(c.ports)}')
                continue
            _, _, d, w, kd = c.ports[pn]
            if kd and kd != s.kind:
                E.append(f'{s.name}: tipo {"vetor" if s.kind == "v" else "1 bit"} mas {inst}.{pn} é '
                         f'{"vetor" if kd == "v" else "1 bit"} (FORMATO_HDS.md regra 4)')
            if w is not None and w != s.width:
                E.append(f'{s.name}: largura {s.width} mas {inst}.{pn} tem {w} bits')
            if d is None:
                unknown_dir = True
            elif d == 'out':
                drivers.append(f'{inst}.{pn}')
        if len(drivers) > 1:
            E.append(f'{s.name}: {len(drivers)} saídas ligadas ({", ".join(drivers)}); deve haver exatamente 1')
        elif not drivers and not unknown_dir and s.conns:
            E.append(f'{s.name}: nenhuma saída ligada (sinal sem driver)')
        if len(s.conns) < 2:
            W.append(f'{s.name}: menos de 2 conexões')
        # geometria
        if not s.segs:
            L.append(f'{s.name}: sem segmentos (invisível no editor)')
            continue
        segs = []
        for a, b in s.segs:
            if a == b:
                L.append(f'{s.name}: segmento nulo em {a}'); continue
            if a[0] != b[0] and a[1] != b[1]:
                L.append(f'{s.name}: segmento diagonal {a}-{b}')
            if any(v % G for v in a + b):
                L.append(f'{s.name}: segmento fora da grade {a}-{b}')
            segs.append((a, b))
        ends = {p for seg in segs for p in seg}
        changed = True
        while changed:
            changed = False
            for e in ends:
                for k, (a, b) in enumerate(segs):
                    if (a[0] == b[0] or a[1] == b[1]) and on_int(e, a, b):
                        segs[k:k + 1] = [(a, e), (e, b)]; changed = True; break
                if changed:
                    break
        deg = {}
        for a, b in segs:
            deg[a] = deg.get(a, 0) + 1; deg[b] = deg.get(b, 0) + 1
        declared = set(s.conns)
        geo = set()
        for pt, d in deg.items():
            if pt in portat:
                geo.update(portat[pt])
                if d != 1:
                    L.append(f'{s.name}: porta {portat[pt]} no meio do fio ({d} segmentos); deve ser ponta')
            elif d == 1:
                L.append(f'{s.name}: ponta solta em {pt}')
        for inst, pn in declared:
            c = P.comps.get(inst)
            if c and c.ports and pn in c.ports and c.orient == '@N' and c.exact and c.p(pn) not in deg:
                L.append(f'{s.name}: nenhum segmento termina em {inst}.{pn} {c.p(pn)}')
        for cp in geo - declared:
            L.append(f'{s.name}: fio toca {cp[0]}.{cp[1]} mas a porta não está nas conexões do sinal')
        for pos, lst in portat.items():
            for a, b in segs:
                if on_int(pos, a, b) and not set(lst) & declared:
                    L.append(f'{s.name}: passa sobre a porta {lst} em {pos}')
        real_dots = sorted(pt for pt, d in deg.items() if d >= 3)
        if set(real_dots) != set(s.dots):
            L.append(f'{s.name}: pontos de solda declarados {sorted(s.dots)} != junções de 3+ segmentos {real_dots}')
        s.segs_split = segs
    # entre sinais
    allsegs = [(s.name, a, b) for s in P.sigs for a, b in getattr(s, 'segs_split', [])]
    for i in range(len(allsegs)):
        ni, a1, b1 = allsegs[i]
        for j in range(i + 1, len(allsegs)):
            nj, a2, b2 = allsegs[j]
            if ni == nj:
                continue
            if overlap((a1, b1), (a2, b2)):
                L.append(f'sobreposição {ni} {a1}-{b1} x {nj} {a2}-{b2}')
            elif any(on_seg(e, a2, b2) for e in (a1, b1)) or any(on_seg(e, a1, b1) for e in (a2, b2)):
                L.append(f'toque entre {ni} e {nj} ({a1}-{b1} / {a2}-{b2})')
    # caixas e entradas abertas
    cl = [c for c in P.comps.values() if c.bbox]
    for i in range(len(cl)):
        for j in range(i + 1, len(cl)):
            if hdslib.box_overlap(cl[i].abbox, cl[j].abbox):
                W.append(f'caixas sobrepostas {cl[i].name} {cl[j].name}')
    for c in P.comps.values():
        for pn, r in (c.ports or {}).items():
            if r[2] == 'in' and (c.name, pn) not in used:
                W.append(f'entrada aberta {c.name}.{pn}')
    # padrão: memória dentro de subcircuito não dá para saber aqui; ROM sem arquivo:
    for c in P.comps.values():
        if c.cls.endswith('memory.ROM') and len(c.params) < 3:
            W.append(f'{c.name}: ROM sem arquivo .rom (ARQUIVOS_PARA_MEMORIA.md)')
    P.lint = list(dict.fromkeys(L)); P.warnings = list(dict.fromkeys(W)); P.errors = list(dict.fromkeys(E))
    return P


def check(text: str, symbols=None, subdesigns=None) -> Parsed:
    return validate(parse(text, symbols, subdesigns))


def referenced_files(P: Parsed) -> dict:
    """Arquivos que o .hds referencia: subcircuitos (.hds/.sym) e memórias (.rom)."""
    subs, roms = [], []
    for c in P.comps.values():
        if c.cls == 'hades.models.Design' and c.params:
            subs.append(c.params[0])
        elif c.cls.startswith('hades.models.rtlib.memory.'):
            roms += [p for p in c.params if p.endswith('.rom')]
    return dict(subcircuits=sorted(set(subs)), roms=sorted(set(roms)))


def to_render_design(P: Parsed):
    """Converte em objeto aceito por hdslib.render()."""
    d = hdslib.Design(P.name or 'hds')

    class _Blk:  # rótulo para render()
        def __init__(self, label):
            self.label = label
    for c in P.comps.values():
        o = hdslib.Comp.__new__(hdslib.Comp)
        o.cls, o.name, o.x, o.y, o.params = c.cls, c.name, c.x, c.y, ' '.join(c.params)
        o.rports = {pn: r for pn, r in (c.ports or {}).items()}
        o.bbox = c.abbox
        o.block = _Blk(_stem(c.params[0])) if c.cls == 'hades.models.Design' and c.params else None
        d.comps[c.name] = o
    d.built = [dict(name=s.name, segs=s.segs, conns=s.conns, dots=s.dots, w=s.width, kind=s.kind) for s in P.sigs]
    return d
