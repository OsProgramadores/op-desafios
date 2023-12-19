"""
A simple program to print all prime numbers up to a given number with nth range.
"""
from soecalc import PrimeCalc

if __name__ == "__main__":

    pn = PrimeCalc()
    for i in pn.get_primes():
        print(i)
