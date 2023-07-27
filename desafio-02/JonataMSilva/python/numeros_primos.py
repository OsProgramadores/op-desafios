"""verificador de numeros primos"""

def verifica_se_numero_eh_primo(numero):
    """função para verificar o numero em uma range"""
    divisor = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            divisor += 1
    if divisor == 2:
        return True
    return False

for numero_primo in range(1, 10000):
    if verifica_se_numero_eh_primo(numero_primo):
        print(numero_primo)
