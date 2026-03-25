"""
Calcula os números primos entre 1 e 10.000
"""


import math


def fast_prime(numero):
    """O fast_prime é um algoritmo que verifica se um número é primo."""
    if numero == 1:
        return False

    if numero == 2:
        return True

    if numero % 2 == 0:
        return False

    x_square_root = int(math.ceil(math.sqrt(numero)))
    for i in range(3, x_square_root, 2):
        if numero % i == 0:
            return False

    return True


for j in range(1, 10001):
    if fast_prime(j):
        print(j)
