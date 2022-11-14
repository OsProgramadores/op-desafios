"""Desafio de geração dos números primos de 1 a 10000."""
import math

for i in range(1, 10001):
    primo = True
    for j in range(2, math.floor(math.sqrt(i) + 1)):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i)
