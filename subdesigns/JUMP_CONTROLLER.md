# JUMP CONTROLLER

Controle de jump do monociclo (TP02, AOC I).

- **Arquivo:** `Documents\CEFET\2026.1\Lab Arquitetura e Organização de Computadores I\TP02_LuanLanaMaia\JUMP CONTROLLER.hds`
- **Caminho para usar na linha `hades.models.Design`:** `C:/Users/Luan/Documents/CEFET/2026.1/Lab\u0020Arquitetura\u0020e\u0020Organiza\u00e7\u00e3o\u0020de\u0020Computadores\u0020I/TP02_LuanLanaMaia/JUMP\u0020CONTROLLER.hds`
- **[name] interno:** `JUMPCONTROLLER`
- **Símbolo (.sym):** 4800×4200

## Portas

| Porta | Direção | Largura | Posição no símbolo (x, y) |
|---|---|---|---|
| `i6` | saída | 1 | (4800, 600) |
| `i5` | entrada | 1 | (0, 3600) |
| `i4` | entrada | 1 | (0, 3000) |
| `i3` | entrada | 1 | (0, 2400) |
| `i2` | entrada | 1 | (0, 1800) |
| `i1` | entrada | 1 | (0, 1200) |
| `i0` | entrada | 1 | (0, 600) |

## Componentes internos

Ipin×6, InvSmall×5, And3×2, Opin×1, And2×1

## Arquivo .sym atual

```
hades.symbols.BboxRectangle  0 0 4800 4200
hades.symbols.Rectangle  0 0 4800 4200
hades.symbols.PortLabel 4650 750 3 i6
hades.symbols.PortSymbol 4800 600 i6
hades.symbols.PortLabel 150 3750 i5
hades.symbols.PortSymbol 0 3600 i5
hades.symbols.PortLabel 150 3150 i4
hades.symbols.PortSymbol 0 3000 i4
hades.symbols.PortLabel 150 2550 i3
hades.symbols.PortSymbol 0 2400 i3
hades.symbols.PortLabel 150 1950 i2
hades.symbols.PortSymbol 0 1800 i2
hades.symbols.PortLabel 150 1350 i1
hades.symbols.PortSymbol 0 1200 i1
hades.symbols.PortLabel 150 750 i0
hades.symbols.PortSymbol 0 600 i0
hades.symbols.InstanceLabel 150 4050 JUMPCONTROLLER
hades.symbols.ClassLabel 150 450 JUMPCONTROLLER
```
