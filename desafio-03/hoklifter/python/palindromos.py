'''Encontrar palíndromos entre dois números.'''
try:
    NUM1 = int(input('Digite o PRIMEIRO número:    '))
    NUM2 = int(input('Digite o SEGUNDO número:    '))
    if NUM1 > 0 and NUM2 > 0 <= 18446744073709551615:
        for x in range(NUM1, NUM2+1):
            if str(x)[::-1] == str(x):
                print(x)
except ValueError:
    print('Número invalido')
