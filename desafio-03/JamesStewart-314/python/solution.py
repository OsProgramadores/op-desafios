r"""
/-------------------------------------\
       Author: @JamesStewart-314
 Minimum python version required: 3.10
\-------------------------------------/
"""

import os
import time
from typing import Callable, TypeAlias, Final

# NumberConstraint: Tuple containing the lower
# and upper bound of the new input number, respectivaly:
NumberConstraint: TypeAlias = tuple[int | None, int | None] | None
MAXINTSIZE: Final[int] = (1 << 64) - 1

number_is_palindromic: Callable[[int], bool] = lambda x: \
               (strNumber := str(x)) == strNumber[::-1]
clear_terminal: Callable[[], None] = lambda: os.system("cls" if os.name == "nt" else "clear")


def clear_upper_lines(quantity: int, /) -> None:
    print("\r", end="")
    for _ in range(quantity + 1):
        print("\033[K\033[1A", end="")
    print()


def validade_number_constraints(number: int,
                              constraints: NumberConstraint, /) -> None:
    # Type Assertions:
    assert isinstance(number, int), "Assertion Error: \'number\' parameter in"\
        " \'validade_number_constraints\' function must be of type \'int\'"
    assert isinstance(constraints, tuple | None), \
    "Assertion Error: \'constraints\' parameter in \'validade_number_constraints\'"\
        " function must be of type \'NumberConstraint\'"

    if constraints is None:
        return

    if constraints[0] is not None and number < constraints[0]:
        raise ValueError(f"Last input number must be \033[33mgreater\033[0m"\
                         f" or equal to \'{constraints[0]}\'.")
    if constraints[1] is not None and number > constraints[1]:
        raise ValueError(f"Last input number must be \033[32mless\033[0m"\
                         f" or equal to \'{constraints[1]}\'.")

    return


def get_valid_number(*, message: str | None = None,
                   constraints: NumberConstraint = None) -> int:
    # Function to get an integer valid number

    # Type Assertions:
    assert isinstance(message, str | None), "Assertion Error: \'message\' parameter"\
                                            " in \'get_valid_number\'"\
                                            " function must be of type \'str\'"
    assert isinstance(constraints, tuple | None), "Assertion Error: \'constraints\'"\
           "parameter in \'get_valid_number\' function must be of type \'NumberConstraint\'"

    while True:
        try:
            userInput: int = int(input(message if message else "\033[0m"))
        except ValueError:
            print("\033[31mInvalid\033[0m Input! You must type an integer value.")
            input("Press Enter to Continue...")
            clear_upper_lines(3)
            continue

        try:
            validade_number_constraints(userInput, constraints)
        except ValueError as error:
            print("\033[31mInvalid\033[0m Input!", error)
            input("Press Enter to Continue...")
            clear_upper_lines(3)
            continue

        return userInput

def impress_palindromic_numbers_in_range(start: int, end: int, /) -> None:
    numbersFoundFlag: bool = False

    print("[ ", end="")
    for number in range(start, end + 1):
        if number_is_palindromic(number):
            print(number, ", ", sep="", end="")
            numbersFoundFlag = True

    print("\b\b", end="")
    if numbersFoundFlag is True:
        print(" ]")
    else:
        print("[ sorry, no palindromic numbers found in the given interval ]")


clear_terminal()

print("\033[4m", f"{"<<< Welcome to the numeric palindrome detector! >>>":^60}",\
      "\033[0m\b ", sep="")
print("|||", " " * 51, "|||")
print("|||", f"{"Please, insert two numbers greater or equal to":^51}", \
      "|||\n||| each other to find palindromic numbers between them |||")
print("\\\\\\", "_" * 53, "///\n", sep="")

firstNumber: int = get_valid_number(message = "• Enter the "\
                                  "\033[33;1mFirst\033[0m Number: ",
                                  constraints = (0, MAXINTSIZE))
secondNumber: int = get_valid_number(message = "• Enter the "\
                                  "\033[34;1mSecond\033[0m Number: ",
                                  constraints = (firstNumber, MAXINTSIZE))

print()
impress_palindromic_numbers_in_range(firstNumber, secondNumber)
print()

input("Press Enter to End the Program!")
for i in range(5, -1, -1):
    print("Thank you for using!!!! Closing in", i, '...', end="")
    time.sleep(1)
    print("\r", end="")

clear_terminal()
