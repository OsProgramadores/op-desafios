#!/usr/bin/env python3

'''main module
'''


__author__ = 'Alexandre Pierre'


from sys import argv
import parseexpression as pexp


if __name__ == '__main__':
    with open(argv[1], 'r', encoding='ascii') as fp:
        for line in fp:
            try:
                print(pexp.evaluate(line))
            except (pexp.ErrDivByZero, pexp.ErrSyntax) as error:
                print(error)
