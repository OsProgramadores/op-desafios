"""Código que imprime todos os números primos entre 1 e 10000"""
primos_list = []

for i in range(2,10001):
    for j in range(2,i+1):
        if i%j == 0:
            if i == j:
                primos_list.append(i)
            else:
                break

print(primos_list)
