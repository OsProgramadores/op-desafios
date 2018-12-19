#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Resposta de Jackson Osvaldo da Silva Braga
GitHub: https://github.com/JacksonOsvaldo
E-mail: jacksonosvaldo@live.com
"""


def primo(numero):
    """Função para testar se é ou não primo retornando valor lógico."""
    num = 0
    for i in range(numero):
        resto = numero % (i + 1)
        if resto == 0:
            num = num + 1
            if num > 2:
                break

    return num == 2

for numeroContador in range(10):
    testeprimo = primo(numeroContador)
    if testeprimo is True:
        print('O número primo é: {}'.format(numeroContador))
    else:
        pass
