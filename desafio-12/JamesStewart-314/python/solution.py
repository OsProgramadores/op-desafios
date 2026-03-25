import os
import math
from typing import TextIO

def is_power_of_two(x: int) -> bool:
    return x > 0 and not x & (x - 1)

if __name__ == '__main__':
    try:
        numbers_file: TextIO = open(os.path.join(os.path.dirname(__file__), "d12.txt"), 'r')
    except FileNotFoundError as error:
        raise Exception(f"Error: Could open file \'{numbers_file}\'.") from error

    for raw_number in numbers_file:
        formatted_number: int = int(raw_number.rstrip())
        is_valid_power: bool = is_power_of_two(formatted_number)
        print(formatted_number, str(is_valid_power).lower(), end=' ')
        if is_valid_power:
            print(int(math.log2(formatted_number)), end='')
        print()
