"""
Escreva um programa para listar todos os números primos entre 1 e 10000.
"""
def is_prime(num):
    """
    Verifica se o parâmetro é um número primo ou não.
    :param num: Recebe um número
    :return:  Retorna o Booleano da função
    """
    div = 2
    if num == 2:
        return True
    while num % div != 0 and div <= num/2:
        div += 1
    if num % div == 0:
        return False
    return True

def main():
    """
    Função principal
    :return: Main
    """
    start = 2
    stop = 1000
    while start < stop:
        if is_prime(start):
            print(start, end=', ')
        start += 1

if __name__ == "__main__":
    main()
