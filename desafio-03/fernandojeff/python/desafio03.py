def eh_palindromo(num):
    return str(num) == str(num)[::-1]

def encontrar_palindromos(inicio, fim):
    for num in range(inicio, fim + 1):
        if eh_palindromo(num):
            print(num)

# Numero inicial
start = int(input("Digite o numero INICIAL: "))

# Numero final
limit = int(input("Digite o numero FINAL: "))

encontrar_palindromos(start, limit)
