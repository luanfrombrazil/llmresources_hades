# Gera examples/monociclo_patterson (uso: python make_mono.py [pasta_de_saida]); padrão: ./saida/MONOCICLO_PATTERSON
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))  # hdslib.py
import shutil
import top_mono as top
from hdslib import render

here = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, 'saida', 'MONOCICLO_PATTERSON')
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)

bl = top.all_blocks()
for b in bl.values():
    e, w = b.d.build()
    assert not e and not w, (b.name, e, w)
    for nt in b.d.notes:
        print('aviso de padrão:', nt)
    b.write(OUT)
d, _ = top.build_top(bl, top.LANES)
e, w = d.build()
assert not e and not w, (e, w)
d.write(os.path.join(OUT, 'MONOCICLO.hds'))
render(d, os.path.join(OUT, '..', 'preview_monociclo.png'), scale=0.016)


def wr(name, lines):
    with open(os.path.join(OUT, name), 'w', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


prog = [
    ('8C01000C', 'lw  $1, 12($0)         # $1 = mem[palavra 3] = 5'),
    ('8C020018', 'lw  $2, 24($0)         # $2 = mem[palavra 6] = 10'),
    ('00221820', 'add $3, $1, $2         # 15'),
    ('00412022', 'sub $4, $2, $1         # 5'),
    ('00222824', 'and $5, $1, $2         # 0'),
    ('00223025', 'or  $6, $1, $2         # 15'),
    ('AC030064', 'sw  $3, 100($0)        # mem[100] = 15 (palavra 25)'),
    ('8C070064', 'lw  $7, 100($0)        # $7 = 15'),
    ('10670001', 'beq $3, $7, +1         # desvia: pula a instrução 9'),
    ('00214020', 'add $8, $1, $1         # PULADA ($8 fica 0)'),
    ('00644820', 'add $9, $3, $4         # 20'),
    ('0800000D', 'j   13                 # pula a instrução 12'),
    ('00215020', 'add $10, $1, $1        # PULADA ($10 fica 0)'),
    ('01255820', 'add $11, $9, $5        # 20'),
    ('08000000', 'j   0                  # recomeça o programa'),
]
wr('program.rom', ['# programa de teste (endereço = PC/4)'] + [f'{i:04X}:{h}   # {c}' for i, (h, c) in enumerate(prog)])
wr('data.rom', ['# memória de dados: endereço = índice da palavra (byte/4)',
                '0003:00000005   # byte 12 -> 5', '0006:0000000A   # byte 24 -> 10'])
# controle: D9 RegDst | D8 Jump | D7 Branch | D6 MemRead | D5 MemtoReg | D4 ALUOp1 D3 ALUOp0 | D2 MemWrite | D1 ALUSrc | D0 RegWrite
wr('control.rom', ['# controle principal: endereço = opcode (6 bits), dado = 10 bits',
                   '# D9 RegDst | D8 Jump | D7 Branch | D6 MemRead | D5 MemtoReg | D4 ALUOp1 | D3 ALUOp0 | D2 MemWrite | D1 ALUSrc | D0 RegWrite',
                   '0000:211   # tipo R: RegDst, ALUOp=10, RegWrite',
                   '0002:100   # j: Jump',
                   '0004:088   # beq: Branch, ALUOp=01',
                   '0023:063   # lw: MemRead, MemtoReg, ALUSrc, RegWrite',
                   '002B:006   # sw: MemWrite, ALUSrc'])
# ALU control: endereço = {ALUOp1, ALUOp0, funct(6)}; dado = OPC da UserDefinedALU
al = ['# ALU control: endereço = ALUOp(2 bits) & funct(6 bits); dado = OPC da UserDefinedALU',
      '# OPC 0 AND, 1 OR, 2 ADD, 6 SUB, 7 SUB (slt não suportado, vira SUB)',
      '# ALUOp=00 (lw/sw): sempre ADD']
al += [f'{f:04X}:2' for f in range(64)]
al += ['# ALUOp=01 (beq): sempre SUB']
al += [f'{0x40 + f:04X}:6' for f in range(64)]
al += ['# ALUOp=10 (tipo R): depende do funct',
       '00A0:2   # add', '00A2:6   # sub', '00A4:0   # and', '00A5:1   # or', '00AA:7   # slt -> sub']
wr('aluctl.rom', al)
print('ok', sorted(os.listdir(OUT)), d.crossings())
