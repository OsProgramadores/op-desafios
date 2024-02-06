numeros = list(range(2, 10001))
primos = []

for numero in numeros:
    if numero in numeros:
        primos.append(numero)
        for multiplo in range(numero * 2, 10001, numero):
            if multiplo in numeros:
                numeros.remove(multiplo)

print (primos)
