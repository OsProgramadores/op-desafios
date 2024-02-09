numeros = list(range(3, 10001, 2))

print (2)
for numero in numeros:
    if numero in numeros:
        print (numero)
        for multiplo in range(numero * 2, 10001, numero):
            if multiplo in numeros:
                numeros.remove(multiplo)
