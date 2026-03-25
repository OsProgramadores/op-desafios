"""
CODIGO PARA LISTAR NUMEROS PALINDROMOS COM LIMITES DEFINIDOS PELO USUARIO
"""

i = 0

#LENDO LIMITE INFERIOR
lim1 = int(input('Digite limite inferior, nao menor que 1: '))
while lim1 < 1 or lim1 > 18446744073709551615:
    lim1 = int(input('Valor fora do limite, tente novamente: '))

#LENDO LIMITE SUPERIOR
lim2 = int(input('Digite limite superior: '))
while lim2 < lim1 or lim2 > 18446744073709551615:
    lim2 = int(input('Valor fora do limite, tente novamente: '))

#LOOP PARA ITERACAO ENTRE OS LIMITES
for n in range(lim1, lim2, 1):
    N1 = str(n)
    N1INVERSO = ''

#LOOP PARA TESTAR E LISTAR NUMERO CASO SEJA PALINDROMO
    for i in range(len(N1)-1, -1, -1):
        N1INVERSO += N1[i]
    if N1 == N1INVERSO:
        print('{}'.format(N1))
