# primes

# Português

Solução para o desafio 3 (palíndromos) do site Os Programadores (acessível 
em http://osprogramadores.com/desafios). Mostra todos os palíndromos decimais 
dentro de uma determinada faixa.

## Como utilizar

Para compilar o projeto é preciso ter o utilitário `cmake` instalado. A 
compilação é feita da seguinte forma:
```
cmake .
cmake --build .
```

Para executar o programa:
```
./palin INICIAL FINAL
```
Onde INICIAL e FINAL referem-se aos números da faixa que será buscada por 
palíndromos (inclusive).

É possível utilizar uma outra base numérica utilizando a opção '-b', porém 
como a busca é feita por palíndromos decimais, os resultados ainda são 
exibidos como números de base 10.

