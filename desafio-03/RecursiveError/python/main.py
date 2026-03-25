"""
Solução desafio 3
Author: Guilherme Silva Schultz
Data: 23-01-2023

retorna todos os numeros palíndromo em uma sequência
"""

import sys

def check_pali(num_input: int) -> bool:
    """
    retorna se um numero é palíndromo

    pega cada digito do numero de entrada
    coloca em ordem invertida em number_result
    e compara os resultado, caso verdadeiro os numeros são palíndromo
    """
    number_digits = 1
    number_result = num_input // number_digits % 10
    number_digits *= 10
    while number_digits < num_input:
        number_result *= 10
        number_result += num_input // number_digits % 10
        number_digits *= 10

    return number_result == num_input


def get_pali(begin:int, end:int)->list:
    """
    retorna uma lista com todos os palíndromo
    apenas filta o iterable retornado pelo range() com a função check_pali
    """
    step = 1 if begin <= end else -1
    return list(filter(check_pali, range(begin, end+1,step)))


def main():
    """
    função principal
    """
    if len(sys.argv) < 3:
        print("chame este programa com dois valores numericos: python main.py begin end")
        print("Ex: python main.py 0 1000 para retornar todos os palíndromo entre 0 e 1000")
        sys.exit(1)

    try:
        begin = int(sys.argv[1])
        end = int(sys.argv[2])
    except ValueError:
        print("input invalido!")
        sys.exit(1)

    for num in get_pali(begin, end):
        print(num, end=' ')
    print('\n')

if __name__ == '__main__':
    main()
