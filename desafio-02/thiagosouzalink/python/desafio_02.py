"""
Listando números primos.

Escreva um programa para listar todos os números primos entre 1 e 10000, na
linguagem de sua preferência.
"""
from math import sqrt


NUMBER = 10000

def verificar_numero_primo(num):
    """ Função que verifica se um determinado número é primo.

    Params:
        num: Número a ser verificado.

    Returns:
        Valor booleano validando a condição de ser ou não ser número primo.
    """
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    for n in range(1, NUMBER + 1):
        if verificar_numero_primo(n):
            print(n)
