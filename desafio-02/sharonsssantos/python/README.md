# README

## Desafio 2 - Descrição

Este código implementa um algoritmo para encontrar todos os números primos até um determinado limite (10000). Ele utiliza um método otimizado, verificando a primalidade de um número apenas até sua raiz quadrada, o que melhora a eficiência, e consequentemente a sua agilidade de achar numeros primos.

A função **'primo'** recebe um número e verifica se ele é primo, retornando o próprio número se for, ou None caso contrário. O código então percorre todos os números de 2 até o limite definido e adiciona os primos encontrados à lista **'lista'**.

Modo de execução

Para rodar o código, execute o seguinte comando no terminal:

  ```pycon
  $ python d2.py
   ```

Isso imprimirá a lista de todos os números primos até o limite definido no código.

## Exemplo:
### Se o limite for 10

  ```pycon
  $ python d2.py
  [2, 3, 5, 7, ... ]