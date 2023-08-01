# Números Palíndromos em Java
## O que são Números Palíndromos?
Números palíndromos são aqueles que se mantêm inalterados quando lidos da mesma forma da esquerda para a direita ou da direita para a esquerda. Por exemplo, os números 121, 454, 2002 e 12321.

## Descrição:
Este é um script simples em Java que imprime todos os números palíndromos entre dois limites dados.

O objetivo é criar uma função que verifique se um número é palíndromo e, em seguida, imprimir todos esses números no intervalo fornecido entre os dois.

Esse projeto foi escrito na linguagem Java e utiliza a IDE Eclipse para desenvolvimento e execução do código.

## Como Funciona?
1. A função `ehPalindromo(numero)` : Verifica se o número fornecido é palíndromo ou não. Para isso, converte o em uma string e compara os caracteres do início ao fim, verificando se são iguais.
2. A função `imprimirPalindromos(inicio, fim)` : Recebe dois inteiros positivos como entrada, representando o início e o fim do intervalo. Ela itera entre os números no intervalo e imprime aqueles que são palíndromos, utilizando a função `ehPalindromo(numero)`.

## Como Executar o Projeto?
1. Instale o Java Development Kit (JDK) em sua máquina, caso ainda não o tenha feito.
2. Baixe e instale a IDE Eclipse, ou verifique se já a possui instalada em sua máquina.
3. Abra a IDE Eclipse e crie um novo projeto Java.
4. Copie o código fornecido no arquivo "NumerosPalindromicos.java" deste repositório e cole-o em uma classe no projeto criado.
5. Chame a função `imprimirPalindromos(inicio, fim)` no método `main()` do arquivo para encontrar e imprimir os números palíndromos no intervalo desejado.
6. Execute a classe que contém o código do projeto clicando com o botão direito do mouse sobre o arquivo e selecionando "Run As" (Executar Como) -> "Java Application" (Aplicativo Java).
