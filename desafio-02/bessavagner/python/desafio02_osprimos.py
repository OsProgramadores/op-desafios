"""Desafio 02 de https://osprogramadores.com/desafios

Escreva um programa para listar todos os números primos
entre 1 e 10000, na linguagem de sua preferência.
"""
import argparse


def seive_eratosthenes(num) :
    """Uses the seiv of Eratosthenes to map primes.
    The returned list is a mask of True/False values,
    with True elements indexes corresponding
    to prime numbers.
    Check https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    Args:
        num (int): Maximum numbers to look for primes

    Returns:
        list: maks of prime numbers
    """
    mask = [True for dumb in range(num + 1)]
    mask[0], mask[1] = False, False

    for i in range(2, int(num**0.5) + 1):
        for j in range(2*i, num + 1, i):
            mask[j] = False
    return mask

def primes_generator(num, seive=seive_eratosthenes):
    """Generator of prime numbers.

    Args:
        num (int): Maximum numbers to look for primes of
        seive (callable, optional):
            a sieve to generate a mask map of primes.
            It must return a list of True/False values,
            where True indexes corresponds to a prime.
            Defaults to seive_eratosthenes.

    Yields:
        int: prime number
    """
    mask = seive(num)
    for index, elem in enumerate(mask):
        if elem:
            yield index


def main():
    """Main module's function. Shows primes from 2 up to N.
    """
    description = "List N primes starting from 2."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('number', metavar='N', nargs=1, type=int,
                        help='integer up to wich primes will be listed')
    arg = parser.parse_args()
    primes = [str(prime) for prime in primes_generator(arg.number[0])]
    print(' '.join(primes))

if __name__ == '__main__':
    main()
