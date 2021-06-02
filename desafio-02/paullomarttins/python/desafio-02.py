#!/usr/bin/python3
"""
Desafio 02, listando números primos de 1 até 10000!
"""
def num_primo(num):
    for valor in range(2, num):
        if num % valor == 0:
            return False
    return True

for valor in range(2, 10000):
    if(num_primo(valor)):
        print(valor)
