""" Resolução do Desafio 3 em Python """


def is_palindrome(num):
    """ Converte um número em string, o inverte e verifica
    se ele é igual ao número original """
   
    reversed_num = ''.join(list(str(num)))
    if int(reversed_num) == num:
        print(reversed_num)


num_inicial = 0
num_final = 1000

print(f'\nNúmeros palíndromos entre {num_inicial} e {num_final}:\n')

for i in range(num_inicial, num_final):
    is_palindrome(i)
