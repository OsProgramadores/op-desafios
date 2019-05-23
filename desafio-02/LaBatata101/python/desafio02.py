"""
Calculate all prime numbers from 1 to 10000
"""

def primes(limit):
    """ Calculate prime numbers from 2 to limit, using Sieve of Eratosthenes"""
    isprime = [True] * limit
    for i in range(2, limit):
        if isprime[i]:
            for factor in range(i**2, limit, i):
                isprime[factor] = False
    return isprime


if __name__ == '__main__':
    # Print prime numbers
    PRIME = primes(10000)
    for n in range(1, len(PRIME)):
        if PRIME[n]:
            print(n, end=' ')
    print('\n')
