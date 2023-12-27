"""
This is the main file of the project.
"""
from palcalc import PalCalc

if __name__ == "__main__":

    pn = PalCalc()
    for i in pn.show_palindromes():
        print(i)
