"""Desafio 14 de https://osprogramadores.com/desafios

Expressões numéricas são sequências de duas ou mais operações que devem ser
realizadas respeitando determinada ordem. Para encontrar sempre um mesmo valor
quando calculamos uma expressão numérica, usamos regras que definem a ordem
que as operações serão feitas.

    12 + 3 * 5 = 27
    2 * ( 5 - 1 ) = 8
    2^2 + 8 / 2 = 8
    2^( 3 - 1) = 4

E assim por diante.

INTRUÇÕES

Este desafio consiste em:

    Ler um arquivo de números (abaixo), contendo uma expressão por linha.
    Imprimir o resultado numérico da expressão.
    Se o programa encontrar um divisão por zero deverá imprimir ERR DIVBYZERO.
    Se o programa encontrar um erro de sintaxe na expressão deverá imprimir ERR SYNTAX.
    Não deverão ser usadas bibliotecas externas para trabalho com expressões numéricas.

EXEMPLO

Considere a lista de números:

1 + 3
2 - 3 * 2
2 ^ 3 / 4
0 * 5 * (4 + 1)
5 + 5 / 0
5 + + 1
5 + ( 465 + 1

A saída deverá ser:

4
-4
2
0
ERR DIVBYZERO
ERR SYNTAX
ERR SYNTAX

"""

import argparse
import operator as op
from typing import List, Union

Number = Union[int, float]

class ErrSyntax(Exception):
    """Handle syntax error from parsing expression
    """

class ErrDivByZero(Exception):
    """Handle division by zero error from evaluating
    """

class ErrOverflow(Exception):
    """Handle large number evaluation
    """


def to_number(string: str)-> Number:
    """Converts a string value to its appropriate type

    Args:
        string (str): number in string format

    Returns:
        Number: int or float
    """
    try:
        number = float(string)
    except OverflowError as err:
        raise ErrOverflow("ERR OVERFLOW") from err
    return int(number) if number.is_integer() else number


def tokenize(expr: str) -> List[str]:
    """Breaks expression in string format into list of tokens"""
    return [char for char in expr if char != ' ']



class Parser:
    def __init__(self, expr=None) -> None:
        self.err_styntax = "ERR SYNTAX"
        self.err_divbyzero = "ERR DIVBYZERO"
        self.operators = '+ - * / ^'.split(' ')
        self.operator_associativeness = {
            self.operators[0]: 'left',
            self.operators[1]: 'left',
            self.operators[2]: 'left',
            self.operators[3]: 'left',
            self.operators[4]: 'right',           
        }
        self.operation = {
            self.operators[0]: op.add,
            self.operators[1]: op.sub,
            self.operators[2]: op.mul,
            self.operators[3]: op.truediv,
            self.operators[4]: op.pow,
        }
        self.precedence = dict(zip(self.operation.keys(), [0, 0, 1, 1, 2]))
        if expr is not None:
            self.input = tokenize(expr)
            self.rpn = self.build_rpn()
        else:
            self.input = self.rpn = ''

    def build_rpn(self, expr=None) -> str:
        """Builds an Reverse Polish Notation from expr.
        expr must have only accepted characters:


        Args:
            expr (str): input expression as a list

        Returns:
            list: expr written in RPN notation
        """
        if expr is None:
            expr = self.input
        if expr[0] in self.operators:
            raise ErrSyntax(self.err_styntax)
        output = ['']
        stack = []
        append_number = False
        for item in expr:
            if item.isdigit() or item == '.':
                if append_number and output[-1] != '':
                    output.append('')
                    append_number = False
                output[-1] += item

            elif item == '(':
                stack.append(item)

            elif item in self.operators:
                while len(stack) > 0 \
                      and stack[-1] != '(' \
                      and (self.precedence[stack[-1]] > self.precedence[item] \
                           or ( self.precedence[stack[-1]] == self.precedence[item]
                                and self.operator_associativeness[item] == 'left')):
                    output.append(stack.pop())
                stack.append(item)
                append_number = True

            elif item == ')':
                while len(stack) > 0 and stack[-1] != '(':
                    output.append(stack.pop())
                if len(stack) == 0 or stack[-1] != '(':
                    raise ErrSyntax(self.err_styntax)
                stack.pop()
                append_number = True

        while len(stack) > 0:
            if stack[-1] == '(':  # mismatch parentheses
                raise ErrSyntax(self.err_styntax)
            output.append(stack.pop())

        return output

    def evaluate(self, rpn_expr: List[str] = None) -> Number:
        """Evaluate expression in Reverse Polish Notation

        Args:
            rpn_expr (List[str], optional): Each Element
            must be on element of the expression. Defaults to None.

        Raises:
            ErrSyntax: Syntax Error
            ErrDivByZero: Zero division error

        Returns:
            Number: result
        """
        result = []
        stack = rpn_expr
        if stack is None:
            stack = self.rpn
        stack.reverse()
        if stack[-1] == '':
            raise ErrSyntax(self.err_styntax)
        while len(stack) > 0:
            if stack[-1] in self.operators:
                num1 = to_number(result.pop())
                try:
                    num2 = to_number(result.pop())
                except IndexError as err:
                    raise ErrSyntax(self.err_styntax) from err
                operation = self.operation[stack.pop()]

                if operation == op.truediv and num1 == 0:  # pylint: disable=W0143
                    raise ErrDivByZero(self.err_divbyzero)

                value = to_number(operation(num2, num1))
                result.append(value)
            else:
                result.append(stack.pop())

        return result[-1]


class Reader:
    """Read lines from a file. Discard '\n' at the end of
    each line
    """
    def __init__(self, filename: str) -> None:
        with open(filename, 'r', encoding='utf-8') as file:
            #  don't include '\n'
            self.lines = [line for line in file.read().splitlines()]


def parse_arg_file(num=1):
    """Parse file path as command line argument

    Args:
        num (int, optional): The number of command-line paths 
            that should be consumed.. Defaults to 1.

    Returns:
        argparse.Namespace: object subclass readable string representation
    """
    description = "Evaluate expression in each line of a file."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('path', metavar='file', nargs=num, type=str,
                        help='path to file')
    return parser.parse_args()


def main():
    """Main module's function. Evaluates expressions
    read from a file.
    """

    ## To read from command line, uncomment following two lines
    ## and comment the next one
    # arg = parse_arg_file()
    # handler = Reader(arg.path[0])
    handler = Reader('d14.txt')
    for expr in handler.lines:
        try:
            parser = Parser(expr)
            print(parser.evaluate())
        except ErrDivByZero as err:
            print(err)
        except ErrSyntax as err:
            print(err)
    # try:
    #     expr = "266 + 54 * 4 - ( 41 + 2 ) * 10 / 5 - 7 ^ 3 - 1 + 1 * 0 - (( 45 / 5 * 3 - 1) * 2)"  # "((79 - 12) * (5 + (2 - 1))"
    #     parser = Parser(expr)
    #     print(parser.evaluate())
    # except ErrDivByZero as err:
    #     print(err)
    # except ErrSyntax as err:
    #     print(err)
    # except ErrOverflow as err:
    #     print(err)

if __name__ == '__main__':
    main()
