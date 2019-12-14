# primes

# Português

Solução para o desafio 2 (números primos) do site Os Programadores (acessível 
em http://osprogramadores.com/desafios).

Esta solução implementa o teste de primalidade simples (conforme descrito em 
https://en.wikipedia.org/wiki/Primality_test), e calcula os número primos de 
forma 'on-line' (o cálculos dos próximos números depende do cálculo dos números 
anteriores).

## Como utilizar

Para compilar o projeto é preciso ter o utilitário `cmake` instalado. A 
compilação é feita da seguinte forma:
```
cmake .
cmake --build .
```

Para executar o programa:
```
./primes
```

