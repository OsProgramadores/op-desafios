"""
1. criar uma lista de numeros primos
2. criar um for ou while que percorra toda a lista dividindo o numero x por todos os anteriores
3. se um deles der resto 0, ele não é primo
4. se ele for primo, dê print

"""
# criando variáveis
lista_numeros = [];
lista_numeros1 = [];
primos = [];
acc = 0;

# populando a lista de numeros
for x in range(1, 10000):
    lista_numeros.append(x);

for x in range(1, 10000):
    lista_numeros1.append(x);

# calculando se ele é primo ou se não é
for x in range(0, 9999):
    for y in range(0, 9999):
        if lista_numeros[x] % lista_numeros1[y] == 0:
            acc += 1;
    if acc == 2:
        print(lista_numeros[x]); # printa o número primo
        acc = 0;
    else:
        acc = 0;
