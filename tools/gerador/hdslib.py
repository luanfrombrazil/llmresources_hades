# hdslib: gerador/validador de .hds/.sym para o HADES. Documentação: GERADOR.md (raiz da biblioteca).
import os, math, json

# Componentes com dados internos editáveis: não vão dentro de subcircuitos (SUBCIRCUITOS.md).
DATA_CLASSES = {'hades.models.rtlib.memory.ROM', 'hades.models.rtlib.memory.ROMoe', 'hades.models.rtlib.memory.RAM',
                'hades.models.rtlib.memory.RAMoe', 'hades.models.rtlib.memory.MipsRegBank',
                'hades.models.rtlib.memory.RegBank', 'hades.models.rtlib.arith.UserDefinedALU',
                'hades.models.microjava.ALU', 'hades.models.rtlib.arith.DcoreALU'}

G = 600

def z(n, c='0'):
    return c * n + '_B'

# ---------------------------------------------------------------- componentes nativos
# porta: (x, y, dir, largura, tipo)  tipo 's' = StdLogic1164, 'v' = vetor
def native(t, **k):
    n = k.get('n', 32)
    if t == 'Ipin':
        return ('hades.models.io.Ipin', 'null ' + k.get('v', 'U'), {'Y': (0, 0, 'out', 1, 's')}, (-1200, -600, 0, 600))
    if t == 'IpinV':
        return ('hades.models.rtlib.io.IpinVector', f'{n} {z(n)} 1.0E-9 0', {'Y': (0, 0, 'out', n, 'v')}, (-4800, -600, 0, 600))
    if t == 'Opin':
        return ('hades.models.io.Opin', '5.0E-9', {'A': (0, 0, 'in', 1, 's')}, (0, -600, 1200, 600))
    if t == 'OpinV':
        return ('hades.models.rtlib.io.OpinVector', f'{n} 1.0E-9 0', {'A': (0, 0, 'in', n, 'v')}, (0, -600, 4800, 600))
    if t == 'RegRE':
        return ('hades.models.rtlib.register.RegRE', f'{n} {z(n)} 1.0E-8',
                {'ENA': (0, 600, 'in', 1, 's'), 'CLK': (0, 1200, 'in', 1, 's'), 'NR': (0, 1800, 'in', 1, 's'),
                 'D': (1800, 0, 'in', n, 'v'), 'Q': (1800, 2400, 'out', n, 'v')}, (0, 0, 3600, 2400))
    if t == 'Add':
        return ('hades.models.rtlib.arith.Add', f'{n} {z(n)} 1.0E-8',
                {'A': (1200, 0, 'in', n, 'v'), 'B': (3600, 0, 'in', n, 'v'), 'SUM': (2400, 2400, 'out', n, 'v')}, (0, 0, 4800, 2400))
    if t == 'Mux21':
        return ('hades.models.rtlib.muxes.Mux21', f'{n} {z(n)} 1.0E-8',
                {'S': (0, 1200, 'in', 1, 's'), 'A1': (1200, 0, 'in', n, 'v'), 'A0': (2400, 0, 'in', n, 'v'),
                 'Y': (1800, 1800, 'out', n, 'v')}, (0, 0, 3600, 1800))
    if t == 'Mux41':
        return ('hades.models.rtlib.muxes.Mux41', f'{n} {z(n)} 1.0E-8',
                {'S1': (0, 600, 'in', 1, 's'), 'S0': (0, 1200, 'in', 1, 's'), 'A3': (600, 0, 'in', n, 'v'),
                 'A2': (1800, 0, 'in', n, 'v'), 'A1': (3000, 0, 'in', n, 'v'), 'A0': (4200, 0, 'in', n, 'v'),
                 'Y': (2400, 1800, 'out', n, 'v')}, (0, 0, 4800, 1800))
    if t == 'UALU':
        return ('hades.models.rtlib.arith.UserDefinedALU', '32 1.0E-8 16 15 16 9 0 0 0 12 12 0 0 0 0 0 0 0 0',
                {'OPC': (0, 1200, 'in', 4, 'v'), 'A': (1200, 0, 'in', 32, 'v'), 'B': (3600, 0, 'in', 32, 'v'),
                 'Y': (2400, 2400, 'out', 32, 'v'), 'CIN': (4200, 0, 'in', 1, 's'), 'COUT': (1800, 2400, 'out', 1, 's'),
                 'ZERO': (3000, 2400, 'out', 1, 's'), 'NEG': (3300, 2400, 'out', 1, 's'), 'EQ': (3600, 2400, 'out', 1, 's'),
                 'OVF': (3900, 2400, 'out', 1, 's')}, (0, 0, 4800, 2400))
    if t == 'Subset':
        u, l = k['u'], k['l']; w = u - l + 1
        return ('hades.models.rtlib.io.Subset', f'{n} {u} {l} {z(w)} 1.0E-8',
                {'A': (0, 0, 'in', n, 'v'), 'Y': (0, 600, 'out', w, 'v')}, (-1200, 0, 1200, 600))
    if t == 'SelectBit':
        i = k['i']
        return ('hades.models.rtlib.io.SelectBit', f'{n} {i} 1.0E-8',
                {'A': (0, 0, 'in', n, 'v'), 'Y': (0, 600, 'out', 1, 's')}, (-1200, 0, 1200, 600))
    if t == 'SRL':
        return ('hades.models.rtlib.arith.ShiftRightLogic', f'{n} {k["s"]} {z(n)} 1.0E-8',
                {'A': (0, 0, 'in', n, 'v'), 'Y': (0, 1800, 'out', n, 'v')}, (-1800, 0, 1800, 1800))
    if t == 'SHL':
        return ('hades.models.rtlib.arith.ShiftLeft', f'{n} {k["s"]} {z(n)} 1.0E-8',
                {'A': (0, 0, 'in', n, 'v'), 'Y': (0, 1800, 'out', n, 'v')}, (-1800, 0, 1800, 1800))
    if t == 'ROM':
        words, bits = k['words'], k['bits']; aw = int(math.ceil(math.log2(words)))
        return ('hades.models.rtlib.memory.ROM', f'{words} {bits} {k["file"]}',
                {'A': (0, 2400, 'in', aw, 'v'), 'D': (3600, 4800, 'out', bits, 'v')}, (0, 0, 6000, 4800))
    if t == 'RAM':
        words, bits = k['words'], k['bits']; aw = int(math.ceil(math.log2(words)))
        p = f'{words} {bits}' + (f' {k["file"]}' if k.get('file') else '')
        return ('hades.models.rtlib.memory.RAM', p,
                {'A': (0, 2400, 'in', aw, 'v'), 'DIN': (3600, 0, 'in', bits, 'v'), 'DOUT': (3600, 4800, 'out', bits, 'v'),
                 'nWE': (0, 3000, 'in', 1, 's'), 'nCS': (0, 1800, 'in', 1, 's')}, (0, 0, 6000, 4800))
    if t == 'MipsRegBank':
        return ('hades.models.rtlib.memory.MipsRegBank', '32 32' + (f' {k["file"]}' if k.get('file') else ''),
                {'AR0': (0, 3000, 'in', 5, 'v'), 'AR1': (0, 3600, 'in', 5, 'v'), 'AW0': (0, 2400, 'in', 5, 'v'),
                 'DR0': (2400, 4800, 'out', 32, 'v'), 'DR1': (4800, 4800, 'out', 32, 'v'), 'DW0': (2400, 0, 'in', 32, 'v'),
                 'nWE': (0, 1800, 'in', 1, 's'), 'nCS': (0, 1200, 'in', 1, 's')}, (0, 0, 7200, 4800))
    if t == 'CmpEq':
        return ('hades.models.rtlib.compare.CompareEqual', f'{n} 0 1.0E-8',
                {'A': (1200, 0, 'in', n, 'v'), 'B': (2400, 0, 'in', n, 'v'), 'Y': (1800, 1800, 'out', 1, 's')}, (0, 0, 3600, 1800))
    if t == 'OrRed':
        return ('hades.models.rtlib.logic.Or', f'{n} 0 1.0E-8',
                {'A': (1800, 0, 'in', n, 'v'), 'Y': (1800, 1800, 'out', 1, 's')}, (0, 0, 3600, 1800))
    if t == 'Const':
        return ('hades.models.rtlib.io.Constant', f'{n} {k["v"]}_B 1.0E-8',
                {'Y': (1800, 1800, 'out', n, 'v')}, (0, 0, 3600, 1800))
    if t == 'SConst':
        return ('hades.models.rtlib.io.SmallConstant', f'{n} {k["v"]}_B 1.0E-8',
                {'Y': (600, 1200, 'out', n, 'v')}, (0, 0, 1200, 1200))
    if t == 'Gnd':
        return ('hades.models.io.Gnd', '', {'GND': (0, 0, 'out', 1, 's')}, (-600, 0, 600, 1500))
    if t in ('Nand2', 'And2', 'Or2'):
        d = k.get('d', '1.0E-8')
        return ('hades.models.gates.' + t, d,
                {'Y': (3600, 1200, 'out', 1, 's'), 'A': (0, 600, 'in', 1, 's'), 'B': (0, 1800, 'in', 1, 's')}, (0, 0, 3600, 2400))
    if t == 'And3':
        return ('hades.models.gates.And3', '1.0E-8',
                {'Y': (3600, 1200, 'out', 1, 's'), 'A': (0, 600, 'in', 1, 's'), 'B': (0, 1200, 'in', 1, 's'),
                 'C': (0, 1800, 'in', 1, 's')}, (0, 0, 3600, 2400))
    if t == 'Inv':
        d = k.get('d', '5.0E-9')
        return ('hades.models.gates.InvSmall', d, {'A': (0, 600, 'in', 1, 's'), 'Y': (1800, 600, 'out', 1, 's')}, (0, 0, 1800, 1200))
    if t == 'Expander':
        p = {'A': (600, 0, 'in', n, 'v')}
        for i in range(n):
            p[f'Y{i}'] = (600 * (n - i), 1200, 'out', 1, 's')
        return ('hades.models.rtlib.io.Expander', f'{n} 1.0E-8', p, (0, 0, 600 * (n + 1), 1200))
    if t == 'ExpV':
        p = {'A': (600, 0, 'in', n, 'v')}
        for i in range(n):
            p[f'Y{i}'] = (1200, 600 * (n - i), 'out', 1, 's')
        return ('hades.models.rtlib.io.ExpanderVertical', f'{n} 1.0E-8', p, (0, 0, 1200, 600 * (n + 1)))
    if t == 'Merge':
        p = {'Y': (600, 1200, 'out', n, 'v')}
        for i in range(n):
            p[f'A{i}'] = (600 * (n - i), 0, 'in', 1, 's')
        return ('hades.models.rtlib.io.MergeBits', f'{n} 1.0E-8', p, (0, 0, 600 * (n + 1), 1200))
    if t == 'ClockGen':
        return ('hades.models.io.ClockGen', k.get('p', '1.0 0.5 0.0'), {'clk': (2400, 1200, 'out', 1, 's')}, (0, 0, 2400, 2400))
    raise KeyError(t)


