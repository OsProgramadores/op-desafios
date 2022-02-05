""" Convert bases. """
import sys

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def find_digit_index(digit, base):
    """ Find digit and return index. """
    for index, dig in enumerate(digits):
        if digit == dig and index < base:
            return index
    return -1

def find_digit(digit):
    """ Find and return digit. """
    for (index, dig) in enumerate(digits):
        if index == digit:
            return dig
    return -1

def to_decimal(base, number):
    """ Convert bases to decimal. """
    decimal = 0
    for index, digit in enumerate(number[::-1]):
        current_value = int(find_digit_index(digit, base)) * int(base**index)
        decimal += current_value
    return int(decimal)

def decimal_to_base(base, decimal):
    """ Convert bases in decimal to any base. """
    remainder = []
    final = ""
    finalized = False
    while not finalized:
        remainder.append(int(decimal % base))
        decimal = (decimal-(decimal%base))//base
        if decimal < base:
            remainder.append(int(decimal))
            finalized = True
    for index, value in enumerate(remainder[::-1]):
        if index == 0 and value == 0:
            pass
        else:
            final += str(find_digit(value))
    return final

def is_big(base, number):
    """ Verify if number is big. """
    limit = to_decimal(62, 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
    number_decimal = to_decimal(base, number)
    return number_decimal > limit

def dont_have_digit_in_base(base, number):
    """ Verify if digit is in base. """
    for _, digit in enumerate(number[::-1]):
        find = find_digit_index(digit, base)
        if find == -1:
            return True
    return False

def verify(base_in, base_out, number):
    """ Verify all. """
    if dont_have_digit_in_base(base_in, number):
        return False
    if base_in > 62 or base_in < 2 or base_out > 62 or base_out < 2:
        return False
    if int(to_decimal(base_in, number)) < 0:
        return False
    if is_big(base_in, number):
        return False
    return True

try:
    filePath = sys.argv[1] if len(sys.argv) == 2 else "./baseconv.txt"
    with open(filePath, "r", encoding="utf-8") as file:
        for l in file:
            line = l.split(" ")
            b_i = int(line[0])
            b_o = int(line[1])
            n = line[2].replace("\n", "")
            if verify(b_i, b_o, n):
                dec = to_decimal(b_i, n)
                converted = decimal_to_base(b_o, dec)
                print(converted)
            else:
                print("???")
except:
    print("File does not exists.")
