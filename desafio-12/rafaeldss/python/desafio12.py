"""
    Desafio 12 do site osprogramadores.com
"""


def ispow(number):
    '''
    Expoente do número
    '''
    for ex in range(number+1):
        if 2 ** ex == number:
            print(f'{number} true {ex}')

        elif 2 ** ex > number:
            print(f'{number} false')
            break

with open('d12.txt', 'r') as file:
    data = file.readlines()

for numero in data:
    ispow(int(numero))
