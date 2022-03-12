# Python 3.9.9
"""System module."""
from math import ceil

def isPrime(number, div, count, primes):
    """Verify if number is prime."""
    if div <= ceil(number**0.5):
        isDiv = [prime for prime in primes if number % prime == 0]
        if (len(isDiv) >= 1 or number == 1):
            count += 1
        div += 1
        return isPrime(number, div, count, primes)
    return primes.append(number)

primesList = []

for i in range(1, 10000):
    isPrime(i, 1, 0, primes=primesList)
print(primesList)
