"""Sieve of Eratosthenes.

Find all the prime numbers less than or equal to a given integer n by Eratosthenes'
method.
"""

import sys


def sieve_of_eratosthenes(limit: int) -> list[int]:
    """Return all primes smaller than or equal to N.

    (including optimization of starting from prime's square)
    """

    is_prime: list[bool] = [True for _ in range(limit + 1)]
    is_prime[0], is_prime[1] = False, False

    prime: int = 2

    while prime*prime <= limit:
        if is_prime[prime]:
            for i in range(prime*prime, limit+1, prime):
                is_prime[i] = False

        prime += 1

    return [number for number, is_prime in enumerate(is_prime) if is_prime]


if __name__ == "__main__":
    number: int = 10000

    if len(sys.argv) > 1:
        try:
            number = int(sys.argv[1])
            if number < 2:
                print('The limit must be greater than 1')
                sys.exit(1)
        except ValueError:
            print('Provide a valid int for the limit,')
            sys.exit(1)

    for result in sieve_of_eratosthenes(number):
        print(result)
