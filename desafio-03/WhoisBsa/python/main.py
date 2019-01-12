
""" Números Palindrômicos """


""" Declaração do intervalo """
while True:
    inicio = int(input('Valor inicial: '))
    fim = int(input('Valor final: '))
    if inicio >= fim:
        print('Valor inicial maior que o final, tente novamente')
    else:
        break

""" Verificação de palíndromo """
for numero in range(inicio, fim + 1):
    if numero == int(str(numero)[::-1]):
        print(numero)
