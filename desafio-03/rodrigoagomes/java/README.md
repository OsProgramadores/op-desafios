#DESAFIO 03

Números palindrômicos.

Um palíndromo é uma palavra ou expressão que pode ser lida da esquerda para a direita ou da direita para a esquerda mantendo o mesmo significado. Um exemplo de palíndromo é a palavra “reviver”.

Neste desafio, a idéia é imprimir todos os números palindrômicos entre dois outros números. Tal como as palavras, os números palindrômicos mantém o mesmo valor se lidos de trás para a frente.

Exemplo 1: Dado o número inicial 1 e número final 20, o resultado seria: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11.

Exemplo 2: Dado o numero inicial 3000 e número final 3010, o resultado seria: 3003.

Para o desafio, assuma:

Apenas inteiros positivos podem ser usados como limites.
Números de um algarismo são palíndromos por definição.
Máximo número: (1 << 64) - 1 (máximo unsigned int de 64 bits).
Bônus: Se o desafio parece fácil demais, implemente um novo tipo de dados para calcular pra qualquer número com precisão arbitrária (limite: 100000 algarismos por número). O uso de bibliotecas matemáticas de precisão arbitrária não será considerado como uma solução válida.


#Compilação:

javac Palindromes.java

#Execução:
java Palindromes #numeroInicial #numeroFinal

onde #numeroInicial e #numeroFinal devem ser números inteiros positivos entre 1 e 9223372036854775807.
e #numeroInicial não pode ser maior que #numeroFinal

#Exemplos execução:
java Palindromes 1 10000

java Palindromes 3000 1000000