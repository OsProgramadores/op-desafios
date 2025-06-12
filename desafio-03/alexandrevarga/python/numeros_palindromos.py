"""Módulo para identificar números palíndromos em um intervalo.

Fornece funções para verificar se um número é palíndromo e para listar todos os
palíndromos em um intervalo especificado.
"""

import sys

def is_palindromo(num):
    """Verifica se um número é palíndromo."""
    s = str(num)
    return s == s[::-1]

def palindromos_entre(inicio, fim):
    """Retorna uma lista de números palíndromos dentro de um intervalo."""
    return [n for n in range(inicio, fim + 1) if is_palindromo(n)]

def ler_limite(mensagem):
    """Lê um número inteiro positivo do usuário ou permite sair com 'q'."""
    while True:
        entrada = input(mensagem)
        if entrada.lower() == 'q':
            print("Saindo do programa.")
            sys.exit(0)
        try:
            valor = int(entrada)
            if valor < 0:
                print("Erro: Não são permitidos números negativos como limites.")
            else:
                return valor
        except ValueError:
            print("Erro: Por favor, digite apenas números inteiros ou 'q' para sair.")

if __name__ == "__main__":
    print(
        "Este programa exibe todos os números palíndromos dentro de um intervalo "
        "informado pelo usuário."
    )
    print("Informe apenas números inteiros positivos para os limites ou 'q' para sair.\n")

    while True:
        minimo = ler_limite("Digite o número mínimo (ou 'q' para sair): ")
        maximo = ler_limite("Digite o número máximo (ou 'q' para sair): ")
        if minimo > maximo:
            print("Erro: O número mínimo não pode ser maior que o número máximo.")
        else:
            break

    resultado = palindromos_entre(minimo, maximo)
    if resultado:
        for palindromo in resultado:
            print(palindromo)
