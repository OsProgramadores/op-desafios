# Números primos


def encontrar_primos(limite_inferior, limite_superior):
    lista_primos = []
    for num in range(limite_inferior, limite_superior + 1):
        if num > 1:
            primo = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    primo = False
                    break
            if primo:
                lista_primos.append(num)
    return lista_primos

# Encontrar números primos entre 1 e 10000
primos = encontrar_primos(1, 10000)
print(primos)
