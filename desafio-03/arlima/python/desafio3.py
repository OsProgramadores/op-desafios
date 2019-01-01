"""
Desafio 3 - Adriano Roberto de Lima
"""

def main():
    """
    Main Function
    """

    number1 = 1001
    number2 = 5005

    for numero in range(number1, number2+1):
        palavra = str(numero)
        if palavra == palavra[::-1]:
            print(numero)

if __name__ == "__main__":
    main()
