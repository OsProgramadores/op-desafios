"""
    Código que implementa a solução do desafio #02 do site Os Programadores
"""


def exibir_numeros_primos():
    """
        Exibe todos os números primos de 1 a 10000 no console
    """
    for numero in range(2, 10001):
        if e_primo(numero):
            print(numero)


def e_primo(numero):
    """
        Determina se o número passado como argumento é primo ou não
    """
    divisor = 2
    while divisor <= numero / 2:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True


if __name__ == "__main__":
    exibir_numeros_primos()
