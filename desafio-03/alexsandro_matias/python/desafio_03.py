""" Desafio 03 """

def percorre_intervalo(inicio, fim):
    """ Função que percorre o intervalo determinado no início do programa."""
    for numero in range(inicio, fim):
        imprime_palindromo(numero)

def imprime_palindromo(numero_original):
    """ Função que verifica se o número é palíndromo ou não. """
    numero_original = str(numero_original)
    invertido = numero_original[::-1]
    if numero_original == invertido:
        print(numero_original)

# início do programa.
percorre_intervalo(3000, 3010)
