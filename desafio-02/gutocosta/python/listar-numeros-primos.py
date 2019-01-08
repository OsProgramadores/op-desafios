'''
    Programa para listar todos os números primos entre 1 e 10000
'''

import math

valor_limite = 10000
lista_num_int = [True for i in range(valor_limite+1)]
p = 2

while (p * p <= valor_limite):
    if (lista_num_int[p] == True):
        for i in range(p * 2, valor_limite+1, p):
            lista_num_int[i] = False
    p += 1

for p in range(2, valor_limite):
    if lista_num_int[p]: 
        print(p)