"""
Autor: Roberto Arruda
#02 - Primos
"""
def printPrimos(num):
    tot = 0
    for n in range(1, num + 1):
        if (num % n == 0):
            tot += 1
    if (tot == 2):
        print("{} é primo".format(num), end='\n')

for num in range(1, 10000 + 1):
    printPrimo(num)