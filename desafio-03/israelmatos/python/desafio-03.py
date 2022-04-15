'''
Autor: Israel Matos(@lolzaws)
Descrição: Soluao do desafio 03(https://osprogramadores.com/desafios/d03/)
Data: 15/04/22
'''

# numero de início
x = int(input('Número inicial: '))

# número final
n = int(input('Número final: '))


for i in range(x, n):
	i = str(i)
	z = i[::-1]
	if i == z:
		print(i)
	else:
		continue