class Comp:
    def __init__(self, cls, name, x, y, params, ports, bbox, block=None):
        assert x % G == 0 and y % G == 0, (name, x, y)
        self.cls, self.name, self.x, self.y, self.params = cls, name, x, y, params
        self.rports = ports
        self.bbox = (x + bbox[0], y + bbox[1], x + bbox[2], y + bbox[3])
        self.block = block

    def p(self, port):
        r = self.rports[port]
        return (self.x + r[0], self.y + r[1])

    def line(self):
        s = f'{self.cls} {self.name} {self.x} {self.y} @N 1001'
        return s + (' ' + self.params if self.params else '')


# ---------------------------------------------------------------- design
class Design:
    def __init__(self, name):
        self.name = name
        self.comps = {}
        self.sigs = []          # (nome, [polilinhas])
        self.pins = []          # pinos do subcircuito, na ordem
        self.allow_open = set() # (inst, porta) que podem ficar abertas
        self.stubs = set()      # pontos de expansão: pontas soltas permitidas (LAYOUT.md, "Ponta de expansão")
        self.is_block = False   # True quando o Design é interno de um Block
        self.notes = []         # avisos de padrão de projeto (não bloqueiam a geração)

    def expansion(self, *pts):
        """Marca pontas de trilho deixadas soltas de propósito (barramento + projeto modular)."""
        self.stubs.update(tuple(p) for p in pts)

    def add(self, t, name, x, y, **k):
        cls, params, ports, bbox = native(t, **k)
        c = Comp(cls, name, x, y, params, ports, bbox)
        assert name not in self.comps, name
        self.comps[name] = c
        if t in ('Ipin', 'IpinV', 'Opin', 'OpinV'):
            self.pins.append(name)
        return c

    def addblock(self, blk, name, x, y):
        ports = {}
        for pn, (px, py) in blk.symports.items():
            d, w, kd = blk.pininfo[pn]
            ports[pn] = (px, py, d, w, kd)
        c = Comp('hades.models.Design', name, x, y, blk.name + '.hds', ports, (0, 0, blk.L, blk.A), block=blk)
        assert name not in self.comps, name
        self.comps[name] = c
        return c

    def wire(self, name, *polys):
        polys = [list(p) for p in polys]
        self.sigs.append((name, polys))

    def P(self, inst, port):
        return self.comps[inst].p(port)

    # ------------------------------------------------------------ montagem dos sinais
    def build(self):
        errs, warns = [], []
        portat = {}
        for c in self.comps.values():
            for pn in c.rports:
                pos = c.p(pn)
                portat.setdefault(pos, []).append((c.name, pn))
        for pos, lst in portat.items():
            if len(lst) > 1:
                errs.append(f'portas coincidentes em {pos}: {lst}')
        built = []
        used_ports = {}
        for name, polys in self.sigs:
            segs = []
            for poly in polys:
                for a, b in zip(poly, poly[1:]):
                    if a == b:
                        errs.append(f'{name}: segmento nulo em {a}')
                        continue
                    if a[0] != b[0] and a[1] != b[1]:
                        errs.append(f'{name}: segmento diagonal {a}-{b}')
                    for v in a + b:
                        if v % G:
                            errs.append(f'{name}: fora da grade {a}-{b}')
                    segs.append((a, b))
            # pontas das polilinhas
            ends = []
            for poly in polys:
                ends += [poly[0], poly[-1]]
            # divide segmentos onde uma ponta cai no meio
            changed = True
            while changed:
                changed = False
                for e in ends:
                    for i, (a, b) in enumerate(segs):
                        if on_interior(e, a, b):
                            segs[i:i + 1] = [(a, e), (e, b)]
                            changed = True
                            break
                    if changed:
                        break
            # sobreposição colinear dentro do mesmo sinal
            for i in range(len(segs)):
                for j in range(i + 1, len(segs)):
                    if overlap(segs[i], segs[j]):
                        errs.append(f'{name}: segmentos sobrepostos {segs[i]} {segs[j]}')
            deg = {}
            for a, b in segs:
                deg[a] = deg.get(a, 0) + 1
                deg[b] = deg.get(b, 0) + 1
            conns = []
            for pt, d in deg.items():
                if pt in portat:
                    for cp in portat[pt]:
                        conns.append(cp)
                    if d != 1:
                        errs.append(f'{name}: porta {portat[pt]} com {d} segmentos (deve ser ponta)')
                elif d == 1 and pt not in self.stubs:
                    errs.append(f'{name}: ponta solta em {pt}')
            # porta tocando interior de segmento
            for pos, lst in portat.items():
                for a, b in segs:
                    if on_interior(pos, a, b):
                        errs.append(f'{name}: passa sobre a porta {lst} em {pos}')
            dots = sorted(pt for pt, d in deg.items() if d >= 3)
            # larguras / driver
            ws = set(); kinds = set(); drivers = []
            for inst, pn in conns:
                r = self.comps[inst].rports[pn]
                ws.add(r[3]); kinds.add(r[4])
                if r[2] == 'out':
                    drivers.append((inst, pn))
                key = (inst, pn)
                if key in used_ports:
                    errs.append(f'porta {key} em dois sinais: {used_ports[key]} e {name}')
                used_ports[key] = name
            if len(ws) != 1:
                errs.append(f'{name}: larguras diferentes {ws} {conns}')
            if len(kinds) != 1:
                errs.append(f'{name}: tipos diferentes {kinds} {conns}')
            if len(drivers) != 1:
                errs.append(f'{name}: {len(drivers)} saídas {drivers} {conns}')
            if len(conns) < 2:
                errs.append(f'{name}: menos de 2 conexões {conns}')
            w = ws.pop() if ws else 1
            kind = kinds.pop() if kinds else 's'
            built.append(dict(name=name, segs=segs, conns=conns, dots=dots, w=w, kind=kind))
        # entre sinais
        allsegs = [(s['name'], a, b) for s in built for a, b in s['segs']]
        for i in range(len(allsegs)):
            ni, a1, b1 = allsegs[i]
            for j in range(i + 1, len(allsegs)):
                nj, a2, b2 = allsegs[j]
                if ni == nj:
                    continue
                if overlap((a1, b1), (a2, b2)):
                    errs.append(f'sobreposição {ni} {a1}-{b1} x {nj} {a2}-{b2}')
                for e in (a1, b1):
                    if on_seg(e, a2, b2):
                        errs.append(f'toque {ni} ponto {e} em {nj} {a2}-{b2}')
                for e in (a2, b2):
                    if on_seg(e, a1, b1):
                        errs.append(f'toque {nj} ponto {e} em {ni} {a1}-{b1}')
        # fios atravessando caixas
        for s in built:
            for a, b in s['segs']:
                for c in self.comps.values():
                    if seg_in_box(a, b, c.bbox):
                        warns.append(f'{s["name"]} atravessa {c.name} {a}-{b}')
        # caixas sobrepostas
        cl = list(self.comps.values())
        for i in range(len(cl)):
            for j in range(i + 1, len(cl)):
                if box_overlap(cl[i].bbox, cl[j].bbox):
                    warns.append(f'caixas sobrepostas {cl[i].name} {cl[j].name}')
        # entradas abertas
        for c in self.comps.values():
            for pn, r in c.rports.items():
                if r[2] == 'in' and (c.name, pn) not in used_ports and (c.name, pn) not in self.allow_open:
                    warns.append(f'entrada aberta {c.name}.{pn}')
        # padrão: dados editáveis fora de subcircuitos
        self.notes = []
        if self.is_block:
            for c in self.comps.values():
                if c.cls in DATA_CLASSES:
                    self.notes.append(f'{self.name}: {c.name} ({c.cls.split(".")[-1]}) dentro de subcircuito; '
                                      'mover para o circuito principal (SUBCIRCUITOS.md)')
        self.built = built
        return errs, warns

    def crossings(self):
        n = 0
        segs = [(s['name'], a, b) for s in self.built for a, b in s['segs']]
        for i in range(len(segs)):
            for j in range(i + 1, len(segs)):
                if segs[i][0] != segs[j][0] and cross(segs[i][1:], segs[j][1:]):
                    n += 1
        return n

    def write(self, path):
        L = ['# hades.models.Design file', '#  ', f'[name] {self.name}', '[components]']
        for c in self.comps.values():
            L.append(c.line())
        L.append('[end components]')
        L.append('[signals]')
        for s in self.built:
            conns = ' '.join(f'{i} {p}' for i, p in s['conns'])
            segs = ' '.join(f'2 {a[0]} {a[1]} {b[0]} {b[1]}' for a, b in s['segs'])
            dots = ' '.join(f'{x} {y}' for x, y in s['dots'])
            head = ('hades.signals.SignalStdLogicVector', f'{s["name"]} {s["w"]}') if s['kind'] == 'v' else \
                   ('hades.signals.SignalStdLogic1164', s['name'])
            line = f'{head[0]} {head[1]} {len(s["conns"])} {conns} {len(s["segs"])} {segs} {len(s["dots"])}'
            if dots:
                line += ' ' + dots
            L.append(line)
        L.append('[end signals]')
        L.append('[end]')
        with open(path, 'w', newline='\n') as f:
            f.write('\n'.join(L) + '\n')


