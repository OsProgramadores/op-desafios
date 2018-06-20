inicial = int(input('Número Inicial: '))
final = int(input('Número Final: '))


for numero in range(inicial, final+1):
    numero = str(numero)
    if numero == numero[::-1]:
        print(numero)

