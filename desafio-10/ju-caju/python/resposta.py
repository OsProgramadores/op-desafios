import os
import sys


class Regra:
    def __init__(self, estado_atual, simbolo_atual, novo_simbolo, direcao, novo_estado, ordem):
        self.estado_atual = estado_atual
        self.simbolo_atual = simbolo_atual
        self.novo_simbolo = novo_simbolo
        self.direcao = direcao
        self.novo_estado = novo_estado
        self.ordem = ordem


def simbolo_para_fita(simbolo):
    if simbolo == "_":
        return " "
    return simbolo


def carregar_regras(caminho):
    regras = []
    ordem = 0

    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.split(";", 1)[0].strip()

            if linha == "":
                continue

            partes = linha.split()

            if len(partes) != 5:
                return None

            estado_atual = partes[0]
            simbolo_atual = partes[1]
            novo_simbolo = partes[2]
            direcao = partes[3]
            novo_estado = partes[4]

            if direcao not in ("l", "r", "*"):
                return None

            if len(simbolo_atual) != 1:
                return None

            if len(novo_simbolo) != 1:
                return None

            simbolo_atual = simbolo_para_fita(simbolo_atual)

            if novo_simbolo != "*":
                novo_simbolo = simbolo_para_fita(novo_simbolo)

            regra = Regra(
                estado_atual,
                simbolo_atual,
                novo_simbolo,
                direcao,
                novo_estado,
                ordem
            )

            regras.append(regra)
            ordem += 1

    return regras


def regra_casa(regra, estado, simbolo):
    estado_casa = regra.estado_atual == estado or regra.estado_atual == "*"
    simbolo_casa = regra.simbolo_atual == simbolo or regra.simbolo_atual == "*"

    return estado_casa and simbolo_casa


def especificidade(regra):
    pontos = 0

    if regra.estado_atual != "*":
        pontos += 1

    if regra.simbolo_atual != "*":
        pontos += 1

    return pontos


def escolher_regra(regras, estado, simbolo):
    melhor_regra = None
    melhor_pontuacao = -1

    for regra in regras:
        if regra_casa(regra, estado, simbolo):
            pontos = especificidade(regra)

            if pontos > melhor_pontuacao:
                melhor_regra = regra
                melhor_pontuacao = pontos

    return melhor_regra


def executar_maquina(regras, entrada):
    fita = list(entrada)

    if len(fita) == 0:
        fita = [" "]

    posicao = 0
    estado = "0"

    while True:
        simbolo = fita[posicao]

        regra = escolher_regra(regras, estado, simbolo)

        if regra is None:
            return "ERR"

        if regra.novo_simbolo != "*":
            fita[posicao] = regra.novo_simbolo

        if regra.direcao == "r":
            posicao += 1

            if posicao == len(fita):
                fita.append(" ")

        elif regra.direcao == "l":
            if posicao == 0:
                fita.insert(0, " ")
            else:
                posicao -= 1

        estado = regra.novo_estado

        if estado.startswith("halt"):
            return "".join(fita)


def processar_arquivo_dados(caminho_dados):
    cache_regras = {}

    if caminho_dados is None:
        arquivo_dados = sys.stdin
        pasta_dados = "."
    else:
        arquivo_dados = open(caminho_dados, "r", encoding="utf-8")
        pasta_dados = os.path.dirname(os.path.abspath(caminho_dados))

    for linha in arquivo_dados:
        linha = linha.rstrip("\n").rstrip("\r")

        if linha == "":
            continue

        partes = linha.split(",", 1)

        if len(partes) != 2:
            print("ERR")
            continue

        nome_regras = partes[0].strip()
        entrada = partes[1]

        if nome_regras not in cache_regras:
            caminho_regras = nome_regras

            if not os.path.isabs(caminho_regras):
                caminho_regras = os.path.join(pasta_dados, nome_regras)

            try:
                cache_regras[nome_regras] = carregar_regras(caminho_regras)
            except:
                cache_regras[nome_regras] = None

        regras = cache_regras[nome_regras]

        if regras is None:
            saida = "ERR"
        else:
            try:
                saida = executar_maquina(regras, entrada)
            except:
                saida = "ERR"

        print(nome_regras + "," + entrada + "," + saida)

    if caminho_dados is not None:
        arquivo_dados.close()


if len(sys.argv) > 1:
    processar_arquivo_dados(sys.argv[1])
else:
    processar_arquivo_dados(None)