# Blocos reutilizáveis

Subcircuitos genéricos (`.hds` + `.sym`). Instanciar com `hades.models.Design` (ver `SUBCIRCUITOS.md`).

## SIGNAL_EXTENDER

Extensão de sinal 16 → 32 bits: OUTPUT[15:0] = INPUT, OUTPUT[31:16] = INPUT[15].

Arquivo: `blocks/SIGNAL_EXTENDER.hds`. 
Símbolo 4800×1200.

| Porta | Dir | Largura | Pos (x,y) |
|---|---|---|---|
| `INPUT` | in | 16 | (0,600) |
| `OUTPUT` | out | 32 | (4800,600) |

## SHIFTLEFT2

Deslocamento fixo de 2 à esquerda, 32 bits: OUTPUT = INPUT << 2.

Arquivo: `blocks/SHIFTLEFT2.hds`. 
Símbolo 4800×1200.

| Porta | Dir | Largura | Pos (x,y) |
|---|---|---|---|
| `INPUT` | in | 32 | (0,600) |
| `OUTPUT` | out | 32 | (4800,600) |
