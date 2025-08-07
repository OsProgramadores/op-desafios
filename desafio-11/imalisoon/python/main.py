#!/usr/bin/python
# author: Alison gh: @imalisoon

import sys

def get_prime(limit: int):
    _primes = []

    for _num in range(2,limit+1, 1):
        for _prime in _primes:
            if _num % _prime == 0:
                break

        else:
            _primes.append(_num)

    return _primes


def load_file(_file):
    char = _file.read(1)
    _bytes = ""

    while char:
        _bytes += char
        char = _file.read(1)

        if char == '.':
            _bytes = ""
            char = _file.read(1)

        if char.isalpha():
            print("ERRO: arquivo deve conter apenas numeros")
            sys.exit(1)

    return _bytes


def generate_bigger_primes(prime_array, array, begin, sequence, bigger_sequence):
    char = ''
    prime_to_add = ''
    num = 0

    for i in range(begin,begin+4):
        try:
            char += array[i]
            num = int(char)

        except IndexError:
            break

        if num in prime_array:
            prime_to_add = sequence + char
            generate_bigger_primes(
                prime_array,
                array,
                i+1,
                prime_to_add,
                bigger_sequence
            )

    if len(prime_to_add) > len(bigger_sequence[0]):
        bigger_sequence.clear()
        bigger_sequence.append(prime_to_add[::])

primes = get_prime(10000)
biggest_sequence = [""]

if len(sys.argv) < 2:
    print("[USO]: python main.py numeros.txt")
    sys.exit(1)

file_name = sys.argv[1]

try:
    with open(file_name, "r", encoding = "utf-8") as file:
        loaded_file = load_file(file)

        for index in range(len(loaded_file)):
            generate_bigger_primes(
                primes,
                loaded_file,index,
                '', biggest_sequence
            )

        print(biggest_sequence[0])

except FileNotFoundError:
    print(f"arquivo: {file_name} não encontrado")
    sys.exit(1)
