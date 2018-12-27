"""
Desafio 2 - Adriano Roberto de Lima
"""

for i in range(1, 10000):
    isprime = 1
    for j in range(2, i-1):
        if i % j == 0:
            isprime = 0
            break
    if isprime:
        print(i)
