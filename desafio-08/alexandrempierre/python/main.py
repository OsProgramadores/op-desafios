#!/usr/bin/env python3
'''main module

Module where the code is executed and the challenge solved
'''


__author__ = 'Alexandre Pierre'


from sys import argv
from fraction import Fraction

if __name__ == '__main__':
    with open(argv[1], 'r') as fp:
        for line in fp:
            print(Fraction(line).extract_whole().reduce())
