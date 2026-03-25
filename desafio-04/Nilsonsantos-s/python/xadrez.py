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
    contador_de_erros = 0
    dicionario = {1: numero.isnumeric(), 2: len(numero) == 8,
                  3: '7' not in numero and '8' not in numero and '9' not in numero}
    if False in dicionario.values():
        while False in dicionario.values():
            contador_de_erros += 1
            avisodado = False
            if contador_de_erros % 3 == 0:
                avisodado = True
                aviso()
            if not dicionario[3]:
                if avisodado is False:
                    print('*Só pode haver dígito menor que 7')
                numero = input(f'Linha {contador}- ')
            elif not dicionario[1]:
                if avisodado is False:
                    print('*Somente números são aceitos')
                numero = input(f'Linha {contador}- ')
            elif not dicionario[2]:
                if avisodado is False:
                    print('*As linhas precisam ter 8 dígitos')
                numero = input(f'Linha {contador}- ')
            dicionario[1] = numero.isnumeric()
            dicionario[2] = len(numero) == 8
            dicionario[3] = '7' not in numero and '8' not in numero\
                            and '9' not in numero
    return numero

def aviso():
    """
    Um aviso sobre o que deve ser preenchido nas linhas.
    """
    print('ATENÇÃO:\n-As linhas precisam ter 8 dígitos')
    print('-Só pode haver dígito menor que 7')
    print('-Somente números são aceitos')
aviso()
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
