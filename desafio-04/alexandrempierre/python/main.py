#!/usr/bin/env python3

'''main module
'''


__author__ = 'Alexandre Pierre'


def readline():
    '''Read one line of chess squares.'''
    return map(int, filter(lambda x: x in '0123456789', input().split(' ')))

def readboard(lines=8):
    '''Read the squares corresponding to the board.'''
    while lines > 0:
        lines -= 1
        for piece in readline():
            yield piece

piece_names = [
    'VAZIO', 'Peão', 'Bispo', 'Cavalo', 'Torre', 'Rainha', 'Rei']
piece_count = [0, 0, 0, 0, 0, 0, 0]
for p in readboard():
    piece_count[p] += 1
piece_names.pop(0)
piece_count.pop(0)
for name, qtty in zip(piece_names, piece_count):
    print(f'{name}: {qtty} peça(s)')
