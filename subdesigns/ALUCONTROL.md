# ALUCONTROL

Controle da ULA: ALUOp + funct → código de operação da ULA.

- **Arquivo:** `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\ALUCONTROL.hds`
- **Caminho para usar na linha `hades.models.Design`:** `C:/Users/Luan/Documents/CEFET/2026.2/HACKING\u0020AOC/Claude_Hades/ALUCONTROL.hds`
- **[name] interno:** `ALUCONTROL`
- **Símbolo (.sym):** 4800×5400

## Portas

| Porta | Direção | Largura | Posição no símbolo (x, y) |
|---|---|---|---|
| `f5` | entrada | 1 | (0, 1800) |
| `f4` | entrada | 1 | (0, 2400) |
| `f3` | entrada | 1 | (0, 3000) |
| `f2` | entrada | 1 | (0, 3600) |
| `f1` | entrada | 1 | (0, 4200) |
| `f0` | entrada | 1 | (0, 4800) |
| `ALUOP1` | entrada | 1 | (0, 1200) |
| `ALUOP0` | entrada | 1 | (0, 600) |
| `OP3` | saída | 1 | (4800, 600) |
| `OP2` | saída | 1 | (4800, 1200) |
| `OP1` | saída | 1 | (4800, 1800) |
| `OP0` | saída | 1 | (4800, 2400) |

## Componentes internos

Ipin×8, Opin×4, InvSmall×3, Or2×3, And2×3

## Arquivo .sym atual

```
hades.symbols.BboxRectangle  0 0 4800 5400
hades.symbols.Rectangle  0 0 4800 5400
hades.symbols.PortLabel 4650 2550 3 OP0
hades.symbols.PortSymbol 4800 2400 OP0
hades.symbols.PortLabel 4650 1950 3 OP1
hades.symbols.PortSymbol 4800 1800 OP1
hades.symbols.PortLabel 4650 1350 3 OP2
hades.symbols.PortSymbol 4800 1200 OP2
hades.symbols.PortLabel 4650 750 3 OP3
hades.symbols.PortSymbol 4800 600 OP3
hades.symbols.PortLabel 150 4950 f0
hades.symbols.PortSymbol 0 4800 f0
hades.symbols.PortLabel 150 4350 f1
hades.symbols.PortSymbol 0 4200 f1
hades.symbols.PortLabel 150 3750 f2
hades.symbols.PortSymbol 0 3600 f2
hades.symbols.PortLabel 150 3150 f3
hades.symbols.PortSymbol 0 3000 f3
hades.symbols.PortLabel 150 2550 f4
hades.symbols.PortSymbol 0 2400 f4
hades.symbols.PortLabel 150 1950 f5
hades.symbols.PortSymbol 0 1800 f5
hades.symbols.PortLabel 150 1350 ALUOP1
hades.symbols.PortSymbol 0 1200 ALUOP1
hades.symbols.PortLabel 150 750 ALUOP0
hades.symbols.PortSymbol 0 600 ALUOP0
hades.symbols.InstanceLabel 150 5250 ALUCONTROL
hades.symbols.ClassLabel 150 450 ALUCONTROL
```
