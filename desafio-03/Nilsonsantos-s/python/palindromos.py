"""
Autor: Nilsonsantos-s
Propósito: Desafio 3
"""

<<<<<<< HEAD

=======
>>>>>>> 734855543318b00a4ee3cc4a380026b733cd57a0
def gerar_positivo(numero, inicial=False, final=False):
    """
    :param numero: Pega um número para ser verificado
    :param inicial: Verifica se o número é um número inicial
    :param final: Verifica se o número é um número final
    :return: Retorna um número natural através do input do usuário.
    """
    if inicial is True:
<<<<<<< HEAD
        if numero < 0 or numeroinicial > INT64:
            while numero < 0 or numero > INT64:
                if numero > INT64:
                    print('Limite ultrapassado.')
                if numero < 0:
                    print('Digite apenas números naturais.')
                numero = int(input('Número inicial: '))
            return numero
    elif final is True:
        if numero < 0 or numerofinal > INT64:
            while numero < 0 or numero > INT64:
                if numero > INT64:
                    print('Limite ultrapassado.')
                if numero < 0:
                    print('Digite apenas números naturais.')
                numero = int(input('Número final: '))
            return numero
    return None

=======
        if numero < 0:
            while numero < 0:
                print('Digite apenas números naturais.')
                numero = int(input('Número inicial: '))
            return numero
    elif final is True:
        if numero < 0:
            while numero < 0:
                print('Digite apenas números naturais.')
                numero = int(input('Número final: '))
            return numero
>>>>>>> 734855543318b00a4ee3cc4a380026b733cd57a0

def gerar_numeros_palindromicos(inicial, final):
    """
    :param inicial: Pega o número inicial
    :param final: Pega o número final
    :return: Retorna números palidrômicos a partir do número
             inicial até o número final, contando o número final.
    """
    print('Números palindrômicos: ')
    if inicial < final:
<<<<<<< HEAD
        for numero in range(numeroinicial, numerofinal + 1):
=======
        for numero in range(numeroinicial, numerofinal+1):
>>>>>>> 734855543318b00a4ee3cc4a380026b733cd57a0
            lista_algarismos = ' '.join(str(numero)).split()
            lista_algarismos_reversa = lista_algarismos[::-1]
            if lista_algarismos == lista_algarismos_reversa:
                print(numero, end=' ')
    elif inicial > final:
<<<<<<< HEAD
        for numero in range(numeroinicial, numerofinal - 1, -1):
=======
        for numero in range(numeroinicial, numerofinal-1, -1):
>>>>>>> 734855543318b00a4ee3cc4a380026b733cd57a0
            lista_algarismos = ' '.join(str(numero)).split()
            lista_algarismos_reversa = lista_algarismos[::-1]
            if lista_algarismos == lista_algarismos_reversa:
                print(numero, end=' ')
    elif inicial == final:
        if inicial < 9:
            print(inicial)
        else:
            algarismo = ' '.join(str(inicial)).split()
            algarismo_reverso = algarismo[::-1]
            if algarismo == algarismo_reverso:
                algarismo = int(''.join(algarismo))
                print(algarismo)


<<<<<<< HEAD
# Programa principal:
# Lê os números, um por vez e utiliza uma condição para verificar se os
# números são negativos. Caso o número seja negativo, ele chama a função
# gerar_positivo. Depois de gerado os números positivos a função
# gerar_numeros_palindromicos é acionada.
INT64 = (1 << 64) - 1
numeroinicial = int(input('Número inicial: '))
if numeroinicial < 0 or numeroinicial > INT64:
    numeroinicial = gerar_positivo(numeroinicial, inicial=True)
numerofinal = int(input('Número final: '))
if numerofinal < 0 or numerofinal > INT64:
    numerofinal = gerar_positivo(numerofinal, final=True)
gerar_numeros_palindromicos(numeroinicial, numerofinal)
=======
"""
Programa principal:
Lê os números, um por vez e utiliza uma condição para verificar se os
números são negativos. Caso o número seja negativo, ele chama a função
gerar_positivo. Depois de gerado os números positivos a função
gerar_numeros_palindromicos é acionada.
"""
numeroinicial = int(input('Número inicial: '))
if numeroinicial < 0:
    numeroinicial = gerar_positivo(numeroinicial, inicial=True)
numerofinal = int(input('Número final: '))
if numerofinal < 0:
    numerofinal = gerar_positivo(numerofinal, final=True)
gerar_numeros_palindromicos(numeroinicial, numerofinal)



>>>>>>> 734855543318b00a4ee3cc4a380026b733cd57a0
