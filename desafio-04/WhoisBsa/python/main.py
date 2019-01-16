
""" Tabuleiro de Xadrez """


pecas = {1: [0, 'Peão'],
         2: [0, 'Bispo'],
         3: [0, 'Cavalo'],
         4: [0, 'Torre'],
         5: [0, 'Rainha'],
         6: [0, 'Rei']}

f1 = open('ex1.txt', 'r')
f2 = open('ex2.txt', 'r')
ex1 = f1.read()
ex2 = f2.read()
print('Exemplo 1:')
print(ex1)
print('Exemplo 2:')
print(ex2)

while True:
    op = str(input('Qual tabuleiro você deseja usar? [1/2] '))
    if op not in '12':
        print('Há apenas 2 opções, tente novamente\n')
    else:
        print('-=' * 20)
        break

print()

if op == '1':
    tabuleiro = ex1
else:
    tabuleiro = ex2

print(tabuleiro)

pecas[1][0] = tabuleiro.count('1')
pecas[2][0] = tabuleiro.count('2')
pecas[3][0] = tabuleiro.count('3')
pecas[4][0] = tabuleiro.count('4')
pecas[5][0] = tabuleiro.count('5')
pecas[6][0] = tabuleiro.count('6')

print()
for i in pecas.values():
    print(f'{i[1]}: {i[0]} peças')

f1.close()
f2.close()
