"""
Números palindrômic2os

Solução de Jonata M Silva
Github: https://github.com/JonataMSilva
"""
inicial = input("digite o numero inicial")
final = input("digite o numero final")


def numero_palindromico():
    """função para buscar os numeros palindrômicos em um range e armazenar em uma lista vazia"""
    palindromico = []
    for numero in range(int(inicial), int(final)):
        if str(numero)[-1] == str(numero)[0]:
            palindromico.append(numero)
    return palindromico


print(numero_palindromico())
