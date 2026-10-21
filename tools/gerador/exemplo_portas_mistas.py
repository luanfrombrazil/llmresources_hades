# Exemplo mínimo de uso do hdslib: gera o subcircuito PORTAS_MISTAS (Y = A AND B, Z = A OR B)
# seguindo PORTAS_MISTAS.md: 1) símbolo padrão, 2) validar, 3) reposicionar portas.
# Uso: python exemplo_portas_mistas.py [pasta_de_saida]   (padrão: ./saida/portas_mistas)
import os, sys
from hdslib import Design, Block

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'saida', 'portas_mistas')
os.makedirs(OUT, exist_ok=True)


def interno():
    d = Design('PORTAS_MISTAS')
    d.add('Ipin', 'A', 1200, 1200, v='0')
    d.add('Ipin', 'B', 1200, 3600, v='0')
    d.add('And2', 'AND', 4800, 1200)
    d.add('Or2', 'OR', 4800, 4800)
    d.add('Opin', 'Y', 10800, 2400)
    d.add('Opin', 'Z', 10800, 6000)
    # polilinhas em coordenadas absolutas; várias polilinhas = derivações (solda automática)
    d.wire('n0', [d.P('A', 'Y'), (3600, 1200), (3600, 1800), d.P('AND', 'A')], [(3600, 1800), (3600, 5400), d.P('OR', 'A')])
    d.wire('n1', [d.P('B', 'Y'), (2400, 3600), (2400, 3000), d.P('AND', 'B')], [(2400, 3600), (2400, 6600), d.P('OR', 'B')])
    d.wire('n2', [d.P('AND', 'Y'), (9600, 2400), d.P('Y', 'A')])
    d.wire('n3', [d.P('OR', 'Y'), (9600, 6000), d.P('Z', 'A')])
    return d


def check(blk):
    e, w = blk.d.build()
    assert not e and not w, (e, w)
    for n in blk.d.notes:
        print('aviso de padrão:', n)


# 1-2) padrão HADES (entradas à esquerda, saídas à direita) e validação
padrao = Block.standard(interno())
check(padrao)
# 3) portas mistas: A e Z no topo, B à esquerda, Y à direita, caixa 4800x1200
final = Block(interno(), 4800, 1200, [('A', 'T', 1200), ('Z', 'T', 3600), ('B', 'L', 600), ('Y', 'R', 600)])
check(final)
final.write(OUT)
print('ok', sorted(os.listdir(OUT)))
