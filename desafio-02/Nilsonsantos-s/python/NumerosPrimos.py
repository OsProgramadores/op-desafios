"""
Autor: Nilsonsantos-s
Propósito: Desafio 2
"""

for n in range(1, 10000):
    contador = 0
    for c in range(1, n+1):
        if n%c == 0:
            contador += 1
    if contador == 2:
        print(n)
