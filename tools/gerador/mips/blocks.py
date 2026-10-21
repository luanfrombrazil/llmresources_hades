# Subcircuitos do datapath (internos + símbolos com portas mistas).
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))  # hdslib.py
from hdslib import Design, Block


def blk_aluctl():
    # ALUOp 00 -> soma (0010), 01 -> subtração (0110), 1x -> tabela do funct (aluctl.rom)
    d = Design('ALUCTL')
    d.add('IpinV', 'IMM', 0, 1200)
    d.add('IpinV', 'ALUOP', 0, 8400, n=2)
    d.add('Subset', 'FUNCT', 3600, 1800, u=5, l=0)
    d.add('ROM', 'TAB', 6000, 1200, words=64, bits=4, file='aluctl.rom')
    d.add('Const', 'OPSUB', 13200, 3600, n=4, v='0110')
    d.add('Const', 'OPADD', 16800, 6600, n=4, v='0010')
    d.add('ExpV', 'SEL', 9600, 9600, n=2)
    d.add('Mux41', 'M', 12000, 9600, n=4)
    d.add('OpinV', 'OP', 15600, 12600, n=4)
    d.wire('nI', [(0, 1200), (3600, 1200), (3600, 1800)])
    d.wire('nF', [(3600, 2400), (3600, 3600), (6000, 3600)])
    d.wire('nT', [(9600, 6000), (9600, 7200), (13800, 7200), (13800, 9600)], [(12600, 7200), (12600, 9600)])
    d.wire('nSUB', [(15000, 5400), (15000, 9600)])
    d.wire('nADD', [(18600, 8400), (18600, 9000), (16200, 9000), (16200, 9600)])
    d.wire('nAO', [(0, 8400), (10200, 8400), (10200, 9600)])
    d.wire('nS1', [(10800, 10200), (12000, 10200)])
    d.wire('nS0', [(10800, 10800), (12000, 10800)])
    d.wire('nY', [(14400, 11400), (14400, 12600), (15600, 12600)])
    return Block(d, 3600, 2400, [('IMM', 'L', 600), ('ALUOP', 'L', 1800), ('OP', 'R', 1200)], label='ALU_CTRL')


def blk_signext():
    # OUTPUT[15:0] = INPUT, OUTPUT[31:16] = INPUT[15]
    d = Design('SIGNEXT')
    d.add('IpinV', 'INPUT', 6000, 0, n=16)
    d.add('Expander', 'BITS', 9600, 600, n=16)
    d.add('Merge', 'WORD', 0, 3000, n=32)
    d.add('OpinV', 'OUTPUT', 1800, 4800)
    d.wire('nIN', [(6000, 0), (10200, 0), (10200, 600)])
    for i in range(15):
        x = 600 * (32 - i)
        d.wire(f'b{i}', [(x, 1800), (x, 3000)])
    d.wire('b15', [(10200, 1800), (10200, 3000)], [(10200, 2400), (600, 2400), (600, 3000)],
           *[[(600 * (32 - i), 2400), (600 * (32 - i), 3000)] for i in range(16, 31)])
    d.wire('nOUT', [(600, 4200), (600, 4800), (1800, 4800)])
    return Block(d, 4800, 1200, [('INPUT', 'L', 600), ('OUTPUT', 'R', 600)], label='SIGN_EXT')


