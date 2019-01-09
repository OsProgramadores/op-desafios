'''
   Programa para imprimir todos os números palindrômicos entre dois outros números
'''

NUMERO1 = 1
NUMERO2 = 20

for i in range(NUMERO1, NUMERO2+1):
    if str(i) == (''.join(reversed(str(i)))):
        print(i, 'eh palidronomo')
