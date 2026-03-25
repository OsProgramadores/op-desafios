import sys

def verificar_entrada(mensagem):
    entrada = input(mensagem)
    if not entrada.isdigit():
        print("Erro: Apenas números positivos podem ser inseridos.")
        sys.exit()
    digito = int(entrada)
    if digito < 0:
        print("Erro: Apenas números positivos podem ser inseridos.")
        sys.exit()
    return digito

try:
    numero_incial = verificar_entrada("Digite um numero inicial: ")
    numero_final = verificar_entrada("Digite um numero final: ")
    if numero_final < numero_incial:
        print("Erro: O primeiro número deve ser menor que o segundo.")
        sys.exit()
except ValueError:
    print("Erro: Apenas números positivos podem ser inseridos.")

numeros_palindromicos = []

for numero in range(numero_incial, numero_final + 1):
    if str(numero) == str(numero)[::-1]:
        numeros_palindromicos.append(numero)

if numeros_palindromicos:
    print("Palindromos encontrados:")
    for polindromico in numeros_palindromicos:
        print(polindromico)
else:
    print("Nenhum palindromo encontrado com esse intervalo.")