def blk_control():
    # ROM 64x9 (control.rom): D8 Branch | D7 MemtoReg D6 RegWrite | D5 MemWrite D4 MemRead |
    #                         D3 ALUOp1 D2 ALUOp0 D1 ALUSrc D0 RegDst
    d = Design('CONTROL')
    d.add('IpinV', 'OPCODE', 0, 3600, n=6)
    d.add('ROM', 'PLA', 1200, 1200, words=64, bits=9, file='control.rom')
    d.add('SelectBit', 'BRANCH', 6000, 7800, n=9, i=8)
    d.add('Subset', 'FWB', 8400, 7800, n=9, u=7, l=6)
    d.add('Subset', 'FM', 10800, 7800, n=9, u=5, l=4)
    d.add('Subset', 'FEX', 13200, 7800, n=9, u=3, l=0)
    d.add('OpinV', 'EX', 15600, 9000, n=4)
    d.add('OpinV', 'M', 15600, 10200, n=2)
    d.add('OpinV', 'WB', 15600, 11400, n=2)
    d.add('And2', 'TAKEN', 7200, 12600)
    d.add('Ipin', 'EQ', 0, 14400)
    d.add('Opin', 'FLUSH', 12000, 13800)
    d.wire('nOP', [(0, 3600), (1200, 3600)])
    d.wire('nD', [(4800, 6000), (4800, 6600), (13200, 6600), (13200, 7800)],
           [(6000, 6600), (6000, 7800)], [(8400, 6600), (8400, 7800)], [(10800, 6600), (10800, 7800)])
    d.wire('nEX', [(13200, 8400), (13200, 9000), (15600, 9000)])
    d.wire('nM', [(10800, 8400), (10800, 10200), (15600, 10200)])
    d.wire('nWB', [(8400, 8400), (8400, 11400), (15600, 11400)])
    d.wire('nBR', [(6000, 8400), (6000, 13200), (7200, 13200)])
    d.wire('nEQ', [(0, 14400), (7200, 14400)])
    d.wire('nFL', [(10800, 13800), (12000, 13800)])
    return Block(d, 4800, 4800, [('OPCODE', 'L', 2400), ('FLUSH', 'T', 1200),
                                  ('WB', 'R', 1200), ('M', 'R', 2400), ('EX', 'R', 3600), ('EQ', 'B', 3600)],
                 label='CONTROL')


def blk_muxctl():
    d = Design('MUXCTL')
    d.add('Ipin', 'STALL', 3600, 0)
    rows = [('WB', 2), ('M', 2), ('EX', 4)]
    taps = []
    for k, (nm, n) in enumerate(rows):
        yk = 3600 + 6000 * k
        d.add('IpinV', nm + '_I', 0, yk - 2400, n=n)
        d.add('SConst', 'Z' + nm, 6600, yk - 1800, n=n, v='0' * n)
        d.add('Mux21', 'M' + nm, 6000, yk, n=n)
        d.add('OpinV', nm, 10200, yk + 2400, n=n)
        d.wire('i' + nm, [(0, yk - 2400), (8400, yk - 2400), (8400, yk)])
        d.wire('z' + nm, [(7200, yk - 600), (7200, yk)])
        d.wire('y' + nm, [(7800, yk + 1800), (7800, yk + 2400), (10200, yk + 2400)])
        taps.append(yk + 1200)
    d.wire('nS', [(3600, 0), (3600, taps[-1]), (6000, taps[-1])],
           *[[(3600, t), (6000, t)] for t in taps[:-1]])
    return Block(d, 2400, 4800, [('STALL', 'T', 1200), ('WB_I', 'L', 1200), ('M_I', 'L', 2400), ('EX_I', 'L', 3600),
                                  ('WB', 'R', 1200), ('M', 'R', 2400), ('EX', 'R', 3600)], label='MUX')


def blk_hazard():
    d = Design('HAZARD')
    d.add('IpinV', 'IFID_RT', 0, 0, n=5)
    d.add('IpinV', 'IDEX_RT', 0, 1200, n=5)
    d.add('IpinV', 'IFID_RS', 0, 2400, n=5)
    d.add('Ipin', 'IDEX_MEMREAD', 0, 10800)
    d.add('CmpEq', 'CRS', 3600, 3600, n=5)
    d.add('CmpEq', 'CRT', 9600, 3600, n=5)
    d.add('Or2', 'OR', 6000, 7200)
    d.add('And2', 'AND', 12000, 7800)
    d.add('Inv', 'NOT', 16800, 10200)
    d.add('Opin', 'STALL', 18000, 9000)
    d.add('Opin', 'PCWRITE', 19800, 10800)
    d.add('Opin', 'IFIDWRITE', 19800, 12000)
    d.wire('nRTX', [(0, 1200), (10800, 1200), (10800, 3600)], [(4800, 1200), (4800, 3600)])
    d.wire('nRS', [(0, 2400), (6000, 2400), (6000, 3600)])
    d.wire('nRT', [(0, 0), (12000, 0), (12000, 3600)])
    d.wire('nE1', [(5400, 5400), (5400, 7800), (6000, 7800)])
    d.wire('nE2', [(11400, 5400), (11400, 6600), (4800, 6600), (4800, 9000), (6000, 9000)])
    d.wire('nOR', [(9600, 8400), (12000, 8400)])
    d.wire('nMR', [(0, 10800), (11400, 10800), (11400, 9600), (12000, 9600)])
    d.wire('nST', [(15600, 9000), (18000, 9000)], [(16200, 9000), (16200, 10800), (16800, 10800)])
    d.wire('nOK', [(18600, 10800), (19800, 10800)], [(19200, 10800), (19200, 12000), (19800, 12000)])
    return Block(d, 7200, 3600, [('IFIDWRITE', 'T', 1200), ('PCWRITE', 'T', 3600),
                                  ('IFID_RS', 'L', 1200), ('IFID_RT', 'L', 2400),
                                  ('IDEX_MEMREAD', 'R', 1200), ('IDEX_RT', 'R', 2400), ('STALL', 'B', 6000)],
                 label='HAZARD_DETECTION')


