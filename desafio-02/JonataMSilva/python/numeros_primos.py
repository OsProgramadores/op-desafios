def encontrar_num_primo(numero):
    divisor = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            divisor += 1
    if divisor == 2:
        return True
    return False

for primos in range(1, 10000):
    if encontrar_num_primo(primos):
        print(primos)
