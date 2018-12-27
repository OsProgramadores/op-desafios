"""
Desafio 3 - Adriano Roberto de Lima
"""
number1 = 1001
number2 = 5005

for i in range(number1, number2+1):
    s = str(i)
    if s == s[::-1]:
        print(i)
        
