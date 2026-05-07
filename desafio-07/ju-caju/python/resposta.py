# tac.py
# Uso:
# python tac.py arquivo.txt

import sys
import os

TAMANHO_BLOCO = 1024 * 1024  # 1 MB


def escrever_trecho(arquivo, inicio, fim):
    """
    Escreve na tela o trecho do arquivo entre inicio e fim.
    Não carrega o trecho inteiro na memória.
    """
    arquivo.seek(inicio)
    faltam = fim - inicio

    while faltam > 0:
        pedaco = arquivo.read(min(TAMANHO_BLOCO, faltam))
        sys.stdout.buffer.write(pedaco)
        faltam -= len(pedaco)


def tac(nome_arquivo):
    with open(nome_arquivo, "rb") as arquivo:
        arquivo.seek(0, os.SEEK_END)
        tamanho = arquivo.tell()

        if tamanho == 0:
            return

        # Se o arquivo termina com \n, esse \n pertence à última linha.
        arquivo.seek(tamanho - 1)
        if arquivo.read(1) == b"\n":
            posicao = tamanho - 1
        else:
            posicao = tamanho

        fim_linha = tamanho

        while posicao > 0:
            inicio_bloco = max(0, posicao - TAMANHO_BLOCO)

            arquivo.seek(inicio_bloco)
            bloco = arquivo.read(posicao - inicio_bloco)

            indice = bloco.rfind(b"\n")

            while indice != -1:
                pos_quebra = inicio_bloco + indice

                escrever_trecho(arquivo, pos_quebra + 1, fim_linha)

                fim_linha = pos_quebra + 1

                bloco = bloco[:indice]
                indice = bloco.rfind(b"\n")

            posicao = inicio_bloco

        escrever_trecho(arquivo, 0, fim_linha)


if len(sys.argv) != 2:
    print("Uso: python tac.py arquivo.txt")
else:
    tac(sys.argv[1])