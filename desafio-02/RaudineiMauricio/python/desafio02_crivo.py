
## Desafio02
#Escrever um programa para listar todos os números primos entre 1 e 10000,
#na linguagem de sua preferência.

def crivo_eratostenes(limite):
    # Cria uma lista de True indicando que todos os números são potencialmente primos
    primos = [True] * (limite + 1)
    primos[0] = primos[1] = False  # 0 e 1 não são primos

    for i in range(2, int(limite ** 0.5) + 1):
        if primos[i]:
            # Marca os múltiplos de i como não primos
            for j in range(i * i, limite + 1, i):
                primos[j] = False

    # Retorna uma lista com todos os números primos encontrados
    return [x for x in range(limite + 1) if primos[x]]

# Encontra todos os primos entre 1 e 10.000
num_primos = crivo_eratostenes(10000)
print("\n".join(map(str, num_primos,)))

