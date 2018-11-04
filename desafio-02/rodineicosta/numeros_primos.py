from math import sqrt

limite, primos = 10000, []

def ehPrimo(numero):
    if  numero < 2:
        return False 
    for i in range(2, int(sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

for p in range(2, limite + 1):
    if ehPrimo(p):
        primos.append(p)

print(primos)
