"""
    Resolucao do Desafio 03:
    Por: Gabriel Rocha
    github: https://github.com/G4BR13LR0CH4
"""
var = int(input())
var1 = int(input())

valores = []
while var <= var1:
    valores.append(str(var))
    var += 1

for x in valores:
    if x == x[::-1]:
        print(x)
