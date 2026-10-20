# FOWARDING UNIT

Unidade de forwarding (adiantamento): compara registradores destino de EX/MEM e MEM/WB com rs/rt de ID/EX e gera os seletores dos Mux41.

- **Arquivo:** `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\FOWARDING UNIT.hds`
- **Caminho para usar na linha `hades.models.Design`:** `C:/Users/Luan/Documents/CEFET/2026.2/HACKING\u0020AOC/Claude_Hades/FOWARDING\u0020UNIT.hds`
- **[name] interno:** `FORWARDINGUNIT`
- **Símbolo (.sym):** 4800×4200

## Portas

| Porta | Direção | Largura | Posição no símbolo (x, y) |
|---|---|---|---|
| `RT` | entrada | 5 | (0, 1200) |
| `EXMEM` | entrada | 2 | (0, 2400) |
| `RS` | entrada | 5 | (0, 600) |
| `RDMEM` | entrada | 5 | (0, 1800) |
| `FORWARD_B` | saída | 2 | (4800, 1200) |
| `RDWB1` | entrada | 5 | (0, 3000) |
| `FORWARD_A` | saída | 2 | (4800, 600) |
| `MEMWB` | entrada | 2 | (0, 3600) |

## Componentes internos

IpinVector×6, CompareEqual×4, Or×4, And3Vertical×4, OpinVector×2, InvSmall×2, And2Vertical×2, MergeBits×2, Expander×2

## Arquivo .sym atual

```
hades.symbols.BboxRectangle  0 0 4800 4200
hades.symbols.Rectangle  0 0 4800 4200
hades.symbols.PortLabel 4650 750 3 FORWARD_A
hades.symbols.PortSymbol 4800 600 FORWARD_A
hades.symbols.PortLabel 4650 1350 3 FORWARD_B
hades.symbols.PortSymbol 4800 1200 FORWARD_B
hades.symbols.PortLabel 150 750 RS
hades.symbols.PortSymbol 0 600 RS
hades.symbols.PortLabel 150 1350 RT
hades.symbols.PortSymbol 0 1200 RT
hades.symbols.PortLabel 150 1950 RDMEM
hades.symbols.PortSymbol 0 1800 RDMEM
hades.symbols.PortLabel 150 2550 EXMEM
hades.symbols.PortSymbol 0 2400 EXMEM
hades.symbols.PortLabel 150 3150 RDWB1
hades.symbols.PortSymbol 0 3000 RDWB1
hades.symbols.PortLabel 150 3750 MEMWB
hades.symbols.PortSymbol 0 3600 MEMWB
hades.symbols.InstanceLabel 150 4050 FORWARDINGUNIT
hades.symbols.ClassLabel 150 450 FORWARDINGUNIT
```
