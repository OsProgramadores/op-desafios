# -*- coding: utf-8 -*-
"""
Created on Sun April 19 22:30:12 2020
Desafio 03 - Listar todos os numeros palindromos
@author: Hiago Leres
"""
palindromes = []
firstNumber = int(input('Type a first number to see all palindromes: '))
finalNumber = int(input('Type a final number to see all palindromes: '))


def isPalindrome(numero):    
    numberInverted = str(numero)[::-1]
        
    if int(numero) == int(numberInverted):
        palindromes.append(i)

for i in range(firstNumber, finalNumber):
    isPalindrome(i)

print(palindromes)

