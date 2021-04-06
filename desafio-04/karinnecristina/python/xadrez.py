'''Descrição: Solução do desafio-04 - osprogramadores.com
Autor(a): karinnecristina
Linguagem: Python'''


print()

TABULEIRO = {1: ['Peão', 0],
             2: ['Bispo', 0],
             3: ['Cavalo', 0],
             4: ['Torre', 0],
             5: ['Rainha', 0],
             6: ['Rei', 0]
             }
MATRIZ = [[4, 3, 2, 5, 6, 2, 3, 4],
          [1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 1],
          [4, 3, 2, 5, 6, 2, 3, 4]]

for elementos in MATRIZ:
    print(elementos)
for linha in MATRIZ:
    for pecas in linha:
        if pecas != 0:
            TABULEIRO[pecas][1] += 1
print()
for pecas in TABULEIRO.values():
    print(f'{pecas[0]}: {pecas[1]} peça(s)')
