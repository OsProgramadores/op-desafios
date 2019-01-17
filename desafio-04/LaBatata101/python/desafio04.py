"""
Valor de cada peça:
    vazio = 0
    peao = 1
    bispo = 2
    cavalo = 3
    torre = 4
    rainha = 5
    rei = 6
"""


TABLE = [[4, 3, 2, 5, 6, 2, 3, 4],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [4, 3, 2, 5, 6, 2, 3, 4]]


def intersection(lst1, lst2):
    '''Return the intersection between two list'''
    return [value for value in lst1 if value in lst2]


def count_pieces():
    '''Count the pieces in the TABLE'''
    peao = bispo = cavalo = torre = rainha = rei = 0
    for i in TABLE:
        peao += len(intersection(i, [1]))
        bispo += len(intersection(i, [2]))
        cavalo += len(intersection(i, [3]))
        torre += len(intersection(i, [4]))
        rainha += len(intersection(i, [5]))
        rei += len(intersection(i, [6]))

    return {'Peão': peao, 'Bispo': bispo, 'Cavalo': cavalo,
            'Torre': torre, 'Rainha': rainha, 'Rei': rei}


if __name__ == '__main__':
    PIECES = count_pieces()
    for k in PIECES:
        print(f'{k}: {PIECES[k]} peça(s)')
