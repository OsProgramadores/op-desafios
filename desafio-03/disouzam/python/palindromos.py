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
    elif len(args) == 2:
        # pylint: disable=line-too-long
        print("Apenas um argumento foi fornecido. É necessário fornecer um limite inferior e um limite superior.")
        return
    elif len(args) == 3:
        limite_inferior = int(args[1])
        limite_superior = int(args[2])


if __name__ == "__main__":
    main(sys.argv)
