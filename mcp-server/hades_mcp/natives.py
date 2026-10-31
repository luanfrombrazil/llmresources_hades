"""Tabela dos tipos de hdslib.native() e conversão inversa (linha .hds -> kwargs de native())."""
from __future__ import annotations

from .library import hdslib

# tipo -> (descrição, kwargs aceitos, exemplo de kwargs para instanciar)
NATIVE = {
    'Ipin': ('Entrada de 1 bit / porta de subcircuito', {'v': "valor inicial: '0' '1' 'U'"}, {}),
    'Opin': ('Saída de 1 bit / porta de subcircuito', {}, {}),
    'IpinV': ('Entrada de n bits', {'n': 'largura (padrão 32)'}, {}),
    'OpinV': ('Saída de n bits', {'n': 'largura (padrão 32)'}, {}),
    'RegRE': ('Registrador com enable e reset', {'n': 'largura (padrão 32)'}, {}),
    'Add': ('Somador', {'n': 'largura (padrão 32)'}, {}),
    'Mux21': ('Mux 2:1 (A1 à esquerda, A0 à direita)', {'n': 'largura (padrão 32)'}, {}),
    'Mux41': ('Mux 4:1', {'n': 'largura (padrão 32)'}, {}),
    'CmpEq': ('Comparador de igualdade', {'n': 'largura (padrão 32)'}, {}),
    'OrRed': ('OR de redução', {'n': 'largura (padrão 32)'}, {}),
    'UALU': ('UserDefinedALU 32 bits, mapeamento MIPS (0 AND, 1 OR, 2 ADD, 6/7 SUB)', {}, {}),
    'Subset': ('Faixa de bits [u:l]', {'n': 'largura de entrada', 'u': 'bit superior', 'l': 'bit inferior'}, {'u': 7, 'l': 0}),
    'SelectBit': ('Seleciona 1 bit', {'n': 'largura de entrada', 'i': 'índice'}, {'i': 0}),
    'SRL': ('Deslocamento lógico à direita fixo', {'n': 'largura', 's': 'quantidade'}, {'s': 2}),
    'SHL': ('Deslocamento à esquerda fixo', {'n': 'largura', 's': 'quantidade'}, {'s': 2}),
    'ROM': ('ROM', {'words': 'nº de palavras', 'bits': 'bits por palavra', 'file': 'arquivo .rom (relativo)'},
            {'words': 1024, 'bits': 32, 'file': 'program.rom'}),
    'RAM': ('RAM assíncrona', {'words': 'nº de palavras', 'bits': 'bits por palavra', 'file': 'arquivo .rom opcional'},
            {'words': 1024, 'bits': 32}),
    'MipsRegBank': ('Banco de registradores MIPS 32x32', {'file': 'arquivo .rom opcional'}, {}),
    'Const': ('Constante', {'n': 'largura', 'v': 'bits MSB..LSB sem _B (exatamente n caracteres)'}, {'v': '0' * 32}),
    'SConst': ('Constante (símbolo pequeno)', {'n': 'largura', 'v': 'bits MSB..LSB sem _B'}, {'v': '0' * 32}),
    'Gnd': ('Terra', {}, {}),
    'And2': ('AND 2 entradas', {'d': 'atraso (padrão 1.0E-8)'}, {}),
    'Or2': ('OR 2 entradas', {'d': 'atraso'}, {}),
    'Nand2': ('NAND 2 entradas', {'d': 'atraso'}, {}),
    'And3': ('AND 3 entradas', {}, {}),
    'Inv': ('Inversor (InvSmall)', {'d': 'atraso (padrão 5.0E-9)'}, {}),
    'Expander': ('Barramento -> n bits (saídas na base)', {'n': 'largura'}, {'n': 4}),
    'ExpV': ('Barramento -> n bits (saídas à direita)', {'n': 'largura'}, {'n': 4}),
    'Merge': ('n bits -> barramento', {'n': 'largura'}, {'n': 4}),
    'ClockGen': ('Gerador de clock', {'p': "'período duty offset' (padrão '1.0 0.5 0.0')"}, {}),
}


def describe(t: str, **k) -> dict:
    kw = dict(NATIVE[t][2]); kw.update(k)
    cls, params, ports, bbox = hdslib.native(t, **kw)
    return dict(type=t, cls=cls, description=NATIVE[t][0], kwargs=NATIVE[t][1], sample_kwargs=kw,
                line=f'{cls} <inst> <x> <y> @N 1001 {params}'.rstrip(), bbox=list(bbox),
                ports={pn: dict(pos=[r[0], r[1]], dir=r[2], width=r[3], kind='vector' if r[4] == 'v' else 'bit')
                       for pn, r in ports.items()})


def table() -> list[dict]:
    return [describe(t) for t in NATIVE]


CLASS_TO_TYPES: dict[str, list[str]] = {}
for _t, (_d, _k, _s) in NATIVE.items():
    CLASS_TO_TYPES.setdefault(hdslib.native(_t, **_s)[0], []).append(_t)


def _int(s):
    return int(s)


def kwargs_from_line(cls: str, params: list[str]):
    """Deduz (tipo, kwargs) de native() a partir dos parâmetros após '1001'. None se não for nativo."""
    types = CLASS_TO_TYPES.get(cls)
    if not types:
        return None
    t = types[0]
    p = params
    try:
        if t in ('IpinV', 'OpinV', 'RegRE', 'Add', 'Mux21', 'Mux41', 'CmpEq', 'OrRed', 'Expander', 'ExpV', 'Merge'):
            return t, {'n': _int(p[0])}
        if t == 'Subset':
            return t, {'n': _int(p[0]), 'u': _int(p[1]), 'l': _int(p[2])}
        if t == 'SelectBit':
            return t, {'n': _int(p[0]), 'i': _int(p[1])}
        if t in ('SRL', 'SHL'):
            return t, {'n': _int(p[0]), 's': _int(p[1])}
        if t == 'ROM':
            return t, {'words': _int(p[0]), 'bits': _int(p[1]), 'file': p[2] if len(p) > 2 else ''}
        if t == 'RAM':
            return t, {'words': _int(p[0]), 'bits': _int(p[1]), 'file': p[2] if len(p) > 2 else None}
        if t in ('Const', 'SConst'):
            return t, {'n': _int(p[0]), 'v': p[1].removesuffix('_B')}
        return t, {}
    except (IndexError, ValueError):
        return None
