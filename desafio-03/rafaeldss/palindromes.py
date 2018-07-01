inicio = int(input())
fim = int(input())

for numero in range(inicio, fim+1):
    numero = str(numero)
    if numero == numero[::-1]:
        print(numero)
