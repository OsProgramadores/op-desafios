"""Este código imprime os números primos entre 1 e 10000."""
for numero in range(2, 10001):
    contador = 0
    for numeroDivisao  in range(1, numero+1):
        if numero%numeroDivisao == 0:
            contador += 1
    if contador == 2:
        print(numero)
