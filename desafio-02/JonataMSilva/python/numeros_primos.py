"""usando o Crivo de Eratóstenes."""


def crivo_eratostenes(limite):
    """Encontra todos os números primos até o limite."""
    numeros = [True] * (limite + 1)
    numeros[0] = numeros[1] = False

    for i in range(2, int(limite ** 0.5) + 1):
        if numeros[i]:
            for j in range(i * i, limite + 1, i):
                numeros[j] = False

    primos = [x for x in range(limite + 1) if numeros[x]]
    return primos


numero_limite = 10000

for numero_primo in crivo_eratostenes(numero_limite):
    print(numero_primo)
