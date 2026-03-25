import os
import re
import string
import collections
from typing import TextIO

def get_op_index(math_expression: str, operator: str, exp_s: set[str]) -> int:
    return math_expression.index(operator) if operator in exp_s\
           else float('inf')


def eval_flat_expression(expression: str) -> str:
    numb_exp: list[str] = re.split(r'[\+\-\*\/\^]', expression)
    exp_oper: list[str] = re.findall(r'[\+\-\*\/\^]', expression)
    while exp_oper:
        exp_set: set[str] = set(exp_oper)
        if "^" in exp_oper:
            oper_idx: int = exp_oper.index('^')
            op_a, op_b = map(int, (numb_exp[oper_idx], numb_exp[oper_idx + 1]))

            result: str = str(op_a ** op_b)

            for _ in range(2):
                numb_exp.pop(oper_idx)

            exp_oper.pop(oper_idx)
            numb_exp.insert(oper_idx, result)

        elif {"*", "/"} & exp_set:
            oper_idx: int = min(get_op_index(exp_oper, '*', exp_set),
                                get_op_index(exp_oper, '/', exp_set))
            op_a, op_b = map(int, (numb_exp[oper_idx], numb_exp[oper_idx + 1]))

            result: str = str(op_a * op_b if exp_oper[oper_idx] == '*' else op_a // op_b)

            for _ in range(2):
                numb_exp.pop(oper_idx)

            exp_oper.pop(oper_idx)
            numb_exp.insert(oper_idx, result)

        else:
            oper_idx: int = min(get_op_index(exp_oper, '+', exp_set),
                                get_op_index(exp_oper, '-', exp_set))
            op_a, op_b = map(int, (numb_exp[oper_idx], numb_exp[oper_idx + 1]))

            result: str = str(op_a + op_b if exp_oper[oper_idx] == '+' else op_a - op_b)

            for _ in range(2):
                numb_exp.pop(oper_idx)

            exp_oper.pop(oper_idx)
            numb_exp.insert(oper_idx, result)

    return numb_exp[0]


def normalize_expression(expression: str) -> str:
    if not ("(" in expression and ")" in expression):
        return eval_flat_expression(expression)

    par_idx_1: int = expression.rindex('(')
    par_idx_2: int = par_idx_1 + expression[par_idx_1:].index(')')

    return normalize_expression(expression[:par_idx_1] +\
           normalize_expression(expression[(par_idx_1 + 1):par_idx_2]) +\
           expression[par_idx_2 + 1:])


def validate_expresssion(expression: str) -> bool:
    all_symbols_and_symbols: set[str] = set("()" + string.digits)
    elements_counter: dict[str, int] = collections.Counter(expression)

    if elements_counter['('] != elements_counter[')']:
        return False

    for idx, elem in enumerate(expression):
        if re.match(r'[1234567890]', elem) or re.match(r'[\(\)]', elem):
            continue

        if not re.match(r'[\+\-\*\/\^]', elem):
            return False

        try:
            if not {expression[idx - 1], expression[idx + 1]}.\
                    issubset(all_symbols_and_symbols):
                return False
        except IndexError:
            return False

    return True


if __name__ == '__main__':
    file_path: str = os.path.join(os.path.dirname(__file__), 'd14.txt')

    try:
        expressions_file: TextIO = open(file_path, 'r')
    except FileNotFoundError as error:
        raise ValueError(f"Error: Could not open file \'{file_path}\'.") from error

    for line in expressions_file:
        line = line.rstrip().replace(' ', '')

        if not validate_expresssion(line):
            print("ERR SYNTAX")
            continue

        try:
            operation_result: str = normalize_expression(line)
        except ZeroDivisionError:
            operation_result: str = "ERR DIVBYZERO"

        print(operation_result)
