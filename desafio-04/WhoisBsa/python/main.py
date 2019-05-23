
""" Tabuleiro de Xadrez """

def main():
    """ Conta as peças do tabuleiro """
    pecas = {1: [0, 'Peão'],
             2: [0, 'Bispo'],
             3: [0, 'Cavalo'],
             4: [0, 'Torre'],
             5: [0, 'Rainha'],
             6: [0, 'Rei']}

    file1 = open('ex1.txt', 'r')
    file2 = open('ex2.txt', 'r')
    ex_1 = file1.read()
    ex_2 = file2.read()
    print('Exemplo 1:')
    print(ex_1)
    print('Exemplo 2:')
    print(ex_2)

    while True:
        op_tab = str(input('Qual tabuleiro você deseja usar? [1/2] '))
        if op_tab not in '12':
            print('Há apenas 2 opções, tente novamente\n')
        else:
            print('-=' * 20)
            break

    print()

    if op_tab == '1':
        tabuleiro = ex_1
    else:
        tabuleiro = ex_2

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

    file1.close()
    file2.close()

if __name__ == "__main__":
    main()
