#!/usr/bin/env python3
'Big Base!'


CHARS_VALUES = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def syntax_check(from_base, to_base, value):
    'Check if the number is valid for a given base.'

    if any(x not in range(2, 63) for x in [from_base, to_base]):
        return False

    if len(value) > 30 and from_base == 62:
        return False

    for algarism in value:
        try:
            CHARS_VALUES[:from_base].index(algarism)
        except ValueError:
            return False

    return True


def to_base_10(from_base, value):
    'Converts any value to base 10.'

    in_base_10 = 0

    for pos, algarism in enumerate(reversed(value)):
        algarism_value = CHARS_VALUES.index(algarism)
        converted = algarism_value * from_base ** pos
        in_base_10 += converted

    return in_base_10


def from_10_to(to_base, value):
    'Converts any value from base 10 to a given number.'
    in_new_base = ''
    quocient = None
    remainder = None
    value_copy = int(str(value)[:])

    while quocient != 0:
        quocient, remainder = value_copy // to_base, value_copy % to_base
        in_new_base = CHARS_VALUES[remainder] + in_new_base
        value_copy = quocient

    return in_new_base


def main():
    'Main.'

    with open('baseconv.txt', 'r', encoding='utf-8') as nums_to_convert:
        for num in nums_to_convert:
            num = num.split()
            num[0], num[1] = int(num[0]), int(num[1])

            if syntax_check(num[0], num[1], num[2]):
                if num[0] != 10:
                    num[2], num[0] = to_base_10(num[0], num[2]), 10
                num = from_10_to(num[1], num[2])
                print(num)
            else:
                print('???')


main()
