#!/usr/bin/python3
'''
Escreva um programa para listar todos os números np_primos entre 1 e 10000.
'''

from math import sqrt

num_primos = []

def np_primo(numero):
    '''
    Verificação de primalidade
    '''
    if  numero < 2:
        return False
    for i in range(2, int(sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

for num in range(2, 10000 + 1):
    if np_primo(num):
        num_primos.append(num)

print(num_primos)
