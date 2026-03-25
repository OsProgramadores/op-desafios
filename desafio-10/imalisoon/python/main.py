#!/usr/bin/python
# author: Alison gh: @imalisoon

import sys
import re


def remove_comments(file):
    _comment = re.sub(";(.*)(?=\n)", '', file.read()).splitlines()

    return [x for x in _comment if x.strip() != ""]


def turing_parser(arq):
    _rules = {}

    for line in arq:
        result = line.strip().split(" ")

        if result[0] not in _rules:
            _rules[result[0]] = {}

        _rules[result[0]][result[1]] = (result[2], result[3], result[4])

    return _rules


def check_generic_rule(sym, rules):
    return (sym in rules['*']) or ('*' in rules['*'])


def execute(input_data, rules):
    data = list(input_data)
    state = '0'
    strip_position = 0
    current_symbol = data[strip_position]

    while 'halt' not in state:
        if '*' in rules:
            if check_generic_rule(current_symbol, rules):
                state = '*'

        if state not in rules:
            return 'ERR'

        if current_symbol not in rules[state]:
            if '*' in rules[state]:
                current_symbol = '*'

            else:
                return 'ERR'

        (new_symbol, move_left, state) = rules[state][current_symbol]

        if new_symbol != '*':
            data[strip_position] = new_symbol

        if move_left == 'r':
            strip_position += 1

            if strip_position > (len(data) - 1):
                data.append('_')

        if move_left == 'l':
            if strip_position == 0:
                data.insert(0, '_')

            else:
                strip_position -= 1

        current_symbol = data[strip_position]

    return ''.join(data)


def main():
    if len(sys.argv) < 2:
        print("[USO]: python main.py datafile")
        sys.exit(1)

    try:
        with open(sys.argv[1], "r", encoding="utf-8") as file:
            for teste in file.readlines():
                (tur_name, input_data) = teste.split(',')
                input_data = input_data.replace('\n', '')

                with open(tur_name, "r", encoding="utf-8") as tur_file:
                    rules = turing_parser(remove_comments(tur_file))
                    result = execute(input_data.replace(' ', '_'), rules).replace('_', ' ').strip()
                    print(f"{tur_name},{input_data},{result}")

    except FileNotFoundError as error:
        print(f"Error {error}")
        sys.exit(1)


if __name__ == '__main__':
    main()
