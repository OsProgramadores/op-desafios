#!/usr/bin/env python3
print('São primos os seguintes números:')
for a in range(2,10000):
    b = 2
    contador = 0
    while b < a:
        if a % b == 0:
            contador = 1
            b += 1
        else:
            b += 1

    if contador == 0:
        print(a)

    