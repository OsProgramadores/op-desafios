"""
##
## Desafio-02: Primos ---- OsProgramadores
## Desenvolvido por: Magnu Windell A Santos (@maagwiin)
## Data: 16/09/2020
## Descrição: listar todos os números primos entre 1 e 10000
##
"""

import math

def primeTest(num_max):
    """Imprime na tela todos os números primos até num_max"""
    values = list(range(2, num_max))
    for i in range(2, int(math.sqrt(num_max)+1)):
        if i in values:
            for n in range(i**2, num_max, i):
                if n in values:
                    values.remove(n)
    print("Os números primos de 0 até {} são:".format(num_max))
    print(values)

primeTest(10000)
