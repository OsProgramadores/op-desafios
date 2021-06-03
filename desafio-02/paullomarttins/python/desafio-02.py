#!/usr/bin/python3
"""
Desafio 02, listando números primos de 1 até 10000
Para otimizar o loop e não percorrer todos os números do range utilizei um while
Optimized School Method [6n + 1 or 6n – 1]
"""

def num_primo(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i = i + 6
    return True

    #for valor in range(2, num):
    #    if num % valor == 0:
    #        return False
    #return True

if __name__ == "__main__":
    for valor in range(1, 10000):
        if(num_primo(valor)):
            print(valor)
