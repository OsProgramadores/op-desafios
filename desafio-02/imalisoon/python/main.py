#!/usr/bin/env python3
# author: Alison  gh: @imalisoon

def display_primes(limit: int) -> None:
    dividers: int = 0
    for n in range(2, limit+1):
        for i in range(2, n+1):
            if n % i == 0:
                dividers += 1

        if dividers == 1:
            print(n)

        dividers = 0


display_primes(10_000)
