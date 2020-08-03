"""
Desafio 3 - Números palindrômicos

"""

def palindromo(valor_inicial=1, valor_final=100):
    """
    Retorna o número se ele for um palindrômo.
    """

    for i in range(valor_inicial, valor_final + 1):
        if i == int(str(i)[::-1]):
            print(i)


if __name__ == '__main__':
    palindromo()
