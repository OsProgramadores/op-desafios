#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    Desenvolvido por Gabriel Ferreira (@GabrielF9)
    Solução para o Desafio 3 do site OsProgramadores
'''

if __name__ == '__main__':
    board = input().split()
    
    parts = ('Peão', 'Bispo', 'Cavalo', 'Torre', 'Rainha', 'Rei')

    for num in range(1, 7):
        print(f'{parts[num-1]}: {board.count(str(num))} peça(s)')
