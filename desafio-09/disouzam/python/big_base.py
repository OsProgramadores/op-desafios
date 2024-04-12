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


if __name__ == "__main__":
    filtered_args = sys.argv[1:]
    main(filtered_args)
