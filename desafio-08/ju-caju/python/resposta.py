import sys


def mdc(a, b):
    a = abs(a)
    b = abs(b)

    while b != 0:
        resto = a % b
        a = b
        b = resto

    return a


def simplificar(numerador, denominador):
    if denominador == 0:
        return "ERR"

    if denominador < 0:
        numerador = -numerador
        denominador = -denominador

    sinal = ""

    if numerador < 0:
        sinal = "-"
        numerador = abs(numerador)

    divisor = mdc(numerador, denominador)

    numerador = numerador // divisor
    denominador = denominador // divisor

    parte_inteira = numerador // denominador
    resto = numerador % denominador

    if resto == 0:
        return sinal + str(parte_inteira)

    if parte_inteira == 0:
        return sinal + str(resto) + "/" + str(denominador)

    return sinal + str(parte_inteira) + " " + str(resto) + "/" + str(denominador)


def processar_linha(linha):
    linha = linha.strip()

    if linha == "":
        return "ERR"

    if linha.count("/") == 0:
        try:
            numero = int(linha)
            return str(numero)
        except:
            return "ERR"

    if linha.count("/") != 1:
        return "ERR"

    partes = linha.split("/")

    try:
        numerador = int(partes[0])
        denominador = int(partes[1])
    except:
        return "ERR"

    return simplificar(numerador, denominador)


def main():
    if len(sys.argv) > 1:
        arquivo = open(sys.argv[1], "r")
    else:
        arquivo = sys.stdin

    for linha in arquivo:
        print(processar_linha(linha))

    if len(sys.argv) > 1:
        arquivo.close()


main()