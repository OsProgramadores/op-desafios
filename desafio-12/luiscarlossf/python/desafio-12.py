"""
Desafio 12 - Luis Carlos da Silva Filho
"""
def main():
    """
    Main Function
    """
    arq = open("d12.txt", 'r')
    for n in arq.readlines():
        number = int(n)
        cont = 0
        while (2 ** cont) < number:
            cont += 1
        if number == (2 ** cont):
            print("{0} true {1}".format(number, cont))
        else:
            print("{0} false".format(number))

if __name__ == "__main__":
    main()
