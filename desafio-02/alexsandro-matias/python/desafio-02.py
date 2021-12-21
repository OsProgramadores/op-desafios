def verifica_primo(numero):
    contador = 0
    for i in range (numero):
        i = i + 1
        if numero % i == 0:
            contador = contador + 1

    if contador == 2:
        print(numero)

for i in range(10000):
    verifica_primo(i)
