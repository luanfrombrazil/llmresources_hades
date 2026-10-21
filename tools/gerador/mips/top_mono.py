# Monociclo MIPS (Patterson Fig. 4.24, com jump). Tudo nativo no topo, exceto SIGNEXT e JUMPADDR.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))  # hdslib.py
import random
from hdslib import Design, cross, overlap
import blocks as B
import blocks_mono as BM

RY = 25200   # y do banco de registradores
TOP_NAMES = ['JUMP_T', 'BRSEL', 'BRTARGET', 'PC4', 'WB']
TOP_YS = [3600, 4200, 4800, 5400, 6000]
CTL_NAMES = ['RegDst', 'JUMP_C', 'Branch', 'MemRead', 'MemtoReg', 'ALUOp1', 'ALUOp0',
             'MemWrite', 'ALUSrc', 'CLKN']
CTL_YS = [14400 + 600 * i for i in range(11)]
YX = lambda i: 27000 + 600 * (10 - i)       # x da saída Yi do Expander de controle (y = 13800)


# faixas escolhidas pela busca (choose_lanes); fixas para a geração ser rápida e reprodutível
LANES = {'RegDst': 15000, 'JUMP_C': 15600, 'Branch': 17400, 'MemRead': 16800, 'MemtoReg': 16200,
         'ALUOp1': 19800, 'ALUOp0': 20400, 'MemWrite': 14400, 'ALUSrc': 18000, 'CLKN': 18600,
         'JUMP_T': 4200, 'BRSEL': 3600, 'BRTARGET': 4800, 'PC4': 6000, 'WB': 5400}


def all_blocks():
    return dict(SIGNEXT=B.blk_signext(), JUMPADDR=BM.blk_jumpaddr(), WBREG=BM.blk_wbreg())


def place(d, bl):
    n, a = d.add, d.addblock
    # geradores
    n('ClockGen', 'RESETGEN', -9600, -3600, p='1000.0 2.5E-4 0.0')
    n('Inv', 'RESETINV', -6000, -3000)
    n('ClockGen', 'CLOCK', -9600, -600, p='1.0 0.5 0.0')
    n('Inv', 'CLKINV', 20400, 1200, d='1.0E-9')      # clock invertido (só para a escrita da RAM)
    # IF
    n('Mux21', 'JMUX', 3600, 10200)
    n('Mux21', 'BRMUX', 7800, 6600)
    a(bl['JUMPADDR'], 'JUMPADDR', 10800, 9000)
    n('Ipin', 'PCEN', 1800, 14400, v='1')
    n('RegRE', 'PC', 3600, 13800)
    n('Const', 'FOUR', 8400, 13200, v='0' * 29 + '100')
    n('Add', 'ADDPC', 4200, 17400)
    n('Subset', 'IMEMADDR', 9600, 16800, u=11, l=2)
    n('ROM', 'IMEM', 12000, 15600, words=1024, bits=32, file='program.rom')
    # ID
    n('Subset', 'S_OPCODE', 20400, 8400, u=31, l=26)
    n('ROM', 'CTRLROM', 24000, 6600, words=64, bits=10, file='control.rom')
    n('Expander', 'CTRLX', 27000, 12600, n=10)
    n('Subset', 'S_RD', 20400, RY + 1200, u=15, l=11)
    n('Subset', 'S_RS', 20400, RY + 2400, u=25, l=21)
    n('Subset', 'S_RT', 20400, RY + 3600, u=20, l=16)
    n('Mux21', 'REGDSTMUX', 24000, RY - 1800, n=5)
    a(bl['WBREG'], 'WBREG', 34200, 21000)
    n('Gnd', 'REGCS', 31800, RY - 600)
    n('MipsRegBank', 'REGS', 33600, RY)
    n('Subset', 'S_IMM', 20400, 30600, u=15, l=0)
    a(bl['SIGNEXT'], 'SIGNEXT', 22800, 30600)
    n('SHL', 'SHL2', 24600, 33000, s=2)
    n('Add', 'ADDBR', 21000, 35400)
    n('Subset', 'S_FUNCT', 20400, 37800, u=5, l=0)
    n('Expander', 'FUNCTX', 28800, 39000, n=6)
    n('Merge', 'ALUCTLADDR', 27600, 41400, n=8)
    n('ROM', 'ALUCTLROM', 33600, 40200, words=256, bits=4, file='aluctl.rom')
    # EX
    n('Mux21', 'ALUSRCMUX', 43200, 33600)
    n('UALU', 'ALU', 41400, 36000)
    d.allow_open.update({('ALU', 'CIN')})
    n('And2', 'BRANCHAND', 49800, 31800, d='1.0E-9')
    # MEM
    n('Subset', 'DMEMADDR', 46200, 39600, u=11, l=2)
    n('Or2', 'MEMOR', 51600, 37800)
    n('Inv', 'MEMNCS', 55800, 39000, d='1.0E-9')
    n('Nand2', 'DMEMWE', 54000, 41400, d='1.0E-9')
    n('RAM', 'DMEM', 58800, 37800, words=1024, bits=32, file='data.rom')
    # WB
    n('Mux21', 'WBMUX', 61200, 45000)


