'Leia as expressões de um arquivo .txt e imprima os resultados.'
#'Descomentar' os prints fará com que você veja o processo de evaluação

def get_expressions():
    '''Pega o arquivo d14.txt, e transforma em valores formatados.'''
    with open('d14.txt', encoding='utf-8') as _openfile_:
        _expressions_ = [x.replace('\n', '').replace(' ', '') for x in _openfile_.readlines()]
    return _expressions_

def split_nums_power(expression):
    '''Separa operando, operador, parentêse e identifica erros de síntaxe.'''
    expression = list(expression)
    expression.append('')
    new_expression = []
    multiple_digit_num = ''
    for element in expression:
        if element.isnumeric():
            multiple_digit_num += element
        else:
            if len(multiple_digit_num) > 0:
                new_expression.append(multiple_digit_num)
            if len(element) > 0:
                new_expression.append(element)
            multiple_digit_num = ''
    expression_with_big_nums = new_expression
    expression_with_big_nums.append('')
    new_expression = []
    double_operator = ''

    for element in expression_with_big_nums:
        if element == '*':
            double_operator += element
        else:
            if len(double_operator) > 0:
                new_expression.append(double_operator)
            if len(element) > 0:
                new_expression.append(element)
            double_operator = ''

    if '**' in new_expression or new_expression.count('(') != new_expression.count(')'):
        return 'ERR SYNTAX'
    return new_expression

def math(_a_, _op_, _b_):
    '''Resolve a sub-expressão.'''
    #print(f'            math(_{_a_}_, _{_op_}_, _{_b_}_)')

    operand_a = float(_a_)
    operand_b = float(_b_)
    result = None

    if _op_ == '+':
        result = operand_a + operand_b
    if _op_ == '-':
        result = operand_a - operand_b
    if _op_ == '*':
        result = operand_a * operand_b
    if _op_ == '/':
        result = operand_a / operand_b
    if _op_ == '^':
        result = operand_a ** operand_b

    return result

def is_num(num):
    '''Python .isnumeric() ou .isdigit() não foram suficientes,
    então fiz essa bem simpleszona.'''
    try:
        num = float(num)
    except ValueError:
        return False
    return True

def remove_no_operator_parenthesis(exp):
    '''O nome é auto-explicativo. Remove parentêses sem operadores.'''
    #print(f'    remove_func({exp})')
    _exp_ = exp[:]
    for open_index, open_p in enumerate(_exp_):
        if open_p == '(' and is_num(_exp_[open_index + 1]) and _exp_[open_index + 2] == ')':
            del _exp_[open_index]
            del _exp_[open_index + 1]
            return [_exp_, True]
    return [_exp_, False]

def get_first_parenthesis_to_eval(exp):
    'Get first parenthesis to be evaluated'
    deepest_index = 0
    for index, deepest in enumerate(exp):
        if deepest == '(':
            deepest_index = index
    return deepest_index

def evaluate(_expression_):
    '''Resolve a expressão.'''

    #print(f'\nStart of evaluation process\n{"-"*100}\n')
    expression = _expression_[:]
    op_list = [('^'), ('*', '/'), ('+', '-'), 'end']

    all_iterated = False
    while not all_iterated:

        #print(f'starting new "while" iteration\n{"-"*100}\n')
        expression = remove_no_operator_parenthesis(expression)
        #print(f'    expression = {expression}')

        if expression[1]:
            expression = expression[0]
            continue

        expression = expression[0]
        #print(f'    expression = expression[0] = {expression}')

        p_index = get_first_parenthesis_to_eval(expression)
        #print(f'    p_index in {expression} is {p_index}')

        for operator in op_list:
            #print(f'\n    for {operator} in {op_list}\n')

            if operator == 'end':
                all_iterated = True
                break

            repeat = False
            for index, element in enumerate(expression[p_index:]):
                #print(f'        for {index}, {element}, in enumerate{expression[p_index:]}')

                if element == ')':
                    break

                index += p_index
                if element in operator:
                    expression[index] = math(expression[index-1], element, expression[index+1])
                    expression[index] = str(expression[index])
                    del expression[index - 1]
                    del expression[index]
                    repeat = True

                    #print(f'            expression = {expression} and repeat = True')
                    break

            if repeat:
                break

        #print(f'\nEnd of while loop\n{"-"*100}\n')
    #print(f'\n{"-"*100}\nEnd of evaluation process\n')
    return int(float(expression[0]))

def main():
    '@hoklifter'
    expressions = get_expressions()
    for expression in expressions:
        expression = split_nums_power(expression)
        if expression != 'ERR SYNTAX':
            try:
                expression = evaluate(expression)
            except ZeroDivisionError:
                expression = 'ERR DIVBYZERO'
        print(expression)

main()
