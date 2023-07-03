"""Numeros primos"""


def num_primo(numero):
    """funcao para encontrar o numero primo"""

    divisor = 0
    for i in range(1, 10000):
        if numero % i == 0:
            divisor += 1
    if divisor == 2:
        return 1
    return None

for primos in range(1, 10000):
    if num_primo(primos) == 1:
        print(primos)
