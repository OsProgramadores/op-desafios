tabuleiro = [[4,3,2,5,6,2,3,4],
            [1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [4,3,2,5,6,2,3,4]]

peoes = sum([i.count(1) for i in tabuleiro])
bispos = sum([i.count(2) for i in tabuleiro])
cavalos = sum([i.count(3) for i in tabuleiro])
torre = sum([i.count(4) for i in tabuleiro])
rei = sum([i.count(5) for i in tabuleiro])
rainha = sum([i.count(6) for i in tabuleiro])

print(f'Peão: {peoes} peça(s)')
print(f'Bispo: {bispos} peça(s)')
print(f'Cavalo: {cavalos} peça(s)')
print(f'Torre: {torre} peça(s)')
print(f'Rainha: {rei} peça(s)')
print(f'Rei: {rainha} peça(s)')