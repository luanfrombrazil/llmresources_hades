# Subcircuitos e `.sym`

Hierarquia: um `.hds` instanciado em outro via `hades.models.Design`.

## Criar bloco

- Entrada: `hades.models.io.Ipin` (1 bit) ou `hades.models.rtlib.io.IpinVector` (n bits).
- Saída: `hades.models.io.Opin` ou `hades.models.rtlib.io.OpinVector`.
- Nome da instância do pino = nome da porta; `n_bits` = largura.
- Criar `<nome>.sym` na mesma pasta do `<nome>.hds`.

## Instanciar

```
hades.models.Design <instância> <x> <y> @N 1001 <caminho.hds>
```

- Caminho relativo à pasta do `.hds` pai (ex.: `IFID.hds`, `../../blocks/SHIFTLEFT2.hds`) ou absoluto com `/` e escapes `\uXXXX`. O editor do HADES regrava caminhos como absolutos ao salvar.
- Sinal: `<instância> <pino>` (ex.: `IFID PC4_I`).
- Porta absoluta = âncora + posição do `PortSymbol` no `.sym`.

## Formato `.sym`

```
hades.symbols.BboxRectangle  0 0 <L> <A>
hades.symbols.Rectangle  0 0 <L> <A>
hades.symbols.PortLabel <L-150> <y+150> 3 <SAIDA>
hades.symbols.PortSymbol <L> <y> <SAIDA>
hades.symbols.PortLabel 150 <y+150> <ENTRADA>
hades.symbols.PortSymbol 0 <y> <ENTRADA>
hades.symbols.InstanceLabel 150 <A-150> <NOME>
hades.symbols.ClassLabel 150 450 <NOME>
```

| Linha | Função |
|---|---|
| `BboxRectangle` | caixa de seleção |
| `Rectangle` | contorno |
| `PortSymbol x y NOME` | posição da porta; NOME = pino interno |
| `PortLabel x y [3] texto` | rótulo; `3` = alinhado à direita |
| `InstanceLabel`, `ClassLabel` | rótulos |

Convenção: L = 4800; entradas x=0, saídas x=L; y = 600, 1200, … (lacunas permitidas); A = maior y + 600; rótulos como acima.

Exemplo (`blocks/SHIFTLEFT2.sym`):

```
hades.symbols.BboxRectangle  0 0 4800 1200
hades.symbols.Rectangle  0 0 4800 1200
hades.symbols.PortLabel 4650 750 3 OUTPUT
hades.symbols.PortSymbol 4800 600 OUTPUT
hades.symbols.PortLabel 150 750 INPUT
hades.symbols.PortSymbol 0 600 INPUT
hades.symbols.InstanceLabel 150 1050 SHIFTLEFT2
hades.symbols.ClassLabel 150 450 SHIFTLEFT2
```

## Checklist

- [ ] Um pino por porta, nomes únicos.
- [ ] `.sym` com mesmo nome base, um `PortSymbol` por pino, nomes idênticos.
- [ ] Larguras no pai = larguras dos pinos.
- [ ] Caminho correto.
- [ ] Bloco genérico novo: adicionar em `blocks/` e em `blocks/README.md`.
