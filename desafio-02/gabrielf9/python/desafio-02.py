#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    Desenvolvido por Gabriel Ferreira (@GabrielF9)
    Solução para o Desafio 2 do site OsProgramadores
'''
if __name__ == '__main__':
    primes = []

    for i in range(2, 10001):
        if i % 2 == 0 and i != 2:
            continue

        _isPrime = True
        for j in range(2, int(i**1/2)+1):
            if i % j == 0 and i != j:
                _isPrime = False

        if _isPrime:
            primes.append(i)
            print(f'{i} é primo')

    print(f'Um total de {len(primes)} primos.')
