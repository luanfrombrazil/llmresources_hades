# Arquivos para memória (`.rom`)

Conteúdo inicial de `ROM`, `ROMoe`, `RAM`, `RAMoe`, `RegBank` e `MipsRegBank`. Mesmo formato e leitor para todos (verificado no hades.jar).

## Uso na linha do componente

```
hades.models.rtlib.memory.ROM IMEM 600 24000 @N 1001 1024 32 program.rom
hades.models.rtlib.memory.RAM DMEM 6000 24000 @N 1001 1024 32 data.rom
hades.models.rtlib.memory.MipsRegBank REGS 12000 24000 @N 1001 32 32 regs.rom
```

- 3º parâmetro após `1001`, opcional. Sem arquivo: memória começa zerada.
- Caminho: padrão relativo, arquivo na mesma pasta do `.hds` (ver `SUBCIRCUITOS.md`).
- Componentes com `.rom` ficam no circuito principal, nunca dentro de subcircuitos (`SUBCIRCUITOS.md`).

## Formato

```
# comentário de linha inteira
<endereço_hex>:<dado_hex>   # comentário no fim da linha
```

| Regra | Detalhe |
|---|---|
| endereço | índice de palavra (não byte), hex, 0..n_words−1 |
| dado | hex, até n_bits bits |
| caixa | maiúsculas ou minúsculas |
| zeros à esquerda | opcionais (`5:abc` = `0005:00000abc`) |
| endereços omitidos | 0 |
| comentários | `#` em linha inteira ou após o dado |
| linha inválida | erro com diálogo no editor |

Formato gravado pelo editor: endereço com 4 dígitos, dado com n_bits/4 dígitos, todas as posições (`0000:8c010003`).

## Padrão de geração

- Nome: `<função>.rom` (`program.rom`, `data.rom`, `regs.rom`), na pasta do `.hds`.
- Endereço com 4 dígitos, dado com n_bits/4 dígitos (32 bits → 8).
- Listar só posições usadas; comentar cada linha.
- ROM de instruções: uma instrução por linha, assembly no comentário.
- Endereço no arquivo = valor que chega na porta A. Se o circuito converte byte→palavra (ShiftRightLogic 2), endereço = byte / 4.

## Particularidades

- `MipsRegBank`: endereço = número do registrador (0..31). Valor do arquivo para o registrador 0 é ignorado (fica 0).
- `RegBank`: endereço = número do registrador.
- `RAM`/`RAMoe`/`RegBank`/`MipsRegBank`: o arquivo define só o estado inicial.

## Modelos

`program.rom` (MIPS, 32 bits):
```
# programa de teste
0000:8C010003   # lw  $1, 3($0)
0001:8C020006   # lw  $2, 6($0)
0002:00421820   # add $3, $2, $2
0003:00612020   # add $4, $3, $1
```

`data.rom` (RAM, 32 bits):
```
# dados iniciais
0003:00000005   # palavra 3 = 5
0006:0000000A   # palavra 6 = 10
```

`regs.rom` (MipsRegBank):
```
# registradores iniciais
0001:00000001   # $1 = 1
0002:00000002   # $2 = 2
001F:0000FFFF   # $31
```
