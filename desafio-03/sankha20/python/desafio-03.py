def is_palindrome(word: str) -> bool:
    return word == word[::-1]


def all_palindromes_between(start: int, end: int):
    for i in range(start, end + 1):
        if is_palindrome(str(i)):
            print(i)


def read_int() -> int:
    try:
        string = input("> ")
        assert string.isnumeric(), "Apenas números naturais"

        return int(string)
    except AssertionError as error:
        print(error)

    return None


def main():
    start = read_int()
    if not start:
        return

    end = read_int()
    if not end:
        return

    all_palindromes_between(start, end)


if __name__ == "__main__":
    main()
