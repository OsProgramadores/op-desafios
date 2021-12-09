'''parseexpression module

Functions to evaluate an expression given as text.
'''


__all__ = ['evaluate', 'ErrSyntax', 'ErrDivByZero']
__author__ = 'Alexandre Pierre'


import collections


class ErrSyntax(Exception):
    '''Exception to be raised when dealing with syntax errors.'''


class ErrDivByZero(Exception):
    '''Exception to be raised when dealing with division by zero.'''


Stack = collections.namedtuple('Stack', ('values', 'operators'))

def pop2(stack):
    '''Gets the two numbers at the top of the stack.'''
    if len(stack) < 2:
        raise ErrSyntax('ERR SYNTAX')
    top = stack.values.pop()
    second = stack.values.pop()
    return top, second

def plus(stack):
    '''Sums the two numbers at the top of the stack.'''
    top, second = pop2(stack)
    stack.values.append(top + second)

def minus(stack):
    '''Subtracts the two numbers at the top of the stack.'''
    subtrahend, minuend = pop2(stack)
    stack.values.append(minuend - subtrahend)

def mul(stack):
    '''Multiplies the two numbers at the top of the stack.'''
    multiplicator, multiplicand = pop2(stack)
    stack.values.append(multiplicand * multiplicator)

def div(stack):
    '''Divides the two numbers at the top of the stack.'''
    divisor, dividend = pop2(stack)
    if divisor == 0:
        raise ErrDivByZero('ERR DIVBYZERO')
    stack.values.append(dividend // divisor)

def power(stack):
    '''Performs exponentiation with the two numbers at the top of the stack.'''
    exponent, base = pop2(stack)
    stack.values.append(base**exponent)

def operate(op):
    '''Selects the right function to perform the operation based on the operator
symbol'''
    return {'+' : plus, '-': minus, '*': mul, '/': div, '^': power}[op]

def right_parenthesis(stack):
    '''Perform all operations until a left parenthesis "(" is found.'''
    while stack.operators and stack.operators[-1] != '(':
        operate(stack.operators.pop())(stack)
    if not stack.operators:
        raise ErrSyntax('ERR SYNTAX')
    stack.operators.pop()

def evaluate(str_expression):
    '''Evaluates an expression given as text.'''
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operators = {'+', '-', '*', '/', '^', '(', ')'}
    stack = Stack(values=[], operators=[])
    acc = ''
    for expression_char in str_expression:
        if expression_char in operators:
            operator_symbol = expression_char
            if acc:
                stack.values.append(int(acc))
                acc = ''
            if operator_symbol == '(':
                stack.operators.append('(')
            elif operator_symbol == ')':
                right_parenthesis(stack)
            elif operator_symbol == '^':
                while (stack.operators and stack.operators[-1] != '(' and
                       precedence[operator_symbol] <\
                         precedence[stack.operators[-1]]):
                    operate(stack.operators.pop())(stack)
                stack.operators.append(operator_symbol)
            else:
                # Not really DRY but the right associativity of the power (^) operator
                # was not easy to deal in a more readable way
                while (stack.operators and stack.operators[-1] != '(' and
                       precedence[operator_symbol] <=\
                         precedence[stack.operators[-1]]):
                    operate(stack.operators.pop())(stack)
                stack.operators.append(operator_symbol)
        elif expression_char not in {' ', '\t', '\n'}:
            acc += expression_char
    if '(' in stack.operators:
        raise ErrSyntax('ERR SYNTAX')
    if acc:
        stack.values.append(int(acc))
    while stack.operators:
        operate(stack.operators.pop())(stack)

    return stack.values.pop()
