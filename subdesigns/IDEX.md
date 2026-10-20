# IDEX

Registrador de pipeline ID/EX: sinais de controle, PC+4, dados lidos, imediato e campos rs/rt/rd.

- **Arquivo:** `Documents\CEFET\2026.2\HACKING AOC\Claude_Hades\IDEX.hds`
- **Caminho para usar na linha `hades.models.Design`:** `C:/Users/Luan/Documents/CEFET/2026.2/HACKING\u0020AOC/Claude_Hades/IDEX.hds`
- **[name] interno:** `IDEX`
- **Símbolo (.sym):** 4800×12000

## Portas

| Porta | Direção | Largura | Posição no símbolo (x, y) |
|---|---|---|---|
| `IMEDIATEO` | saída | 32 | (4800, 6000) |
| `DATA2O` | saída | 32 | (4800, 5400) |
| `IMEDIATE` | entrada | 32 | (0, 9600) |
| `ENABLEWRITE` | entrada | 1 | (0, 600) |
| `RTO` | saída | 5 | (4800, 6600) |
| `RT` | entrada | 5 | (0, 10200) |
| `DATA1O` | saída | 32 | (4800, 4800) |
| `RDO` | saída | 5 | (4800, 7200) |
| `RD` | entrada | 5 | (0, 10800) |
| `NOTRESET` | entrada | 1 | (0, 1200) |
| `ALUSRC` | saída | 1 | (4800, 3600) |
| `PCPLUS4` | entrada | 32 | (0, 7800) |
| `DATA2` | entrada | 32 | (0, 9000) |
| `DATA1` | entrada | 32 | (0, 8400) |
| `CLK` | entrada | 1 | (0, 1800) |
| `REGDST` | saída | 1 | (4800, 1800) |
| `MEM` | saída | 3 | (4800, 1200) |
| `PC_PLUS_4` | saída | 32 | (4800, 4200) |
| `ALUOP2` | saída | 1 | (4800, 3000) |
| `ALUOP1` | saída | 1 | (4800, 2400) |
| `WB` | saída | 2 | (4800, 600) |
| `RS` | entrada | 5 | (0, 11400) |
| `RSO` | saída | 5 | (4800, 7800) |
| `CTL` | entrada | 9 | (0, 2400) |

## Componentes internos

RegRE×10, OpinVector×9, IpinVector×8, Opin×4, MergeBits×3, Ipin×3, Expander×2

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
hades.symbols.PortLabel 150 2550 CTL
hades.symbols.PortSymbol 0 2400 CTL
hades.symbols.PortLabel 150 1950 CLK
hades.symbols.PortSymbol 0 1800 CLK
hades.symbols.PortLabel 150 1350 NOTRESET
hades.symbols.PortSymbol 0 1200 NOTRESET
hades.symbols.PortLabel 150 750 ENABLEWRITE
hades.symbols.PortSymbol 0 600 ENABLEWRITE
hades.symbols.InstanceLabel 150 11850 IDEX
hades.symbols.ClassLabel 150 450 IDEX
```
