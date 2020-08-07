"""
Autor: Roberto Arruda
#02 - Primos
"""
for num in range(1, 10000 + 1):
    tot = 0
    for n in range(1, num + 1):
        if num % n == 0:
            tot += 1

    if tot == 2:
        print('\033[32m', end='')
        print("{} é primo".format(num), end='\n')