def on_seg(p, a, b):
    (x, y), (x1, y1), (x2, y2) = p, a, b
    if x1 == x2 == x:
        return min(y1, y2) <= y <= max(y1, y2)
    if y1 == y2 == y:
        return min(x1, x2) <= x <= max(x1, x2)
    return False

def on_interior(p, a, b):
    return on_seg(p, a, b) and p != a and p != b

def overlap(s1, s2):
    (a1, b1), (a2, b2) = s1, s2
    if a1[0] == b1[0] == a2[0] == b2[0]:
        lo1, hi1 = sorted((a1[1], b1[1])); lo2, hi2 = sorted((a2[1], b2[1]))
        return min(hi1, hi2) - max(lo1, lo2) > 0
    if a1[1] == b1[1] == a2[1] == b2[1]:
        lo1, hi1 = sorted((a1[0], b1[0])); lo2, hi2 = sorted((a2[0], b2[0]))
        return min(hi1, hi2) - max(lo1, lo2) > 0
    return False

def cross(s1, s2):
    (a1, b1), (a2, b2) = s1, s2
    h1 = a1[1] == b1[1]; h2 = a2[1] == b2[1]
    if h1 == h2:
        return False
    if not h1:
        (a1, b1), (a2, b2) = (a2, b2), (a1, b1)
    y = a1[1]; x = a2[0]
    return min(a1[0], b1[0]) < x < max(a1[0], b1[0]) and min(a2[1], b2[1]) < y < max(a2[1], b2[1])