def static(d, bl):
    w = d.wire
    P = d.P
    # reset / clock
    w('RSTCLK', [(-7200, -2400), (-6000, -2400)])
    w('NR', [(-4200, -2400), (-4200, 15600), (3600, 15600)],
      [(-4200, -600), (43200, -600), (43200, 23400), (40800, 23400)])
    w('CLK', [(-7200, 600), (-3000, 600), (-3000, 15000), (3600, 15000)],
      [(-3000, 600), (42600, 600), (42600, 22200), (40800, 22200)],
      [(19800, 600), (19800, 1800), (20400, 1800)])
    w('PCEN', [(1800, 14400), (3600, 14400)])
    # IF
    w('NEXTPC', [(5400, 12000), (5400, 13800)])
    w('BRPC', [(9600, 8400), (9600, 9000), (6000, 9000), (6000, 10200)])
    w('PCQ', [(5400, 16200), (5400, 16800), (5400, 17400)], [(5400, 16800), (9600, 16800)])
    w('FOURW', [(10200, 15000), (10200, 16200), (7800, 16200), (7800, 17400)])
    w('IADDR', [(9600, 17400), (9600, 18000), (12000, 18000)])
    # instrução (tronco vertical x=18600)
    w('INSTR', [(15600, 20400), (15600, 21000), (18600, 21000), (18600, 8400)],
      [(18600, 21000), (18600, 37800)],
      [(18600, 10200), (16200, 10200)],
      *[[(18600, y), (20400, y)] for y in (8400, RY + 1200, RY + 2400, RY + 3600, 30600, 37800)])
    # controle
    w('OPC6', [(20400, 9000), (24000, 9000)])
    w('CTRLW', [(27600, 11400), (27600, 12600)], [(27600, 12000), (38400, 12000), (38400, 21000)])
    # banco de registradores
    w('RDF', [(20400, RY + 1800), (22800, RY + 1800), (22800, RY - 2400), (25200, RY - 2400), (25200, RY - 1800)])
    w('RSF', [(20400, RY + 3000), (33600, RY + 3000)])
    w('RTF', [(20400, RY + 4200), (32400, RY + 4200), (32400, RY + 3600), (33600, RY + 3600)],
      [(23400, RY + 4200), (23400, RY - 3000), (26400, RY - 3000), (26400, RY - 1800)])
    w('WAIN', [(25800, RY), (25800, RY + 600), (29400, RY + 600), (29400, 21600), (34200, 21600)])
    w('WAOUT', [(34200, 22800), (33000, 22800), (33000, RY + 2400), (33600, RY + 2400)])
    w('RNWE', [(34200, 24000), (32400, 24000), (32400, RY + 1800), (33600, RY + 1800)])
    w('WDOUT', [(36000, 24600), (36000, RY)])
    w('RNCS', [(31800, RY - 600), (30600, RY - 600), (30600, RY + 1200), (33600, RY + 1200)])
    # imediato
    w('IMM16', [(20400, 31200), (22800, 31200)])
    w('IMM32', [(27600, 31200), (30600, 31200), (30600, 32400), (44400, 32400), (44400, 33600)],
      [(30600, 32400), (24600, 32400), (24600, 33000)])
    w('IMMSH', [(24600, 34800), (24600, 35400)])
    # EX
    w('RD1', [(36000, RY + 4800), (36000, 31200), (42600, 31200), (42600, 36000)])
    w('RD2', [(38400, RY + 4800), (38400, 30600), (45600, 30600), (45600, 33600)],
      [(45600, 30600), (62400, 30600), (62400, 37800)])
    w('ALUB', [(45000, 35400), (45000, 36000)])
    w('FUNCT', [(20400, 38400), (29400, 38400), (29400, 39000)])
    for i in range(6):
        x = 28800 + 600 * (6 - i)
        w(f'f{i}', [(x, 40200), (x, 41400)])
    w('ALUADDR', [(28200, 42600), (33600, 42600)])
    w('ALUCTL', [(37200, 45000), (37200, 45600), (33000, 45600), (33000, 37200), (41400, 37200)])
    w('ALURES', [(43800, 38400), (43800, 44400), (63600, 44400), (63600, 45000)],
      [(43800, 39600), (46200, 39600)])
    w('ZERO', [(44400, 38400), (44400, 39000), (47400, 39000), (47400, 33600), (49800, 33600)])
    # MEM
    w('DADDR', [(46200, 40200), (58800, 40200)])
    w('MEMORO', [(55200, 39000), (55200, 39600), (55800, 39600)])
    w('MEMNCSW', [(57600, 39600), (58800, 39600)])
    w('DMEMNWE', [(57600, 42600), (58200, 42600), (58200, 40800), (58800, 40800)])
    w('RDATA', [(62400, 42600), (62400, 45000)])
    w('JADDRW', [(10800, 11400), (9600, 11400), (9600, 9600), (4800, 9600), (4800, 10200)])


