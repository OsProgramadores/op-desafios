#!/usr/bin/python
"""Palindrome

Compare an integer converted do a string and reverses to check is it is a palindrome
"""

import sys


def is_palindrome(value: int | str) -> bool:
    """Check if a string or integer is a palindrome."""

    return str(value) == str(value)[::-1]


if __name__ == "__main__":
    start: int = 101  # default
    stop: int = 121  # default

    if len(sys.argv) > 2:
        try:
            # 'is_palindrome' can handle both integer and string values, but
            # we will limit the input to integers.
            start = int(sys.argv[1])
            stop = int(sys.argv[2])

            if stop < 0 or start < 0:
                print('The start and stop numbers must both be positive.')
                sys.exit(1)
        except ValueError:
            print('Provide a valid integer number.')
            sys.exit(1)

    for number in range(start, stop+1):
        if is_palindrome(number):
            print(number)
