"""resposta desafio-02"""

def get_prime(limit: int):
    """retorna todos os numeros primos de 2 ate limit usando Crivo de Eratóstenes"""
    _primes = []
    for _num in range(2,limit+1, 1):
        for _prime in _primes:
            if _num % _prime == 0:
                break
        else:
            _primes.append(_num)
    return _primes
