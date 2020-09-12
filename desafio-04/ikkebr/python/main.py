""" Desafio 04 em Python por @ikkebr g- OsProgramadores"""
entrada = []

for linhas in range(8):
    entrada += map(int, input().split(' '))

print("""Peão: {} peça(s)
Bispo: {} peça(s)
Cavalo: {} peça(s)
Torre: {} peça(s)
Rainha: {} peça(s)
Rei: {} peça(s)""".format(entrada.count(1), entrada.count(2), entrada.count(3),
                          entrada.count(4), entrada.count(5), entrada.count(6)))
