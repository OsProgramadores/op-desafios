"""
Listando números primos

Escreva um programa para listar todos os números primos entre 1 e 10000, 
na linguagem de sua preferência.
"""

import sys

def search_primes(n):
    
    # Aumentando o limite de recursão, por padrão é 1000.
    sys.setrecursionlimit(10500)
    
    # Variável para checar se o número é primo
    prime = 0
    
    # O programa vai checar até 10000.
    if n == 10000:
        return 0
 
    for c in range(1, n + 1):
        if n % c == 0:
            prime += 1

    # Caso o número seja primo, será printado aqui.    
    if prime == 2:
        print(f'[{n}]', end='')
    
    # Função recursiva, chamando ela mesma como número sendo incrementado +1.
    search_primes(n + 1)        
        
if __name__ == '__main__':
    search_primes(1)
