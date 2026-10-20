# Exemplos

Todos com caminhos relativos; carregam e simulam no hades.jar.

| Pasta | Conteúdo |
|---|---|
| `mux4/` | Mínimo: 1 Mux41 16 bits, entradas e saída |
| `contador4/` | Contador 4 bits com subcircuito próprio (`INC4`), reset automático, comparador, Expander + And2 |
| `mips_pipeline/` | Pipeline MIPS de 5 estágios com 8 subcircuitos específicos + 2 de `blocks/` |
| `portas_mistas/` | Subcircuito com portas no topo, à esquerda e à direita (`PORTAS_MISTAS.md`) |

## mux4/MUX4.hds

```
hades.models.rtlib.muxes.Mux41 i2 8400 6600 @N 1001 16 0000000000000011_B 1.0E-8
```
Portas absolutas: A3 (9000,6600), A2 (10200,6600), A1 (11400,6600), A0 (12600,6600), S1 (8400,7200), S0 (8400,7800), Y (10800,8400).

```
hades.models.rtlib.io.IpinVector i7 7200 0 @N 1001 16 0000000000000011_B 1.0E-9 0
hades.signals.SignalStdLogicVector n5 16 2 i7 Y i2 A0 2 2 7200 0 12600 0 2 12600 0 12600 6600 0
```
`i7.Y` na âncora (7200,0) → horizontal até x=12600 → vertical até A0.

```
hades.models.io.Ipin i4 6000 8400 @N 1001 null U
hades.signals.SignalStdLogic1164 n1 2 i4 Y i2 S0 1 2 6000 8400 8400 7800 0
```
Segmento diagonal: aceito, mas preferir ortogonal.

## contador4/

- `INC4.hds` + `INC4.sym`: Y = A + 1 (4 bits): IpinVector, Constant, Add, OpinVector.
- `CONTADOR4.hds`: RegRE 4 + INC4; reset automático (ClockGen + InvSmall); `MATCH` = (COUNT == TARGET `0101`); `LOW2` = bit1 AND bit0.
- Simulação: COUNT 0,1,2,… por borda de subida; LOW2 = 1 em 3,7,11,15; MATCH = 1 em 5.

## mips_pipeline/

Ver `mips_pipeline/README.md`.
