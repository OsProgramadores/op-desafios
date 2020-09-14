"""Função que fala se numero é primo feita por @otaru1921"""

def primo_numero(num):
    """Diz se é número primo"""
    if num < 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False

    print(num, "é um número primo")
    return True


for number in range(1, 10001):
    primo_numero(number)
