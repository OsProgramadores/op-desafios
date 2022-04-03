# Desafio 02 - Números Primos

O exercício proposto pelo desafio é a geração de números primos dentro do intervalo fornecido

A solução apresentada consiste na implementação do [Crivo de Eratóstenes](https://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes) (sugestão do [@marcopaganini](https://github.com/marcopaganini)) em Java utilizando a classe [BitSet](https://docs.oracle.com/javase/9/docs/api/java/util/BitSet.html) e filtrando os valores do intervalo fornecido

## Requisitos

- Java 9 ou superior

## Compilação

```
javac EratosthenesPrimeNumbers.java
```

## Execução

- Com intervalo padrão (0 a 1000)
```
java -cp . EratosthenesPrimeNumbers
```

- Com intervalo definido (15 a 70)
```
java -cp . EratosthenesPrimeNumbers 15 70
```
