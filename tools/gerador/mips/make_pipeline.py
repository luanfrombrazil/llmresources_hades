# Gera examples/pipeline_patterson (uso: python make_pipeline.py [pasta_de_saida]); padrão: ./saida/PIPELINE_PATTERSON
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))  # hdslib.py
import shutil
import top_pipeline as top
from hdslib import render

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'saida', 'PIPELINE_PATTERSON')
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)

bl = top.all_blocks()
for b in bl.values():
    e, w = b.d.build()
    assert not e and not w, (b.name, e, w)
    for nt in b.d.notes:
        print('aviso de padrão:', nt)
    b.write(OUT)
best = top.choose_lanes(bl)
d = top.build_top(bl, best[1])
e, w = d.build()
assert not e and not w, (e, w)
d.write(os.path.join(OUT, 'MIPS_PIPELINE.hds'))
render(d, os.path.join(OUT, '..', 'preview_pipeline.png'), scale=0.016)

prog = [
    ('8C010003', 'lw  $1, 3($0)'), ('8C020006', 'lw  $2, 6($0)'),
    ('00421820', 'add $3, $2, $2      # load-use: 1 bolha'), ('00612020', 'add $4, $3, $1'),
    ('00832820', 'add $5, $4, $3'), ('00A43022', 'sub $6, $5, $4'), ('00C53824', 'and $7, $6, $5'),
    ('00E64025', 'or  $8, $7, $6'), ('01084820', 'add $9, $8, $8'), ('00214820', 'add $9, $1, $1'),
    ('01205020', 'add $10, $9, $0'), ('AC0A0064', 'sw  $10, 100($0)'), ('8C0B0064', 'lw  $11, 100($0)'),
    ('016A6022', 'sub $12, $11, $10   # load-use: 1 bolha'), ('01066822', 'sub $13, $8, $6'),
    ('00227020', 'add $14, $1, $2'), ('01C17820', 'add $15, $14, $1'),
    ('11A0FFEE', 'beq $13, $0, -18    # volta ao endereço 0 (IF.Flush)'),
]
with open(os.path.join(OUT, 'program.rom'), 'w', newline='\n') as f:
    f.write('# programa de teste (endereço = PC/4)\n')
    for i, (h, c) in enumerate(prog):
        f.write(f'{i:04X}:{h}   # {c}\n')
with open(os.path.join(OUT, 'data.rom'), 'w', newline='\n') as f:
    f.write('# memória de dados (endereço = resultado da ULA, bits 9..0)\n')
    f.write('0003:00000005   # mem[3] = 5\n0006:0000000A   # mem[6] = 10\n')
with open(os.path.join(OUT, 'control.rom'), 'w', newline='\n') as f:
    f.write('# controle principal: endereço = opcode, dado (9 bits)\n')
    f.write('# D8 Branch | D7 MemtoReg D6 RegWrite (WB) | D5 MemWrite D4 MemRead (M) | D3 ALUOp1 D2 ALUOp0 D1 ALUSrc D0 RegDst (EX)\n')
    f.write('0000:049   # tipo R\n0004:104   # beq\n0023:0D2   # lw\n002B:022   # sw\n')
with open(os.path.join(OUT, 'aluctl.rom'), 'w', newline='\n') as f:
    f.write('# ALU control para ALUOp = 1x: endereço = funct, dado = OPC da UserDefinedALU\n')
    f.write('# OPC 0 AND, 1 OR, 2 ADD, 6 SUB, 7 SUB (slt não suportado)\n')
    f.write('0020:2   # add\n0022:6   # sub\n0024:0   # and\n0025:1   # or\n002A:7   # slt -> sub\n')
print('ok', best, d.crossings())
print(sorted(os.listdir(OUT)))
