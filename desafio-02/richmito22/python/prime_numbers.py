import math

for i in range(2,10001):    #Percorre números de 2 até 10.000(Número 1 não é primo).

    raiz_quadrada = int(math.sqrt(i))    #identifica a raiz quadrada do número atual.

    for x in range(2, raiz_quadrada + 1):#percorre raiz_quadrada do loop. Início: 2, + 1 no final.

        if i % x == 0:    #verifico se o resto da divisão entre i e x é igual a 0.
            break #Não preciso continuar no loop, se já encontrei o divisor.

    else:
        print(i)    #Imprimir números que não foram encontrados divisores.
