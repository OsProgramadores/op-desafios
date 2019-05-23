
""" Retorna os valores primos de 1 a 10000 """


import math


def fast_prime(numero):
    """Função de retorno rapido de números primos"""
    if numero == 1:
        return False

    if numero == 2:
        return True

    if numero % 2 == 0:
        return False

    maiorraiz = int(math.ceil(math.sqrt(numero)))
    #    Recebe o maior valor da raiz quadrada do numero
    #    Caso queira saber mais sobre o ceil:
    #    https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Math/ceil

    for i in range(3, maiorraiz, 2):
        if numero % i == 0:
            return False

    return True


print(1)
for j in range(1, 10001):
    if fast_prime(j):
        print(j)
