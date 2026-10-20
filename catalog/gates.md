# Catálogo HADES — pacote `hades.models.gates`

Gerado automaticamente a partir do `hades.jar` (parâmetros PADRÃO). Componentes marcados com ✅ têm documentação detalhada em `components/`.
Para os demais: portas, posições e bbox valem para os parâmetros padrão; componentes de largura variável mudam com `n_bits`. Antes de usar um deles pela primeira vez, documente-o (veja `ADICIONANDO_COMPONENTES.md`).

## And2 ✅

`hades.models.gates.And2` — Standard 2-input AND gate.

Doc detalhada: [components/portas/And2.md](../components/portas/And2.md)

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `Y` out 1b @(3600,1200), `A` in 1b @(0,600), `B` in 1b @(0,1800)

## And2Vertical ✅

`hades.models.gates.And2Vertical` — 2-input AND gate with vertically oriented symbol.

Doc detalhada: [components/portas/And2Vertical.md](../components/portas/And2Vertical.md)

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(2400, 3600)
- Portas: `Y` out 1b @(1200,3600), `A` in 1b @(600,0), `B` in 1b @(1800,0)

## And3 ✅

`hades.models.gates.And3` — Standard 3-input AND gate.

Doc detalhada: [components/portas/And3.md](../components/portas/And3.md)

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `Y` out 1b @(3600,1200), `A` in 1b @(0,600), `B` in 1b @(0,1200), `C` in 1b @(0,1800)

## And3Vertical ✅

`hades.models.gates.And3Vertical` — 3-input AND gate with vertically oriented symbol.

Doc detalhada: [components/portas/And3Vertical.md](../components/portas/And3Vertical.md)

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(2400, 3600)
- Portas: `Y` out 1b @(1200,3600), `A` in 1b @(600,0), `B` in 1b @(1200,0), `C` in 1b @(1800,0)

## And4

`hades.models.gates.And4` — Standard 4-input AND gate.

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `Y` out 1b @(3600,1200), `A` in 1b @(0,300), `B` in 1b @(0,900), `C` in 1b @(0,1500), `D` in 1b @(0,2100)

## And4Neg2

`hades.models.gates.And4Neg2` — 4-input AND gate (with two positive and two inverted inputs).

- Parâmetros padrão: `1001 1.0E-8`
- Portas: `Y` out 1b (sem posição), `A` in 1b (sem posição), `B` in 1b (sem posição), `C` in 1b (sem posição), `D` in 1b (sem posição)

## And6

`hades.models.gates.And6` — Standard 6-input AND gate.

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 4200)
- Portas: `Y` out 1b @(3600,1800), `A` in 1b @(0,600), `B` in 1b @(0,1200), `C` in 1b @(0,1800), `D` in 1b @(0,2400), `E` in 1b @(0,3000), `F` in 1b @(0,3600)

## Buffer

`hades.models.gates.Buffer` — Simple non-inverting buffer.

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(2400, 2400)
- Portas: `Y` out 1b @(2400,1200), `A` in 1b @(0,1200)

## BufferSmall

`hades.models.gates.BufferSmall` — Simple non-inverting buffer, with small symbol.

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(1800, 1200)
- Portas: `Y` out 1b @(1800,600), `A` in 1b @(0,600)

## DelayNode_LR

`hades.models.gates.DelayNode_LR` — "DelayNode" with left-to-right oriented symbol

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (-150, -150)..(150, 150)
- Portas: `A` in 1b @(-150,0), `Y` out 1b @(150,0)

## DelayNode_TB

`hades.models.gates.DelayNode_TB` — "DelayNode" with top-to-bottom oriented symbol

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (-150, -150)..(150, 150)
- Portas: `A` in 1b @(0,-150), `Y` out 1b @(0,150)

## Demux14

`hades.models.gates.Demux14` — Simple 1-to-4 demultiplexer.

- Parâmetros padrão: `1001 1.5E-8`
- bbox: (0, 0)..(3000, 3000)
- Portas: `Y0` out 1b @(3000,2400), `Y1` out 1b @(3000,1800), `Y2` out 1b @(3000,1200), `Y3` out 1b @(3000,600), `S0` in 1b @(1800,3000), `S1` in 1b @(1200,3000), `A` in 1b @(0,1500)

## Inv

`hades.models.gates.Inv` — Simple inverter gate.

