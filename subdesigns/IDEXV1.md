# IDEXV1

Versão anterior do IDEX. Usada por PIPELINE.hds.

- **Arquivo:** `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\IDEXV1.hds`
- **Caminho para usar na linha `hades.models.Design`:** `C:/Users/Luan/Documents/CEFET/2026.2/HACKING\u0020AOC/Claude_Hades/IDEXV1.hds`
- **[name] interno:** `IDEX`
- **Símbolo (.sym):** 4800×12000

## Portas

| Porta | Direção | Largura | Posição no símbolo (x, y) |
|---|---|---|---|
| `IMEDIATEO` | saída | 32 | (4800, 6000) |
| `IALUOP1` | entrada | 1 | (0, 7200) |
| `IALUOP0` | entrada | 1 | (0, 6600) |
| `DATA2O` | saída | 32 | (4800, 5400) |
| `MEMWRITE` | entrada | 1 | (0, 5400) |
| `IMEDIATE` | entrada | 32 | (0, 9600) |
| `ENABLEWRITE` | entrada | 1 | (0, 600) |
| `RTO` | saída | 5 | (4800, 6600) |
| `RT` | entrada | 5 | (0, 10200) |
| `DATA1O` | saída | 32 | (4800, 4800) |
| `MEMREAD` | entrada | 1 | (0, 4800) |
| `RDO` | saída | 5 | (4800, 7200) |
| `REGWRITE` | entrada | 1 | (0, 4200) |
| `RD` | entrada | 5 | (0, 10800) |
| `NOTRESET` | entrada | 1 | (0, 1200) |
| `ALUSRC` | saída | 1 | (4800, 3600) |
| `PCPLUS4` | entrada | 32 | (0, 7800) |
| `MEM_TO_REG` | entrada | 1 | (0, 3600) |
| `DATA2` | entrada | 32 | (0, 9000) |
| `DATA1` | entrada | 32 | (0, 8400) |
| `CLK` | entrada | 1 | (0, 1800) |
| `REGDST` | saída | 1 | (4800, 1800) |
| `IALUSRC` | entrada | 1 | (0, 3000) |
| `MEM` | saída | 3 | (4800, 1200) |
| `PC_PLUS_4` | saída | 32 | (4800, 4200) |
| `ALUOP2` | saída | 1 | (4800, 3000) |
| `IBRANCH` | entrada | 1 | (0, 6000) |
| `ALUOP1` | saída | 1 | (4800, 2400) |
| `WB` | saída | 2 | (4800, 600) |
| `IREGDST` | entrada | 1 | (0, 2400) |
| `RS` | entrada | 5 | (0, 11400) |
| `RSO` | saída | 5 | (4800, 7800) |

## Componentes internos

Ipin×12, RegRE×10, OpinVector×9, IpinVector×7, Opin×4, MergeBits×3, Expander×1

## Arquivo .sym atual

```
hades.symbols.BboxRectangle  0 0 4800 12000
hades.symbols.Rectangle  0 0 4800 12000
hades.symbols.PortLabel 4650 7950 3 RSO
hades.symbols.PortSymbol 4800 7800 RSO
hades.symbols.PortLabel 4650 7350 3 RDO
hades.symbols.PortSymbol 4800 7200 RDO
hades.symbols.PortLabel 4650 6750 3 RTO
hades.symbols.PortSymbol 4800 6600 RTO
hades.symbols.PortLabel 4650 6150 3 IMEDIATEO
hades.symbols.PortSymbol 4800 6000 IMEDIATEO
hades.symbols.PortLabel 4650 5550 3 DATA2O
hades.symbols.PortSymbol 4800 5400 DATA2O
hades.symbols.PortLabel 4650 4950 3 DATA1O
hades.symbols.PortSymbol 4800 4800 DATA1O
hades.symbols.PortLabel 4650 4350 3 PC_PLUS_4
hades.symbols.PortSymbol 4800 4200 PC_PLUS_4
hades.symbols.PortLabel 4650 3750 3 ALUSRC
hades.symbols.PortSymbol 4800 3600 ALUSRC
hades.symbols.PortLabel 4650 3150 3 ALUOP2
hades.symbols.PortSymbol 4800 3000 ALUOP2
hades.symbols.PortLabel 4650 2550 3 ALUOP1
hades.symbols.PortSymbol 4800 2400 ALUOP1
hades.symbols.PortLabel 4650 1950 3 REGDST
hades.symbols.PortSymbol 4800 1800 REGDST
hades.symbols.PortLabel 4650 1350 3 MEM
hades.symbols.PortSymbol 4800 1200 MEM
hades.symbols.PortLabel 4650 750 3 WB
hades.symbols.PortSymbol 4800 600 WB
hades.symbols.PortLabel 150 11550 RS
hades.symbols.PortSymbol 0 11400 RS
hades.symbols.PortLabel 150 10950 RD
hades.symbols.PortSymbol 0 10800 RD
hades.symbols.PortLabel 150 10350 RT
hades.symbols.PortSymbol 0 10200 RT
hades.symbols.PortLabel 150 9750 IMEDIATE
hades.symbols.PortSymbol 0 9600 IMEDIATE
hades.symbols.PortLabel 150 9150 DATA2
hades.symbols.PortSymbol 0 9000 DATA2
hades.symbols.PortLabel 150 8550 DATA1
hades.symbols.PortSymbol 0 8400 DATA1
hades.symbols.PortLabel 150 7950 PCPLUS4
hades.symbols.PortSymbol 0 7800 PCPLUS4
hades.symbols.PortLabel 150 7350 IALUOP1
hades.symbols.PortSymbol 0 7200 IALUOP1
hades.symbols.PortLabel 150 6750 IALUOP0
hades.symbols.PortSymbol 0 6600 IALUOP0
hades.symbols.PortLabel 150 6150 IBRANCH
hades.symbols.PortSymbol 0 6000 IBRANCH
hades.symbols.PortLabel 150 5550 MEMWRITE
hades.symbols.PortSymbol 0 5400 MEMWRITE
hades.symbols.PortLabel 150 4950 MEMREAD
hades.symbols.PortSymbol 0 4800 MEMREAD
hades.symbols.PortLabel 150 4350 REGWRITE
hades.symbols.PortSymbol 0 4200 REGWRITE
hades.symbols.PortLabel 150 3750 MEM_TO_REG
hades.symbols.PortSymbol 0 3600 MEM_TO_REG
hades.symbols.PortLabel 150 3150 IALUSRC
hades.symbols.PortSymbol 0 3000 IALUSRC
hades.symbols.PortLabel 150 2550 IREGDST
hades.symbols.PortSymbol 0 2400 IREGDST
hades.symbols.PortLabel 150 1950 CLK
hades.symbols.PortSymbol 0 1800 CLK
hades.symbols.PortLabel 150 1350 NOTRESET
hades.symbols.PortSymbol 0 1200 NOTRESET
hades.symbols.PortLabel 150 750 ENABLEWRITE
hades.symbols.PortSymbol 0 600 ENABLEWRITE
hades.symbols.InstanceLabel 150 11850 IDEX
hades.symbols.ClassLabel 150 450 IDEX
```
