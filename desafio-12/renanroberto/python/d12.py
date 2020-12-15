"""
Reads a file containing a number per line and test if they are a power of 2
"""

import math


def power2(num):
    """Takes a number x and compute log2(x) of that number. If it is
    a integer n, then 2^n = x"""
    if num == 0:
        return (num, False, 0)

    result = math.log2(num)

    if result.is_integer():
        return (num, True, int(result))

    return (num, False, 0)


def main():
    """Reads d12.txt, applies power2 and pretty print the results"""
    file = open("d12.txt", "r")

    nums = [int(num) for num in file]
    results = map(power2, nums)

    for (num, has_solution, solution) in results:
        if has_solution:
            print(f"{num} true {solution}")
        else:
            print(f"{num} false")


if __name__ == "__main__":
    main()
