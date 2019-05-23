# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:00:09 2019

Desafio 04  - Contabilizar Peças de Xadrez sem a utilização de condicionais

@author: Aline
"""
# Importando a biblioteca collections
import collections as c

def chessPieces(chess):
    # Contando quantos elementos de cada tipo existem na lista    
    pieces = c.Counter(chess)
        
    # Imprimindo esses elementos de acordo com o código de cada um
    print("Peão: " + str(pieces[1]) + " peça(s)")
    print("Bispo: " + str(pieces[2]) + " peça(s)")
    print("Cavalo: " + str(pieces[3]) + " peça(s)")
    print("Torre: " + str(pieces[4]) + " peça(s)")
    print("Rainha: " + str(pieces[5]) + " peça(s)")
    print("Rei: " + str(pieces[6]) + " peça(s)")

def main():
    # Lendo o arquivo input.txt que contém uma das opções de input dada no
    # Exemplo
    file = open("input.txt", "r")
    
    # Colocando todos os elementos da matrix 8x8 em uma lista
    chess = list(map(int, file.read().split()))
    
    # Verificando a quantidade de cada peça na função chessPieces
    chessPieces(chess)

if __name__ == "__main__":
    main()

