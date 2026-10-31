"""Arquivos .rom (ARQUIVOS_PARA_MEMORIA.md): geração no padrão da biblioteca e validação."""
from __future__ import annotations

import math
import re

LINE = re.compile(r'^\s*([0-9A-Fa-f]+)\s*:\s*([0-9A-Fa-f]+)\s*(?:#(.*))?$')


def _int(v) -> int:
    if isinstance(v, int):
        return v
    s = str(v).strip().replace('_', '')
    if s[:2].lower() == '0x':
        s = s[2:]
    return int(s, 16)   # strings são sempre hex: '0B000001' = 0x0B000001 (sem prefixo binário ambíguo)


def make(entries: list[dict], bits: int = 32, words: int | None = None, header: str | None = None) -> str:
    """entries: [{"addr": 0 | "0x0", "data": "8C010003" | 123, "comment": "lw $1, 3($0)"}].
    Endereços e dados em string são sempre hex (prefixo 0x opcional); inteiros JSON são decimais. Endereço = índice de palavra."""
    dw = max(1, math.ceil(bits / 4))
    out = []
    if header:
        out += [f'# {h}' for h in header.splitlines()]
    seen = set()
    for e in entries:
        a = _int(e['addr']); v = _int(e['data'])
        if a < 0 or (words is not None and a >= words):
            raise ValueError(f'endereço {a:#x} fora de 0..{(words or 1) - 1:#x}')
        if v < 0 or v >= (1 << bits):
            raise ValueError(f'dado {v:#x} não cabe em {bits} bits (endereço {a:#x})')
        if a in seen:
            raise ValueError(f'endereço repetido {a:#x}')
        seen.add(a)
        line = f'{a:04X}:{v:0{dw}X}'
        if e.get('comment'):
            line += f'   # {e["comment"]}'
        out.append(line)
    return '\n'.join(out) + '\n'


def validate(text: str, bits: int | None = None, words: int | None = None) -> dict:
    errors, warnings, n = [], [], 0
    seen = {}
    for i, ln in enumerate(text.splitlines(), 1):
        s = ln.strip()
        if not s or s.startswith('#'):
            continue
        m = LINE.match(s)
        if not m:
            errors.append(f'linha {i}: formato inválido (esperado <endereço_hex>:<dado_hex>): {s[:50]}')
            continue
        a, v = int(m.group(1), 16), int(m.group(2), 16)
        n += 1
        if words is not None and a >= words:
            errors.append(f'linha {i}: endereço {a:#x} >= {words} palavras')
        if bits is not None and v >= (1 << bits):
            errors.append(f'linha {i}: dado {m.group(2)} não cabe em {bits} bits')
        if a in seen:
            warnings.append(f'linha {i}: endereço {a:#x} repetido (linha {seen[a]})')
        seen[a] = i
    return dict(ok=not errors, entries=n, errors=errors, warnings=warnings)
