# -*- coding: utf-8 -*-

"""
Desafio 02
"""

primos = []

for numero in range(2, 10001):
    if numero == 2:
        primos.append(numero)
    if numero > 2:
        for divisor in range(2, numero):
            if numero % divisor == 0:
                break
        else:
            primos.append(numero)

# Exibe a relação de números primos
print('\n\n\n')
for i in range(0, len(primos), 25):
    print(*primos[i:i+25])
