# Números primos em JavaScript

O intuito código é analisar todos os números até 10000 para saber se são números primos.

## Como funciona?

O código é bem simples e intuitivo, primeiro temos uma função chamada númeroPrimos que recebe um parâmetro max(valor que quero analisar quais são primos entre certo valor e ele), dentro dessa função temos uma constante com uma array vazia que iremos colocar os valores que são primos, logo após a array temos um loop com uma variável num com valor inicial 2, onde caso num seja menor ou igual ao max ele irá atribuir true para esse valor, logo em seguida temos outro loop com uma variável divisor com valor inicial 2, que caso seja menor ou igual a raiz quadrada(arredondada) de num ele irá fazer uma verificação de num dividido por divisor resta 0, se sim vai atribuir a esse número o valor false e logo em seguida dar um break para finalizar o segundo loop. Após todas essas verificações um if dentro do primeiro loop irá verificar, se o numeroPrimo for true, caso seja true vai adicionar esse valor a array vazia no inicio da função e no final da função irá retornar essa array com os valores primos.

# Crivo de Eratótenes

## O que é

O Crivo de Eratóstenes é um algoritmo e um método simples e prático para encontrar números primos até um certo valor limite
