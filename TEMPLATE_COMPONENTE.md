# <Classe> — <título curto em português>

- **Classe HADES:** `hades.models.<pacote>.<Classe>`
- **Categoria:** <io | barramentos | portas | logica-vetorial | aritmetica | mux | registradores | memoria | outra>
- **Dimensões (bbox, relativo à âncora):** x <x0>..<x1>, y <y0>..<y1> → <L> × <A>

## O que faz

<Uma ou duas frases. Fórmula se couber: `Y = A + B`.>

## Linha de componente

```
hades.models.<pacote>.<Classe> <nome> <x> <y> @N 1001 <parâmetros>
```

Parâmetros depois de `@N 1001` (1001 é a versão do modelo, sempre igual):

| # | Parâmetro | Significado |
|---|---|---|
| 1 | `n_bits` | <…> |
| 2 | `delay` | atraso em segundos (ex.: `1.0E-8`) |

## Portas

| Porta | Direção | Largura (bits) | Posição relativa (x, y) | Lado |
|---|---|---|---|---|
| `A` | entrada | n_bits | (x, y) | topo |
| `Y` | saída | n_bits | (x, y) | base |

Posição absoluta da porta = (x da instância + x relativo, y da instância + y relativo). Coordenadas em unidades HADES (grade de 600).

## Comportamento

- <regras de funcionamento, bordas de clock, sinais ativos em nível baixo, valores com X/U…>

## Dicas

- <pegadinhas: nomes de portas, posições fora da grade, fórmulas de símbolo dinâmico…>

## Exemplo

```
<linha de componente real>
<linha de sinal real ligada a ele>
```
