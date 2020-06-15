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
cat tabuleiro_N.txt | ./chess
```

Onde `tabuleiro_N.txt` refere-se a um arquivo texto contendo a descrição do
tabuleiro no formato descrito pelo desafio.

Alternativamente pode-se executar somente o comando `./chess`, caso no qual a
descrição do tabuleiro será lida da entrada padrão. Caracteres não válidos 
para indicação das peças são ignorados.
