#!/usr/bin/env python3
"""
Desafio 02: Listar números primos entre 1 e 10000
"""
import math
for num in range(2, 10001):
    md = int(math.sqrt(num))
    for div in range(2, md+1):
        if num % div == 0:
            break
    else:
        print(num)
