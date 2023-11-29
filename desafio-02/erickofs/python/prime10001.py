from math import floor, sqrt

limit = 1001

primelist = []

primelist.extend(range(2, limit))

def sieve_of_eratosthenes(limit):

    # Iterate through every number from 2 to the square root of the limit.
    for i in range(2, int(limit**0.5) + 1):
    #
        for j in range(i*2, limit, i):
            if j in primelist:
                primelist.remove(j)
    # Retorna a lista de números primos.
    return primelist

print(sieve_of_eratosthenes(limit))
