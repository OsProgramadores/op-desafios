#!/usr/bin/env python3
# author: Alison gh: @imalisoon


def find_digit_index(digit, base):
    for i, dig in enumerate(digits):
        if digit == dig and i < base:
            return i

    return -1

def find_digit(digit):
    for i, dig in enumerate(digits):
        if i == digit:
            return dig

    return -1

def to_decimal(base, number):
    _decimal: int = 0

    for i, digit in enumerate(number[::-1]):
        current_value = int(find_digit_index(digit, base)) * int(base**i)
        _decimal += current_value

    return int(_decimal)

def decimal_to_base(base, decimal):
    remainder = []
    final = ""
    finalized = False

    while not finalized:
        remainder.append(int(decimal % base))
        decimal = (decimal-(decimal%base))//base

        if decimal < base:
            remainder.append(int(decimal))
            finalized = True

    for i, value in enumerate(remainder[::-1]):

        if i == 0 and value == 0:
            pass

        else:
            final += str(find_digit(value))

    return final

def is_big(base, number):
    limit = to_decimal(62, 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
    number_decimal = to_decimal(base, number)

    return number_decimal > limit

def dont_have_digit_in_base(base, number):
    for _, digit in enumerate(number[::-1]):
        find = find_digit_index(digit, base)

        if find == -1:
            return True

    return False

def verify(base_in, base_out, number):
    if dont_have_digit_in_base(base_in, number):
        return False

    if base_in > 62 or base_in < 2 or base_out > 62 or base_out < 2:
        return False

    if int(to_decimal(base_in, number)) < 0:
        return False

    if is_big(base_in, number):
        return False

    return True


def load_file(path: str):
    _file: list = []

    with open(path, "r") as f:
        for _l in f.readlines():
            _file.append(_l.strip())

    return _file


if __name__ == "__main__":
    digits: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    input_nums = load_file("baseconv.txt")

    for l in input_nums:
        line = l.split(" ")
        base_input = int(line[0])
        base_output = int(line[1])
        n = line[2].replace("\n", "")

        if verify(base_input, base_output, n):
            dec = to_decimal(base_input, n)
            converted = decimal_to_base(base_output, dec)
            print(converted)
        else:
            print("???")
