""" Desafio 04 em Python """


xadrez = open('xadrez.txt', 'r')

pecas = {
    1: ['Peão', 0],
    2: ['Bispo', 0],
    3: ['Cavalo', 0],
    4: ['Torre', 0],
    5: ['Rainh', 0],
    6: ['Rei', 0],
    0: ['Vazio', 0],
    }

for linha in xadrez:
    for peca in linha:
        try:
            peca = int(peca)
        except ValueError:
            continue
        pecas.get(int(peca))[1] += 1

for p in pecas:
    print(pecas[p][0], pecas[p][1], 'peça (s)')
