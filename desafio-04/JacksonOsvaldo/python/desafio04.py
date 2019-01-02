#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Resposta de Jackson Osvaldo da Silva Braga
GitHub: https://github.com/JacksonOsvaldo
E-mail: jacksonosvaldo@live.com
"""


resultado = []
pecas = ['1', '2', '3', '4', '5', '6'] #Peão[1], Bispo[2], Cavalo[3], Torre[4], Rainha[5], Rei[6]
vazio = Peao = Bispo = Cavalo = Torre = Rainha = Rei = 0


def valores (numeros):
    num = numeros
    a = [num.split(' ')]
    return a


def tabuleiro(listValores):
    quantasPecas = []
    contar = 0
    for linha in listValores:
        contar = contar + 1
        for segLin in pecas:
            quantasPecas.append(linha.count(segLin))
    return quantasPecas


for i in range(8):
    pecasDoJogo = input()
    pecasJogo = valores(pecasDoJogo)
    resultado = tabuleiro(pecasJogo)
    Peao = resultado[1] + Peao
    Bispo = resultado[2] + Bispo
    Cavalo = resultado[3] + Cavalo
    Torre = resultado[4] + Torre
    Rainha = resultado[5] + Rainha
    Rei = resultado[6] + Rei

print("""\nPeão: {} peça(s)\nBispo: {} peça(s)\nCavalo: {} peça(s)\nTorre: {} peça(s)\nRainha: {} peça(s)\nRei: {} peça(s)""".format(Peao, Bispo, Cavalo, Torre, Rainha, Rei))
