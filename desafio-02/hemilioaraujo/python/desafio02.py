'''
Resolução de Hemílio Araújo
Github: @hemilioaraújo
'''

inicio = 2
fim = 10000
trigger = True
primos = []

while inicio < fim:
    divisor = 1
    cont = 0
    # encontra o primeiro número primo
    while divisor <= inicio and trigger:
        if inicio % divisor == 0:
            cont += 1
        if inicio == divisor and cont == 2:
            primos.append(inicio)
            trigger = False
        divisor += 1
    inicio += 1

for num in range(primos[0]+1, fim):
    for item in primos:
        if num % item == 0:
            break
    else:
        primos.append(num)

print(primos)
