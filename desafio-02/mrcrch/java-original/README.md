# Desafio 02 - Números Primos

O exercício proposto pelo desafio é a geração de números primos dentro do intervalo fornecido

A solução apresentada consiste na implementação da geração dos números através de _força bruta_ com algumas otimizações pelo caminho como geração de tabela intermediária de números compostos, iteração de 2 em 2 a partir de números primos e assim por diante.

## Requisitos

- Java 8 ou superior

## Compilação

```
javac PrimeNumbers.java
```

## Execução

- Com intervalo padrão (0 a 1000)
```
java -cp . PrimeNumbers
```

- Com intervalo definido (15 a 70)
```
java -cp . PrimeNumbers 15 70
```
