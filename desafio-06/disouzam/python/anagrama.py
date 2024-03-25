"""
    Processa uma palavra ou frase e retorna todas as combinações possíveis de anagramas com palavras
    presentes no arquivo desafio-06/disouzam/python/words.txt (cópia local do arquivo disponível em
    https://osprogramadores.com/desafios/d06/words.txt)
"""
from ctypes import ArgumentError
import string
import sys
import re


def main(args):
    """
        Processa os valores passados na linha de comando, descritos pelo parâmetro args
        e retorna todos os palíndromos entre o limite inferior e o limite superior, ambos
        inclusos na avaliação de números palíndromos
    """
    expressao = ""

    # Análise dos argumentos recebidos em args
    if len(args) <= 1:
        print("Nenhum argumento foi fornecido.")
        return

    if len(args) == 2:
        expressao = args[1]
        expressao = converte_expressao(expressao)
        if not e_valida(expressao):
            raise ArgumentError("Expressão contém caracteres inválidos")

    print(converte_expressao(expressao))


def converte_expressao(expressao):
    """
        Converte expressão para letras maiúsculas e remove os espaços existentes
    """
    # Primeiro converte todas as letras em maiúsculas
    result = expressao.upper()

    # pylint: disable=line-too-long
    # Depois remove os espaços em branco https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string#remove-all-spaces-using-the-replace-method
    result = result.replace(" ", "")

    return result


def e_valida(expressao):
    """
        Verifica se a expressão fornecida como argumento contém caracteres inválidos
    """
    # https://www.geeksforgeeks.org/string-punctuation-in-python/
    for letra in expressao:
        if letra in string.punctuation:
            return False

    # https://stackoverflow.com/a/22162423
    if not re.match('^[a-zA-Z]+$', expressao):
        return False

    return True


if __name__ == "__main__":
    main(sys.argv)
