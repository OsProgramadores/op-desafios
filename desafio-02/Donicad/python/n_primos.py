
def primos():
    list_primos = []
    numeros = list(range(1, 1001))

    for n in numeros:
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                list_primos.append(n)
    return list_primos

for primo in primos():
    print(primo)
