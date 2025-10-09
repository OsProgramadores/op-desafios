# Desafio 02

Este exercício faz parte dos desafios de OsProgramadores

## Enunciado:

> Escreva um programa para listar todos os números primos
> entre 1 e 10000, na linguagem de sua preferência.

link: https://osprogramadores.com/desafios/d02/

## Solução implementada:

A função `eh_primo()` primeiro verifica se o número recebido é primo
da seguinte forma:

1. Se o número for igual a 2, considera-o como primo desde já.
   Isso é útil no passo 3.
2. Se o número for menor que 2 ou o número for par, considera-o como
   não primo desde já. Isso evita mais processamento desnecessário.
3. Percorre a lista de números primos já encontrados em iterações
   anteriores da função (lista de valores iniciada com o passo 1).
   1. Se o valor do divisor ficar mais alto do que a raiz quadrada
      do número que está sendo testado, sai do loop e considera este
      número como primo.
   2. Do contrário, testa a divisão do número pelo divisor e, se o
      resto for igual a zero, então não é primo.

Observação:
1. Optei por considerar na função a entrada de iteração anterior
   porque o enunciado deixa claro que vai ser executado de 1 a 10000.
   Se houvesse necessidade expressa de executar apenas um número
   específico, então seria necessidade de mudar a implementação.
2. Outro motivo de usar como entrada da função a lista de primos
   obtidos até então é que a divisão pode ser feita por primos ao
   invés de percorrer todos os valores. Me baseei isso na fala
   _Sempre que um número natural for composto (isto é, não-primo),
   ele vai ser divisível por um número **primo** menor que ou igual
   ao valor da sua raiz quadrada_, do Prof. Demóclis Rocha em
   https://youtu.be/gXV2iIeVR9g?t=24.
