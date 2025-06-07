"""Módulo para identificar números palindrômicos em um intervalo.

Fornece funções para verificar se um número é palíndromo e para listar todos os
palíndromos em um intervalo especificado.
"""

def is_palindromo(num):
    """Verifica se um número é palíndromo.

    Args:
        num (int): Número a ser verificado.

    Returns:
        bool: True se o número for palíndromo, False caso contrário.
    """
    s = str(num)
    return s == s[::-1]

def palindromos_entre(inicio, fim):
    """Retorna uma lista de números palíndromos dentro de um intervalo.

    Args:
        inicio (int): Início do intervalo (inclusivo).
        fim (int): Fim do intervalo (inclusivo).

    Returns:
        list: Lista de números palíndromos no intervalo especificado.
    """
    resultado = []
    for n in range(inicio, fim + 1):
        if is_palindromo(n):
            resultado.append(n)
    return resultado

# Solicita os valores ao usuário
minimo = int(input("Digite o número mínimo: "))
maximo = int(input("Digite o número máximo: "))

# Exibe os palíndromos no intervalo informado
for palindromo in palindromos_entre(minimo, maximo):
    print(palindromo)
