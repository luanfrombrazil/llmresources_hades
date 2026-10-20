# CACHE4WAY — cache associativa de 4 vias (Fig. 5.18, Patterson & Hennessy)

Abrir `CACHE4WAY.hds` no HADES (todos os arquivos na mesma pasta; caminhos relativos).

| Arquivo | Conteúdo |
|---|---|
| `CACHE4WAY.hds` | circuito principal |
| `MUX41_SEMDEC.hds` / `.sym` | mux 4:1 de 32 bits com seleção one-hot (sem decodificador) |
| `V0..V3.rom` | bit de validade de cada via (256 × 1) |
| `TAG0..TAG3.rom` | tag de cada via (256 × 22) |
| `DATA0..DATA3.rom` | dado de cada via (256 × 32) |

## Funcionamento

- `ADDRESS` (IpinVector 32, hex) → `TAG` = A[31:10] (22 bits), `INDEX` = A[9:2] (8 bits).
- INDEX endereça as 12 ROMs. Por via: `CMPw` = (TAGw == tag do endereço); `VBITw` converte a saída de 1 bit da ROM V (vetor) em sinal de 1 bit; `HITw` = V AND igual.
- `MUX41_SEMDEC`: Y = (D0·S0) | (D1·S1) | (D2·S2) | (D3·S3), com `N1And` (dado AND bit de seleção) + árvore de 3 `BitwiseOr`. Os selects são os próprios HITw (one-hot), então não há codificação para S1S0 nem decodificador. Sem hit, Y = 0.
- `HIT` = OR dos 4 HITw (`MergeBits` 4 + `rtlib.logic.Or` 4).

## Conteúdo das ROMs

DATA da via w no índice i = `0x(A+w)00000ii` → o valor lido diz a via e o conjunto (A=via0, B=via1, C=via2, D=via3).

| Via | Índice | V | Tag |
|---|---|---|---|
| 0 | 0x00 | 1 | 0x000001 |
| 1 | 0x00 | 1 | 0x000000 |
| 2 | 0x01 | 1 | 0x000ABC |
| 3 | 0x01 | 0 | 0x000ABC (tag bate, mas inválido) |
| 3 | 0x02 | 1 | 0x3FFFFF |
| 0 | 0xFF | 1 | 0x000000 |
| demais | — | 0 | 0x000000 |

## Testes

| ADDRESS | Tag / Índice | HIT | DATA |
|---|---|---|---|
| 0x00000000 | 0x000000 / 0x00 | 1 (via 1) | 0xB0000000 |
| 0x00000400 | 0x000001 / 0x00 | 1 (via 0) | 0xA0000000 |
| 0x002AF004 | 0x000ABC / 0x01 | 1 (via 2; via 3 ignorada por V=0) | 0xC0000001 |
| 0xFFFFFC08 | 0x3FFFFF / 0x02 | 1 (via 3) | 0xD0000002 |
| 0x000003FC | 0x000000 / 0xFF | 1 (via 0) | 0xA00000FF |
| 0x00000008 | 0x000000 / 0x02 | 0 | 0x00000000 |
| 0x00000804 | 0x000002 / 0x01 | 0 | 0x00000000 |
