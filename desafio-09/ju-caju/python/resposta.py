# bigbase.py
import sys


DIGITOS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
LIMITE = 62 ** 30 - 1


def valor_do_digito(caractere):
    for i in range(len(DIGITOS)):
        if DIGITOS[i] == caractere:
            return i

    return -1


def converter_para_decimal(numero, base):
    valor = 0

    if numero == "":
        return None

    if numero[0] == "-":
        return None

    for caractere in numero:
        digito = valor_do_digito(caractere)

        if digito == -1:
            return None

        if digito >= base:
            return None

        valor = valor * base + digito

        if valor > LIMITE:
            return None

    return valor


def converter_de_decimal(numero, base):
    if numero == 0:
        return "0"

    resultado = ""

    while numero > 0:
        resto = numero % base
        resultado = DIGITOS[resto] + resultado
        numero = numero // base

    return resultado


def processar_linha(linha):
    partes = linha.strip().split()

    if len(partes) != 3:
        return "???"

    try:
        base_entrada = int(partes[0])
        base_saida = int(partes[1])
    except:
        return "???"

    numero_entrada = partes[2]

    if base_entrada < 2 or base_entrada > 62:
        return "???"

    if base_saida < 2 or base_saida > 62:
        return "???"

    numero_decimal = converter_para_decimal(numero_entrada, base_entrada)

    if numero_decimal is None:
        return "???"

    return converter_de_decimal(numero_decimal, base_saida)


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