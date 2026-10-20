# MEM INDEXER FIX

Ajuste do endereço de memória (bloco auxiliar).

- **Arquivo:** `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\MEM INDEXER FIX.hds`
- **Caminho para usar na linha `hades.models.Design`:** `C:/Users/Luan/Documents/CEFET/2026.2/HACKING\u0020AOC/Claude_Hades/MEM\u0020INDEXER\u0020FIX.hds`
- **[name] interno:** `MEMINDEXER`
- **Símbolo (.sym):** 4800×1200

## Portas

| Porta | Direção | Largura | Posição no símbolo (x, y) |
|---|---|---|---|
| `i1` | saída | 10 | (4800, 600) |
| `i0` | entrada | 32 | (0, 600) |

## Componentes internos

MergeBits×1, Expander×1, OpinVector×1, IpinVector×1

## Arquivo .sym atual

```
hades.symbols.BboxRectangle  0 0 4800 1200
hades.symbols.Rectangle  0 0 4800 1200
hades.symbols.PortLabel 4650 750 3 i1
hades.symbols.PortSymbol 4800 600 i1
hades.symbols.PortLabel 150 750 i0
hades.symbols.PortSymbol 0 600 i0
hades.symbols.InstanceLabel 150 1050 MEMINDEXER
hades.symbols.ClassLabel 150 450 MEMINDEXER
```
