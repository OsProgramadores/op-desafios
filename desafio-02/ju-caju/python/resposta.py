LIMITE = 10000


def crivo_de_eratostenes(limite):
    primos = [True] * (limite + 1)
    primos[0] = False
    primos[1] = False

    for numero in range(2, int(limite ** 0.5) + 1):
        if primos[numero]:
            for multiplo in range(numero * numero, limite + 1, numero):
                primos[multiplo] = False

    return [numero for numero, primo in enumerate(primos) if primo]


for primo in crivo_de_eratostenes(LIMITE):
    print(primo)
