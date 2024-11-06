def eh_palindromo(num):
    return str(num) == str(num)[::-1]

def encontrar_palindromos(inicio, fim):
    for num in range(inicio, fim + 1):
        if eh_palindromo(num):
            print(num)

def verfi(entrada):
    max = (1 << 64) - 1

    try:
        numero = int(entrada)
    except ValueError:
        print("O valor digitado não é um número válido.")
        return False

    if numero <= 0:
        print("Digite um INTEIRO POSITIVO!")
        return False

    if numero > max:
        print("O numero execede o valor limite! Digite outro numero menor.")
        return False

    return numero

while True:
    primeiro_numero = input("Digite o numero INICIAL: ")

    if verfi(primeiro_numero) is False:
        continue

    start = verfi(primeiro_numero)

    break

while True:

    ultimo_numero = input("Digite o numero FINAL: ")

    if verfi(ultimo_numero) is False:
        continue

    limit = verfi(ultimo_numero)

    if limit < start:
        print("O ultimo numero deve ser menor que o primeiro.")
        continue

    break

encontrar_palindromos(start, limit)
