"""Calculate palindrome numbers between two numbers"""


def palindromo(start, end):
    """Returns a list of palindrome numbers between start and end"""
    return [i for i in range(start, end + 1) if str(i) == str(i)[::-1]]


def main():
    """Main function"""
    start = int(input('Entre o numero inicial: '))
    end = int(input('Entre o numero final: '))
    if start > end:
        print('Número inicial maior que final. Por favor, tente de novo.')
        return
    print(palindromo(start, end))


if __name__ == '__main__':
    main()
