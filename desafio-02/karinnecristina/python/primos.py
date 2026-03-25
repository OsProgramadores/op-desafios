'''Descrição: Solução do desafio-02 - osprogramadores.com
Autor(a): karinnecristina
Linguagem: Python'''

for numero in range(1, 10001):
    if numero > 1:
        for divisor in range(2, numero):
            if numero % divisor == 0:
                break
        else:
            print(numero)
