#!/usr/bin/python
# author: Alison gh: imalisoon

def parser_expression(expression):
    expression = list(expression)
    expression.append('')
    new_expression = []
    multiple_number = ''

    for item in expression:
        if item.isnumeric():
            multiple_number += item

        else:
            if len(multiple_number) > 0:
                new_expression.append(multiple_number)

            if len(item) > 0:
                new_expression.append(item)

            multiple_number = ''

    expression_with_big_nums = new_expression
    expression_with_big_nums.append('')
    new_expression = []
    double_operator = ''

    for item in expression_with_big_nums:
        if item == '*':
            double_operator += item

        else:
            if len(double_operator) > 0:
                new_expression.append(double_operator)

            if len(item) > 0:
                new_expression.append(item)

            double_operator = ''

    if '**' in new_expression or new_expression.count('(') != new_expression.count(')'):
        return 'ERR SYNTAX'

    return new_expression

def resolve_sub_eq(a, operator, b):
    first_op = float(a)
    second_op = float(b)
    result = None

    if operator == '+':
        result = first_op + second_op
    if operator == '-':
        result = first_op - second_op
    if operator == '*':
        result = first_op * second_op
    if operator == '/':
        result = first_op / second_op
    if operator == '^':
        result = first_op ** second_op

    return result

def is_number_confirm(num):
    try:
        num = float(num)

    except ValueError:
        return False

    return True

def remove_empty_parenthesis(exp):
    _exp_ = exp[:]

    for open_index, open_p in enumerate(_exp_):
        if open_p == '(' and is_number_confirm(_exp_[open_index + 1]) and _exp_[open_index + 2] == ')':
            del _exp_[open_index]
            del _exp_[open_index + 1]

            return [_exp_, True]

    return [_exp_, False]

def get_first_parenthesis_to_eval(exp):
    deep_index = 0

    for index, deep in enumerate(exp):
        if deep == '(':
            deep_index = index

    return deep_index

def evaluate(_expression_):
    expression = _expression_[:]
    op_list = [
        ('^'), ('*', '/'), ('+', '-'), 'end'
    ]

    all_iterated = False
    while not all_iterated:
        expression = remove_empty_parenthesis(expression)

        if expression[1]:
            expression = expression[0]
            continue

        expression = expression[0]
        p_index = get_first_parenthesis_to_eval(expression)

        for operator in op_list:
            if operator == 'end':
                all_iterated = True
                break

            repeat = False

            for index, item in enumerate(expression[p_index:]):
                if item == ')':
                    break

                index += p_index

                if item in operator:
                    expression[index] = resolve_sub_eq(expression[index-1], item, expression[index+1])
                    expression[index] = str(expression[index])
                    del expression[index - 1]
                    del expression[index]
                    repeat = True

                    break

            if repeat:
                break

    return int(float(expression[0]))

def load_file():
    with open('d14.txt', 'r') as _openfile:
        _expressions = [
            x.replace('\n', '').replace(' ', '')
            for x in _openfile.readlines()
        ]

    return _expressions

def main():
    expressions = load_file()

    for expression in expressions:
        expression = parser_expression(expression)

        if expression != 'ERR SYNTAX':
            try:
                expression = evaluate(expression)

            except ZeroDivisionError:
                expression = 'ERR DIVBYZERO'

        print(expression)


if __name__ == "__main__":
    main()
