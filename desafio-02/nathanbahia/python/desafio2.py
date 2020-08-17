'''
RESOLUÇÃO DO DESAFIO 2 EM PYTHON

Modifiquei a função e ficou bem mais rápida a execução, obrigado!

Fonte de Pesquisa:

https://brasilescola.uol.com.br/matematica/
como-reconhecer-os-numeros-primos.htm
'''


primos = []


def verifica_primo(num):
    ''' Recebe um número como parâmetro avalia se ele é primo ou não '''
    div = 2
    while True:
        if num // div < div:
            primos.append(num)
            return
        elif num % div == 0:
            return
        else:
            div += 1


for i in range(2, 10000):
    verifica_primo(i)

print(primos)
