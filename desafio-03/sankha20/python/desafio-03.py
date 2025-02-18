def is_palindrome(word: str) -> bool:
    return word == word[::-1]


def all_palindromes_between(start: int, end: int):
    for i in range(start, end + 1):
        if is_palindrome(str(i)):
            print(i)


def read_int() -> int:
    while True:
        try:
            string = input("Digite um número natural [S ou 0 para sair]: ")

            if string.upper() == "S":
                return 0

            assert string.isnumeric(), "Apenas números naturais"

            return int(string)
        except AssertionError as error:
            print(error)


def main():
    start = read_int()
    if not start:
        return

    end = read_int()
    if not end:
        return

    if start > end:
        start, end = end, start

    all_palindromes_between(start, end)


if __name__ == "__main__":
    main()
