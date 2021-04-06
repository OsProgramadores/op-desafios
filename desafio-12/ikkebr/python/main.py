"""Solução do Desafio 12 em Python"""
from math import log

with open('d12.txt', 'r') as f:
    for line in f:
        numero = int(line.strip())

        if numero == 0:
            print('0 false')
            continue

        if numero == 1:
            print('1 true 0')
            continue

        print(numero, end=' ')
        olog = round(log(numero, 2))

        res = numero == 2**olog

        if res:
            print(str(res).lower(), end=' ')
            print(round(log(numero, 2)))
        else:
            print(str(res).lower())
