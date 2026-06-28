limite = 10000

numeros_primos = [True] * (limite + 1)

numeros_primos[0] = False
numeros_primos[1] = False

for numero in range(2, limite + 1):

    if numeros_primos[numero]:

        for multiplo in range(numero * 2, limite + 1, numero):

            numeros_primos[multiplo] = False

for numero in range(2, limite + 1):

    if numeros_primos[numero]:

        print(numero)
