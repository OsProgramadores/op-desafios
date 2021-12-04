"""
Autor: Nilsonsantos-s
Propósito: Desafio 4
"""


def verifica_string(numero):
    """
    :param numero: Exclui qualquer número que não se encaixe
                   no padrão correto.
    :return: retorna um número no padrão.
    """
    dicionario = {1: numero.isnumeric(), 2: len(numero) == 8,
                  3: '7' not in numero and '8' not in numero and '9' not in numero}
    if False in dicionario.values():
        while False in dicionario.values():
            if not dicionario[3]:
                print('Digite somente algarismos menores que 7.')
                numero = input()
            elif not dicionario[1]:
                print('Digite somente números.')
                numero = input()
            elif not dicionario[2]:
                print('Digite 8 algarismos.')
                numero = input()
            dicionario[1] = numero.isnumeric()
            dicionario[2] = len(numero) == 8
            dicionario[3] = '7' not in numero and '8' not in numero\
                            and '9' not in numero
    return numero

lista = []
for contador in range(1, 9):
    for string in [input(f'Linha {contador}- ')]:
        string = string.replace(' ', '')
        lista.append(verifica_string(string))

fragmento = []
for numeros in lista:
    fragmento += numeros

pecas = {'Peão': fragmento.count('1'), 'Bispo': fragmento.count('2'),
         'Cavalo': fragmento.count('3'), 'Torre': fragmento.count('4'),
         'Rainha': fragmento.count('5'), 'Rei': fragmento.count('6')}

for key, value in pecas.items():
    print(f'{key}: {value} peça(s)')
