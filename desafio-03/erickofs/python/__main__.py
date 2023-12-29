"""
This is the main file of the project. It calls the PalCalc class and prints the palindromes.
"""
from palcalc import PalCalc

if __name__ == "__main__":

    pn = PalCalc()
    for i in pn.show_palindromes():
        print(i)
