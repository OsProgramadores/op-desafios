primos = {2}

for num in range(1, 10001):
    ehPrimo = True

    for var in primos:
        if num % var == 0:
            ehPrimo = False

        if ehPrimo and num != 1:
            primos.add(num)

for var in primos:
    print(var)
