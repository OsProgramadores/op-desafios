#coding: utf-8
"""
    Resolução do Desafio 12,
    Por: Gabriel Rocha,
    Github: github.com/g4br13lr0ch4
"""
def verifica(valor):
    """Verifica se o valor é uma potência de 2"""
    x = 0
    while x >= 0:
        aux = (2 ** x)
        if aux > valor:
            return 0, 0
        if aux == valor:
            return 1, str(x)
        x += 1

def main():
    """Funlçâo Principal"""
    with open('d12.txt', 'r') as file_object:
        for item in file_object:
            status, p = verifica(int(item))
            if status == 1:
                print(str(item).rstrip() + " true " + p)
            else:
                print(str(item).rstrip() + " false")


if __name__ == "__main__":
    main()
