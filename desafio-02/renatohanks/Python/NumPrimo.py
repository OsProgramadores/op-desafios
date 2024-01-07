"""
Nome: Renato Oliveira
Github: @renatohanks
Criado: 07/01/2024 / 00:40hrs
"""

numPrimo = ('\033[32mEsses são os números PRIMOS:\033[m')
print(numPrimo)

print('\033[33m')
def get_prime(limit: int):
    _primes = []
    for _num in range(2,limit+1, 1):
        for _prime in _primes:
            if _num % _prime == 0:
                break
        else:
            _primes.append(_num)
    return _primes

prime = get_prime(10000)
print(f"{prime}")