def seg_in_box(a, b, box):
    x0, y0, x1, y1 = box
    if a[0] == b[0]:
        x = a[0]
        if not (x0 < x < x1):
            return False
        lo, hi = sorted((a[1], b[1]))
        return min(hi, y1) - max(lo, y0) > 0
    y = a[1]
    if not (y0 < y < y1):
        return False
    lo, hi = sorted((a[0], b[0]))
    return min(hi, x1) - max(lo, x0) > 0

def box_overlap(b1, b2):
    return min(b1[2], b2[2]) - max(b1[0], b2[0]) > 0 and min(b1[3], b2[3]) - max(b1[1], b2[1]) > 0


# ---------------------------------------------------------------- blocos (subcircuitos)
class Block:
    """Subcircuito: Design interno + símbolo com portas em qualquer lado.

    Procedimento (PORTAS_MISTAS.md): gerar primeiro com Block.standard(design) (entradas à esquerda,
    saídas à direita), validar, e só então trocar `ports` pelo posicionamento final."""
    def __init__(self, design, L, A, ports, label=None, inner=()):
        # ports: lista (nome, lado, pos) lado em 'L','R','T','B'; pos = y (L/R) ou x (T/B)
        self.d = design
        design.is_block = True
        self.name = design.name
        self.L, self.A = L, A
        self.label = label or design.name
        self.portspec = ports
        self.inner = inner
        self.symports = {}
        for pn, side, pos in ports:
            self.symports[pn] = {'L': (0, pos), 'R': (L, pos), 'T': (pos, 0), 'B': (pos, A)}[side]
        self.pininfo = {}
        for pn in design.pins:
            c = design.comps[pn]
            r = list(c.rports.values())[0]
            d = 'in' if r[2] == 'out' else 'out'   # Ipin (saída interna) = entrada do bloco
            self.pininfo[pn] = (d, r[3], r[4])
        assert set(self.pininfo) == set(self.symports), (self.name, set(self.pininfo) ^ set(self.symports))

    @staticmethod
    def standard_ports(design):
        """Portas no padrão HADES/SUBCIRCUITOS.md: entradas x=0, saídas x=L, y = 600, 1200, ..."""
        ins, outs = [], []
        for pn in design.pins:
            r = list(design.comps[pn].rports.values())[0]
            (ins if r[2] == 'out' else outs).append(pn)
        ports = [(pn, 'L', 600 * (i + 1)) for i, pn in enumerate(ins)]
        ports += [(pn, 'R', 600 * (i + 1)) for i, pn in enumerate(outs)]
        return ports, 600 * (max(len(ins), len(outs)) + 1)

    @classmethod
    def standard(cls, design, label=None):
        ports, A = cls.standard_ports(design)
        return cls(design, 4800, A, ports, label=label)

    def sym(self):
        L, A = self.L, self.A
        out = [f'hades.symbols.BboxRectangle  0 0 {L} {A}', f'hades.symbols.Rectangle  0 0 {L} {A}']
        for pn, side, pos in self.portspec:
            x, y = self.symports[pn]
            out.append(f'hades.symbols.PortSymbol {x} {y} {pn}')
            if side == 'L':
                out.append(f'hades.symbols.PortLabel 150 {y + 150} {pn}')
            elif side == 'R':
                out.append(f'hades.symbols.PortLabel {L - 150} {y + 150} 3 {pn}')
            elif side == 'T':
                out.append(f'hades.symbols.PortLabel {x} 450 2 {pn}')
            else:
                out.append(f'hades.symbols.PortLabel {x} {A - 150} 2 {pn}')
        lx, ly = self.labelpos()
        out.append(f'hades.symbols.ClassLabel {lx} {ly} 2 {self.label}')
        out.append(f'hades.symbols.InstanceLabel {L // 2} {A + 450} 2 {self.name}')
        return '\n'.join(out) + '\n'

    def labelpos(self):
        bottoms = [p for _, s, p in self.portspec if s == 'B']
        if self.A >= 6000:
            return self.L // 2, self.A - 750 if bottoms else self.A - 150
        if not bottoms:
            return self.L // 2, self.A - 150
        # bloco baixo com portas na base: rótulo no meio
        return self.L // 2, self.A // 2 + 150

    def write(self, folder):
        self.d.write(os.path.join(folder, self.name + '.hds'))
        with open(os.path.join(folder, self.name + '.sym'), 'w', newline='\n') as f:
            f.write(self.sym())


