"""
Autor: Roberto Arruda
#02 - Primos

## Desafio
Escrever um programa para listar todos os números primos entre 1 e 10000,
na linguagem de sua preferência.

## Objetivo
Listando números primos entre 1 e 10000.
"""
for num in range(1, 10000 + 1):
    for n in range(2, num):
        if num % n == 0:
            break
    else:
        print("{} é primo".format(num), end='\n')
