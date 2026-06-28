# Desafio #02 - Primos

## Sobre o desafio
Listar todos os números primos entre 1 e 10.000.

## Linguagem
Java

## Versão do Java
OpenJDK 21.0.11 (LTS)

## Como executar

1. Compilar o código:
   ```bash
   javac Primos.java
   ```

2. Executar o programa:
   ```bash
   java Primos
   ```

O programa irá imprimir todos os números primos de 2 a 10.000, um por linha.

## Lógica utilizada

A verificação de primalidade foi extraída para o método `ehPrimo(int numero)`,
que testa divisores apenas até a **raiz quadrada** do número (`i * i <= numero`),
otimizando o algoritmo em relação à verificação até `numero - 1`.

Para cada número `i` de 2 a 10.000, chamamos `ehPrimo(i)`. Se retornar `true`,
o número é exibido na tela.
