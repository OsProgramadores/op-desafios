#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    Desenvolvido por Gabriel Ferreira (@GabrielF9)
    Solução para o Desafio 3 do site OsProgramadores
'''

if __name__ == '__main__':
    smaller, bigger = input().split()
    
    for num in range(int(smaller), int(bigger) + 1):
        str_num = str(num)
        if str_num == str_num[::-1]:
            print(str_num)
