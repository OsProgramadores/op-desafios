import os
import string
from collections import deque
from typing import Final

number_base_symbols: str = string.digits + string.ascii_uppercase + string.ascii_lowercase
number_base_symbols_mapping: dict[str, int] = {key: value for value, key\
                                              in enumerate(number_base_symbols)}

UPPERLIMIT: Final[int] = 62 ** 30 - 1

def check_base(x: int) -> bool:
    return x < 2 or x > 62

def from_decimal_to(number_to_convert: str, new_base: int) -> str:
    string_builder: deque[str] = deque()

    while (division_result := divmod(number_to_convert, new_base))[0] != 0:
        string_builder.appendleft(number_base_symbols[division_result[1]])
        number_to_convert = division_result[0]

    string_builder.appendleft(number_base_symbols[division_result[1]])

    return ''.join(string_builder)


def to_decimal_from(number_to_convert: str, number_base: int) -> int:
    total_sum: int = 0
    number_size: int = len(number_to_convert)

    for index in range(number_size - 1, -1, -1):
        total_sum += number_base_symbols_mapping[number_to_convert[index]] * \
                    (number_base ** (number_size - index - 1))

    return total_sum

def validate_number_input(current_number: str, start_base_num: int, end_base_num: int) -> bool:
    if any((current_number[0] == '-', *map(check_base, (start_base_num, end_base_num)))):
        return False

    if any(map(lambda x: number_base_symbols_mapping[x] >= start_base_num,\
               current_number.lstrip('-'))):
        return False

    return True

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'baseconv.txt'), 'r') as bases_file:
        for line in bases_file:
            start_base, end_base, number = line.strip().split()
            start_base, end_base = map(int, (start_base, end_base))

            if not validate_number_input(number, start_base, end_base):
                print('???')
                continue

            number_converted_to_decimal_base: int = to_decimal_from(number, start_base)

            if number_converted_to_decimal_base > UPPERLIMIT:
                print('???')
                continue

            print(from_decimal_to(number_converted_to_decimal_base, end_base))
