"""
|-------------------------------------|
        Author: @JamesStewart-314
  Minimum python version required: 3.10
|-------------------------------------|
"""

from typing import Final

MAXINTSIZE: Final[int] = (1 << 64) - 1


def number_is_palindromic(number: int):
    return (strNumber := str(number)) == strNumber[::-1]


def validade_number_constraints(number: int, constraints) -> None:
    if constraints is None:
        return
    if constraints[0] is not None and number < constraints[0]:
        raise ValueError(f"Last input number must be greater"\
                         f" or equal to '{constraints[0]}'.")
    if constraints[1] is not None and number > constraints[1]:
        raise ValueError(f"Last input number must be less"\
                         f" or equal to '{constraints[1]}'.")
    return


def get_valid_number(message: str | None = None, constraints = None) -> int:
    while True:
        try:
            user_input: int = int(input(message if message else ""))
        except ValueError:
            print("Invalid Input! You must type an integer value.")
            continue
        try:
            validade_number_constraints(user_input, constraints)
        except ValueError as error:
            print("Invalid Input!", error)
            continue
        return user_input


def get_pal_numbers(start: int, end: int) -> None:
    palindromic_numbers_found: list[int] = []

    for number in range(start, end + 1):
        if number_is_palindromic(number):
            palindromic_numbers_found.append(number)
    if palindromic_numbers_found:
        print("[ ", end="")
        print(*palindromic_numbers_found, sep=", ", end="")
        print(" ]")
    else:
        print("[ sorry, no palindromic numbers found in the given interval ]")


if __name__ == '__main__':
    print("Select two numbers to find palindromes between them:")
    first_number: int = get_valid_number(message = "• Enter the First Number: ",
                                         constraints = (0, MAXINTSIZE))
    second_number: int = get_valid_number(message = "• Enter the Second Number: ",
                                          constraints = (first_number, MAXINTSIZE))
    get_pal_numbers(first_number, second_number)
