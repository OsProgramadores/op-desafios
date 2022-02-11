# Listando numeros primos de 1 a 10000
primos = []
z = 2
# funcao para definir se um numero eh primo
def ehprimo(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i=5
    while i < n:
        if n % i == 0:
            return False
        i=i+2
    return True
# teste dos numeros 1 ate 10000
while z <= 10000:
    if ehprimo(z):
        primos.append(z)
    z = z+1
print(primos)
