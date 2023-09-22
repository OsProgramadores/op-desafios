"""
    @Author: Thiago Felix.
    Propósito: Resolução do desafio-2.
"""
def verificaPrimos(number: int):
    for num in range(2, number + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            print(num)

verificaPrimos(10000)
