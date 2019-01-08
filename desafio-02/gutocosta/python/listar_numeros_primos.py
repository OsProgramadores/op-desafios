'''
    Programa para listar todos os números primos entre 1 e 10000
'''

VALOR_LIMITE = 10000
LISTA_NUM_INT = [True for i in range(VALOR_LIMITE+1)]
P = 2

while P * P <= VALOR_LIMITE:
    if LISTA_NUM_INT[P]:
        for i in range(P * 2, VALOR_LIMITE+1, P):
            LISTA_NUM_INT[i] = False
    P += 1

for P in range(2, VALOR_LIMITE):
    if LISTA_NUM_INT[P]:
        print(P)
