"""Processa um arquivo texto e transforma o número de uma base em outra"""
from ctypes import ArgumentError
import os
import sys


def main(args):
    """main(args):
    Processa o arquivo texto passado como parâmetro contendo a base de entrada e a base de saída e
    o número na base de entrada a ser convertido na base de saída e exibe o resultado
    no console

    Parâmetros:
    args: Lista de argumentos recebido da linha de comando e
          pré-processado na chamada da função main. Deve conter 1 argumento apenas indicando
          o caminho relativo ou absoluto do arquivo contendo linhas com bases de entrada e saída e
          números para converter na base de saída.
    """
    # Análise dos argumentos recebidos em args
    nargs = len(args)
    if nargs == 0:
        raise ArgumentError("Nenhum argumento foi fornecido.")

    elementos_para_conversao = []
    # Validação dos argumentos
    if nargs >= 1:
        caminho_do_arquivo_conversao_base = args[0]

        if not os.path.isfile(caminho_do_arquivo_conversao_base):
            mensagem1 = "Arquivo não encontrado. Caminho fornecido ou nome do arquivo incorreto."
            print(mensagem1)
            return

        with open(caminho_do_arquivo_conversao_base, "r", encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha_processada = linha.split("\n")
                elementos_entrada = linha_processada[0].split(" ")
                elementos_para_conversao.append(elementos_entrada)

    if nargs >= 2:
        mensagem1 = f"Você informou um número excessivo de argumentos ({nargs}). "
        mensagem1 += "Apenas um argumento que aponte o caminho (relativo ou absoluto) "
        mensagem1 += "do arquivo contendo as bases e o número a ser convertido é necessário."
        print(mensagem1)

        mensagem2 = "Deseja prosseguir ignorando os demais argumentos? (S para Sim e N para não)"
        escolha_do_usuario = input(mensagem2)

        if escolha_do_usuario.lower() != "s":
            print("Programa abortado.")
            return

    for elemento_a_converter in elementos_para_conversao:
        base_entrada = int(elemento_a_converter[0])
        base_saida = int(elemento_a_converter[1])
        numero_a_converter = elemento_a_converter[2]
        numero_convertido = obter_numero_convertido(
            base_entrada, numero_a_converter, base_saida)
        print(numero_convertido)


def obter_numero_convertido(base_entrada, numero_entrada, base_saida):
    """obter_numero_convertido(base_entrada, numero_entrada, base_saida):
    Converte um número de entrada na base de entrada em um número correspondente na base de saída
    e retorna o número convertido ou "???" se acontecer um erro

    Parâmetros:
    base_entrada: base na qual o número de entrada está representado. Valores entre 2 e 62
    numero_entrada: número a ser convertido
    base_saida: o número convertido deve estar nessa base. Valores entre 2 e 62
    """
    valor_para_erro = "???"
    if base_entrada < 2 or base_entrada > 62:
        return valor_para_erro

    if base_saida < 2 or base_saida > 62:
        return valor_para_erro

    if "-" in numero_entrada:
        return valor_para_erro

    if len(numero_entrada) == 1 and numero_entrada[0] == "0":
        return "0"

    numero_entrada = numero_entrada[::-1]
    elementos_numero_entrada = list(numero_entrada)

    elementos_base_entrada = obtem_elementos_da_base(base_entrada)
    elementos_base_saida = obtem_elementos_da_base(base_saida)

    total_em_base_10 = 0
    for posicao, elemento in enumerate(elementos_numero_entrada):
        if elemento not in elementos_base_entrada:
            return valor_para_erro
        valor_elemento = elementos_base_entrada.index(elemento)
        total_em_base_10 += valor_elemento * pow(base_entrada, posicao)

    if total_em_base_10 > 591222134364399413463902591994678504204696392694759423:
        return valor_para_erro

    numero_convertido = []
    numero_remanescente = total_em_base_10
    while numero_remanescente >= base_saida:
        resto = numero_remanescente % base_saida
        numero_remanescente = numero_remanescente // base_saida
        elemento = elementos_base_saida[resto]
        numero_convertido.append(elemento)

    if numero_remanescente != 0:
        elemento = elementos_base_saida[numero_remanescente]
        numero_convertido.append(elemento)

    numero_convertido = numero_convertido[::-1]
    numero_convertido = ''.join(numero_convertido)

    return numero_convertido


def obtem_elementos_da_base(base):
    """obtem_elementos_da_base(base):
    Obtém os elementos que fazem parte da base

    Parâmetro:
    base: base selecionada (valores entre 2 e 62)
    """
    elementos_possiveis = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    elementos_da_base = []

    if base >= 2 and base <= 62:
        subconjunto = elementos_possiveis[0:base]
        elementos_da_base = list(subconjunto)

    return elementos_da_base


if __name__ == "__main__":
    filtered_args = sys.argv[1:]
    main(filtered_args)
