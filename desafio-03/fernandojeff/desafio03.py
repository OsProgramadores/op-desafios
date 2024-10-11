
def eh_palindromo(num):
    return str(num) == str(num)[::-1]

def encontrar_palindromos(inicio, fim):
    for num in range(inicio, fim + 1):
        if eh_palindromo(num):
            print(num)

# Altere aqui os numeros finais e iniciais
inicio = 1 # Numero inicial
fim = 20    # Numero

encontrar_palindromos(inicio, fim)
