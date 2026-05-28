#Programa que imprime todos os números palíndromos entre 100 e 10.000.

for numero in range(100,10001):

    numero=str(numero)

    if numero == numero[::-1]:

        print(numero)
