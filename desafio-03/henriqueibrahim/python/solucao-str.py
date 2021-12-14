input1 = int(input())
input2 = int(input())

numbersList = list(range(input1, input2 + 1)) # +1 para poder incluir o último número, já que começa a contar do 0

for n in numbersList:
    number = str(n) # [::-1] Não inverte int, por isso transforma em str
    if number == number[::-1]: # Confere se a string inicial é igual a string invertida.
        print(number)
