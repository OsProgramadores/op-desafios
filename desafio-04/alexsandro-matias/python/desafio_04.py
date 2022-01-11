""" Desafio 04 """

TABULEIRO = [
    2, 3, 2, 5, 6, 2, 0, 0,
    0, 0, 1, 0, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 3, 0, 0,
    1, 0, 0, 0, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 0, 0, 0,
    3, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 0,
    4, 0, 0, 5, 6, 2, 3, 4
]

CONTADOR_PEAO = CONTADOR_BISPO = CONTADOR_CAVALEIRO = 0
CONTADOR_TORRE = CONTADOR_DAMA = CONTADOR_REI = 0

for i in range(64):
    if TABULEIRO[i] == 1:
        CONTADOR_PEAO += 1

for i in range(64):
    if TABULEIRO[i] == 4:
        CONTADOR_TORRE += 1

for i in range(64):
    if TABULEIRO[i] == 3:
        CONTADOR_CAVALEIRO += 1

for i in range(64):
    if TABULEIRO[i] == 2:
        CONTADOR_BISPO += 1

for i in range(64):
    if TABULEIRO[i] == 6:
        CONTADOR_REI += 1

for i in range(64):
    if TABULEIRO[i] == 2:
        CONTADOR_DAMA += 1

print(f'PEÃO: {CONTADOR_PEAO} peça(s)')
print(f'BISPO: {CONTADOR_BISPO} peça(s)')
print(f'CAVALEIRO: {CONTADOR_CAVALEIRO} peça(s)')
print(f'TORRE: {CONTADOR_TORRE} peça(s)')
print(f'DAMA: {CONTADOR_DAMA} peça(s)')
print(f'REI: {CONTADOR_REI} peça(s)')
