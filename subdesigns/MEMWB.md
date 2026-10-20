# MEMWB

Registrador de pipeline MEM/WB.

- **Arquivo:** `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\MEMWB.hds`
- **Caminho para usar na linha `hades.models.Design`:** `C:/Users/Luan/Documents/CEFET/2026.2/HACKING\u0020AOC/Claude_Hades/MEMWB.hds`
- **[name] interno:** `MEMWB`
- **Símbolo (.sym):** 4800×5400

## Portas

| Porta | Direção | Largura | Posição no símbolo (x, y) |
|---|---|---|---|
| `ENA` | entrada | 1 | (0, 600) |
| `MEMTOREG` | saída | 1 | (4800, 1200) |
| `REGWRITE` | saída | 1 | (4800, 600) |
| `NR` | entrada | 1 | (0, 1800) |
| `WB_I` | entrada | 2 | (0, 2400) |
| `MEMDATA_O` | saída | 32 | (4800, 1800) |
| `REGDEST_O` | saída | 5 | (4800, 3000) |
| `ALURESULT_O` | saída | 32 | (4800, 2400) |
| `MEMDATA_I` | entrada | 32 | (0, 3000) |
| `CLK` | entrada | 1 | (0, 1200) |
| `REGDEST_I` | entrada | 5 | (0, 4200) |
| `ALURESULT_I` | entrada | 32 | (0, 3600) |
| `WB_O` | saída | 2 | (4800, 3600) |

## Componentes internos

RegRE×4, IpinVector×4, OpinVector×4, Ipin×3, Opin×2, Expander×1

## Arquivo .sym atual

```
hades.symbols.BboxRectangle  0 0 4800 5400
hades.symbols.Rectangle  0 0 4800 5400
hades.symbols.PortLabel 4650 3750 3 WB_O
hades.symbols.PortSymbol 4800 3600 WB_O
hades.symbols.PortLabel 4650 3150 3 REGDEST_O
hades.symbols.PortSymbol 4800 3000 REGDEST_O
hades.symbols.PortLabel 4650 2550 3 ALURESULT_O
hades.symbols.PortSymbol 4800 2400 ALURESULT_O
hades.symbols.PortLabel 4650 1950 3 MEMDATA_O
hades.symbols.PortSymbol 4800 1800 MEMDATA_O
hades.symbols.PortLabel 4650 1350 3 MEMTOREG
hades.symbols.PortSymbol 4800 1200 MEMTOREG
hades.symbols.PortLabel 4650 750 3 REGWRITE
hades.symbols.PortSymbol 4800 600 REGWRITE
hades.symbols.PortLabel 150 4350 REGDEST_I
hades.symbols.PortSymbol 0 4200 REGDEST_I
hades.symbols.PortLabel 150 3750 ALURESULT_I
hades.symbols.PortSymbol 0 3600 ALURESULT_I
hades.symbols.PortLabel 150 3150 MEMDATA_I
hades.symbols.PortSymbol 0 3000 MEMDATA_I
hades.symbols.PortLabel 150 2550 WB_I
hades.symbols.PortSymbol 0 2400 WB_I
hades.symbols.PortLabel 150 1950 NR
hades.symbols.PortSymbol 0 1800 NR
hades.symbols.PortLabel 150 1350 CLK
hades.symbols.PortSymbol 0 1200 CLK
hades.symbols.PortLabel 150 750 ENA
hades.symbols.PortSymbol 0 600 ENA
hades.symbols.InstanceLabel 150 5250 MEMWB
hades.symbols.ClassLabel 150 450 MEMWB
```