def lanes(d, L):
    """sinais que dependem das faixas de volta (L = dict nome -> y)."""
    w = d.wire
    out = {}
    def add(name, *polys):
        out[name] = [list(p) for p in polys]
    Lc = lambda k: L[k]
    # --- globais do topo
    add('JUMP', [(YX(8), 13800), (YX(8), Lc('JUMP_C')), (34200, Lc('JUMP_C')), (34200, Lc('JUMP_T')),
                 (3000, Lc('JUMP_T')), (3000, 11400), (3600, 11400)])
    add('BRSEL', [(53400, 33000), (54000, 33000), (54000, Lc('BRSEL')), (7200, Lc('BRSEL')), (7200, 7800), (7800, 7800)])
    add('BRTARGET', [(23400, 37800), (23400, 39000), (-1800, 39000), (-1800, Lc('BRTARGET')),
                     (9000, Lc('BRTARGET')), (9000, 6600)])
    add('PC4', [(6600, 19800), (6600, 22200)],
        [(6600, 22200), (0, 22200), (0, Lc('PC4')), (13200, Lc('PC4')), (13200, 9000)],
        [(10200, Lc('PC4')), (10200, 6600)],
        [(6600, 22200), (22200, 22200), (22200, 35400)])
    add('WRITEDATA', [(63000, 46800), (63000, 47400), (66000, 47400), (66000, Lc('WB')), (36000, Lc('WB')), (36000, 21000)])
    # --- faixas de controle
    c = lambda i: YX(i)
    add('RegDst', [(c(9), 13800), (c(9), Lc('RegDst')), (21000, Lc('RegDst')), (21000, RY - 600), (24000, RY - 600)])
    add('Branch', [(c(7), 13800), (c(7), Lc('Branch')), (46800, Lc('Branch')), (46800, 32400), (49800, 32400)])
    add('MemRead', [(c(6), 13800), (c(6), Lc('MemRead')), (48600, Lc('MemRead')), (48600, 38400), (51600, 38400)])
    add('MemtoReg', [(c(5), 13800), (c(5), Lc('MemtoReg')), (67200, Lc('MemtoReg')), (67200, 48000),
                     (60000, 48000), (60000, 46200), (61200, 46200)])
    add('ALUOp1', [(c(4), 13800), (c(4), Lc('ALUOp1')), (28200, Lc('ALUOp1')), (28200, 41400)])
    add('ALUOp0', [(c(3), 13800), (c(3), Lc('ALUOp0')), (28800, Lc('ALUOp0')), (28800, 41400)])
    add('MemWrite', [(c(2), 13800), (c(2), Lc('MemWrite')), (48000, Lc('MemWrite')), (48000, 39600), (51600, 39600)],
        [(48000, 39600), (48000, 42000), (54000, 42000)])
    add('ALUSrc', [(c(1), 13800), (c(1), Lc('ALUSrc')), (42000, Lc('ALUSrc')), (42000, 34800), (43200, 34800)])
    add('CLKN', [(22200, 1800), (22800, 1800), (22800, Lc('CLKN')), (49200, Lc('CLKN')), (49200, 43200), (54000, 43200)])
    return out


