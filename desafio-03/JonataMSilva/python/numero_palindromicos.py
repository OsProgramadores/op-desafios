"""
Números palindrômicos

Solução de Jonata M Silva
Github: https://github.com/JonataMSilva
"""
inicial = 1
final = 65


def numero_palindromico():
    """função para buscar os numeros palindrômicos em um range"""
    for numero in range(inicial, final):
        if str(numero)[-1] == str(numero)[0]:
            print(numero)


numero_palindromico()
