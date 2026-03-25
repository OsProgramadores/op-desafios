#! python3
#coding: utf-8

""" Desafio 12 - Matheus Barbosa Souza """

def check_exponentiation(number):
    """ Checks whether a number is a power of 2 or not """

    i = 0
    while 2 ** i <= number:
        if 2 ** i == number:
            return True, i
        i += 1
    return False, i


def main():
    """ Main Function """

    with open('d12.txt', 'r') as file:
        numbers = file.readlines()
        for number in numbers:
            ispower, num = check_exponentiation(int(number))
            if ispower:
                print(f'{int(number)} true {num}')
            else:
                print(f'{int(number)} false')

if __name__ == "__main__":
    main()
