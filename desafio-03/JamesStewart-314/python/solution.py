r"""
/-------------------------------------\
       Author: @JamesStewart-314
 Minimum python version required: 3.10
\-------------------------------------/
"""

import os
import time
import inspect
from typing import Callable, TypeAlias, Final


# -------------------------------------- // Type Alias \\ -------------------------------------- ||
# NumberConstraint: Tuple containing the lower
# and upper bound of the new input number, respectivaly:
NumberConstraint: TypeAlias = tuple[int | None, int | None] | None
# ---------------------------------------------------------------------------------------------- ||

# -------------------------------------- // Constants \\ --------------------------------------- ||
MAXINTSIZE: Final[int] = (1 << 64) - 1
# ---------------------------------------------------------------------------------------------- ||

# ----------------------------------- // Lambda Functions \\ ----------------------------------- ||
number_is_palindromic: Callable[[int], bool] = lambda x: (strNumber := str(x)) == strNumber[::-1]

clear_terminal: Callable[[], int] = lambda: os.system("cls" if os.name == "nt" else "clear")

skip_terminal_lines: Callable[[int], None] = lambda qty: print('\n' * qty, end="")
# ---------------------------------------------------------------------------------------------- ||

def constraints_assertion(constraints: NumberConstraint, functionName: str, /) -> None:

    """
     Specific function to define the validation routine
    for a variable of the "NumberConstraint" type.

    :param constraints: A variable corresponding to the
     "NumberConstraint" type to be validated.
    :type constraints: NumberConstraint

    :param functionName: The name of the original function
     that invoked the validation of the "constraints" variable.
    :type functionName: str

    :return: No return
    :rtype: None
    """

    assert isinstance(functionName, str), \
           "\'functionName\' parameter in \'constraints_assertion\'"\
           " function must be of type \'str\'."

    assert isinstance(constraints, tuple | None), \
           f"\'constraints\' parameter in \'{functionName}\'"\
           " function must be of type \'NumberConstraint\'."

    if constraints is not None:
        assert len(constraints) == 2, "\'constraints\'"\
              f" parameter in \'{functionName}\' function must have lenght equal to two."

        assert all((isinstance((exc := element), int | None)) for element in constraints),\
              f"\'constraints\' parameter in \'{functionName}\' function must"\
              f" contain only elements of type \'int\' or \'None\'."\
              f" (Exception Caught: \'{exc}\')"


def clear_upper_lines(quantity: int, /) -> None:

    """
     Deletes the contents of the upper lines of the terminal,
    including the current line on which the cursor is located
    when this function is called.

    :param quantity: Number of terminal predecessor lines to
     be cleared, including the current one.
    :type quantity: int

    :return: No return
    :rtype: None
    """

    # Type Assertions:
    assert isinstance(quantity, int), "\'quantity\' parameter in "\
           "\'clear_upper_lines\' function must be of type \'int\'."

    print("\r", end="")

    for _ in range(quantity + 1):
        print("\033[K\033[1A", end="")
    skip_terminal_lines(1)


def validade_number_constraints(number: int,
                                constraints: NumberConstraint, /) -> None:
    """
     Checks whether a given integer value is obeying the
    constraints specified in the "constraints" parameter.

    :param number: The parsed integer value.
    :type number: int

    :param constraints: A tuple containing the range in
     which the number should be contained.
    :type constraints: NumberConstraint

    :return: No return
    :rtype: None
    """

    # Type Assertions:
    assert isinstance(number, int), "\'number\' parameter in"\
           " \'validade_number_constraints\' function must be of type \'int\'."
    constraints_assertion(constraints, inspect.stack()[0][3])

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
    """
     Function to obtain an integer from the terminal, limited or not
    by a closed interval specified by two other integer values.

    :param message: The optional message that will be displayed in the
     terminal when prompted to input a new integer.
    :type message: str | None

    :param constraints: Defines a tuple with two optional values that represent
     the lower and upper bounds for inputting a value. If there is no lower bound,
     the first element of the tuple is None. If there is no upper bound, the
     second element is None.

      E.g.: (10, None) means that the value must be greater than or equal to 10,
      while (None, 20) means that the value must be less than or equal to 20.
      The tuple (None, None) indicates that there are no bound restrictions.

    :type constraints: NumberConstraint

    :return: An integer value provided by the user through the terminal,
     to which the value will be limited if a range is specified during the function call.
    :rtype: int
    """

    # Type Assertions:
    assert isinstance(message, str | None), "\'message\' parameter"\
           " in \'get_valid_number\' function must be of type \'str\'."
    constraints_assertion(constraints, inspect.stack()[0][3])

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

def get_pal_numbers(start: int, end: int, /) -> None:

    """
     Function to display on the terminal a set
    of palindromic numeric values identified in
    a range specified by the 'start' and 'end'
    parameters.

    :param start: The inclusive lower limit
     of the analyzed range.
    :type start: int

    :param end: The inclusive upper limit
     of the analyzed range.
    :type end: int

    :return: No return
    :rtype: None
    """

    # Type Assertions:
    assert isinstance(start, int), "\'start\' parameter in \'get_pal_numbers\'"\
           " function must be of type \'int\'."
    assert isinstance(end, int), "\'end\' parameter in \'get_pal_numbers\'"\
           " function must be of type \'int\'."

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

    # Clear the terminal before
    # the program starts:
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

    skip_terminal_lines(1)
    get_pal_numbers(firstNumber, secondNumber)
    skip_terminal_lines(1)

    input("Press Enter to Exit!")

    # Countdown to end of program:
    print("Thank you for using this program!!!! Closing in  ...", end='\b' * 4)
    for counter in range(5, -1, -1):
        print(counter, end="\033[3C")
        time.sleep(1)
        print('\b' * 4, end="")

    clear_terminal()
