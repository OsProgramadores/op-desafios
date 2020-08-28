""" Solução do desafio 12 em Python """


def is_power(num):
    """ Verifica se um número é petência de 2 e imprime
    na tela suas informações """
    c = 0
    n = 2
    while True:
        res = n ** c
        if res > num:
            print(num, 'false')
            return
        if res == num:
            print(num, 'true', c)
            return
        c += 1


with open('d12.txt', 'r') as txt:
    for line in txt.readlines():
        number = int(line)
        is_power(number)