def blk_forward():
    # FWDx = {EX/MEM, MEM/WB}; no Mux41 do pai, A3 = A2 = EX/MEM (prioridade quando ambos)
    d = Design('FORWARD')
    d.add('IpinV', 'EXMEM_RD', 0, 1200, n=5)
    d.add('IpinV', 'IDEX_RS', 0, 2400, n=5)
    d.add('IpinV', 'IDEX_RT', 0, 3600, n=5)
    d.add('IpinV', 'MEMWB_RD', 0, 4800, n=5)
    d.add('Ipin', 'EXMEM_RW', 0, 9000)
    d.add('Ipin', 'MEMWB_RW', 0, 10200)
    d.add('OrRed', 'NZE', 1200, 6000, n=5)
    d.add('CmpEq', 'CEA', 7200, 6000, n=5)
    d.add('CmpEq', 'CEB', 14400, 6000, n=5)
    d.add('CmpEq', 'CMA', 21600, 6000, n=5)
    d.add('CmpEq', 'CMB', 28800, 6000, n=5)
    d.add('OrRed', 'NZM', 36000, 6000, n=5)
    for nm, x in (('EXA', 10800), ('EXB', 18000), ('MEMA', 25200), ('MEMB', 32400)):
        d.add('And3', nm, x, 11400)
    d.add('Merge', 'MA', 40200, 16800, n=2)
    d.add('Merge', 'MB', 43200, 16800, n=2)
    d.add('OpinV', 'FWDB', 46800, 19200, n=2)
    d.add('OpinV', 'FWDA', 46800, 20400, n=2)
    d.wire('bEXRD', [(0, 1200), (15600, 1200), (15600, 6000)], [(3000, 1200), (3000, 6000)], [(8400, 1200), (8400, 6000)])
    d.wire('bRS', [(0, 2400), (24000, 2400), (24000, 6000)], [(9600, 2400), (9600, 6000)])
    d.wire('bRT', [(0, 3600), (31200, 3600), (31200, 6000)], [(16800, 3600), (16800, 6000)])
    d.wire('bMWRD', [(0, 4800), (37800, 4800), (37800, 6000)], [(22800, 4800), (22800, 6000)], [(30000, 4800), (30000, 6000)])
    d.wire('rEXRW', [(0, 9000), (17400, 9000), (17400, 12000), (18000, 12000)], [(10200, 9000), (10200, 12000), (10800, 12000)])
    d.wire('rEXNZ', [(3000, 7800), (3000, 9600), (16800, 9600), (16800, 12600), (18000, 12600)],
           [(9600, 9600), (9600, 12600), (10800, 12600)])
    d.wire('rMWRW', [(0, 10200), (31800, 10200), (31800, 12000), (32400, 12000)], [(24600, 10200), (24600, 12000), (25200, 12000)])
    d.wire('rMNZ', [(37800, 7800), (37800, 10800), (24000, 10800), (24000, 12600), (25200, 12600)],
           [(31200, 10800), (31200, 12600), (32400, 12600)])
    for cmp_, x in (('CEA', 9000), ('CEB', 16200), ('CMA', 23400), ('CMB', 30600)):
        d.wire('c' + cmp_, [(x, 7800), (x, 13200), (x + 1800, 13200)])
    d.wire('oEXA', [(14400, 12600), (15000, 12600), (15000, 14400), (40800, 14400), (40800, 16800)])
    d.wire('oEXB', [(21600, 12600), (22200, 12600), (22200, 15000), (43800, 15000), (43800, 16800)])
    d.wire('oMEMA', [(28800, 12600), (29400, 12600), (29400, 15600), (41400, 15600), (41400, 16800)])
    d.wire('oMEMB', [(36000, 12600), (36600, 12600), (36600, 16200), (44400, 16200), (44400, 16800)])
    d.wire('nFB', [(43800, 18000), (43800, 19200), (46800, 19200)])
    d.wire('nFA', [(40800, 18000), (40800, 20400), (46800, 20400)])
    return Block(d, 12000, 3600, [('FWDA', 'T', 1200), ('FWDB', 'T', 10800),
                                   ('IDEX_RS', 'L', 1200), ('IDEX_RT', 'L', 2400),
                                   ('EXMEM_RD', 'R', 1200), ('EXMEM_RW', 'R', 2400),
                                   ('MEMWB_RD', 'B', 3600), ('MEMWB_RW', 'B', 8400)], label='FORWARDING_UNIT')


