# <Classe> — <título>

Classe: `hades.models.<pacote>.<Classe>`  
bbox: (x0,y0)..(x1,y1)

<Função em uma linha; fórmula se couber.>

## Linha

```
hades.models.<pacote>.<Classe> <nome> <x> <y> @N 1001 <parâmetros>
```

| # | Parâmetro após `1001` | Significado |
|---|---|---|
| 1 | `n_bits` | largura em bits |
| 2 | `delay` | atraso em s |

## Portas

| Porta | Dir | Largura | Pos (x,y) | Lado |
|---|---|---|---|---|
| `A` | in | n_bits | (x,y) | topo |
| `Y` | out | n_bits | (x,y) | base |

## Comportamento

- <regras: clock, ativo baixo, valores X/U>

## Notas

- <nomes de portas incomuns, posições fora da grade, fórmulas de símbolo dinâmico>

## Exemplo

```
<linha de componente>
<linha de sinal ligada a ele>
```
