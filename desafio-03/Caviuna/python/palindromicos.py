""" O Programa determina se o número é palindromico. """

import math


numero_inicial = int(input("Digite o número inicial: "))
numero_final = int(input("Digite o número final: "))

def rev(num):
    """ Determina a reversão de um número inteiro. """

    return int(num != 0) and ((num % 10) * (10**int(math.log(num, 10))) + rev(num // 10))
for i in range(numero_inicial, numero_final):
    if i == rev(i):
        print(i)
