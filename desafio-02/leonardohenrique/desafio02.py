def numsprimos(n):
    primos = [True] * (n + 1)
    primos[0] = primos[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primos[i]:
            for j in range(i * i, n + 1, i):
                primos[j] = False

    for num in range(n + 1):
        if primos[num]:
            print(num ,"é um numero primo!")

numsprimos(10000)
