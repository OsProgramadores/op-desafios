"""Módulo para identificar números palindrômicos em um intervalo.

Fornece funções para verificar se um número é palíndromo e para listar todos os
palíndromos em um intervalo especificado.
"""

import sys

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
    return [n for n in range(inicio, fim + 1) if is_palindromo(n)]

if __name__ == "__main__":
    print(
        "Este programa exibe todos os números palíndromos dentro de um intervalo "
        "informado pelo usuário."
    )
    print("Informe apenas números inteiros positivos para os limites.\n")

    try:
        minimo = int(input("Digite o número mínimo: "))
        maximo = int(input("Digite o número máximo: "))
    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros.")
        sys.exit(1)

    if minimo < 0 or maximo < 0:
        print("Erro: Não são permitidos números negativos como limites.")
        sys.exit(1)
    if minimo > maximo:
        print("Erro: O número mínimo não pode ser maior que o número máximo.")
        sys.exit(1)

    # Exibe os palíndromos no intervalo informado
    resultado = palindromos_entre(minimo, maximo)
    if resultado:
        for palindromo in resultado:
            print(palindromo)
    else:
        print("Nenhum número palíndromo encontrado no intervalo informado.")
