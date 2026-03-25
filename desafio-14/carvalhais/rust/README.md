# solver

Solução para o desafio 14 (expressões numéricas) do site
[Os Programadores](http://osprogramadores.com/).

Resolvedor de expressões matemáticas com implementação própria do algoritmo da
jarda de manobras de Edsger Wybe Dijkstra.

## Comno utilizar

Compilar com o cargo:

```console
cargo build
```

Executar o binário gerado:

```console
./target/debug/solver filename.txt
```

Ajuda:

````console
$solver --help

solver 0.1.0
André Carvalhais

USAGE:
    solver <FILENAME>

ARGS:
    <FILENAME>    files to load expressions from, one per line

OPTIONS:
    -h, --help       Print help information
    -V, --version    Print version information
```
