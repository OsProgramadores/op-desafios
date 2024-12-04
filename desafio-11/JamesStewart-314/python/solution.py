import os
from collections import defaultdict
from typing import Generator

def sieve_of_eratosthenes_prime_generator() -> Generator[int, None, None]:
    yield 2
    sieveofEratosthenesDict: dict[int, int] = {}
    currentNumber: int = 3

    while True:
        if currentNumber not in sieveofEratosthenesDict:
            yield currentNumber
            sieveofEratosthenesDict[currentNumber * currentNumber] = currentNumber
        else:
            currentNumberKey: int = currentNumber + (sieveofEratosthenesDict[currentNumber] << 1)
            while sieveofEratosthenesDict.get(currentNumberKey):
                currentNumberKey += (sieveofEratosthenesDict[currentNumber] << 1)
            sieveofEratosthenesDict[currentNumberKey] = sieveofEratosthenesDict[currentNumber]
            del sieveofEratosthenesDict[currentNumber]

        currentNumber += 2


def find_biggest_seq(pi_digits: str, upper_limit: int | float = 10e4) -> str:
    prime_numbers: set[str] = set()
    for prime_number in sieve_of_eratosthenes_prime_generator():
        if prime_number >= upper_limit:
            break
        prime_numbers.update(str(prime_number).zfill(z_qty) for z_qty in range(1, 5))

    prim_seq: defaultdict[int, str] = defaultdict(str)
    for idx in range(2, len(pi_digits)):
        curent_num: str = ""
        for qty in range(4):
            try:
                curent_num += pi_digits[idx + qty]
                if not curent_num in prime_numbers:
                    continue
                if len(prim_seq[idx + qty + 1]) < (len(prim_seq[idx]) + len(curent_num)):
                    prim_seq[idx + qty + 1] = prim_seq[idx] + curent_num
            except IndexError:
                continue

    return max(prim_seq.values(), key=len, default='')


if __name__ == '__main__':
    file_path: str = os.path.join(os.path.dirname(__file__), "pi-1M.txt")
    try:
        print(find_biggest_seq(open(file_path, "r").readline().strip()))
    except FileNotFoundError as error:
        raise Exception(f"Error: Could open file \'{file_path}\'.") from error
