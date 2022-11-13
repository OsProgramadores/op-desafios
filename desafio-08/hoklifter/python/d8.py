'''
Desafio 08 - Frações
'''
with open('frac.txt', 'r') as OPEN:
    READFILE = OPEN.readlines()

def m_d_c(num_1, num_2):
    '''Reduzir as mistas'''
    divisors_of_num_1 = []
    divisors_of_num_2 = []
    divisors_of_both = []

    for divnum_1 in range(1, num_1+1):
        if num_1 % divnum_1 == 0:
            divisors_of_num_1.append(divnum_1)
    for divnum_2 in range(1, num_2+1):
        if num_2 % divnum_2 == 0:
            divisors_of_num_2.append(divnum_2)

    if len(divisors_of_num_1) > len(divisors_of_num_2):
        for comparator in divisors_of_num_1:
            if comparator in divisors_of_num_2:
                divisors_of_both.append(comparator)

    else:
        for comparator in divisors_of_num_2:
            if comparator in divisors_of_num_1:
                divisors_of_both.append(comparator)

    return max(divisors_of_both, default=0)

def math_from_string(string):
    """Fração Mista."""

    if '/' in string:
        try:
            num_string = string.split('/')
            division_result = int(num_string[0]) // int(num_string[1])
            division_rest = int(num_string[0]) % int(num_string[1])

            mdc = m_d_c(division_rest, int(num_string[1]))

            if int(num_string[1]) == 1:
                print(num_string[0])
            elif division_result == 0:
                print(f"{division_rest // mdc}/{int(num_string[1]) // mdc}")
            elif int(num_string[0]) == int(num_string[1]):
                print(1)
            else:
                print(f"{division_result} {division_rest // mdc}/{int(num_string[1]) // mdc}")

        except ZeroDivisionError:
            print('ERR')

    else:
        print(string)

for READ in READFILE:
    READ = READ.replace('\n', '')
    math_from_string(READ)
