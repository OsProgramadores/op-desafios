#!/usr/bin/env python3

'''main module
'''


__author__ = 'Alexandre Pierre'


from sys import argv
from math import ceil, log10
from typing import Set, Tuple, Iterable, Callable
from functools import reduce
from operator import or_


def is_palindrome(number:int) -> bool:
    '''Checks whether a number is a palindrome.'''
    str_number = str(number)
    return str_number == str_number[::-1]

def palindromic_basis(number_of_digits: int) -> Tuple[int]:
    '''Returns a tuple with palindromes that for a basis-like structure (like
in Linear Algebra) for all the palindromes with a certain number of digits.'''
    binary_palindromes = set((10**exp10 + 10**(number_of_digits - 1 - exp10)
                              if exp10 != number_of_digits - 1 - exp10
                              else 10**exp10
                              for exp10 in range(number_of_digits//2 + 1)))
    return tuple(sorted(binary_palindromes, reverse=True))

def coeff_bounds(basis:Tuple[int], lower_bound:int, upper_bound:int) -> range:
    '''Calculates bounds to the coefficients of the combinations to cut the
number of computations a little'''
    start = 2
    while lower_bound > basis[0] * start:
        start += 1
    stop = 9
    while upper_bound < basis[0] * stop:
        stop -= 1
    return range(start - 1, stop + 1)

def fixed_length_combinations(basis:Tuple[int], lower_bound:int,
                              upper_bound:int) -> Set[int]:
    '''Calculates the combinations with a fixed number of digits'''
    coeffs = ([coeff_bounds(basis, lower_bound, upper_bound)] +
              [range(1,10)]*(len(basis) - 1))
    palindromes_set = set(basis[0] * coeff for coeff in coeffs[0])
    for basis_number, coeff_list in zip(basis[1:], coeffs[1:]):
        palindromes_set |= set(basis_number * coeff + pal
                           for coeff in coeff_list
                           for pal in palindromes_set)
    return palindromes_set

def combinations(basis_iter:Iterable[Tuple[int]], lower_bound:int,
                 upper_bound:int) -> Set[int]:
    '''Calculate the union of the combination sets'''
    return reduce(or_,
                  (fixed_length_combinations(basis, lower_bound, upper_bound)
                   for basis in basis_iter))

def bound_filter_fn(lower:int, upper:int) -> Callable[[int], bool]:
    '''Returns a functions that takes a number and checks whether it's in the
desired open interval'''
    return lambda number: lower < number < upper

def bounded_palindromes(palindromes:set, lower_bound:int,
                        upper_bound:int) -> filter:
    '''Returns the palindromes bounded by lower_bound and upper_bound'''
    return filter(bound_filter_fn(lower_bound, upper_bound), palindromes)

def ceillog10(number: int) -> int:
    '''Returns the ceil of the log10 of a number converted to int'''
    return int(ceil(log10(number)))

def closedrange(start:int, stop:int, step:int = 1) -> range:
    '''Provides a range with at least the start value.'''
    open_range = range(start, stop, step)
    if len(open_range) == 0:
        return range(start, start + 1, 1)
    return open_range

def digitsrange(lower_bound:int, upper_bound:int) -> range:
    '''Provides the range of digits number from lower_bound to upper_bound'''
    start = 1
    if lower_bound != 0:
        start = ceillog10(lower_bound)
    upper_exp = ceillog10(upper_bound) - 1
    if lower_bound == 10**start or not str(lower_bound).replace('9', ''):
        start += 1
    if upper_bound <= 10**upper_exp + 1:
        return closedrange(start, upper_exp + 1)
    return closedrange(start, upper_exp + 2)

if __name__ == '__main__':
    lower_bound_palindromes, upper_bound_palindromes = int(argv[1]), int(argv[2])
    digits = digitsrange(lower_bound_palindromes, upper_bound_palindromes)
    curr_basis = list(map(palindromic_basis, digits))
    digits_palindromes = combinations(curr_basis, lower_bound_palindromes,
                               upper_bound_palindromes)
    ans = bounded_palindromes(digits_palindromes, lower_bound_palindromes,
                              upper_bound_palindromes)
    print(*ans, sep=', ')
