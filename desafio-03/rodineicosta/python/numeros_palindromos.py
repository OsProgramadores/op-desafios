#!/usr/bin/python3
'''
Desafio #3 - OsProgramadores
Imprimir todos os números palindrômicos entre dois números.
Rodinei Costa (https://repl.it/@rodineicosta/numeros_palindromos)
'''

def main():
    ''' Definição do intervalo de números '''
    inicio = int(str(input('Digite o número inicial: ')))
    fim = int(str(input('Digite o número final: ')))

    #Validação do intervalo
    if inicio < 1 or fim < 1:
        print('Favor inserir um número maior que zero!')

    elif inicio > ((1 << 64) -1) or fim > ((1 << 64) -1):
        print('Número muito grande, insira um número menor!')

    elif inicio >= fim:
        print('Favor inserir um número final maior que o número inicial!')

    else:
        for numero in range(inicio, fim + 1):
            #Impressão dos números, caso existam
            if numero == int(str(numero)[::-1]):
                print('O número', numero, 'é palíndromo')

if __name__ == "__main__":
    main()
