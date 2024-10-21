
def listar_primos(n_final):
    primos = [True] * (n_final + 1)
    p = 2
    while p * p <= n_final:
        if primos[p] is True:
            for i in range(p * p, n_final + 1, p):
                primos[i] = False
        p += 1
    return [p for p in range(2, n_final + 1) if primos[p]]

for primo in listar_primos(1000):
    print(primo)
