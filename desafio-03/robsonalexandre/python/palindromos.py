#!/usr/bin/env python3
""" Desafio 03: Imprimir todos os números palindrômicos entre dois outros números """
import sys
def main():
    """ Inverte número e imprime se igual ao seu reverso. """
    for num in range(int(sys.argv[1]), int(sys.argv[2])):
        if int(str(num)[::-1]) == num:
            print(num)

if len(sys.argv) > 1:
    main()
else:
    print("É necessário informar 2 números:\n  palindromos.py NUM NUM")
