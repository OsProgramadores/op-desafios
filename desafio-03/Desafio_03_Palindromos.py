# Desafio números Palíndromos
# https://osprogramadores.com/desafios/d03/
# Developer: Andre Félix
# Email: 2011349@univesp.aluno.br
# 25 de novembro de 2020

# Objetivo do código
# Imprimir os números palindrômicos entre duas variaveis.

# variaveis


inic = int
fim = int

# Definição das funções


def valida_entrada(min, max):
    valida = 0
    while valida == 0:
        print("Insira o numero inicial: \n")
        min = int(input())
        if min >= 0:
            print("Insira o numero final: \n")
            max = int(input())

            if max > min:
                valida = 1
                return min, max
            else:
                print("Número invalido!\nNúmero final deve ser maior que o numero inicial.")

        else:
            print("Número invalido!\nNúmero inicial deve ser maior que 0")


def palindromo(a, b):
    print("\n\n*********************************"
          "\nOs números palindrômicos são:\n"
          "*********************************\n")
    while a < b:

        c = int(str(a)[::-1])

        if a <= 9:
            print(a)
        elif a == c:
            print(a)
        a += 1

# lógica principal
inic, fim = valida_entrada(inic, fim)
palindromo(inic, fim)


