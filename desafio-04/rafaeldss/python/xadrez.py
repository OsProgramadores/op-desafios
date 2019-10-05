"""
    Desafio-04 do osprogramadores.com
"""


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

qt_pecas = {
    0: [0],
    1: [0, 'Peão'],
    2: [0, 'Bispo'],
    3: [0, 'Cavalo'],
    4: [0, 'Torre'],
    5: [0, 'Rainha'],
    6: [0, 'Rei']
}

for row in tabuleiro:
    for peca in row:
        qt_pecas[peca][0] += 1

for key in range(1, 7):
    print(f'{qt_pecas[key][0]}: {qt_pecas[key][1]} peça(s)')
