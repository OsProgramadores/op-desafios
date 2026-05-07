import sys


def verificar_potencia_de_2(texto):
    try:
        numero = int(texto)
    except:
        return texto + " false"

    if numero < 1:
        return texto + " false"

    expoente = 0
    valor = numero

    while valor > 1 and valor % 2 == 0:
        valor = valor // 2
        expoente = expoente + 1

    if valor == 1:
        return texto + " true " + str(expoente)

    return texto + " false"


def main():
    if len(sys.argv) > 1:
        arquivo = open(sys.argv[1], "r")
    else:
        arquivo = sys.stdin

    for linha in arquivo:
        linha = linha.strip()

        if linha != "":
            print(verificar_potencia_de_2(linha))

    if len(sys.argv) > 1:
        arquivo.close()


main()