"""
    Processa uma palavra ou frase e retorna todas as combinações possíveis de anagramas com palavras
    presentes no arquivo desafio-06/disouzam/python/words.txt (cópia local do arquivo disponível em
    https://osprogramadores.com/desafios/d06/words.txt)
"""
from ctypes import ArgumentError
import sys


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
        if not e_valida(expressao):
            raise ArgumentError("Expressão contém caracteres inválidos")


def e_valida(expressao):
    """
        Verifica se a expressão fornecida como argumento contém caracteres inválidos
    """
    return True


if __name__ == "__main__":
    main(sys.argv)
