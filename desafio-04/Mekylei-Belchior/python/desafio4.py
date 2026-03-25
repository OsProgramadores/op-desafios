#!/usr/bin/python
#-*- coding: utf-8 -*-


"""
Desafio 04
"""

def entrada():
    """ Exibe a entrada """

    tabuleiro = [
        2, 3, 2, 5, 6, 2, 0, 0,
        0, 0, 1, 0, 1, 1, 1, 0,
        0, 1, 0, 0, 0, 3, 0, 0,
        1, 0, 0, 0, 0, 0, 0, 0,
        1, 0, 0, 0, 0, 0, 0, 0,
        3, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 0, 1, 1, 1, 0,
        4, 0, 0, 5, 6, 2, 3, 4
    ]

    print('\nENTRADA:\n')
    for linha in range(0, 64, 8):
        print(tabuleiro[linha:linha + 8])

    return tabuleiro


def saida(tabuleiro):
    """ Exibe o resultado """

    pecas = {1: 'Peão', 2: 'Bispo', 3: 'Cavalo', 4: 'Torre', 5: 'Rainha', 6: 'Rei'}

    print('\nSAÍDA:\n')
    for indice, valor in pecas.items():
        print(f'{valor}: {tabuleiro.count(indice)}')


def comecar():
    """ Função principal """
    saida(entrada())


if __name__ == '__main__':
    comecar()
