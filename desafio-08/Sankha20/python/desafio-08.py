from os import path
from sys import exit as sys_exit

file_name = "frac.txt"

class Fraction:
    def __init__(self, numerator, denominator = 1):
        self.original = f'{numerator}/{denominator}'
        self.numerator = numerator
        self.denominator = denominator
        self.integer = 0

        self.simplify()


    def simplify(self):
        mdc = MDC(self.numerator, self.denominator)
        if mdc > 1:
            print("MDC: ", self.numerator, self.denominator)
            self.numerator //= mdc
            self.denominator //= mdc

        if self.denominator in (0, 1):
            return

        self.integer = self.numerator // self.denominator
        self.numerator = self.numerator - (self.integer * self.denominator)


    def __str__(self):
        if self.denominator == 0:
            return "ERR"

        if self.denominator == 1:
            return str(self.numerator)

        if self.numerator == 0:
            return str(self.integer)

        returnValue = f'{self.numerator}/{self.denominator}'

        if self.integer != 0:
            returnValue = f'{self.integer} {returnValue}'

        return returnValue


def MDC(x, y):
    if y == 0:
        return x

    return MDC(y, (x % y))

def read_file_lines(file_path: str) -> list[str]:
    if path.isfile(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()

    print("Arquivo não encontrado.")
    return None


def read_file(file_path: str) -> list[str]:
    while True:
        file_lines = read_file_lines(file_path)
        if file_lines:
            return file_lines

        file_path = input("Por favor, digite o endereço de arquivo válido ou 'S' para sair.\n> ")
        if file_path.upper() == "S":
            sys_exit()


def convertToInteger(string: str) -> int:
    try:
        number = int(string)
        return number
    except ValueError:
        print(f'Uma entrada inválida encontrada: {string}')

    return None


def parseFraction(fractionString: str) -> Fraction:
    parts = fractionString.split("/")
    numerator = 0
    denominator = 1

    length = len(parts)

    if length < 1:
        return None

    if length >= 1:
        numerator = convertToInteger(parts[0])
        if not numerator:
            return None

    if length >= 2:
        denominator = convertToInteger(parts[1])
        if denominator is None:
            return None

    return Fraction(numerator, denominator)


def parseFractions(fractionList: list[str]) -> list[Fraction]:
    fractions = []

    for fractionString in fractionList:
        fraction = parseFraction(fractionString.strip())
        if fraction:
            fractions.append(fraction)

    return fractions


def printFractions(fractions:list) -> None:
    for fraction in fractions:
        print(fraction)


def main():
    file_lines = read_file(file_name)
    fractions = parseFractions(file_lines)
    printFractions(fractions)


if __name__ == "__main__":
    main()