# ---------------------------------------------------------------- render
def render(design, path, scale=0.02, margin=1200, labels=True):
    from PIL import Image, ImageDraw, ImageFont
    xs = []; ys = []
    for c in design.comps.values():
        xs += [c.bbox[0], c.bbox[2]]; ys += [c.bbox[1], c.bbox[3]]
    for s in design.built:
        for a, b in s['segs']:
            xs += [a[0], b[0]]; ys += [a[1], b[1]]
    x0, y0 = min(xs) - margin, min(ys) - margin
    W = int((max(xs) + margin - x0) * scale); H = int((max(ys) + margin - y0) * scale)
    im = Image.new('RGB', (W, H), 'white')
    dr = ImageDraw.Draw(im)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', max(9, int(500 * scale)))
        sfont = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', max(7, int(330 * scale)))
    except Exception:
        font = sfont = ImageFont.load_default()
    T = lambda x, y: ((x - x0) * scale, (y - y0) * scale)
    pal = ['#1f77b4', '#d62728', '#2ca02c', '#9467bd', '#ff7f0e', '#8c564b', '#e377c2', '#17becf', '#bcbd22', '#555555']
    for c in design.comps.values():
        a = T(c.bbox[0], c.bbox[1]); b = T(c.bbox[2], c.bbox[3])
        dr.rectangle([a, b], outline='black', width=1, fill='#f4f4f4')
        if labels:
            lab = c.block.label if c.block else c.cls.split('.')[-1]
            dr.text((a[0] + 2, a[1] + 2), lab, fill='black', font=font)
            dr.text((a[0] + 2, b[1] + 1), c.name, fill='#666', font=sfont)
        for pn in c.rports:
            px, py = T(*c.p(pn))
            dr.ellipse([px - 2, py - 2, px + 2, py + 2], fill='black')
            if labels and c.block:
                dr.text((px + 2, py - 1), pn, fill='#444', font=sfont)
    for i, s in enumerate(design.built):
        col = pal[i % len(pal)]
        wdt = 2 if s['kind'] == 'v' and s['w'] > 1 else 1
        for a, b in s['segs']:
            dr.line([T(*a), T(*b)], fill=col, width=wdt)
        for d in s['dots']:
            px, py = T(*d)
            dr.ellipse([px - 3, py - 3, px + 3, py + 3], fill=col)
    im.save(path)
    return W, H


