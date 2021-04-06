''' resolução do desafio #2 utilizando o crivo de Eratóstenes'''
def sieve_of_eratosthenes(limit):
    ''' definição do crivo de Eratóstenes '''
    primes = []
    not_primes = []
    for i in range(2, limit + 1):
        if i not in not_primes:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                not_primes.append(j)
    return primes

print(sieve_of_eratosthenes(10000))
