"""
    @Author: Thiago Felix
    Propósito: Resolução do desafio-2
"""

prime = []

for num in range(2, 1000):
    # Validando se o numero não é divisivel por 2 3 5 7
    if not(num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0) or num in [2, 3, 5, 7]:
        prime.append(num)

print(prime)