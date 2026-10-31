import asyncio
import glob
import json
import os

import pytest

from hades_mcp import hdsparse, library, rom, server, spec

ROOT = library.ROOT


def _inner():
    """Circuito de examples/portas_mistas (ver tools/gerador/exemplo_portas_mistas.py) como especificação JSON."""
    return {
        'components': [
            {'type': 'Ipin', 'name': 'A', 'x': 1200, 'y': 1200, 'params': {'v': '0'}},
            {'type': 'Ipin', 'name': 'B', 'x': 1200, 'y': 3600, 'params': {'v': '0'}},
            {'type': 'And2', 'name': 'AND', 'x': 4800, 'y': 1200},
            {'type': 'Or2', 'name': 'OR', 'x': 4800, 'y': 4800},
            {'type': 'Opin', 'name': 'Y', 'x': 10800, 'y': 2400},
            {'type': 'Opin', 'name': 'Z', 'x': 10800, 'y': 6000},
        ],
        'wires': [
            {'name': 'n0', 'paths': [['A.Y', [3600, 1200], [3600, 1800], 'AND.A'], [[3600, 1800], [3600, 5400], 'OR.A']]},
            {'name': 'n1', 'paths': [['B.Y', [2400, 3600], [2400, 3000], 'AND.B'], [[2400, 3600], [2400, 6600], 'OR.B']]},
            {'name': 'n2', 'paths': [['AND.Y', 'Y.A']]},
            {'name': 'n3', 'paths': [['OR.Y', 'Z.A']]},
        ],
        'symbol': {'width': 4800, 'height': 1200,
                   'ports': [['A', 'T', 1200], ['Z', 'T', 3600], ['B', 'L', 600], ['Y', 'R', 600]]},
    }


def test_build_reproduces_example_byte_for_byte():
    top = {'name': 'TOP', 'components': [], 'wires': [], 'subcircuits': {'PORTAS_MISTAS': _inner()}}
    res = spec.build(top)
    for f in ('PORTAS_MISTAS.hds', 'PORTAS_MISTAS.sym'):
        assert res['files'][f] == open(ROOT / 'examples/portas_mistas' / f, encoding='utf-8').read()
    assert res['designs']['PORTAS_MISTAS']['errors'] == []


def test_build_reports_errors():
    s = {'name': 'BAD', 'components': [
        {'type': 'Ipin', 'name': 'A', 'x': 0, 'y': 0}, {'type': 'Ipin', 'name': 'B', 'x': 0, 'y': 1200},
        {'type': 'Opin', 'name': 'Y', 'x': 6000, 'y': 0}],
        'wires': [{'name': 'n0', 'paths': [['A.Y', 'Y.A']]}, {'name': 'n1', 'paths': [['B.Y', [6000, 1200], 'Y.A']]}]}
    res = spec.build(s)
    assert not res['ok']
    errs = ' '.join(res['designs']['BAD']['errors'])
    assert 'em dois sinais' in errs and 'diagonal' not in errs


def test_auto_elbow():
    s = {'name': 'T', 'components': [{'type': 'Ipin', 'name': 'A', 'x': 0, 'y': 0},
                                     {'type': 'Opin', 'name': 'Y', 'x': 6000, 'y': 1200}],
         'wires': [{'name': 'n0', 'paths': [['A.Y', 'Y.A']], 'auto_elbow': True}]}
    assert spec.build(s)['ok']


def test_bad_port_message():
    with pytest.raises(spec.SpecError, match='portas'):
        spec.build({'name': 'T', 'components': [{'type': 'And2', 'name': 'G', 'x': 0, 'y': 0}],
                    'wires': [{'name': 'n', 'paths': [['G.Q', [600, 600]]]}]})


@pytest.mark.parametrize('f', sorted(glob.glob(str(ROOT / 'examples/*/*.hds')) + glob.glob(str(ROOT / 'blocks/*.hds'))))
def test_examples_have_no_errors(f):
    d = os.path.dirname(f)
    syms = {os.path.basename(s): open(s, encoding='utf-8').read() for s in glob.glob(d + '/*.sym') + glob.glob(str(ROOT / 'blocks/*.sym'))}
    P = hdsparse.check(open(f, encoding='utf-8').read(), syms)
    assert P.errors == []


@pytest.mark.parametrize('ex', ['pipeline_patterson', 'monociclo_patterson', 'portas_mistas', 'contador4'])
def test_generated_examples_are_lint_clean(ex):
    for f in glob.glob(str(ROOT / 'examples' / ex / '*.hds')):
        d = os.path.dirname(f)
        syms = {os.path.basename(s): open(s, encoding='utf-8').read() for s in glob.glob(d + '/*.sym')}
        P = hdsparse.check(open(f, encoding='utf-8').read(), syms)
        assert P.lint == [], (f, P.lint)


def test_validator_catches_broken_file():
    txt = open(ROOT / 'examples/contador4/CONTADOR4.hds', encoding='utf-8').read()
    broken = txt.replace('CNT 7200 3600 @N 1001 4 0000_B', 'CNT 7200 3600 @N 1001 8 0000_B')
    P = hdsparse.check(broken)
    assert any('largura' in e for e in P.errors)
    assert any('vetor 0000_B' in e for e in P.errors)
    broken2 = txt.replace('CNT CLK', 'CNT CLOCK')
    assert any('não tem porta CLOCK' in e for e in hdsparse.check(broken2).errors)


def test_rom_roundtrip():
    t = rom.make([{'addr': 0, 'data': '8C010003', 'comment': 'lw $1, 3($0)'}, {'addr': '0x1f', 'data': 5}], bits=32)
    assert t.splitlines() == ['0000:8C010003   # lw $1, 3($0)', '001F:00000005']
    assert rom.validate(t, bits=32, words=1024)['ok']
    assert not rom.validate('zz:1\n')['ok']
    for f in glob.glob(str(ROOT / 'examples/*/*.rom')):
        assert rom.validate(open(f, encoding='utf-8').read())['ok'], f


def test_native_table_matches_catalog():
    assert library.hdslib.check_native(str(ROOT / 'catalog/components.json')) == []


def test_mcp_client_roundtrip(tmp_path, monkeypatch):
    from mcp import Client
    monkeypatch.setenv('HADES_WORKSPACE', str(tmp_path))

    async def go():
        async with Client(server.mcp) as c:
            names = {t.name for t in (await c.list_tools()).tools}
            assert {'build_design', 'validate_hds', 'get_component', 'render_hds'} <= names
            r = await c.call_tool('get_component', {'name': 'Mux21'})
            assert 'A1' in r.content[0].text
            top = {'name': 'TOP', 'components': [], 'wires': [], 'subcircuits': {'PORTAS_MISTAS': _inner()}}
            # subcircuito sozinho não é instanciado; build salva todos os arquivos
            r = await c.call_tool('build_design', {'spec': top, 'save_to': 'out', 'preview': False})
            body = json.loads(r.content[0].text)
            assert body['ok'] and 'out/PORTAS_MISTAS.hds' in body['saved']
            r = await c.call_tool('validate_hds', {'path': 'out/PORTAS_MISTAS.hds'})
            assert json.loads(r.content[0].text)['clean'] is True
            r = await c.call_tool('render_hds', {'path': 'out/PORTAS_MISTAS.hds'})
            assert r.content[0].type == 'image'
            docs = await c.list_resources()
            assert any(str(x.uri) == 'hades://docs/FORMATO_HDS' for x in docs.resources)
    asyncio.run(go())
