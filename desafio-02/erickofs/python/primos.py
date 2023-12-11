"""
A simple program to print all prime numbers up to a given number with nth range.
"""
from soe_calc import sieve_of_eratosthenes_set

for prime in sieve_of_eratosthenes_set():
    print(prime)
