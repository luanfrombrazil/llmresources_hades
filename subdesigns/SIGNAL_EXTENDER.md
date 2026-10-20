# SIGNAL EXTENDER

Extensor de sinal 16 → 32 bits.

- **Arquivo:** `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\SIGNAL EXTENDER.hds`
- **Caminho para usar na linha `hades.models.Design`:** `C:/Users/Luan/Documents/CEFET/2026.2/HACKING\u0020AOC/Claude_Hades/SIGNAL\u0020EXTENDER.hds`
- **[name] interno:** `SIGNAL_EXTENDER`
- **Símbolo (.sym):** 4800×1200

## Portas

| Porta | Direção | Largura | Posição no símbolo (x, y) |
|---|---|---|---|
| `OUTPUT` | saída | 32 | (4800, 600) |
| `INPUT` | entrada | 16 | (0, 600) |

## Componentes internos

OpinVector×1, MergeBits×1, Expander×1, IpinVector×1

## Arquivo .sym atual

```
hades.symbols.BboxRectangle  0 0 4800 1200
hades.symbols.Rectangle  0 0 4800 1200
hades.symbols.PortLabel 4650 750 3 OUTPUT
hades.symbols.PortSymbol 4800 600 OUTPUT
hades.symbols.PortLabel 150 750 INPUT
hades.symbols.PortSymbol 0 600 INPUT
hades.symbols.InstanceLabel 150 1050 SIGNAL_EXTENDER
hades.symbols.ClassLabel 150 450 SIGNAL_EXTENDER
```
