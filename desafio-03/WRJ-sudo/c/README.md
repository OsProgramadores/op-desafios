# Desafio-03 - Números Palíndromos

## Descrição

Este algoritmo é capaz de encontrar todos os números palíndromos com até 64 bits.

Um palíndromo é uma palavra ou expressão que pode ser lida da esquerda para a direita ou da direita para a esquerda mantendo o mesmo significado.

Neste programa lidamos apenas como os números inteiros.

Exemplo de um número inteiro palíndromo: 101. Se lermos o número da direita para a esquerda obteremos o mesmo valor, 101.

## Instruções

Para que este algoritmo execute de forma adequada é preciso que todas as instruções e requisitos aqui expostos sejam seguidos.

## Requisitos

É priciso que seu sistema operacional suporte o compilador GCC.

## Requisitos Para Executar O Programa No Windows

1. Faça um **fork** deste repositório para que você tenha uma cópia do mesmo na sua conta do github.

1. Dê um `git clone` do repositório em que você fez o fork para sua maquina.

1. Instale o compilador [GCC](https://sourceforge.net/projects/mingw-w64/) em seu sistema operacional.

1. Certifique eu o GCC foi instalado corretamenta em sua máquina com o comando: `gcc --version`

## Como Executar o arquivo desafio-03.c

1. Crie o arquivo objeto do programa com o comando:

```
gcc desafio-03.c -o meu_programa
```

1. Execute o comando `./meu_programa` se seu sistema operacional for Linux e `meu_programa.exe` para Windows.

## Lógica Do Algoritmo

-É recebido da entrada dois valores arbitrários, o primeiro interpretado como ponto de partida e o segundo como o ultimo número a comparar.
-Para fazer a comparação do número com o seu "espelho" é feito uma conversão do inteiro para um vetor de char.

- É utilizado dois vetores do tipo char onde:
  - O primeiro vetor `str_lida` armazena o número que vai ser comparado.
  - O segundo vetor `str_a_acomparar` armazena o mesmo número lido da direita para esquerda.

- Comparação dos vetores:
  - Para comparação do vetores é feito um casting para uma comparação direta de números inteiros.
  - Apos a conversão o programa compara os dois valores e exibe o resultado para o usuário.
