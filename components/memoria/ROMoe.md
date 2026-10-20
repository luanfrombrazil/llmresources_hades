# ROMoe — ROM com chip-select e output-enable

Classe: `hades.models.rtlib.memory.ROMoe`  
bbox: (0,0)..(6000,4800)

ROM com nCS e nOE (ativos baixo; desabilitada → Z).

## Linha

```
hades.models.rtlib.memory.ROMoe <nome> <x> <y> @N 1001 16 16
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_words` | palavras |
| 2 | `n_bits` | bits por palavra |
| 3 | `arquivo` | opcional, `.rom` |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | ceil(log2(n_words)) | (0,2400) | esq |
| `D` | out | n_bits | (3600,4800) | base |
| `nCS` | in | 1 | (0,1800) | esq |
| `nOE` | in | 1 | (0,3000) | esq |
