"""This is the example module.

This module does stuff.
"""


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
    print(sieve_of_eratosthenes(10000))
