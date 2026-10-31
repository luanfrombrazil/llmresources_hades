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


# ---------------------------------------------------------------- regressões (revisão do PR)
def _mini(name='T'):
    return {'name': name, 'components': [{'type': 'Ipin', 'name': 'A', 'x': 0, 'y': 0},
                                         {'type': 'Opin', 'name': 'Y', 'x': 6000, 'y': 0}],
            'wires': [{'name': 'n0', 'paths': [['A.Y', 'Y.A']]}]}


@pytest.mark.parametrize('bad', ['../../tmp/x', 'a/b', 'com espaço', '', '..'])
def test_design_name_cannot_be_a_path(bad, tmp_path):
    with pytest.raises(spec.SpecError):
        spec.build(_mini(bad) if bad else {**_mini(), 'name': bad})
    sub = {**_mini(), 'subcircuits': {bad or 'X': {**_mini(bad or 'X'), 'name': bad}}}
    with pytest.raises(spec.SpecError):
        spec.build(sub)


def test_duplicate_design_names_rejected():
    with pytest.raises(spec.SpecError, match='mesmo nome'):
        spec.build({**_mini('X'), 'subcircuits': {'X': _mini('X')}})


def test_duplicate_wire_names_rejected():
    s = _mini()
    s['components'] += [{'type': 'Ipin', 'name': 'B', 'x': 0, 'y': 2400}, {'type': 'Opin', 'name': 'Z', 'x': 6000, 'y': 2400}]
    s['wires'].append({'name': 'n0', 'paths': [['B.Y', 'Z.A']]})
    with pytest.raises(spec.SpecError, match='duplicado'):
        spec.build(s)


def test_rom_hex_strings_starting_with_0b():
    assert rom.make([{'addr': '0B', 'data': '0B000001'}]).strip() == '000B:0B000001'
    assert rom.make([{'addr': 1, 'data': '0x1f'}]).strip() == '0001:0000001F'


def test_malformed_native_params_reported():
    txt = ('# hades.models.Design file\n[name] T\n[components]\n'
           'hades.models.rtlib.muxes.Mux21 M 0 0 @N 1001 abc\n[end components]\n[signals]\n[end signals]\n[end]\n')
    assert any('malformados' in e for e in hdsparse.check(txt).errors)


def test_workspace_escape_via_symlink_and_dotdot(tmp_path, monkeypatch):
    ws = tmp_path / 'ws'; ws.mkdir(); outside = tmp_path / 'secret'; outside.mkdir()
    (outside / 'S.sym').write_text('hades.symbols.PortSymbol 0 600 LEAK\n')
    (outside / 'S.hds').write_text('x')
    monkeypatch.setenv('HADES_WORKSPACE', str(ws))
    # .hds referenciando subcircuito fora do workspace
    (ws / 'TOP.hds').write_text('# hades.models.Design file\n[name] TOP\n[components]\n'
                                'hades.models.Design U 0 0 @N 1001 ../secret/S.hds\n[end components]\n'
                                '[signals]\n[end signals]\n[end]\n')
    r = server.validate_hds(path='TOP.hds')
    assert '../secret/S.sym' in r['outside_workspace'] and 'LEAK' not in json.dumps(r)
    # link simbólico no destino de save_to
    (ws / 'out').mkdir(); (ws / 'out' / 'T.hds').symlink_to(outside / 'S.hds')
    with pytest.raises(ValueError, match='fora do workspace'):
        server.build_design(_mini(), save_to='out')
    assert (outside / 'S.hds').read_text() == 'x'


def test_subcircuit_paths_do_not_collide(tmp_path, monkeypatch):
    monkeypatch.setenv('HADES_WORKSPACE', str(tmp_path))
    for d, port in (('a', 'P'), ('b', 'Q')):
        (tmp_path / d).mkdir()
        (tmp_path / d / 'X.sym').write_text(f'hades.symbols.BboxRectangle 0 0 4800 1200\nhades.symbols.PortSymbol 0 600 {port}\n')
    (tmp_path / 'TOP.hds').write_text(
        '# hades.models.Design file\n[name] TOP\n[components]\n'
        'hades.models.Design U1 0 0 @N 1001 a/X.hds\nhades.models.Design U2 0 6000 @N 1001 b/X.hds\n'
        'hades.models.io.Ipin I 0 600 @N 1001 null 0\n[end components]\n[signals]\n'
        'hades.signals.SignalStdLogic1164 n0 2 I Y U1 P 0 0\n[end signals]\n[end]\n')
    r = server.validate_hds(path='TOP.hds')
    assert not any('não tem porta' in e for e in r['errors']), r['errors']


def test_make_rom_is_write_annotated():
    t = asyncio.run(server.mcp.list_tools())
    ann = {x.name: x.annotations for x in t}
    assert ann['make_rom'].read_only_hint is False


def test_library_found_from_cwd(tmp_path, monkeypatch):
    import subprocess, sys
    code = 'import hades_mcp.library as l; print(l.ROOT)'
    env = {**os.environ, 'PYTHONPATH': str(ROOT / 'mcp-server')}
    env.pop('HADES_LIB_ROOT', None)
    out = subprocess.run([sys.executable, '-c', code], cwd=ROOT / 'examples', env=env, capture_output=True, text=True)
    assert out.stdout.strip() == str(ROOT)
