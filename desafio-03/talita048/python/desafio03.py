def eh_numero(val):
    return val.isdigit()

def eh_positivo(val):
    return int(val) >= 0

def check_numero(mensagem):
    while True:
        num = input(mensagem)
        if not eh_numero(num):
            print("Por favor, insira um número válido.")
        elif not eh_positivo(num):
            print("Por favor, insira um número positivo.")
        else:
            return int(num)

print("\nBem-vindo(a) ao detector de números palíndromos!")
print("Um número palíndromo é aquele que permanece igual quando lido de trás para frente.")
print("Insira dois números e vou te informar todos os palíndromos que existem entre eles :D")

while True:
    limite_a = check_numero("Digite o primeiro número: ")
    limite_b = check_numero("Digite o segundo número: ")
    if limite_a >= limite_b:
        print("O primeiro número deve ser menor que o segundo. Tente novamente.")
    else:
        break

lista_pal = []

while limite_a <= limite_b :
    reverso = int(str(limite_a)[::-1])
    if limite_a == reverso :
        lista_pal.append(limite_a)
    limite_a += 1

print("Números palíndromos encontrados:")
for palindromo in lista_pal:
    print(palindromo)
