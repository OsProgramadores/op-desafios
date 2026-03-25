""" Desafio 02 """


def verifica_primo(numero):
    """Esta função verifica se o número é primo, caso afirmativo, ela imprime este valor."""

    contador = 0
    i = 1
    for i in range(numero):
        i = i + 1
        if numero % i == 0:
            contador = contador + 1

    if contador == 2:
        print(numero)

for a in range(10000):
    verifica_primo(a)
