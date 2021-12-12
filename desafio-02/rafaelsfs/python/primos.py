"""
Autor: Rafael Garcia
#02 - Primos

## Desafio
Escrever um programa para listar todos os números primos entre 1 e 10000,
na linguagem de sua preferência.

## Objetivo
Listando números primos entre 1 e 10000.
"""

i = 1
while i <= 10000:
    if i == 2:
        print(f"{i}")
    if i == 3:
        print(f"{i}")
    else:
        x = 3
        while x < i:
            if i % x == 0:
                break
            x += 2
        if x == i:
            print(f"{x}")
    i += 1

