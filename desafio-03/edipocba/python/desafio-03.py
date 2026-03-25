"""Algoritmo para identificação de números
palíndromos em um intervalo de valores digitados pelo usuário."""
def palindromo(vi, vf):
    """Função que identifica quais números são
    palíndomos em um intervalor de valores."""
    for numero in range(vi, vf+1):
        aux = str(numero)
        if aux == aux[::-1]:
            print("{}".format(aux))

valorInicial = 1
valorFinal = 0

while(valorInicial > valorFinal or valorFinal < 0 or valorInicial < 0):
    valorInicial = int(input("digite um número inicial: "))
    valorFinal = int(input("digite um número final: "))
    if valorInicial > valorFinal:
        print("POR FAVOR, DIGITE UM NÚMERO INICIAL MENOR QUE O NÚMERO FINAL.")
    elif valorInicial < 0 or valorFinal < 0:
        print("POR FAVOR, NÃO DIGITE NÚMEROS NEGATIVOS")

palindromo(valorInicial, valorFinal)
