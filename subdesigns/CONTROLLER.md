# CONTROLLER

Unidade de controle principal: opcode (6 bits) → barramento de controle CTL (9 bits) + BRANCH.

- **Arquivo:** `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\CONTROLLER.hds`
- **Caminho para usar na linha `hades.models.Design`:** `C:/Users/Luan/Documents/CEFET/2026.2/HACKING\u0020AOC/Claude_Hades/CONTROLLER.hds`
- **[name] interno:** `CONTROLLER`
- **Símbolo (.sym):** 4800×1800

## Portas

| Porta | Direção | Largura | Posição no símbolo (x, y) |
|---|---|---|---|
| `BRANCH` | saída | 1 | (4800, 1200) |
| `OPCODE` | entrada | 6 | (0, 600) |
| `CTL` | saída | 9 | (4800, 600) |

## Componentes internos

InvVertical×16, And3Vertical×8, And2×4, Or2×2, Opin×1, IpinVector×1, ExpanderVertical×1, MergeBits×1, OpinVector×1

## Arquivo .sym atual

```
hades.symbols.BboxRectangle  0 0 4800 1800
hades.symbols.Rectangle  0 0 4800 1800
hades.symbols.PortLabel 4650 750 3 CTL
hades.symbols.PortSymbol 4800 600 CTL
hades.symbols.PortLabel 4650 1350 3 BRANCH
hades.symbols.PortSymbol 4800 1200 BRANCH
hades.symbols.PortLabel 150 750 OPCODE
hades.symbols.PortSymbol 0 600 OPCODE
hades.symbols.InstanceLabel 150 1650 CONTROLLER
hades.symbols.ClassLabel 150 450 CONTROLLER
```