def build_top(bl, L):
    d = Design('MONOCICLO')
    place(d, bl)
    static(d, bl)
    # ROM do controle/expansores
    w = d.wire
    ex = lambda i: YX(i)
    for nm, i in (('RegDst', 9), ('Jump', 8), ('Branch', 7), ('MemRead', 6), ('MemtoReg', 5), ('ALUOp1', 4),
                  ('ALUOp0', 3), ('MemWrite', 2), ('ALUSrc', 1), ('RegWrite', 0)):
        pass
    lw = lanes(d, L)
    for name, polys in lw.items():
        w(name, *polys)
    return d, lw


def _segs(polys, name):
    return [(name, a, b) for p in polys for a, b in zip(p, p[1:])]


def lane_cost(static_segs, L, d):
    lw = lanes(d, L)
    segs = []
    for nm, polys in lw.items():
        segs += _segs(polys, nm)
    bad = nx = 0
    for i, s in enumerate(segs):
        for t in static_segs:
            nx += cross(s[1:], t[1:]); bad += overlap(s[1:], t[1:])
        for t in segs[i + 1:]:
            if t[0] != s[0]:
                nx += cross(s[1:], t[1:]); bad += overlap(s[1:], t[1:])
    return (bad, nx)


def choose_lanes(bl, seed=1, iters=3000):
    d0 = Design('x')
    place(d0, bl); static(d0, bl)
    st = []
    for nm, polys in d0.sigs:
        st += _segs(polys, nm)
    rnd = random.Random(seed)
    ctl = dict(zip(CTL_NAMES, rnd.sample(CTL_YS, len(CTL_YS))))
    top = dict(zip(TOP_NAMES, rnd.sample(TOP_YS, len(TOP_YS))))
    L = {**ctl, **top}
    cur = lane_cost(st, L, d0)
    for _ in range(iters):
        grp = rnd.choice((CTL_NAMES, TOP_NAMES))
        a, b = rnd.sample(grp, 2)
        L2 = dict(L); L2[a], L2[b] = L[b], L[a]
        c = lane_cost(st, L2, d0)
        if c <= cur:
            L, cur = L2, c
    return cur, L


if __name__ == '__main__':
    import sys
    bl = all_blocks()
    best = None
    for sd in range(6):
        r = choose_lanes(bl, seed=sd, iters=1500)
        print(sd, r[0])
        if best is None or r[0] < best[0]:
            best = r
    print('lanes', best)
    d, _ = build_top(bl, best[1])
    e, wn = d.build()
    print('ERR', len(e)); [print(' ', x) for x in e[:60]]
    print('WARN', len(wn)); [print(' ', x) for x in wn[:60]]
    print('crossings', d.crossings())
    from hdslib import render
    render(d, 'mono.png', scale=0.016)
