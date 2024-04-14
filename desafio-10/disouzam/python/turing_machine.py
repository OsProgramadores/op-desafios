"""Implementação de uma máquina de Turing
"""
from ctypes import ArgumentError
import os
import pathlib
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

    linhas_de_instrucao = []
    # Validação dos argumentos
    if nargs >= 1:
        arquivo_de_dados = args[0]

        if not os.path.isfile(arquivo_de_dados):
            mensagem1 = "Arquivo não encontrado. Caminho fornecido ou nome do arquivo incorreto."
            print(mensagem1)
            return

        caminho_do_arquivo_de_dados = pathlib.Path(arquivo_de_dados)
        pasta_raiz = caminho_do_arquivo_de_dados.parent
        with open(arquivo_de_dados, "r", encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha_processada = linha.split("\n")
                arquivo_de_regras_e_dados = linha_processada[0].split(",")
                linhas_de_instrucao.append(arquivo_de_regras_e_dados)

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

    for instrucao in linhas_de_instrucao:
        arquivo_regras = instrucao[0]
        dados = instrucao[1]

        caminho_do_arquivo_de_regras = os.path.join(
            pasta_raiz.absolute(), arquivo_regras)
        print(instrucao)
        print(caminho_do_arquivo_de_regras)
        print(dados)

        if not os.path.isfile(caminho_do_arquivo_de_regras):
            continue

        regras = obter_regras(caminho_do_arquivo_de_regras)

        for regra in regras:
            print(regra)


def obter_regras(caminho_do_arquivo):
    """obter_regras(caminho_do_arquivo):
    Obtém as regras a partir do arquivo indicado

    Parâmetro:
    caminho_do_arquivo: caminho do arquivo contendo as regras a serem aplicadas pela máquina de
                        Turing
    """
    regras = []

    if not os.path.isfile(caminho_do_arquivo):
        return regras

    with open(caminho_do_arquivo, "r", encoding='utf-8') as arquivo:
        for linha in arquivo:
            # Remove fim de linha
            linha_processada = linha.split("\n")
            linha_processada = linha_processada[0]

            # Remove comentários
            if ";" in linha_processada:
                posicao_comentario = linha_processada.index(";")
                linha_processada = linha_processada[0:posicao_comentario]

            # Linha vazia
            if len(linha_processada) == 0:
                continue

            # Remove espaços extras
            linha_processada = linha_processada.strip()

            linha_processada = linha_processada.split(" ")
            regra = linha_processada
            regras.append(regra)

    return regras


if __name__ == "__main__":
    filtered_args = sys.argv[1:]
    main(filtered_args)
