import math

numero_limite = 10000
lista = []

def primo(num):
    raiz = int(math.sqrt(num))
    for i in range(2, raiz + 1):
        if num % i == 0:
            return None
    return num

for num in range(2, numero_limite + 1):
    if primo(num):
        lista.append(num)

print(lista)