# ---------------------------------------------------------------- registradores de pipeline
def pipereg(name, label, L, A, fields, symports, ena_pin=None, flush_pin=None):
    """fields: (pino_entrada, largura, [(pino_saida, tipo, arg)]) tipo: 'v' direto, 'sub' (u,l), 'bit' i.
    Um campo com flush=True passa por um Mux21 (FLUSH -> zero) antes do registrador."""
    d = Design(name)
    xE, xC, xN, xF = 6000, 6600, 7200, 7800
    d.add('Ipin', 'CLK', xC, -1200)
    d.add('Ipin', 'NR', xN, -2400)
    if ena_pin:
        d.add('Ipin', ena_pin, xE, 0)
    else:
        d.add('Gnd', 'G0', 3000, 600)
        d.add('Inv', 'ON', 4200, -600)
        d.wire('nG', [(3000, 600), (3000, 0), (4200, 0)])
    if flush_pin:
        d.add('Ipin', flush_pin, xF, -3600)
    tapsE, tapsC, tapsN, tapsF = [], [], [], []
    y0 = 3600
    for fi, (pin, w, outs, *fl) in enumerate(fields):
        flush = bool(fl and fl[0])
        d.add('IpinV', pin, 3600, y0, n=w)
        if flush:
            d.add('SConst', 'Z' + pin, 10200, y0 + 600, n=w, v='0' * w)
            d.add('Mux21', 'F' + pin, 9600, y0 + 2400, n=w)
            d.wire('i' + pin, [(3600, y0), (12000, y0), (12000, y0 + 2400)])
            d.wire('z' + pin, [(10800, y0 + 1800), (10800, y0 + 2400)])
            tapsF.append(y0 + 3600)
            d.wire('m' + pin, [(11400, y0 + 4200), (11400, y0 + 4800)])
            ry = y0 + 4800
        else:
            d.wire('i' + pin, [(3600, y0), (11400, y0), (11400, y0 + 1200)])
            ry = y0 + 1200
        reg = 'R' + pin
        d.add('RegRE', reg, 9600, ry, n=w)
        tapsE.append(ry + 600); tapsC.append(ry + 1200); tapsN.append(ry + 1800)
        q = (11400, ry + 2400)
        ys = [ry + 3000 + 2400 * k for k in range(len(outs))]
        polys = []
        for k, (on, kind, arg) in enumerate(outs):
            yk = ys[k]
            if kind == 'v':
                d.add('OpinV', on, 19200, yk, n=w)
                tail = [(11400, yk), (19200, yk)]
            else:
                if kind == 'sub':
                    u, l = arg
                    d.add('Subset', 'S' + on, 15000, yk + 600, n=w, u=u, l=l)
                    if u == l:
                        raise ValueError('use bit')
                    d.add('OpinV', on, 19200, yk + 1200, n=u - l + 1)
                else:
                    d.add('SelectBit', 'S' + on, 15000, yk + 600, n=w, i=arg)
                    d.add('Opin', on, 19200, yk + 1200)
                tail = [(11400, yk), (15000, yk), (15000, yk + 600)]
                d.wire('o' + on, [(15000, yk + 1200), (19200, yk + 1200)])
            if k == len(outs) - 1:
                polys.insert(0, [q] + tail)
            else:
                polys.append(tail)
        d.wire('q' + pin, *polys)
        y0 = ys[-1] + 3600
    def rail(nm, x, y_top, taps):
        d.wire(nm, [(x, y_top), (x, taps[-1]), (9600, taps[-1])], *[[(x, t), (9600, t)] for t in taps[:-1]])
    rail('rENA', xE, 0, tapsE)
    rail('rCLK', xC, -1200, tapsC)
    rail('rNR', xN, -2400, tapsN)
    if flush_pin:
        d.wire('rFL', [(xF, -3600), (xF, tapsF[-1]), (9600, tapsF[-1])])
    blk = Block(d, L, A, symports, label=label)
    return blk
