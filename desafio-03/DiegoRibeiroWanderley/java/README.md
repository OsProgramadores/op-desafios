# Palíndromos de números naturais

O seguinte programa é um algoritmo capaz de identificar os palíndromos em um 
intervalo fornecido pelo usuário.

Palíndromos são palavras, nesse caso números, que tem a mesma forma se invertidos,
nesse caso 101 é palíndromo, já que seu inverso é 101.

# Como funciona

O programa funciona percorrendo o espaço entre os dois números fornecidos, eles
inclusos, e verificando se esse número é palíndromo.

A verificação ocorre da seguinte forma:

1. Começa um for com `int i = numeroComeco` até que `i >= numeroFim`
2. Para cada iteração cria uma variavel `numeroInvertido`, começando em 0 e `numeroTemporario` que recebe `i`
3. Entra no while e só sai de o `numeroTemporario` for menor ou igual a 0;
4. Dentro do while cria uma variável `ultimoDigito`, que recebe o ultimo digito de `numeroTemporario` com ajuda da operação módulo
5. Adiciona em `numeroInvertido` o produto dele mesmo com 10 somado com o último dígito
6. Divide `numeroTemporario` por 10 a fim de retirar seu último algarismo
7. Repete o loop se a condição for verdadeira
8. Ao fim, compara se `i == numeroInvertido`
9. Se sim, imprime na tela

# Tecnologias utilizadas

Linguagem: Java 11+

# Execução

Para rodar o programa, basta seguir os seguintes passos:

1. Esteja no diretório onde a classe se encontra
2. Rode no terminal:
```bash
$ java MeuPrograma.java numero_1 numero_2
```
# Saída

Ao executar o programa você verá uma lista dos números palíndromos no intervalo escolhido

Ex.: Se o intervalo for de 1000 a 1200 
```java
1001
1111
