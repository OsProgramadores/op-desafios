"""Desafio para listar todos os palíndromos de 1 a 3010"""
for i in range(1, 3011):
    if str(i) == str(i)[::-1]:
        print(i)
