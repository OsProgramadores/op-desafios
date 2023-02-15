""" Author: lucasfturos | Description: Resolve frações simples contidas em arquivo *.txt """

import sys
from math import gcd

def fracao_simples(fracao: str) -> str:
    """ Função que resolve a fração e retorna o resultado """
    try:
        if '/' in fracao:
            numerador, denominador = list(map(int,fracao.split('/')))
            result_div = numerador / denominador
            div_int = numerador // denominador
            mod_div = numerador % denominador
            max_div_comum = gcd(numerador, denominador)

            if result_div == 1:
                return str(1)
            if div_int > 0 and denominador != 1:
                return f'{div_int} {mod_div}/{denominador}'
            if denominador == 1:
                return numerador
            return f'{numerador // max_div_comum}/{denominador // max_div_comum}'
        return fracao
    except ZeroDivisionError:
        return 'ERR'
try:
    with open(sys.argv[1], encoding='utf-8') as fracao_file:
        for value in fracao_file.readlines():
            print(fracao_simples(value.replace('\n','')))
    fracao_file.close()
except IOError:
    print('Erro ao abrir arquivo')
