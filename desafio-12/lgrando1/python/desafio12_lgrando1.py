"""Module providingFunction printing python version."""
#!/usr/bin/env python3

from math import log
#para trabalhar com numeros grandes
from decimal import Decimal, getcontext
getcontext().prec = 6

def potencia_de_2(numero):
    """Calculo da potencia de 2 utilizando
    log(numero)/log(2)"""
    numero = int(numero)
    # criado um excessão, pois náo existe log de 0
    if numero == 0:
        print(str(numero) , "false")
    else:
        value = Decimal(log(numero)) / Decimal(log(2))
        if float(value) == float(round(value)):
            print(numero, "true" , int(value))
        else: print(numero , "false")

with open("d12.txt", 'r', encoding='UTF-8') as lin:
    linhas = lin.readlines()
    for linha in linhas:
        potencia_de_2(linha)
