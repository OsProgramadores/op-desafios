# Python 3.9.9
"""System module."""
board = [input().split(' ') for i in range(8)]

[pawn, bishop, horse, rook, queen, king] = [[
    row.count('1'),
    row.count('2'),
    row.count('3'),
    row.count('4'),
    row.count('5'),
    row.count('6'),
] for row in board][0]

print(f'Peão: {pawn} peça(s)')
print(f'Bispo: {bishop} peça(s)')
print(f'Cavalo: {horse} peça(s)')
print(f'Torre: {rook} peça(s)')
print(f'Rainha: {queen} peça(s)')
print(f'Rei: {king} peça(s)')
