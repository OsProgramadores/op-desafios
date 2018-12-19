# -*- coding: utf-8 -*-
from collections import Counter
print("digite os numeros de cada linha, separados por espaco")
num = 1
tabuleiro = list()
while num < 9:
    linha = input(f"linha {num} >>>" )
    tabuleiro.extend(linha.split(" "))
    num +=1
counter = Counter(tabuleiro)
#0 0 0 0 0 0 0 0
pecas =(
        ('Cavalo', '1'),
        ('Bispo', '2'),
        ('Cavalo', '3'),
        ('Torre', '4'),
        ('Rainha', '5'),
        ('Rei', '6'),
)

for nome, valor in pecas:
    print('{nome}: {total} peca(s)'.format(nome=nome, total=counter[valor]))