# ---------------------------------------------------------------- coerência com a biblioteca
def check_native(catalog_json):
    """Compara posições de portas e bbox de native() com catalog/components.json (parâmetros padrão).
    Componentes de símbolo dinâmico (Expander, ExpV, Merge) são conferidos pelas fórmulas de components/."""
    cat = json.load(open(catalog_json, encoding='utf-8'))
    samples = {'Ipin': {}, 'IpinV': {}, 'Opin': {}, 'OpinV': {}, 'RegRE': {}, 'Add': {}, 'Mux21': {}, 'Mux41': {},
               'UALU': {}, 'Subset': dict(u=7, l=0), 'SelectBit': dict(i=0), 'SRL': dict(s=2), 'SHL': dict(s=2),
               'ROM': dict(words=1024, bits=32, file='x.rom'), 'RAM': dict(words=1024, bits=32),
               'MipsRegBank': {}, 'CmpEq': {}, 'OrRed': {}, 'Const': dict(v='0' * 32), 'SConst': dict(v='0' * 32),
               'Gnd': {}, 'Nand2': {}, 'And2': {}, 'Or2': {}, 'And3': {}, 'Inv': {}, 'ClockGen': {}}
    errs = []
    for t, k in samples.items():
        cls, _, ports, bbox = native(t, **k)
        e = cat.get(cls)
        if not e:
            errs.append(f'{t}: {cls} ausente do catálogo'); continue
        if e['bbox'] and tuple(e['bbox']) != tuple(bbox):
            errs.append(f'{t}: bbox {bbox} != catálogo {e["bbox"]}')
        cp = {p['name']: p['pos'] for p in e['ports']}
        for pn, r in ports.items():
            if pn not in cp:
                errs.append(f'{t}.{pn}: porta ausente no catálogo')
            elif cp[pn] and tuple(cp[pn]) != (r[0], r[1]):
                errs.append(f'{t}.{pn}: {(r[0], r[1])} != catálogo {tuple(cp[pn])}')
    return errs
