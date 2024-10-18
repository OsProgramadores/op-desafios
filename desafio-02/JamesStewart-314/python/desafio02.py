from typing import Generator

def sieveofEratosthenesPrimeGenerator() -> Generator[int, None, None]:
    # Dictionary to allocate the numbers that isn't prime:
    sieveofEratosthenesDict: dict[int, int] = {}
    # Number currently analyzed:
    currentNumber: int = 2

    while True:
        # If number is not in the dict, it's Prime!
        if currentNumber not in sieveofEratosthenesDict:
            # Prime Number Found:
            yield currentNumber
            sieveofEratosthenesDict[currentNumber * currentNumber] = currentNumber

        else:
            currentNumberKey: int = currentNumber + sieveofEratosthenesDict[currentNumber]

            # looks for the next multiple of the corresponding value that is
            # not previously in the dictionary and assigns it the prime associated
            # with the previous value:
            while sieveofEratosthenesDict.get(currentNumberKey, None) is not None:
                currentNumberKey += sieveofEratosthenesDict[currentNumber]

            sieveofEratosthenesDict[currentNumberKey] = sieveofEratosthenesDict[currentNumber]
            # Deleting the old value to optimize memory usage:
            del sieveofEratosthenesDict[currentNumber]

        currentNumber += 1


print("\033[1A", end="")
for number in sieveofEratosthenesPrimeGenerator():
    if number > 10_000:
        break

    print(f"\n• \033[32m{number:,}\033[0m;", end="")
print("\b \r")
