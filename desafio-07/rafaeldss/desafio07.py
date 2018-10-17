""" Desafio 7 feito em python - rafaeldss"""

import sys

FILE_NAME = sys.argv[1]

with open(FILE_NAME) as file:
    LINES = file.readlines()
INDEX = len(LINES)

while INDEX > 0:
    print(LINES[INDEX-1], end='')
    INDEX -= 1
