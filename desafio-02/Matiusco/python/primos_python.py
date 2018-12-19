"""Créditos.

pt.stackoverflow em:
# https://pt.stackoverflow.com/a/331991/126107

Adaptação: @Matiusco
site: https://osprogramadores.com/
"""


def eratosthenes():
    """Gera números primos."""
    # dicionario para armazenar os futuros primos
    d_dict = {}
    # primeiro inteiro a testar
    q_marca = 2
    while True:
        if q_marca not in d_dict:
            # nao esta marcado entao eh primo
            yield q_marca
            # armazena somente o primeiro multiplo
            # que ainda nao esta armazenado
            d_dict[q_marca*q_marca] = [q_marca]
        else:
            # todos os nao-primos armazenados aqui precisam andar
            for p_calc in d_dict[q_marca]:
                d_dict.setdefault(p_calc + q_marca, []).append(p_calc)
            # libera memoria do que ja passou
            del d_dict[q_marca]
        q_marca += 1


def primos(limite_primo):
    """Calcula cada primo.

    param: None
    return: p_calc (primo)
    """
    for p_calc in eratosthenes():
        if p_calc > limite_primo:
            break
        print(p_calc)



primos(10000)
