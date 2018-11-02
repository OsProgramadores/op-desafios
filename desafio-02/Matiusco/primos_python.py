"""Créditos.

pt.stackoverflow em:
# https://pt.stackoverflow.com/a/331991/126107

Adaptação: @Matiusco
site: https://osprogramadores.com/
"""


def eratosthenes():
    """Gera números primos."""
    # dicionario para armazenar os futuros primos
    D = {}
    # primeiro inteiro a testar
    q = 2
    while True:
        if q not in D:
            # nao esta marcado entao eh primo
            yield q
            # armazena somente o primeiro multiplo
            # que ainda nao esta armazenado
            D[q*q] = [q]
        else:
            # todos os nao-primos armazenados aqui precisam andar
            for p in D[q]:
                D.setdefault(p+q, []).append(p)
            # libera memoria do que ja passou
            del D[q]
        q += 1


def primos(limite):
    """Calcula cada primo.

    param: None
    return: p (primo)
    """
    for p in eratosthenes():
        if p > limite:
            break
        print(p)


limite = 10000
primos(limite)
