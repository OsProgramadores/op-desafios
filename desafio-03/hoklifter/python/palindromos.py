'''Encontrar palíndromos entre dois números.'''
try:
    NUM1 = int(input('Digite o PRIMEIRO número:    '))
    NUM2 = int(input('Digite o SEGUNDO número:    '))
    if NUM1 > NUM2:
        for x in range(NUM1, NUM2+1):
            if str(x)[::-1] == str(x):
                print(x)
    else:
        raise ValueError
except ValueError:
    print('Número invalido')
