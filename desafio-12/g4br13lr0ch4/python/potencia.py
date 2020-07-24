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
            return False, " "
        if aux == valor:
            return True, str(x)
        x += 1

def main():
    """Main"""
    with open('d12.txt', 'r') as file_object:
        for item in file_object:
            status, p = verifica(int(item))
            print(str(item) + " " + str(status) + " " + p)

if __name__ == "__main__":
    main()
