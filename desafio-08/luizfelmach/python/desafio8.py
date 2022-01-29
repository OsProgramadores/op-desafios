''' Convert fractions.'''

def min_fraction(numerator, denominator):
    ''' Take a a min fraction.'''
    finalized = False
    count = 2
    while not finalized:
        if numerator % count == 0 and denominator % count == 0:
            numerator = int(numerator/count)
            denominator = int(denominator/count)
        else:
            count += 1
        if count > numerator or count > denominator:
            finalized = True
            return [numerator, denominator]

def parser(line):
    ''' Parser fractions.'''
    line_split = line.split('/')
    if len(line_split) == 1:
        return int(line_split[0])
    numerator = int(line_split[0])
    denominator = int(line_split[1])
    if denominator == 0:
        return "ERR"
    [numerator, denominator] = min_fraction(numerator, denominator)
    if numerator % denominator == 0:
        return numerator//denominator
    if numerator % 2 == 0 and denominator % 2 == 0:
        return parser(f"{int(numerator/2)}/{int(denominator/2)}")
    if denominator % numerator == 0 and numerator != 1:
        return f"{1}/{denominator//numerator}"
    if denominator > numerator:
        return f"{numerator}/{denominator}"
    first = int((numerator-numerator%denominator)/denominator)
    newNumerator = numerator%denominator
    return f"{first} {newNumerator}/{denominator}"

with open("frac.txt", "r") as file:
    for l in file:
        print(parser(l))
