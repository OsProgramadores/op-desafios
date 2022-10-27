'''
Este script irá retornar os número primos entre 1 e 10.000.
'''

primos = []
for numero in range(1, 10001):
    cont = 0
    for antecessor in range(1, numero + 1):
        if numero % antecessor == 0:
            cont += 1
        if cont == 3:
            break
    if cont == 2 :
        primos.append(numero)
print(f'Entre 1 e 10.000 existem {len(primos)} números primos.')
