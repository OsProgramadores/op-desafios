""" Resolução do Desafio 3 em Python """


def is_palindrome(num):
    """ Converte um número em string, o inverte e verifica
    se ele é igual ao número original """

    split_num = [n for n in str(num)]
    split_num.reverse()
    reversed_num = ''
    for n in split_num:
        reversed_num += n
    if int(reversed_num) == num:
        print(reversed_num)


num_inicial = 0
num_final = 10

print(f'\nNúmeros palíndromos entre {num_inicial} e {num_final}:\n')

for i in range(num_inicial, num_final):
    is_palindrome(i)
