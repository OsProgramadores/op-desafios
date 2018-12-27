"""
Desafio 3 - Adriano Roberto de Lima
"""
NUMBER1 = 1001
NUMBER2 = 5005

for i in range(NUMBER1, NUMBER2+1):
    s = str(i)
    if s == s[::-1]:
        print(i)
