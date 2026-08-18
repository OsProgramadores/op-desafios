import math

for i in range(2,10001):    #Percorre números de 2 até 10.000(Número 1 não é primo).

    total_divisores = 0    #Contador, para contabilizar se o resto da divisão de i % x for 0.
    raiz_quadrada = int(math.sqrt(i))    #identifica a raiz quadrada do número atual.

    for x in range(2, raiz_quadrada +1):#percorre raiz_quadrada do loop. Início: 2, +1 no final.

        if i % x == 0:    #verifico se o resto da divisão entre i e x é igual a 0.
            total_divisores += 1    #Incremento 1 no contador, caso o primeiro if seja verdadeiro.

    if total_divisores == 0:    #Condição para saber se o contador está zerado.
        print(i)    #Mostrar númmeros do primeiro for, caso sejam primos.
        