"""
Author: Guilherme Silva Schultz
Data: 17/01/2023

Solução para desafio 2 usando o metodo "Crivo de Eratóstenes"

essa metodo é bem simples e eficiente
começando em um array de 2 até N, divida cada numero do array pelo indice atual
os numeros divisiveis são removidos do array e passa para o proximo indice até o fim do array

ex:
array = [2,3,4,5,6,7,8,9,10]
array[0] = 2

remova todos os numeros divisiveis por 2

[2,3,5,7,9]
array[1] = 3
remova todos os numeros divisiveis por 3

[2,3,5,7]
e assim segue.....
"""


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

prime = get_prime(10000)
print(f"{prime}")