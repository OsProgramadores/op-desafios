'''
Resolução de Hemílio Araújo
Github: @hemilioaraújo
'''

inicio = 2
fim = 10000
trigger = True
primos = []

for num in range(2, fim):
    for item in primos:
        if num % item == 0:
            break
    else:
        primos.append(num)

print(primos)
