"""
    Verifica quais os números palíndromos entre dois números fornecidos,
    extremos inclusos na pesquisa
"""
import sys


def main(args):
    """
        Processa os valores passados na linha de comando, descritos pelo parâmetro args
        e retorna todos os palíndromos entre o limite inferior e o limite superior, ambos
        inclusos na avaliação de números palíndromos
    """
    limite_inferior = 0
    limite_superior = 0

    # Análise dos argumentos recebidos em args
    if len(args) <= 1:
        print("Nenhum argumento foi fornecido.")
        return

    if len(args) == 2:
        # pylint: disable=line-too-long
        print("Apenas um argumento foi fornecido. É necessário fornecer um limite inferior e um limite superior.")
        return

    if len(args) == 3:
        limite_inferior = int(args[1], 10)
        limite_superior = int(args[2], 10)
    else:
        print(f"Número incorreto de argumentos. Esperados 2 argumentos mas foram recebidos {
              len(args) - 1}")
        return

    lista_de_palindromos = []
    if limite_inferior != 0 and limite_superior != 0:
        lista_de_palindromos = obter_todos_palindromos(
            limite_inferior, limite_superior)

    lista_concatenada = ','.join(lista_de_palindromos)
    print(lista_concatenada)


def obter_todos_palindromos(limite_inferior, limite_superior):
    """
        Obtém todos os palíndromos entre limite inferior e limite superior e
        retorna todos numa lista
    """
    lista_de_palindromos = []

    for numero in range(limite_inferior, limite_superior + 1, 1):
        if e_palindromo(numero):
            lista_de_palindromos.append(str(numero))

    return lista_de_palindromos


def e_palindromo(numero):
    """
        Verifica se o número é palíndromo ou não
    """
    numero_como_string = str(numero)

    # Reference: https://realpython.com/reverse-string-python/
    numero_como_string_invertido = numero_como_string[::-1]

    result = numero_como_string == numero_como_string_invertido
    return result


if __name__ == "__main__":
    main(sys.argv)
