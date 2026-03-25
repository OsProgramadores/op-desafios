"""
Desafio 9 - Adriano Roberto de Lima
"""

import string
import sys

DIGITOS = list(string.digits + string.ascii_uppercase + string.ascii_lowercase)

def convertebase10basen(basedest, numero):
    """
    Convertebase10basen converte um numero na base 10 para uma string
    representando o numero na base N
    """
    ret = ""
    while True:
        digit = numero%basedest
        ret = ret + DIGITOS[digit]
        numero = numero // basedest
        if numero == 0:
            break
    return ret[::-1]

def convertebasenbase10(baseorig, numero):
    """
    Convertebasenbase10 converte uma string em uma base N para um numero
    na base 10
    """
    base10 = 0
    for i in range(len(numero)-1, -1, -1):
        base10 += DIGITOS.index(numero[i]) * baseorig**(len(numero)-i-1)

    return base10


def valida(baseorig, basedest, numero):
    """
    Valida uma string para conversão entre base origem e destino
    """
    if baseorig < 2 or baseorig > 62:
        return False

    if basedest < 2 or basedest > 62:
        return False

    for i in numero:
        if i not in DIGITOS:
            return False

    for i in numero:
        if DIGITOS.index(i) >= baseorig:
            return False

    return True

def main():
    """
    Main Function
    """

    maxnumber = convertebasenbase10(62, "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")

    if len(sys.argv) < 2:
        print("Erro ! Sintaxe: python desafio9.py nomedoarquivo")
        sys.exit(0)

    try:
        file = open(sys.argv[1], "r")
    except IOError:
        print("Não consegui abrir o arquivo", sys.argv[1])
        sys.exit(0)

    linhas = file.readlines()

    for linha in linhas:
        dados = linha.split(" ")

        try:
            baseorig = int(dados[0])
            basedest = int(dados[1])
            numero = dados[2].rstrip()
        except IndexError:
            print("???")
            continue

        if not valida(baseorig, basedest, numero):
            print("???")
            continue

        base10 = convertebasenbase10(baseorig, numero)

        if base10 > maxnumber:
            print("???")
            continue

        print(convertebase10basen(basedest, base10))

    file.close()

if __name__ == "__main__":
    main()
