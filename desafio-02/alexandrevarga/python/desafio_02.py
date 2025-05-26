"""
Este módulo encontra e imprime todos os números primos em um intervalo especificado.
"""


def encontrar_primos(limite_inferior, limite_superior):
    """
    Retorna uma lista com os números primos no intervalo especificado.
    """
    lista_primos = []
    for num in range(limite_inferior, limite_superior + 1):
        if num > 1:
            is_primo = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_primo = False
                    break
            if is_primo:
                lista_primos.append(num)
    return lista_primos

# Encontrar números primos entre 1 e 10000
primos = encontrar_primos(1, 10000)

for primo in primos:
    print(primo)
