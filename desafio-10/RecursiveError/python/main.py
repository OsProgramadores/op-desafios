"""
Solução desafio 10
Author: Guilherme Silva Schultz
03/04/2023
"""

import sys
import re


def remove_comment(file):
    """
     remove toda sub-string que começa com ';' e termina com \n (não incluindo \n)
     """
    remove_string = re.sub(";(.*)(?=\n)", '', file.read()).splitlines()
    return [x for x in remove_string if x.strip() != ""]  #remove \n restante


def tur_parser(arq):
    """
     transforma as regras no arquivo.tur em um dicionario
     """
    rules = {}
    for line in arq:
        result = line.strip().split(" ")
        if result[0] not in rules:
            rules[result[0]] = {}
        rules[result[0]][result[1]] = (result[2], result[3], result[4])
    return rules


def check_generic_rule(sym, rules):
    """
     verifica se a regra generica pode ser executada
     """
    return (sym in rules['*']) or ('*' in rules['*'])


def execute(input_data, rules):
    """
     executa o programa
     """
    data = list(input_data)
    state = '0'
    strip_posi = 0
    corrent_sym = data[strip_posi]
    while 'halt' not in state:
        if '*' in rules:
            if check_generic_rule(corrent_sym, rules):
                state = '*'
        if state not in rules:
            return 'ERR'

        if corrent_sym not in rules[state]:
            if '*' in rules[state]:
                corrent_sym = '*'
            else:
                return 'ERR'

        (new_sym, move_dir, state) = rules[state][corrent_sym]

        if new_sym != '*':
            data[strip_posi] = new_sym

        if move_dir == 'r':
            strip_posi += 1
            if strip_posi > (len(data) - 1):
                data.append('_')
        if move_dir == 'l':
            if strip_posi == 0:
                data.insert(0, '_')
            else:
                strip_posi -= 1
        corrent_sym = data[strip_posi]

    return ''.join(data)


def main():
    """
     Programa principal
     """
    if len(sys.argv) < 2:
        print("Executa esse programa com: python main.py datafile")
        sys.exit(1)
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as file:
            for teste in file.readlines():
                (tur_name, input_data) = teste.split(',')
                input_data = input_data.replace('\n', '')
                with open(tur_name, "r", encoding="utf-8") as tur_file:
                    rules = tur_parser(remove_comment(tur_file))
                    result = execute(input_data.replace(' ', '_'),
                                     rules).replace('_', ' ').strip()
                    print(f"{tur_name},{input_data},{result}")
    except FileNotFoundError as error:
        print(f"Error {error}")
        sys.exit(1)


if __name__ == '__main__':
    main()
