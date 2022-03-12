'''sieve_of_eratosthenes module

Module with the necessary functions to perform the Sieve of Eratosthenes
'''

__all__ = ['sieve_of_eratosthenes']
__author__ = 'Alexandre Pierre'


from pair import first, second


def update_sieve(sieve, number, upper_limit):
    '''Sets primality of the multiples of number to False'''
    qtty = (upper_limit - number * number) // number + 1
    sieve[number * number::number] = [False] * qtty

def sieve_of_eratosthenes(upper_limit):
    '''Function that performs the Sieve of Eratosthenes to find all primes up to upper_limit'''
    sieve = [True] * (upper_limit + 1)
    sieve[0] = False
    sieve[1] = False

    for number, is_prime in enumerate(sieve):
        if is_prime:
            update_sieve(sieve, number, upper_limit)

    return list(map(first, filter(second, enumerate(sieve))))
