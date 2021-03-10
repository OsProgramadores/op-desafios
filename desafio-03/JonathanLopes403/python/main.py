"""
Esse progama mostrar todos os números palindrômicos entre um número e outro
"""
import sys

def num_palindromicos(inicio, fim):
    # Conjunto dos números que são palindrômicos
    palindromicos = set()
    # Verifica se fim é menor que inicio e se o número é maior que um unsigned int de 64 bits
    if inicio > 18446744073709551615 or fim > 18446744073709551615:
        print("Os números passados devem ser menor que 18446744073709551615!")
        sys.exit(1)
    elif fim < inicio:
        print ("Número de fim é menor que o do inicio!")
        sys.exit(1)
    # Verifica se os números passados são positivos:
    if inicio < 0 or fim < 0:
        print("Só devem ser passado números positivos!")
        sys.exit(1)
    # Printa os números palindrômicos
    for numero in range(inicio, fim+1):
        # Convertendo o número para string para verificar se é palindrômico
        reverse_number = str(numero)[::-1]
        if str(numero) == reverse_number:
            palindromicos.add(numero)
    return palindromicos

numeros = num_palindromicos(0, 1000)
# Colocando em Ordem Crescente
numeros_ordenados = list(numeros)
numeros_ordenados.sort()
print(numeros_ordenados)
