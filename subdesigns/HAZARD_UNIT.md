# HAZARD UNIT

Unidade de detecção de hazard load-use: gera PCWRITE, IFIDWRITE, NOBUBBLE e STALL.

- **Arquivo:** `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\HAZARD UNIT.hds`
- **Caminho para usar na linha `hades.models.Design`:** `C:/Users/Luan/Documents/CEFET/2026.2/HACKING\u0020AOC/Claude_Hades/HAZARD\u0020UNIT.hds`
- **[name] interno:** `HAZARDUNIT`
- **Símbolo (.sym):** 4800×3000

## Portas

| Porta | Direção | Largura | Posição no símbolo (x, y) |
|---|---|---|---|
| `MEMREAD` | entrada | 1 | (0, 600) |
| `IDEX_RT` | entrada | 5 | (0, 1200) |
| `IFID_RS` | entrada | 5 | (0, 1800) |
| `IFID_RT` | entrada | 5 | (0, 2400) |
| `PCWRITE` | saída | 1 | (4800, 600) |
| `IFIDWRITE` | saída | 1 | (4800, 1200) |
| `NOBUBBLE` | saída | 1 | (4800, 1800) |
| `STALL` | saída | 1 | (4800, 2400) |

## Componentes internos

Opin×4, IpinVector×3, CompareEqual×2, Ipin×1, Or2×1, And2×1, InvSmall×1

## Arquivo .sym atual

```
hades.symbols.BboxRectangle  0 0 4800 3000
hades.symbols.Rectangle  0 0 4800 3000
hades.symbols.PortLabel 4650 750 3 PCWRITE
hades.symbols.PortSymbol 4800 600 PCWRITE
hades.symbols.PortLabel 4650 1350 3 IFIDWRITE
hades.symbols.PortSymbol 4800 1200 IFIDWRITE
hades.symbols.PortLabel 4650 1950 3 NOBUBBLE
hades.symbols.PortSymbol 4800 1800 NOBUBBLE
hades.symbols.PortLabel 4650 2550 3 STALL
hades.symbols.PortSymbol 4800 2400 STALL
hades.symbols.PortLabel 150 750 MEMREAD
hades.symbols.PortSymbol 0 600 MEMREAD
hades.symbols.PortLabel 150 1350 IDEX_RT
hades.symbols.PortSymbol 0 1200 IDEX_RT
hades.symbols.PortLabel 150 1950 IFID_RS
hades.symbols.PortSymbol 0 1800 IFID_RS
hades.symbols.PortLabel 150 2550 IFID_RT
hades.symbols.PortSymbol 0 2400 IFID_RT
hades.symbols.InstanceLabel 150 2850 HAZARDUNIT
hades.symbols.ClassLabel 150 450 HAZARDUNIT
```
