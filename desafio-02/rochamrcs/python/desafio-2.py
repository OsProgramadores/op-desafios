def primos(n):
    raiz = int(n ** 0.5)
    for d in range(2, raiz + 1):
        if n % d == 0:
            return False
    return True


p = []
for x in range(1, 10001):
    if primos(x):
        p.append(x)

print(p)