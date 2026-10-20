# IFID

Registrador de pipeline IF/ID: guarda PC+4 e a instrução.

- **Arquivo:** `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\IFID.hds`
- **Caminho para usar na linha `hades.models.Design`:** `C:/Users/Luan/Documents/CEFET/2026.2/HACKING\u0020AOC/Claude_Hades/IFID.hds`
- **[name] interno:** `IFID`
- **Símbolo (.sym):** 4800×3600

## Portas

| Porta | Direção | Largura | Posição no símbolo (x, y) |
|---|---|---|---|
| `ENA` | entrada | 1 | (0, 600) |
| `INSTRUCTION_I` | entrada | 32 | (0, 3000) |
| `NR` | entrada | 1 | (0, 2400) |
| `PC4_O` | saída | 32 | (4800, 600) |
| `PC4_I` | entrada | 32 | (0, 1800) |
| `CLK` | entrada | 1 | (0, 1200) |
| `INSTRUCTION_O` | saída | 32 | (4800, 1200) |

## Componentes internos

Ipin×3, IpinVector×2, OpinVector×2, RegRE×2

## Arquivo .sym atual

```
hades.symbols.BboxRectangle  0 0 4800 3600
hades.symbols.Rectangle  0 0 4800 3600
hades.symbols.PortLabel 4650 1350 3 INSTRUCTION_O
hades.symbols.PortSymbol 4800 1200 INSTRUCTION_O
hades.symbols.PortLabel 4650 750 3 PC4_O
hades.symbols.PortSymbol 4800 600 PC4_O
hades.symbols.PortLabel 150 3150 INSTRUCTION_I
hades.symbols.PortSymbol 0 3000 INSTRUCTION_I
hades.symbols.PortLabel 150 2550 NR
hades.symbols.PortSymbol 0 2400 NR
hades.symbols.PortLabel 150 1950 PC4_I
hades.symbols.PortSymbol 0 1800 PC4_I
hades.symbols.PortLabel 150 1350 CLK
hades.symbols.PortSymbol 0 1200 CLK
hades.symbols.PortLabel 150 750 ENA
hades.symbols.PortSymbol 0 600 ENA
hades.symbols.InstanceLabel 150 3450 IFID
hades.symbols.ClassLabel 150 450 IFID
```
