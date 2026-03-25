#!/usr/bin/python3
# coding: utf-8
""" Função para exibir números primos de 1 até 10000. """

from __future__ import print_function
import math

def primos(num):
    """ Função para exibir números primos de 1 até 10000. """
    nprimos = list(range(2, num))

    for i in range(2, int(math.sqrt(num)+1)):
        if i in nprimos:
            for j in range(i ** 2, num, i):
                if j in nprimos:
                    nprimos.remove(j)
    for num in nprimos:
        print(num)
    print('Total de números primos: {} '.format(len(nprimos)))

primos(10000)
