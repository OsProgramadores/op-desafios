def is_palindrome(word: str) -> bool:
    return word == word[::-1]


def all_palindromes_between(start: int, end: int):
    for i in range(start, end + 1):
        if is_palindrome(str(i)):
            print(i)


def read_int() -> int:
    string = input("> ")
    assert string.isnumeric(), "Apenas números naturais"

    return int(string)


if __name__ == "__main__":
    all_palindromes_between(read_int(), read_int())
