def listar_primos_ate_1000():
    primos = []
    for num in range(2, 1000):
        is_primo = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_primo = False
                break
        if is_primo:
            primos.append(num)
    return primos

if __name__ == "__main__":
    primos_ate_1000 = listar_primos_ate_1000()
    print(primos_ate_1000)
