""" Desafio 04 - Xadrez """

from collections import Counter

M1 = [4, 3, 2, 5, 6, 2, 3, 4,
    1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1, 1, 1,
    4, 3, 2, 5, 6, 2, 3, 4]



counter = Counter(M1)
pieces = (
        ('Peão', 1),
        ('Bispo', 2),
        ('Cavalo', 3),
        ('Torre', 4),
        ('Rainha', 5),
        ('Rei', 6)
    )

for name, value, in pieces:
    print("{name}: {total} peça(s)".format(name=name, total=counter[value]))
