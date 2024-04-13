"""Implementação de uma máquina de Turing
"""
from ctypes import ArgumentError
import os
import sys


def main(args):
    """main(args):

    Parâmetros:
    args: Lista de argumentos recebido da linha de comando e
          pré-processado na chamada da função main. Deve conter 1 argumento apenas indicando
          o caminho relativo ou absoluto do arquivo contendo os dados para simulação da máquina
          de Turing
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
