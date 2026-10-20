# CONTROLLERV1

Versão anterior do CONTROLLER (saídas separadas). Usada por PIPELINE.hds.

- **Arquivo:** `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\CONTROLLERV1.hds`
- **Caminho para usar na linha `hades.models.Design`:** `C:/Users/Luan/Documents/CEFET/2026.2/HACKING\u0020AOC/Claude_Hades/CONTROLLERV1.hds`
- **[name] interno:** `unnamed`
- **Símbolo (.sym):** 4800×6000

## Portas

| Porta | Direção | Largura | Posição no símbolo (x, y) |
|---|---|---|---|
| `i5` | entrada | 1 | (0, 600) |
| `i4` | entrada | 1 | (0, 1200) |
| `i3` | entrada | 1 | (0, 1800) |
| `i2` | entrada | 1 | (0, 2400) |
| `MEMWRITE` | saída | 1 | (4800, 3600) |
| `i1` | entrada | 1 | (0, 3000) |
| `i0` | entrada | 1 | (0, 3600) |
| `MEMREAD` | saída | 1 | (4800, 3000) |
| `REGWRITE` | saída | 1 | (4800, 2400) |
| `ALUSRC` | saída | 1 | (4800, 1200) |
| `MEMTOREG` | saída | 1 | (4800, 1800) |
| `BRANCH` | saída | 1 | (4800, 4200) |
| `REGDST` | saída | 1 | (4800, 600) |
| `ALUOP1` | saída | 1 | (4800, 5400) |
| `ALUOP0` | saída | 1 | (4800, 4800) |

## Componentes internos

InvVertical×16, Opin×9, And3Vertical×8, Ipin×6, And2×4, Or2×2

## Arquivo .sym atual

```
hades.symbols.BboxRectangle  0 0 4800 6000
hades.symbols.Rectangle  0 0 4800 6000
hades.symbols.PortLabel 4650 5550 3 ALUOP1
hades.symbols.PortSymbol 4800 5400 ALUOP1
hades.symbols.PortLabel 4650 4950 3 ALUOP0
hades.symbols.PortSymbol 4800 4800 ALUOP0
hades.symbols.PortLabel 4650 4350 3 BRANCH
hades.symbols.PortSymbol 4800 4200 BRANCH
hades.symbols.PortLabel 4650 3750 3 MEMWRITE
hades.symbols.PortSymbol 4800 3600 MEMWRITE
hades.symbols.PortLabel 4650 3150 3 MEMREAD
hades.symbols.PortSymbol 4800 3000 MEMREAD
hades.symbols.PortLabel 4650 2550 3 REGWRITE
hades.symbols.PortSymbol 4800 2400 REGWRITE
hades.symbols.PortLabel 4650 1950 3 MEMTOREG
hades.symbols.PortSymbol 4800 1800 MEMTOREG
hades.symbols.PortLabel 4650 1350 3 ALUSRC
hades.symbols.PortSymbol 4800 1200 ALUSRC
hades.symbols.PortLabel 4650 750 3 REGDST
hades.symbols.PortSymbol 4800 600 REGDST
hades.symbols.PortLabel 150 3750 i0
hades.symbols.PortSymbol 0 3600 i0
hades.symbols.PortLabel 150 3150 i1
hades.symbols.PortSymbol 0 3000 i1
hades.symbols.PortLabel 150 2550 i2
hades.symbols.PortSymbol 0 2400 i2
hades.symbols.PortLabel 150 1950 i3
hades.symbols.PortSymbol 0 1800 i3
hades.symbols.PortLabel 150 1350 i4
hades.symbols.PortSymbol 0 1200 i4
hades.symbols.PortLabel 150 750 i5
hades.symbols.PortSymbol 0 600 i5
hades.symbols.InstanceLabel 150 5850 unnamed
hades.symbols.ClassLabel 150 450 unnamed
```
