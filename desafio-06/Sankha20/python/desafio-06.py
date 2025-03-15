from os.path import isfile

anagrams = []

def read_expression():
    while True:
        expression = input("Digite a expressão ou 'S' para sair.\n> ")

        if expression.upper() == "S":
            return None

        expression = expression.replace(" ", "")

        if not expression.isalpha():
            print("Por favor, digite apenas letras e espaços.")
            continue

        return expression.upper()


def is_valid_file(file_lines: list[str]) -> bool:
    return all(
        string.isupper()
        and string.isalpha()
        and " " not in string
        for string in file_lines)


def read_words_file() -> bool:
    file_name = "words.txt"

    while True:
        if not isfile(file_name):
            file_name = input(
                "Por favor, digite um caminho válido para o arquivo com as palavras\
                     ou 'S' para sair.\n> ")
            continue

        if file_name.upper() == "S":
            return False

        with open(file_name) as file:
            all_words = [word.replace("\n", "") for word in file.readlines()]

        if is_valid_file(all_words):
            return all_words

        print("O arquivo contém conteúdo inválido.")
        file_name = ""


def count_letters(word: str) -> dict:
    return {letter: word.count(letter) for letter in word}


def filter_valid_words(expression: str, words: list[str]) -> list:
    expression_letters = count_letters(expression)

    return [
        word
        for word in words
        if all(letter in expression for letter in word)
        and all(word.count(letter) <= expression_letters[letter] for letter in word)
    ]


def remove_letters(expression: str, word: str) -> str:
    expression_letters = count_letters(expression)
    word_letters = count_letters(word)

    for key, value in word_letters.items():
        expression_letters[key] -= value

    return "".join(letter * amt for letter, amt in expression_letters.items() if amt > 0)


def generate_anagrams_list(valid_words: list[str], expression: str, result: list[str]):
    if len(valid_words) == 0:
        anagrams.append(result)
        return

    for word in valid_words:
        copy_result = result.copy()
        copy_result.append(word)

        copy_expression = remove_letters(expression, word)
        copy_valid_words = filter_valid_words(copy_expression, valid_words)

        generate_anagrams_list(copy_valid_words, copy_expression, copy_result)


def sort_valid_anagrams(expression:str, anagrams_list: list[list[str]]) -> list:
    expression_letters = count_letters(expression)
    return {
        " ".join(sorted(anagram)): 1
        for anagram in
        filter(lambda x: count_letters("".join(x)) == expression_letters, anagrams_list)
    }.keys()


def main():
    expression = read_expression()
    if not expression:
        return

    all_words = read_words_file()
    if not all_words:
        return

    valid_words = filter_valid_words(expression, all_words)
    generate_anagrams_list(valid_words, expression, [])

    for anagram in sort_valid_anagrams(expression, anagrams):
        print("".join(anagram))


if __name__ == "__main__":
    main()
