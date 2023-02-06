""" Author: lucasfturos | Description: Resolve frações simples contidas em arquivo *.txt """

import sys
from fractions import Fraction

def fracao_simples(fracao: str) -> str:
    """ Função que resolve a fração e retorna o resultado """
    try:
        frac = Fraction(fracao)
        numerador = frac.numerator % frac.denominator
        complemento = frac.numerator // frac.denominator
        is_zero = '' if complemento == 0 else f'{complemento} '

        if frac.denominator == 1:
            return frac.numerator
        return f'{is_zero}{numerador}/{frac.denominator}'
    except ZeroDivisionError:
        return 'ERR'

try:
    with open(sys.argv[1], encoding='utf-8') as fracao_file:
        for value in fracao_file.readlines():
            print(fracao_simples(value))
    fracao_file.close()
except IOError:
    print('Erro ao abrir arquivo')
