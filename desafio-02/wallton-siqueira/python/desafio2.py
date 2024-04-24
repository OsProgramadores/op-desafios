# Escreva um programa para listar todos os números primos entre 1 e 10000, na linguagem de sua preferência.


# Lista vazia para armazenar os números primos 
primos = []

# Loop para verificar os números
for c in range(2, 1001):
    cont = 0

# Loop para verificar se é primo
    for p in range(1, c +1):
        if c % p == 0:
             cont += 1
        
    if cont <= 2:
        primos.append(c)
print(primos)