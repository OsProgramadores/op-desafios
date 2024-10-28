def eh_palindromo(num):
    return str(num) == str(num)[::-1]

def encontrar_palindromos(start, limit):
    for num in range(start, limit + 1):
        if eh_palindromo(num):
            print(num)

# Numero inicial
start = 3000

# Numero final
limit = 3010

encontrar_palindromos(start, limit)
