# pwr

Solução para o desafio 12 (potências de 2) do site
[Os Programadores](http://osprogramadores.com/).

O algoritmo é implementado por um teste inicial da divisibilidade do número por
potência de 2, que é feito através da contagem direta da quantidade de bits
setados na representação binária do número (que deve ser sempre igual a um).

A determinação do expoente necessário para a obtenção da potência de 2 é feita
pela contagem direta dos zeros à direita do algarismo 1 na representação binária
do número.

É utilizada a biblioteca num-bigint para implementação das operações
anteriormente descritas, de sorte que a solução pode ser considerada do tipo
"baunilha".

**TODO:**

- [ ] Implementar funcionalidade de "big integer", de forma a eliminar a
dependência de biblioteca externa.
- [ ] Implementar algoritmo de contagem de população eficiente, tipo SWAR,
sideways sum, ou outro.

## Comno utilizar

Compilar com o cargo:

```console
cargo build
```

Executar o binário gerado:

```conole
./target/debug/pwr filename.txt
```

Ajuda:

````console
$pwr --help

pwr 0.1.0

USAGE:
    pwr [OPTIONS] <FILENAME>

ARGS:
    <FILENAME>    files to load the numbers from, one per line

OPTIONS:
    -h, --help       Print help information
        --tabular    outputs a nicely formatted table with big numbers shortened
    -V, --version    Print version information
```
