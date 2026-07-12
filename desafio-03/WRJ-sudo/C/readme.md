# Algoritmo para exibir números Palíndromos

## Descrição
Este algoritmo é capaz de encontrar todos os números palíndromos com até 64 bits.

Um palíndromo é uma palavra ou expressão que pode ser lida da esquerda para a direita ou da direita para a esquerda mantendo o mesmo significado. 

Neste programa lidamos apenas como os números inteiros.

Exemplo de um número inteiro palíndromo: 101. Se lermos o número da direita para a esquerda obteremos o mesmo valor, 101.

## Requisitos
-Possuir o GCC ou outro compilador para linguagem C instalado no sistema operacional.
Para a execução do código é preciso acessar o terminal e digitar o comando `gcc nomedoprograma.c -o nomeparaobject'`

## Lógica do Algoritmo
-É recebido da entrada dois valores arbitrários, o primeiro interpretado como ponto de partida e o segundo como o ultimo número a comparar.
-Para fazer a comparação do número com o seu "espelho" é feito uma conversão do inteiro para um vetor de char.

- É utilizado dois vetores do tipo char onde:
  - O primeiro vetor `str_lida` armazena o número que vai ser comparado.
  - O segundo vetor `str_a_acomparar` armazena o mesmo número lido da direita para esquerda.  

- Comparação dos vetores:
  - Para comparação do vetores é feito um casting para uma comparação direta de números inteiros.
  - Apos a conversão o programa compara os dois valores e exibe o resultado para o usuário.
    