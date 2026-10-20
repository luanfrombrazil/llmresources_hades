# Exemplos reais

Cópias de arquivos seus (pasta `HACKING AOC\Claude_Hades`) para servir de referência de formato. **Não edite aqui**: os originais continuam na pasta da disciplina.

| Arquivo | Tipo | Por que olhar |
|---|---|---|
| `MUX4.hds` | circuito de teste | o menor exemplo completo: 1 Mux41, entradas e saída, lido linha a linha abaixo |
| `IFID.hds` + `IFID.sym` | subcircuito | registrador de pipeline: pinos que viram portas, clock/reset/enable distribuídos com pontos de solda |
| `HAZARD_UNIT.hds` + `HAZARD_UNIT.sym` | subcircuito | layout limpo da esquerda para a direita, CompareEqual + portas, saída em leque |
| `PIPELINEPOSHAZ.hds` | circuito principal | pipeline MIPS completo com 10 subcircuitos (`hades.models.Design`) |
| `contador4/` | circuito novo + subcircuito | **escrito só a partir desta documentação** e validado: carregado e simulado no `hades.jar` (veja abaixo) |

> Os nomes originais têm espaço (`HAZARD UNIT.hds`); aqui foram trocados por `_`. Se copiar um subcircuito, o `.sym` precisa ter o mesmo nome base do `.hds`.

## `MUX4.hds` linha a linha

```
hades.models.rtlib.muxes.Mux41 i2 8400 6600 @N 1001 16 0000000000000011_B 1.0E-8
```
Mux 4:1 de 16 bits com âncora em (8400, 6600). Pela tabela de `components/mux/Mux41.md`:
A3 (600,0) → **(9000, 6600)**, A2 (1800,0) → **(10200, 6600)**, A1 (3000,0) → **(11400, 6600)**, A0 (4200,0) → **(12600, 6600)**, S1 (0,600) → **(8400, 7200)**, S0 (0,1200) → **(8400, 7800)**, Y (2400,1800) → **(10800, 8400)**.

```
hades.models.rtlib.io.IpinVector i7 7200 0 @N 1001 16 0000000000000011_B 1.0E-9 0
hades.signals.SignalStdLogicVector n5 16 2 i7 Y i2 A0 2 2 7200 0 12600 0 2 12600 0 12600 6600 0
```
Entrada de 16 bits `i7`; a porta `Y` fica na própria âncora (7200, 0). O sinal `n5` (16 bits) liga `i7.Y` a `i2.A0` com dois segmentos: horizontal até x=12600 e vertical até a porta A0 em (12600, 6600). Zero pontos de solda.

```
hades.models.io.Ipin i4 6000 8400 @N 1001 null U
hades.signals.SignalStdLogic1164 n1 2 i4 Y i2 S0 1 2 6000 8400 8400 7800 0
```
Entrada de 1 bit. Aqui o fio é **um segmento diagonal** de (6000, 8400) até S0 (8400, 7800). Funciona, mas o certo é traçar segmentos ortogonais.

```
hades.models.rtlib.io.OpinVector i1 18600 10800 @N 1001 16 1.0E-9 0
hades.signals.SignalStdLogicVector n6 16 2 i2 Y i1 A 2 2 10800 8400 10800 10800 2 10800 10800 18600 10800 0
```
Saída: desce de Y (10800, 8400) e segue até a porta A do OpinVector, na âncora (18600, 10800).

## `contador4/`: teste da documentação

Circuito escrito do zero seguindo apenas `FORMATO_HDS.md`, `LAYOUT.md`, `SUBCIRCUITOS.md` e os arquivos de `components/`, para provar que a biblioteca basta:

- `INC4.hds` + `INC4.sym`: subcircuito novo, Y = A + 1 (4 bits), com `IpinVector`, `Constant`, `Add` e `OpinVector`.
- `CONTADOR4.hds`: contador de 4 bits (`RegRE` + `INC4`) com reset automático (`ClockGen` + `InvSmall`), comparação com um alvo (`CompareEqual` → `MATCH`) e detecção de "bits 1 e 0 em 1" (`Expander` + `And2` → `LOW2`).

Resultado no simulador do `hades.jar`: COUNT = 0, 1, 2, 3, 4, 5… a cada borda de subida; `LOW2` = 1 em 3 (e 7, 11, 15); `MATCH` = 1 em 5 (alvo `0101`). Todas as 31 extremidades de fio caem exatamente nas portas.

> O caminho do INC4 dentro de `CONTADOR4.hds` aponta para esta pasta (`C:/Users/Luan/Documents/PersonalProjects/llmresources_hades/examples/contador4/INC4.hds`). Se mover a pasta, ajuste a linha `hades.models.Design`.
