
tabuleiro = [
    [0, 0, 0, 0, 2, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 5, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
    ]

qt_pecas = {1:[0, 'Peão'],
            2:[0, 'Bispo'],
            3:[0, 'Cavalo'],
            4:[0, 'Torre'],
            5:[0, 'Rainha'],
            6:[0, 'Rei']
            }

for row in tabuleiro:
    for peca in row:
        if peca != 0:
            qt_pecas[peca][0] += 1
                
for val in qt_pecas.values():
    print(f'{val[1]}: {val[0]} peça(s)')
    

