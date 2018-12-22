#Numeros primos ate 10000
#Autor: Wilque Muriel
from math import sqrt
#Gerando lista com numeros impares ate 10000
ListaN = [2]#Colocando o 2 unico par primo
for i in range (0, 10001):
    if (i%2 == 1):
        ListaN.append(i)
ListaN.pop(1)#Gambiarra :)
def primo (n):#funcao que determina se e primo ou nao
    raiz = sqrt(n)#usando metodo por raiz quadrada do num
    partInt = round(raiz)#pegando o round do numero da raiz
    dtrmd = int()
    for i in range(1, partInt+1):#fazendo as contas entre o intervalo :)
        if (n%i == 0):
            dtrmd +=1
    if (dtrmd == 1):#caso seja primo
        print(n)
    return
for n in ListaN:
    primo(n)
