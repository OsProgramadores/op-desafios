#!/usr/bin/env python3

'''main module
'''


__author__ = 'Alexandre Pierre'


from sys import argv
import reverseread as rr


if __name__ == '__main__':
    with open(argv[1], 'rb') as fp:
        for line in rr.reverse_readlines(fp):
            print(line.decode('utf8'))
