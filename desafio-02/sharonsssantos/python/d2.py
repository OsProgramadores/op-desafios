def isqrt(num: int):
    return int(num ** 0.5)

def crivo(limit: int):
    if limit < 2:
        return []

    primos = [1] * (limit + 1)
    primos[0] = primos[1] = 0

    for i in range(2, (isqrt(limit) + 1)):
        for j in range(i*i, (limit + 1), i):
            if primos[j]:
                primos[j] = 0

    return [num for num in range(limit + 1) if primos[num]]

def main():
    resultado = crivo(10_000)
    print(resultado)

if __name__ == "__main__":
    main()
