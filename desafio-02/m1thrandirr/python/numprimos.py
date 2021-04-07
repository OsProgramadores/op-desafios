<<<<<<< HEAD
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
=======
for i in range(1001):
    if i==2 or i==3 or i==5:
        print(i)
    if i%2!=0 and i%3!=0 and i%5!=0:
        print(i)
>>>>>>> d11d2996d18f443caaeb1c1d7db93eab08f27a1c
