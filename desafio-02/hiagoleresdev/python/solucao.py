# -*- coding: utf-8 -*-
"""
Created on Thu April 14 01:17:33 2020
Desafio 02 - Listar todos os números primos de 1 à 10000
@author: Hiago
"""
primes = [1]
dividers = 0
for i in range(2, 10000):
    dividers = 0
    for n in range(2, 10000):

        if i%n == 0:
            dividers = dividers + 1

    if dividers == 1:
        primes.append(i)

print(primes)
