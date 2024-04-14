"""Implementação de uma máquina de Turing
"""
from ctypes import ArgumentError
import dataclasses
import os
import pathlib
import sys
from typing import List


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

        if not os.path.isfile(caminho_do_arquivo_de_regras):
            continue

        regras = obter_regras(caminho_do_arquivo_de_regras)
        resultado = processa_dados(regras, dados)
        print(f"{arquivo_regras},{dados},{resultado}")


def processa_dados(regras, dados):
    """processa_dados(regras, dados):
    Processa os dados usando as regras fornecidas e devolve uma string que representa o resultado

    Parâmetro:
    regras: Lista de regras para alterar o estado da máquina de Turing e executar transformações
            sobre os dados
    dados: Informação que será consumida pela máquina de Turing
    """
    resultado = ''
    espaco_vazio = " "
    lista_de_dados = list(dados)

    # Define o estado inicial da máquina de Turing
    estado_da_maquina_de_turing = '0'

    # Initializa a posicao de leitura dos dados
    posicao_de_leitura = 0

    while 'halt' not in estado_da_maquina_de_turing:
        simbolo_atual = lista_de_dados[posicao_de_leitura]

        regra_do_estado_atual: List[regra_da_maquina_de_turing] = [
            r for r in regras if r.estado_atual == estado_da_maquina_de_turing or r.estado_atual == "*"]

        if len(regra_do_estado_atual) == 1:
            regra = regra_do_estado_atual[0]
        else:
            simbolo_atual_modificado = simbolo_atual
            if simbolo_atual == espaco_vazio:
                simbolo_atual_modificado = "_"

            regra_especifica: List[regra_da_maquina_de_turing] = [
                r for r in regra_do_estado_atual if r.simbolo_atual == simbolo_atual_modificado]

            regra_geral: List[regra_da_maquina_de_turing] = [
                r for r in regra_do_estado_atual if r.simbolo_atual == "*"]

            if len(regra_especifica) == 1:
                regra = regra_especifica[0]
            elif len(regra_geral) == 1:
                regra = regra_geral[0]
            elif len(regra_especifica) == 0 and len(regra_geral) == 0:
                return "ERR"

        estado_da_maquina_de_turing = regra.novo_estado

        if regra.novo_simbolo != "*" and regra.novo_simbolo != "_":
            lista_de_dados[posicao_de_leitura] = regra.novo_simbolo

        if regra.novo_simbolo != "*" and regra.novo_simbolo == "_":
            lista_de_dados[posicao_de_leitura] = espaco_vazio

        if regra.direcao == "l":
            posicao_de_leitura -= 1
        elif regra.direcao == "r":
            posicao_de_leitura += 1
        elif regra.direcao != "*":
            return "ERR"

        if posicao_de_leitura < 0:
            lista_de_dados = list(espaco_vazio) + lista_de_dados
            posicao_de_leitura = 0

        if posicao_de_leitura > len(lista_de_dados) - 1:
            lista_de_dados = lista_de_dados + list(espaco_vazio)

    resultado = "".join(lista_de_dados)
    resultado = resultado.strip()
    return resultado


def obter_regras(caminho_do_arquivo):
    """obter_regras(caminho_do_arquivo):
    Obtém as regras a partir do arquivo indicado

    Parâmetro:
    caminho_do_arquivo: caminho do arquivo contendo as regras a serem aplicadas pela máquina de
                        Turing
    """
    regras: List[regra_da_maquina_de_turing] = []

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

            regra = regra_da_maquina_de_turing(
                linha_processada[0],
                linha_processada[1],
                linha_processada[2],
                linha_processada[3],
                linha_processada[4])

            regras.append(regra)

    return regras


@dataclasses.dataclass()
class regra_da_maquina_de_turing:
    """regra_da_maquina_de_turing:
    Classe que armazena as informaçoes de uma regra em propriedades bem definidas
    """

    def __init__(self, estado_atual, simbolo_atual, novo_simbolo, direcao, novo_estado) -> None:
        self.estado_atual = estado_atual
        self.simbolo_atual = simbolo_atual
        self.novo_simbolo = novo_simbolo
        self.direcao = direcao
        self.novo_estado = novo_estado

    def __str__(self) -> str:
        resultado = f"estado atual: {self.estado_atual}, "
        resultado += f"simbolo atual: {self.simbolo_atual}, "
        resultado += f"novo simbolo: {self.novo_simbolo}, "
        resultado += f"direcao: {self.direcao}, "
        resultado += f"novo estado: {self.novo_estado}"
        return resultado


if __name__ == "__main__":
    filtered_args = sys.argv[1:]
    main(filtered_args)
