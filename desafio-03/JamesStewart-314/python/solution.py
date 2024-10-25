# /-------------------------------------\
#        Author: @JamesStewart-314
#  Minimum python version required: 3.10
# \-------------------------------------/

from typing import Callable, TypeAlias, Final

NumberConstraint: TypeAlias = tuple[int | None, int | None] | None

MAXINTSIZE: Final[int] = (1 << 64) - 1

number_is_palindromic: Callable[[int], bool] = lambda x: (strNumber := str(x)) == strNumber[::-1]

def validade_number_constraints(number: int,
                                constraints: NumberConstraint) -> None:
    if constraints is None:
        return
    if constraints[0] is not None and number < constraints[0]:
        raise ValueError(f"Last input number must be greater"\
                         f" or equal to '{constraints[0]}'.")
    if constraints[1] is not None and number > constraints[1]:
        raise ValueError(f"Last input number must be less"\
                         f" or equal to '{constraints[1]}'.")
    return


def get_valid_number(message: str | None = None,
                     constraints: NumberConstraint = None) -> int:
    while True:
        try:
            userInput: int = int(input(message if message else ""))
        except ValueError:
            print("Invalid Input! You must type an integer value.")
            continue
        try:
            validade_number_constraints(userInput, constraints)
        except ValueError as error:
            print("Invalid Input!", error)
            continue
        return userInput

def get_pal_numbers(start: int, end: int) -> None:
    palindromicNumbersFound: list[int] = []
    for number in range(start, end + 1):
        if number_is_palindromic(number):
            palindromicNumbersFound.append(number)
    if palindromicNumbersFound:
        print("[ ", end="")
        print(*palindromicNumbersFound, sep=", ", end="")
        print(" ]")
    else:
        print("[ sorry, no palindromic numbers found in the given interval ]")


if __name__ == '__main__':
    print("Select two numbers to find palindromes between them:")
    firstNumber: int = get_valid_number(message = "• Enter the First Number: ",
                                    constraints = (0, MAXINTSIZE))
    secondNumber: int = get_valid_number(message = "• Enter the Second Number: ",
                                    constraints = (firstNumber, MAXINTSIZE))
    get_pal_numbers(firstNumber, secondNumber)
