"""Minha solução para imprimir todos os primos de 1 a 10000"""


def primos(n):
    """Aqui é feito a validação se um numero é primo"""
    raiz = int(n ** 0.5)
    for d in range(2, raiz + 1):
        if n % d == 0:
            return False
    return True


p = []
for x in range(1, 10001):
    if primos(x):
        p.append(x)

print(p)
