"""
Números palindrômicos

Solução de Jonata M Silva
Github: https://github.com/JonataMSilva
"""
inicial = input("digite o numero inicial: ")
final = input("digite o numero final: ")


def numero_palindromico():
    """função para buscar os numeros palindrômicos em um range e armazenar em uma lista vazia"""
    palindromico = []
    for numero in range(int(inicial), int(final)+1):
        if str(numero) == str(numero)[::-1]:
            palindromico.append(numero)
    return palindromico


print(numero_palindromico())
