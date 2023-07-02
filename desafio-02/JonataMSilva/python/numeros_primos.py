def num_primo(n):
    divisor = 0
    for i in range(1, 10001):
        if n % i == 0:
            divisor += 1
    if divisor == 2:
        return 1
    else:
        return 0


for numero in range(1, 10001):
    if num_primo(numero) == 1:
        print(numero)