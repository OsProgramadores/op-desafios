"""
Desafio 10 - Adriano Roberto de Lima.
"""

import sys


def lerprograma(arquivoprograma):
    """
    lerprograma é uma função para ler o arquivo com as instruções da máquina
    de Turing.
    """
    programa = list()
    try:
        file = open(arquivoprograma, "r")
    except IOError:
        return -1

    linhas = file.readlines()

    for linha in linhas:
        dados = linha.split(";")
        semcomentarios = dados[0].strip()
        if semcomentarios != "":
            comando = semcomentarios.split(" ")
            if len(comando) < 5:
                return -2
            programa.append(comando)

    return programa


def buscacomando(estadoatual, leitura, programa):
    """
    buscacomando identifica qual o próximo comando a ser executado
    baseado no estado atual e na leitura da fita de dados.
    """
    ret = []
    ret2 = []

    ret = [i for i in programa if i[0] == estadoatual or i[0] == "*"]

    if not ret:
        return -1

    ret2 = [i for i in ret if i[1] == leitura or i[1] == "*"]

    if not ret2:
        return -1

    for i in ret2:
        if i[0] == estadoatual and i[1] == leitura:
            return i

    return ret2[0]


def turing(programa, dado):
    """
    turing é a função que executa o programa especificado com o a fita de dados.
    """
    posicaocabeca = 0
    estadoatual = "0"

    while True:
        leitura = dado[posicaocabeca]
        comando = buscacomando(estadoatual, leitura, programa)
        if comando == -1:
            return "ERR"
        if comando[2] != "*":
            dado[posicaocabeca] = comando[2]
        estadoatual = comando[4]
        if "halt" in estadoatual:
            break
        if comando[3] == "l":
            posicaocabeca = posicaocabeca - 1
            if posicaocabeca == -1:
                dado = ["_"] + dado
                posicaocabeca = 0
        elif comando[3] == "r":
            posicaocabeca = posicaocabeca + 1
            if posicaocabeca == len(dado):
                dado = dado + ["_"]

    return dado


def main():
    """
    Main Function.
    """

    if len(sys.argv) < 2:
        print("Erro ! Sintaxe: python desafio10.py nomedoarquivo")
        sys.exit(0)

    try:
        file = open(sys.argv[1], "r")
    except IOError:
        print("Não consegui abrir o arquivo", sys.argv[1])
        sys.exit(0)

    linhas = file.readlines()

    for linha in linhas:
        dados = linha.split(",")
        try:
            arquivoprograma = dados[0].rstrip()
            dados = dados[1].rstrip()
            dados = dados.replace(" ", "_")

        except IndexError:
            print("Arquivo de entrada", sys.argv[1], "inválido !")
            sys.exit(0)

        dado = list(dados)
        programa = lerprograma(arquivoprograma)

        if programa == -1:
            print("Erro na leitura do arquivo", arquivoprograma)
            sys.exit(0)
        elif programa == -2:
            print("Comandos inválidos no arquivo", arquivoprograma)
            sys.exit(0)

        ret = turing(programa, dado)
        ret = "".join(ret)
        ret = ret.replace("_", " ").strip()
        dados = dados.replace("_", " ")
        print(arquivoprograma, dados, ret, sep=',')

    file.close()


if __name__ == "__main__":
    main()
