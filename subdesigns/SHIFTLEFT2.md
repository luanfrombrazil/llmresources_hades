# SHIFTLEFT2

Deslocamento de 2 bits à esquerda (32 bits), para o alvo de desvio.

- **Arquivo:** `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\SHIFTLEFT2.hds`
- **Caminho para usar na linha `hades.models.Design`:** `C:/Users/Luan/Documents/CEFET/2026.2/HACKING\u0020AOC/Claude_Hades/SHIFTLEFT2.hds`
- **[name] interno:** `SHIFTLEFT2`
- **Símbolo (.sym):** 4800×1200

## Portas

| Porta | Direção | Largura | Posição no símbolo (x, y) |
|---|---|---|---|
| `INPUT` | entrada | 32 | (0, 600) |
| `OUTPUT` | saída | 32 | (4800, 600) |

## Componentes internos

IpinVector×1, Expander×1, MergeBits×1, Gnd×1, OpinVector×1

## Arquivo .sym atual

```
hades.symbols.BboxRectangle  0 0 4800 1200
hades.symbols.Rectangle  0 0 4800 1200
hades.symbols.PortLabel 4650 750 3 OUTPUT
hades.symbols.PortSymbol 4800 600 OUTPUT
hades.symbols.PortLabel 150 750 INPUT
hades.symbols.PortSymbol 0 600 INPUT
hades.symbols.InstanceLabel 150 1050 SHIFTLEFT2
hades.symbols.ClassLabel 150 450 SHIFTLEFT2
```
