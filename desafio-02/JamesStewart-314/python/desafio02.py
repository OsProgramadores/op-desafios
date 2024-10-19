from typing import Generator

def sieveofEratosthenesPrimeGenerator() -> Generator[int, None, None]:

    """
     Generates an infinite sequence of prime numbers 
    using the Sieve of Eratosthenes algorithm.
     
     This generator function uses a dictionary to keep track of 
    non-prime numbers and their smallest prime factors.
    It starts from the number 2 and iteratively finds the next
    prime number by checking if the current number is
    in the dictionary. If it is not, the number is prime and is
    yielded. If it is, the function updates the dictionary
    to mark the next multiple of the corresponding prime factor
    as non-prime. The dictionary is also optimized for
    memory usage by deleting old values.

    :return: A generator to produce prime numbers
    :rtype: Generator[int, None, None]
    """

    # Yields the first
    # and only even prime:
    yield 2

    # Dictionary to allocate the numbers that isn't prime:
    sieveofEratosthenesDict: dict[int, int] = {}
    # Number currently analyzed:
    currentNumber: int = 3

    while True:
        # If number is not in the dict, it's Prime!
        if currentNumber not in sieveofEratosthenesDict:
            # Prime Number Found:
            yield currentNumber
            sieveofEratosthenesDict[currentNumber * currentNumber] = currentNumber

        else:
            currentNumberKey: int = currentNumber + (sieveofEratosthenesDict[currentNumber] << 1)

            # looks for the next multiple of the corresponding value that is
            # not previously in the dictionary and assigns it the prime associated
            # with the previous value. Even values for 'currentNumberKey' are skipped:
            while sieveofEratosthenesDict.get(currentNumberKey):
                currentNumberKey += (sieveofEratosthenesDict[currentNumber] << 1)

            sieveofEratosthenesDict[currentNumberKey] = sieveofEratosthenesDict[currentNumber]
            # Deleting the old value to optimize memory usage:
            del sieveofEratosthenesDict[currentNumber]

        currentNumber += 2


print("\033[1A", end="")
for number in sieveofEratosthenesPrimeGenerator():
    if number > 10_000:
        break

    print(f"\n• \033[32m{number:,}\033[0m;", end="")
print("\b \r")
