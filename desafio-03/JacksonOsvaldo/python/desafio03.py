#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Resposta de Jackson Osvaldo da Silva Braga
GitHub: https://github.com/JacksonOsvaldo
E-mail: jacksonosvaldo@live.com
"""


def negative(inicio, fim):
    """Copy of the list in reverse order"""
    for numero in range(inicio, fim+1):
        num = str(numero)
        if num == num[::-1]:
            print('Palíndromo: {}'.format(num))

negative(1, 100000)
