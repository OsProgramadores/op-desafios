# -*- coding: utf-8 -*-

"""
Desafio 02
"""

numeros = (n for n in range(1, 10001))
primos = []

for numero in numeros:
    if numero == 2:
        primos.append(numero)

    if numero > 2:
        divisores = (n for n in range(1, numero + 1))
        contador = 0
        for divisor in divisores:
            if contador > 2:
                break
            if numero % divisor == 0:
                contador += 1
        if contador <= 2:
            primos.append(numero)

# Exibe a relação de números primos
print('\n\n\n')
for i in range(0, len(primos), 25):
    print(*primos[i:i+25])
