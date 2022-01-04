#!/usr/bin/env python3

'''main module
'''


__author__ = 'Alexandre Pierre'


from sys import argv


class InvalidBaseError(ValueError):
    '''Exceção usada para o caso de encontrar um valor de base inválido'''


class InvalidNumberError(ValueError):
    '''Exceção usada para o caso de encontrar um valor de número inválido na
base'''


class NegativeNumberError(ValueError):
    '''Exceção usada para o caso de encontrar um número negativo'''


class AboveLimitError(ValueError):
    '''Exceção usada para o caso de encontrar um número acima do limite'''

def convert(number:str, base_in:int, base_out:int) -> str:
    '''Função de conversão de números da bse de entrada para a base de saída'''
    error_message = f'''base in: {base_in}
base out: {base_out}
number: {number}'''
    if base_in < 2 or base_in > 62 or base_out < 2 or base_out > 62:
        raise InvalidBaseError(error_message)
    if number.startswith('-'):
        raise NegativeNumberError(error_message)
    if not validate_number(number, base_in):
        raise InvalidNumberError(error_message)
    if not check_number_limit(number, base_in):
        raise AboveLimitError(error_message)

    if base_in == base_out or number == '0':
        return number
    if base_in == 10:
        return decimal2any(int(number), base_out)
    if base_out == 10:
        return str(any2decimal(number, base_in))
    return decimal2any(any2decimal(number, base_in), base_out)

def check_number_limit(number:str, base_in:int) -> bool:
    '''Verifica se o número está dentro do limite'''
    return (
        any2decimal(number, base_in) <=
            591222134364399413463902591994678504204696392694759423
        )

def any2decimal(number:str, base_in:int) -> int:
    '''Converte o número de qualquer base para a base 10'''
    return sum(digit2value(digit) * base_in**exponent
               for exponent, digit in enumerate(number[::-1]))

def decimal2any(number:int, base_out:int) -> str:
    '''Converte o número da base 10 para qualquer base'''
    str_number_out = ''
    while number > 0:
        str_number_out = value2digit(number % base_out) + str_number_out
        number //= base_out
    return str_number_out

def validate_number(number:str, base_in:int) -> bool:
    '''Verifica se o número dado é válido na base dada'''
    return all(map(lambda digit: digit2value(digit) < base_in, number))

def digit2value(digit:str) -> int:
    '''Transforma o dígito de string para um valor inteiro'''
    return {
        digit: value for value, digit in enumerate(
            '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    }[digit]

def value2digit(value:int) -> str:
    '''Transforma o dígito de um inteiro para string'''
    return (
        '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'[value]
        )

if __name__ == '__main__':
    with open(argv[1], 'r', encoding='ascii') as fp:
        for line in fp:
            input_line = line.strip().split(' ')
            str_base_input, str_base_output, str_number = input_line
            base_input, base_output = int(str_base_input), int(str_base_output)
            try:
                output_value = convert(str_number, base_input, base_output)
            except (
                InvalidBaseError, InvalidNumberError,
                NegativeNumberError, AboveLimitError) as base_error:
                output_value = '???'
            finally:
                print(output_value)
