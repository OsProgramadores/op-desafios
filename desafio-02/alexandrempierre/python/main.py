#!/usr/bin/env python3

'''main module

Module to wrap the problem solution.
'''


from sieve_of_eratosthenes import sieve_of_eratosthenes

if __name__ == '__main__':
    PRIMES = sieve_of_eratosthenes(10_000)
    print(*PRIMES, sep='\n')
