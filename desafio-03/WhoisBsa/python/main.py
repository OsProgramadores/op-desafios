
""" Números Palindrômicos """


""" Declaração do intervalo """
while True:
    INICIO = int(input('Valor inicial: '))
    FIM = int(input('Valor final: '))
    if INICIO >= FIM:
        print('Valor inicial maior que o final, tente novamente')
    else:
        break

""" Verificação de palíndromo """
for numero in range(INICIO, FIM + 1):
    if numero == int(str(numero)[::-1]):
        print(numero)
