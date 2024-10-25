def verificar_entrada(mensagem):
    entrada = input(mensagem)
    if not entrada.isdigit():
        print("Erro: Apenas números podem ser inseridos.")
        exit()
    
    numero = int(entrada)
    if numero < 0:
        print("Erro: Apenas números positivos podem ser inseridos.")
        exit()
    
    return numero

numero_incial = verificar_entrada("Digite um numero inicial: ")
numero_final = verificar_entrada("Digite um numero final: ")

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
