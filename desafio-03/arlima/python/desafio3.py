"""
Desafio 3 - Adriano Roberto de Lima
"""

def main():
    """
    Main Function
    """

    number1 = 1001
    number2 = 5005

    for i in range(number1, number2+1):
        s = str(i)
        if s == s[::-1]:
            print(i)

if __name__ == "__main__":
    main()
