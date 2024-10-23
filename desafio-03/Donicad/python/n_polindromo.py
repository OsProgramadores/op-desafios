try:
    numero_incial = int(input("Digite um numero inicial: "))
    numero_final = int(input("Digite um numero final: "))
    if numero_incial < 0 or numero_final < 0:
        raise ValueError("Apenas números positivos")
except ValueError as erro:
    print(f"Erro: {erro}")

numeros_palindromos = []

for numero in range(numero_incial, numero_final + 1):
    if str(numero) == str(numero)[::-1]:
        numeros_palindromos.append(numero)

if numeros_palindromos:
    print(numeros_palindromos)