- Parâmetros padrão: `1001 5.0E-9`
- bbox: (0, 0)..(2400, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(2400,1200)

## InvOpenCollector

`hades.models.gates.InvOpenCollector` — Inverter with open-collector output.

- Parâmetros padrão: `1001 5.0E-9`
- bbox: (0, 0)..(1800, 2400)
- Portas: `A` in 1b @(0,1200), `Y` out 1b @(1800,600)

## InvSmall ✅

`hades.models.gates.InvSmall` — Inverter gate (with small symbol).

Doc detalhada: [components/portas/InvSmall.md](../components/portas/InvSmall.md)

- Parâmetros padrão: `1001 5.0E-9`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## Mux21

`hades.models.gates.Mux21` — 2-to-1 Multiplexer gate.

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(2400, 2400)
- Portas: `Y` out 1b @(2400,1200), `A0` in 1b @(0,1800), `A1` in 1b @(0,600), `S` in 1b @(1200,2400)

## Mux41

`hades.models.gates.Mux41` — 4-to-1 multiplexer gate.

- Parâmetros padrão: `1001 1.5E-8`
- bbox: (0, 0)..(3000, 3000)
- Portas: `Y` out 1b @(3000,1500), `A0` in 1b @(0,2400), `A1` in 1b @(0,1800), `A2` in 1b @(0,1200), `A3` in 1b @(0,600), `S0` in 1b @(1800,3000), `S1` in 1b @(1200,3000)

## Nand2 ✅

`hades.models.gates.Nand2` — Standard 2-input NAND gate.

Doc detalhada: [components/portas/Nand2.md](../components/portas/Nand2.md)

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `Y` out 1b @(3600,1200), `A` in 1b @(0,600), `B` in 1b @(0,1800)

## Nand3

`hades.models.gates.Nand3` — Standard 3-input NAND gate.

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `Y` out 1b @(3600,1200), `A` in 1b @(0,600), `B` in 1b @(0,1200), `C` in 1b @(0,1800)

## Nand4

`hades.models.gates.Nand4` — Standard 4-input NAND gate.

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `Y` out 1b @(3600,1200), `A` in 1b @(0,300), `B` in 1b @(0,900), `C` in 1b @(0,1500), `D` in 1b @(0,2100)

## NandMetastable2

`hades.models.gates.NandMetastable2` — "Metastable" 2-input NAND gate. 

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `Y` out 1b @(3600,1200), `A` in 1b @(0,600), `B` in 1b @(0,1800)

## NandMetastable3

`hades.models.gates.NandMetastable3` — "Metastable" 3-input NAND gate.

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `Y` out 1b @(3600,1200), `A` in 1b @(0,600), `B` in 1b @(0,1200), `C` in 1b @(0,1800)

## Nor2

`hades.models.gates.Nor2` — Standard 2-input NOR gate.

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `Y` out 1b @(3600,1200), `A` in 1b @(0,600), `B` in 1b @(0,1800)

## Nor3

`hades.models.gates.Nor3` — Standard 3-input NOR gate.

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `Y` out 1b @(3600,1200), `A` in 1b @(0,600), `B` in 1b @(0,1800), `C` in 1b @(0,1200)

## Nor4

`hades.models.gates.Nor4` — Standard 4-input NOR gate.

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `Y` out 1b @(3600,1200), `A` in 1b @(0,300), `B` in 1b @(0,900), `C` in 1b @(0,1500), `D` in 1b @(0,2100)

## Or2 ✅

`hades.models.gates.Or2` — Standard 2-input OR gate.

Doc detalhada: [components/portas/Or2.md](../components/portas/Or2.md)

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `Y` out 1b @(3600,1200), `A` in 1b @(0,600), `B` in 1b @(0,1800)

## Or3

`hades.models.gates.Or3` — Standard 3-input OR gate.

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `Y` out 1b @(3600,1200), `A` in 1b @(0,600), `B` in 1b @(0,1200), `C` in 1b @(0,1800)

## Or4

`hades.models.gates.Or4` — Standard 4-input OR gate.

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `Y` out 1b @(3600,1200), `A` in 1b @(0,300), `B` in 1b @(0,900), `C` in 1b @(0,1500), `D` in 1b @(0,2100)

## Or6

`hades.models.gates.Or6` — 6-input OR gate.

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 4200)
- Portas: `Y` out 1b @(3600,1800), `A` in 1b @(0,600), `B` in 1b @(0,1200), `C` in 1b @(0,1800), `D` in 1b @(0,2400), `E` in 1b @(0,3000), `F` in 1b @(0,3600)

## Tri

`hades.models.gates.Tri` — Inverting buffer with Tristate output.

- Parâmetros padrão: `1001 5.0E-9`
- bbox: (0, 0)..(2400, 2400)
- Portas: `Y` out 1b @(2400,1200), `A` in 1b @(0,1200), `S` in 1b @(1200,2400)

## WeakBuffer

`hades.models.gates.WeakBuffer` — Weak non-inverting buffer. This component generates the

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(1800, 1200)
- Portas: `Y` out 1b @(1800,600), `A` in 1b @(0,600)

## WeakInverter

`hades.models.gates.WeakInverter` — Weak inverting buffer. This component generates a

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(1800, 1200)
- Portas: `Y` out 1b @(1800,600), `A` in 1b @(0,600)

## Xnor2

`hades.models.gates.Xnor2` — Standard 2-input XNOR gate.

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `Y` out 1b @(3600,1200), `A` in 1b @(0,600), `B` in 1b @(0,1800)

## Xor2

`hades.models.gates.Xor2` — Standard 2-input XOR gate.

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(3600, 2400)
- Portas: `Y` out 1b @(3600,1200), `A` in 1b @(0,600), `B` in 1b @(0,1800)

## Xor2Vertical

`hades.models.gates.Xor2Vertical` — Standard 2-input XOR gate.

- Parâmetros padrão: `1001 1.0E-8`
- bbox: (0, 0)..(2400, 3600)
- Portas: `Y` out 1b @(1200,3600), `A` in 1b @(600,0), `B` in 1b @(1800,0)
