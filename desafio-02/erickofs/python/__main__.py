"""
A simple program to print all prime numbers up to a given number with nth range.
"""
from soecalc import PrimeCalc

if __name__ == "__main__":
    for prime in PrimeCalc.sieve_of_eratosthenes_set():
        print(prime)
