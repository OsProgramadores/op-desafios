'''fraction module

Module with the data model of the fraction and the corresponding logic
'''


__all__ = ['Fraction']
__author__ = 'Alexandre Pierre'


def euler_gcd(m, n):
    '''Calculates greatest common divisor using Euler's algorithm'''
    while n != 0:
        m, n = n, m % n

    return m

def parse_fraction(fraction_str):
    '''Extract values that define a fraction from the corresponding text'''
    whole, n, d = 0, 0, 0
    fraction_str = fraction_str.replace('\n', '')
    if '/' in fraction_str:
        parts = fraction_str.split('/')
        n, d = int(parts[0]), int(parts[1])
    else:
        whole, d = int(fraction_str), 1

    return (whole, n, d)


class Fraction():
    '''Fraction representation'''
    whole, n, d = 0, 0, 0
    irreducible = False

    def __init__(self, fraction_str):
        '''Build an object with the values that define a fraction'''
        self.whole, self.n, self.d = parse_fraction(fraction_str)
        self.irreducible = self.n == 0 or self.d == 0
        if self.n == 0 and self.d != 0:
            self.d = 1

    def reduce(self):
        '''Change the fraction to its reduced equivalent'''
        if not self.irreducible:
            gcd = euler_gcd(self.d, self.n)
            self.n //= gcd
            self.d //= gcd
            self.irreducible = True

        return self

    def extract_whole(self):
        '''Extract the whole part of the fraction'''
        if self.n != 0 and self.d != 0:
            quocient = self.n // self.d
            self.whole += quocient
            if quocient != 0:
                self.n -= quocient*self.d

        return self

    def __repr__(self):
        fraction_repr = ''
        if self.d == 0:
            fraction_repr = 'ERR'
        elif self.n == 0:
            fraction_repr = f'{self.whole}'
        elif self.whole == 0:
            fraction_repr = f'{self.n}/{self.d}'
        else:
            fraction_repr = f'{self.whole} {self.n}/{self.d}'

        return fraction_repr
