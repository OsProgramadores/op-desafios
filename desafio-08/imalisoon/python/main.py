#!/bin/usr/env python3
# author: Alison gh: @imalisoon


import sys
import math

def load_file(name_file: str):
    _list: list = []

    with open(name_file, "r") as file:
        for line in file.readlines():
            _list.append(line.strip())

    return _list

def main(frac_list):
    for i in frac_list:
        fraction = i.split("/")

        if len(fraction) == 1:
            print(i)
            continue

        try:
            numerator, denominator = int(fraction[0]), int(fraction[1])
            int_division = numerator // denominator
            rest_division = numerator % denominator
            max_division_common = math.gcd(numerator, denominator)

            if rest_division == 0:
                print(int_division)
                continue

            denominator //= max_division_common
            rest_division //= max_division_common

            num_string = f"{int_division} " if int_division != 0 else ""
            print(f"{num_string}{rest_division}/{denominator}")

        except ZeroDivisionError:
            print("ERR")
            continue


if __name__ == "__main__":
    _file = sys.argv

    if len(_file) == 2:
        _frac_list = load_file(_file[1])
        main(_frac_list)

    elif len(_file) <= 1:
        print("[USO] python main.py arquivo.txt")

    else:
        print("[ERRO] passe apenas 1 argumento.")
