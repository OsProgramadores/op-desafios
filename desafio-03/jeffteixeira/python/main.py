"""Prints all palindromous numbers between two numbers"""


MIN_NUMBER = 1
MAX_NUMBER = 18446744073709551615


def main():
    """Function main of the program"""
    inferior_limit = get_valid_inferior_limit()
    superior_limit = get_valid_superior_limit(inferior_limit)
    get_palindromous_numbers(inferior_limit, superior_limit)


def get_valid_inferior_limit():
    """Function that returns a valid inferior limit"""
    while True:
        try:
            inferior_limit = int(input('Enter a positive integer number from {} to {}: '
            .format(MIN_NUMBER, MAX_NUMBER)))
            if MIN_NUMBER <= inferior_limit <= MAX_NUMBER:
                return inferior_limit
        except ValueError:
            print('Only integer values are acepted!')


def get_valid_superior_limit(inferior_limit):
    """Function that returns a valid superior limit"""
    while True:
        try:
            superior_limit = int(input('Enter a positive integer number from {} to {}: '.
            format(inferior_limit, MAX_NUMBER)))
            if inferior_limit <= superior_limit <= MAX_NUMBER:
                return superior_limit
        except ValueError:
            print('Only integer values are acepted!')


def get_palindromous_numbers(inferior_limit, superior_limit):
    """Function that prints the palindromous numbers between two numbers"""
    for number in range(inferior_limit, superior_limit + 1):
        if is_palindrome(number):
            print(number)


def is_palindrome(number):
    """Function that checks if a number is palindrome or not"""
    if number < 10:
        return number
    return number == get_inverted_number(number)


def get_inverted_number(number):
    """Function that returns a inverted number"""
    if len(str(number)) == 1:
        return number
    return int(str(number)[::-1])


if __name__ == '__main__':
    main()
