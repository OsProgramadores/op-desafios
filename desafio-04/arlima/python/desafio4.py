"""
Desafio 4 - Adriano Roberto de Lima
"""

def main():
    """
    Main Function
    """

    nomes = {1:"Peão", 2:"Bispo", 3:"Cavalo", 4:"Torre", 5:"Rainha", 6:"Rei"}
    pecas = dict()

    file = open("input.txt", "r")
    linhas = file.readlines()

    for linha in linhas:
        for peca in linha.split():
            pecas[int(peca)] = pecas.get(int(peca), 0) + 1

    for key, value in nomes.items():
        print(value, ":", pecas.get(key, 0), "peça(s)")

if __name__ == "__main__":
    main()
