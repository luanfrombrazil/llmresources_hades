# Bloco extra do monociclo: endereço de jump = {PC+4[31:28], INSTR[25:0], 00}
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))  # hdslib.py
from hdslib import Design, Block


def blk_jumpaddr():
    d = Design('JUMPADDR')
    d.add('IpinV', 'INSTR', 0, 0, n=32)
    d.add('IpinV', 'PC4', 0, -3600, n=32)
    d.add('Subset', 'SJ', 5400, 0, n=32, u=25, l=0)
    d.add('Subset', 'SP', 1200, -3600, n=32, u=31, l=28)
    d.add('Expander', 'EJ', 3000, 1800, n=26)
    d.add('Expander', 'EP', 600, -1800, n=4)
    d.add('Merge', 'WORD', 600, 4200, n=32)
    d.add('Gnd', 'G0', 22200, 3600)
    d.add('OpinV', 'JADDR', 1200, 6600, n=32)
    d.wire('nI', [(0, 0), (5400, 0)])
    d.wire('nP', [(0, -3600), (1200, -3600)])
    d.wire('nJ', [(5400, 600), (5400, 1200), (3600, 1200), (3600, 1800)])
    d.wire('nPH', [(1200, -3000), (1200, -1800)])
    for i in range(26):
        x = 18600 - 600 * i
        d.wire(f'j{i}', [(x, 3000), (x, 4200)])
    for j in range(4):
        x = 3000 - 600 * j
        d.wire(f'p{j}', [(x, -600), (x, 4200)])
    d.wire('g', [(22200, 3600), (19200, 3600), (19200, 4200)], [(19800, 3600), (19800, 4200)])
    d.wire('nO', [(1200, 5400), (1200, 6600)])
    return Block(d, 5400, 3600, [('INSTR', 'R', 1200), ('PC4', 'T', 2400), ('JADDR', 'L', 2400)], label='JUMP_ADDR')


def blk_wbreg():
    """Registrador de write-back: captura (dado, endereço, palavra de controle) na borda de subida.
    O banco de registradores escreve a partir das saídas dele (estáveis durante o ciclo todo),
    o que quebra o laço combinacional banco -> ULA -> dado de escrita."""
    d = Design('WBREG')
    xE, xC, xN = 6000, 6600, 7200
    d.add('Ipin', 'CLK', xC, -1200)
    d.add('Ipin', 'NR', xN, -2400)
    d.add('Gnd', 'G0', 3000, 600)
    d.add('Inv', 'ON', 4200, -600)
    d.wire('nG', [(3000, 600), (3000, 0), (4200, 0)])
    tapsE, tapsC, tapsN = [], [], []
    y0 = 3600
    for pin, w, out in (('DATA_I', 32, 'DATA_O'), ('ADDR_I', 5, 'ADDR_O'), ('CTRL_I', 10, None)):
        d.add('IpinV', pin, 3600, y0, n=w)
        d.wire('i' + pin, [(3600, y0), (11400, y0), (11400, y0 + 1200)])
        ry = y0 + 1200
        d.add('RegRE', 'R' + pin, 9600, ry, n=w)
        tapsE.append(ry + 600); tapsC.append(ry + 1200); tapsN.append(ry + 1800)
        if out:
            d.add('OpinV', out, 19200, ry + 3000, n=w)
            d.wire('q' + pin, [(11400, ry + 2400), (11400, ry + 3000), (19200, ry + 3000)])
        else:
            d.add('SelectBit', 'SWE', 15000, ry + 3600, n=10, i=0)
            d.add('Inv', 'NWEINV', 16800, ry + 3600)
            d.add('Opin', 'NWE', 19200, ry + 4200)
            d.wire('qCTRL', [(11400, ry + 2400), (11400, ry + 3000), (15000, ry + 3000), (15000, ry + 3600)])
            d.wire('nW1', [(15000, ry + 4200), (16800, ry + 4200)])
            d.wire('nW2', [(18600, ry + 4200), (19200, ry + 4200)])
        y0 = ry + 6000

    def rail(nm, x, y_top, taps):
        d.wire(nm, [(x, y_top), (x, taps[-1]), (9600, taps[-1])], *[[(x, t), (9600, t)] for t in taps[:-1]])
    rail('rENA', xE, 0, tapsE)
    rail('rCLK', xC, -1200, tapsC)
    rail('rNR', xN, -2400, tapsN)
    return Block(d, 6600, 3600, [('DATA_I', 'T', 1800), ('CTRL_I', 'T', 4200), ('CLK', 'R', 1200), ('NR', 'R', 2400),
                                 ('ADDR_I', 'L', 600), ('ADDR_O', 'L', 1800), ('NWE', 'L', 3000),
                                 ('DATA_O', 'B', 1800)], label='WB_REG')
