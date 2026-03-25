# Desafio 02 - OsProgramadores
# Nicholas Borba

lista = []; listaPrimos = []
for num in range(1, 10000, 2): #Preenche com números impares
    lista.append(num)

lista.insert(1,2) #Acrescenta o número 2 na lista na 2ª posição, ele é único número primo, por isso acrescentado assim

for num in lista: #Varre a lista
    prova = 0; x = 1
    while x <= num:
        if num%x == 0:
            prova+=1
            if prova >= 3: #Se prova > 3, o número foi dividido com resto zero mais de duas vez (1 e ele mesmo), então não é primo
                break
        x+=1
    if prova == 2:
        listaPrimos.append(num)

print(listaPrimos)
