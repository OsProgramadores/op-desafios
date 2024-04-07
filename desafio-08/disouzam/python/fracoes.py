"""Processa um arquivo texto e simplifica frações
"""
from ctypes import ArgumentError
import os
import sys


def main(args):
    """main(args):
    Processa o arquivo texto passado como parâmetro contendo frações a serem analisadas e retorna
    no console 

    Parâmetros:
    args: Lista de argumentos recebido da linha de comando e
          pré-processado na chamada da função main. Deve conter 1 argumento apenas indicando
          o caminho relativo ou absoluto do arquivo contendo frações a serem analisadas.
    """
    # Análise dos argumentos recebidos em args
    nargs = len(args)
    if nargs == 0:
        raise ArgumentError("Nenhum argumento foi fornecido.")

    elementos_fracoes = []
    # Validação dos argumentos
    if nargs >= 1:
        caminho_do_arquivo_fracoes = args[0]

        if not os.path.isfile(caminho_do_arquivo_fracoes):
            mensagem1 = "Arquivo não encontrado. Caminho fornecido ou nome do arquivo incorreto."
            print(mensagem1)
            return

        with open(caminho_do_arquivo_fracoes, "r", encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha_processada = linha.split("\n")
                numerador_e_denominador = linha_processada[0].split("/")
                elementos_fracoes.append(numerador_e_denominador)

    if nargs >= 2:
        mensagem1 = f"Você informou um número excessivo de argumentos ({nargs}). "
        mensagem1 += "Apenas um argumento que aponte o caminho (relativo ou absoluto) "
        mensagem1 += "do arquivo contendo frações a serem processadas é necessário."
        print(mensagem1)

        mensagem2 = "Deseja prosseguir ignorando os demais argumentos? (S para Sim e N para não)"
        escolha_do_usuario = input(mensagem2)

        if escolha_do_usuario.lower() != "s":
            print("Programa abortado.")
            return

    fracoes_simples = obtem_fracoes_simples(elementos_fracoes)

    for fracao in fracoes_simples:
        print(fracao)


def obtem_fracoes_simples(elementos_fracoes):
    """obtem_fracoes_simples(elementos_fracoes):
    Processa uma lista contendo listas com elementos de frações e retorna uma lista de strings
    com as frações transformadas em frações simples, números inteiros ou ERR quando houver erro como
    por exemplo divisão por zero.

    Parâmetro:
    elementos_fracoes: Lista de listas onde cada sublista tem 1 ou 2 elementos, 1 quando é um número
                       inteiro, 2 quando existe numerador e denominador
    """
    fracoes_simples = []

    for fracao in elementos_fracoes:
        if len(fracao) == 1:
            fracoes_simples.append(str(fracao[0]))
        elif len(fracao) == 2:
            if int(fracao[1]) == 0:
                fracoes_simples.append("ERR")
            else:
                numerador = int(fracao[0])
                denominador = int(fracao[1])

                parte_inteira = int(numerador/denominador)
                resto = numerador % denominador

                if resto == 0:
                    fracoes_simples.append(str(parte_inteira))
                else:
                    mdc = obter_maximo_divisor_comum(resto, denominador)
                    resto = int(resto / mdc)
                    denominador = int(denominador / mdc)

                    if parte_inteira == 0:
                        fracao_como_string = f"{resto}/{denominador}"
                    else:
                        fracao_como_string = f"{parte_inteira} {resto}/{denominador}"
                    fracoes_simples.append(fracao_como_string)

    return fracoes_simples


def obter_maximo_divisor_comum(numero1, numero2):
    """obter_maximo_divisor_comum(numero1, numero2):
    Obtém o máximo divisor comum entre dois números

    Parâmetros:
    numero1, numero2: São números inteiros para os quais se busca o máximo divisor comum
    """
    if numero1 < numero2:
        menor = numero1
        maior = numero2
    else:
        menor = numero2
        maior = numero1

    mdc = 1
    divisor = 1
    while divisor <= menor:
        if menor % divisor == 0 and maior % divisor == 0:
            mdc = divisor
        divisor += 1

    return mdc


if __name__ == "__main__":
    filtered_args = sys.argv[1:]
    main(filtered_args)
