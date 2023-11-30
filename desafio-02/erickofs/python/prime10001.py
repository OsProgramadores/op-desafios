"""
Module docstring for prime10001.py.

Prime calculation based on the Sieve of Eratosthenes algorithm.
"""
def sieve_of_eratosthenes():
    """
    Implements the Sieve of Eratosthenes algorithm to find all prime numbers up to a given limit.

    Returns:
    - primelist (list): List of prime numbers up to the given limit.
    """
    primelimit = 1001

    primelist = []

    primelist.extend(range(2, primelimit))
    # Iterate through every number from 2 to the square root of the limit.
    for i in range(2, int(primelimit**0.5) + 1):
        for j in range(i*2, primelimit, i):
            if j in primelist:
                primelist.remove(j)
    # Return the list of prime numbers.
    return primelist

print(sieve_of_eratosthenes())
