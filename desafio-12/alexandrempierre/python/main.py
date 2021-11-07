#!/usr/bin/env python3

'''main module
'''


__author__ = 'Alexandre Pierre'


from sys import argv

def find_interval(n, min_exp=0, max_exp=1):
    '''Find a suitable interval to bissection.'''
    return (
        find_interval(n, max_exp, 2*max_exp)
        if 2**max_exp < n
        else (min_exp, max_exp))

def is_successor(n, m):
    '''Checks whether one argument os successor of the other.'''
    return m - n == 1 or n - m == 1

def bissect(n, min_exp, max_exp):
    '''Performs a binary search to find out whether n is a power of 2.'''
    if is_successor(min_exp, max_exp):
        if n == 2**min_exp:
            return True, min_exp

        if n == 2**max_exp:
            return True, max_exp

        return False, -1

    middle_point = (min_exp + max_exp) // 2

    if n < 2**middle_point:
        return bissect(n, min_exp, middle_point)

    if n > 2**middle_point:
        return bissect(n, middle_point, max_exp)

    return True, middle_point


if __name__ == '__main__':
    with open(argv[1]) as fp:
        for line in fp:
            num = int(line[:-1])
            x0, x1 = find_interval(num)
            is_power, exp = bissect(num, x0, x1)
            print(f'{num}', f'true {exp}' if is_power else f'false', sep=' ')
