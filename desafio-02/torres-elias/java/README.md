# Desafio 02 - Listando Números Primos

## Descrição
Um programa que lista todos os números primos entre 1 e 10000.

## Solução
A abordagem consiste em iterar somente sobre os números ímpares a partir de 3 (visto que o 2 é tratado separadamente e se trata do único primo par) verificando para cada candidato se ele possui algum divisor entre 3 e sua raiz quadrada. Caso nenhum divisor seja encontrado, o número é primo.

## Como executar
```bash
javac ListaPrimos.java
java ListaPrimos
```
