def primo_numero(num):
    if num < 1:
        return False
    for x in range(2, num):
        if (num % x == 0):
            return False
    else:
        print(num, "é um número primo")
        return True


for x in range(1, 10001):
    primo_numero(x)
