"""
Solução do Desafio 04 em Python por Junior Vieira
"""
def exemplo_1():
    """
    Utilização do exemplo 1 demonstrado no site OsProgramadores
    """
    print()
    tabuleiro = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    peao = bispo = cavalo = torre = rainha = rei = 0
    for linha in tabuleiro:
        print(f'{linha} ')
        for valor in linha:
            peao += 1 if valor == 1 else 0
            bispo += 1 if valor == 2 else 0
            cavalo += 1 if valor == 3 else 0
            torre += 1 if valor == 4 else 0
            rainha += 1 if valor == 5 else 0
            rei += 1 if valor == 6 else 0
    print()
    print(f'Peão: {peao} peça(s)')
    print(f'Bispo: {bispo} peça(s)')
    print(f'Cavalo: {cavalo} peça(s)')
    print(f'Torre: {torre} peça(s)')
    print(f'Rainha: {rainha} peça(s)')
    print(f'Rei: {rei} peça(s)')

def exemplo_2():
    """
    Utilização do exemplo 2 demonstrado no site OsProgramadores
    """
    print()
    tabuleiro = [
        [4, 3, 2, 5, 6, 2, 3, 4],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [4, 3, 2, 5, 6, 2, 3, 4],
    ]
    peao = bispo = cavalo = torre = rainha = rei = 0
    for linha in tabuleiro:
        print(f'{linha} ')
        for valor in linha:
            peao += 1 if valor == 1 else 0
            bispo += 1 if valor == 2 else 0
            cavalo += 1 if valor == 3 else 0
            torre += 1 if valor == 4 else 0
            rainha += 1 if valor == 5 else 0
            rei += 1 if valor == 6 else 0
    print()
    print(f'Peão: {peao} peça(s)')
    print(f'Bispo: {bispo} peça(s)')
    print(f'Cavalo: {cavalo} peça(s)')
    print(f'Torre: {torre} peça(s)')
    print(f'Rainha: {rainha} peça(s)')
    print(f'Rei: {rei} peça(s)')

exemplo_1()
exemplo_2()
