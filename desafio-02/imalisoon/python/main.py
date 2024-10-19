#!/usr/bin/env python3
# author: Alison  gh: @imalisoon

def crivo(limit: int) -> list:
    primes: list = [True] * (limit+1)
    primes[0], primes[1] = False, False

    prime: int = 2
    while (prime*prime) <= limit:
        if primes[prime]:
            for n in range(prime*prime, limit+1, prime):
                primes[n] = False

        prime += 1

    return primes


limit_numbers: int = 10_000

for number, is_prime in enumerate(crivo(limit_numbers)):
    if is_prime:
        print(number)
