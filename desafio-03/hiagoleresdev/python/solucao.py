#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    Desenvolvido por Hiago Leres da Costa (@hiagoleresdev)
    Solução para o Desafio 3 do site OsProgramadores
'''
palindromes = []
firstNumber = int(input('Type a first number to see all palindromes: '))
finalNumber = int(input('Type a final number to see all palindromes: '))


def isPalindrome(numero):
    """Verificando se o número é palindromo"""
    numberInverted = str(numero)[::-1]
    if int(numero) == int(numberInverted):
        palindromes.append(i)

for i in range(firstNumber, finalNumber):
    isPalindrome(i)

print(palindromes)
