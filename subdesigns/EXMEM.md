# EXMEM

Registrador de pipeline EX/MEM.

- **Arquivo:** `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\EXMEM.hds`
- **Caminho para usar na linha `hades.models.Design`:** `C:/Users/Luan/Documents/CEFET/2026.2/HACKING\u0020AOC/Claude_Hades/EXMEM.hds`
- **[name] interno:** `EXMEM`
- **Símbolo (.sym):** 4800×6600

## Portas

| Porta | Direção | Largura | Posição no símbolo (x, y) |
|---|---|---|---|
| `REGDEST_O` | saída | 5 | (4800, 5400) |
| `DATA_I` | entrada | 32 | (0, 5400) |
| `JUMPADDRESS_I` | entrada | 32 | (0, 3600) |
| `ZERO_O` | saída | 1 | (4800, 3600) |
| `BRANCH` | saída | 1 | (4800, 1200) |
| `WB_O` | saída | 2 | (4800, 600) |
| `REGDEST_I` | entrada | 5 | (0, 6000) |
| `MEM_I` | entrada | 3 | (0, 3000) |
| `ZERO_I` | entrada | 1 | (0, 4200) |
| `WB_I` | entrada | 2 | (0, 2400) |
| `CLK` | entrada | 1 | (0, 1200) |
| `ENA` | entrada | 1 | (0, 600) |
| `MEMREAD` | saída | 1 | (4800, 1800) |
| `MEMWRITE` | saída | 1 | (4800, 2400) |
| `NR` | entrada | 1 | (0, 1800) |
| `ALUR_O` | saída | 32 | (4800, 4200) |
| `DATA_O` | saída | 32 | (4800, 4800) |
| `JUMPADDRESS_O` | saída | 32 | (4800, 3000) |
| `ALUR_I` | entrada | 32 | (0, 4800) |

## Componentes internos

RegRE×7, IpinVector×6, OpinVector×5, Opin×4, Ipin×4, Expander×2, MergeBits×1

## Arquivo .sym atual

```
hades.symbols.BboxRectangle  0 0 4800 6600
hades.symbols.Rectangle  0 0 4800 6600
hades.symbols.PortLabel 4650 5550 3 REGDEST_O
hades.symbols.PortSymbol 4800 5400 REGDEST_O
hades.symbols.PortLabel 4650 4950 3 DATA_O
hades.symbols.PortSymbol 4800 4800 DATA_O
hades.symbols.PortLabel 4650 4350 3 ALUR_O
hades.symbols.PortSymbol 4800 4200 ALUR_O
hades.symbols.PortLabel 4650 3750 3 ZERO_O
hades.symbols.PortSymbol 4800 3600 ZERO_O
hades.symbols.PortLabel 4650 3150 3 JUMPADDRESS_O
hades.symbols.PortSymbol 4800 3000 JUMPADDRESS_O
hades.symbols.PortLabel 4650 2550 3 MEMWRITE
hades.symbols.PortSymbol 4800 2400 MEMWRITE
hades.symbols.PortLabel 4650 1950 3 MEMREAD
hades.symbols.PortSymbol 4800 1800 MEMREAD
hades.symbols.PortLabel 4650 1350 3 BRANCH
hades.symbols.PortSymbol 4800 1200 BRANCH
hades.symbols.PortLabel 4650 750 3 WB_O
hades.symbols.PortSymbol 4800 600 WB_O
hades.symbols.PortLabel 150 6150 REGDEST_I
hades.symbols.PortSymbol 0 6000 REGDEST_I
hades.symbols.PortLabel 150 5550 DATA_I
hades.symbols.PortSymbol 0 5400 DATA_I
hades.symbols.PortLabel 150 4950 ALUR_I
hades.symbols.PortSymbol 0 4800 ALUR_I
hades.symbols.PortLabel 150 4350 ZERO_I
hades.symbols.PortSymbol 0 4200 ZERO_I
hades.symbols.PortLabel 150 3750 JUMPADDRESS_I
hades.symbols.PortSymbol 0 3600 JUMPADDRESS_I
hades.symbols.PortLabel 150 3150 MEM_I
hades.symbols.PortSymbol 0 3000 MEM_I
hades.symbols.PortLabel 150 2550 WB_I
hades.symbols.PortSymbol 0 2400 WB_I
hades.symbols.PortLabel 150 1950 NR
hades.symbols.PortSymbol 0 1800 NR
hades.symbols.PortLabel 150 1350 CLK
hades.symbols.PortSymbol 0 1200 CLK
hades.symbols.PortLabel 150 750 ENA
hades.symbols.PortSymbol 0 600 ENA
hades.symbols.InstanceLabel 150 6450 EXMEM
hades.symbols.ClassLabel 150 450 EXMEM
```
