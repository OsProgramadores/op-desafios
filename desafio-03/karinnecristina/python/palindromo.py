'''Descrição: Solução do desafio-03 - osprogramadores.com
Autor(a): karinnecristina
Linguagem: Python'''

for numero in range(1, 100000):
    inverso = str(numero)
    if inverso == inverso[::-1]:
        print(numero)
