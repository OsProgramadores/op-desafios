Números Palindrômicos em C

Este programa identifica e lista todos os números palindrômicos dentro de um intervalo.

A solução foi desenvolvida em C utilizando lógica matemática para inverter os números:
1.O programa recebe dois valores de entrada (início e fim do intervalo).
2.Para cada número no intervalo, uma função inverte o valor usando o resto da divisão por 10 (`% 10`) e multiplicações sucessivas.
3.Se o número original for igual ao número invertido, ele é impresso na tela.
4.Foi utilizado o tipo `unsigned long long` para garantir compatibilidade com números grandes, conforme sugerido no desafio.

Necessário ter o compilador `gcc` instalado em seu ambiente. No terminal, execute:
gcc palindromos.c -o palindromos