import sys
import os
import re
from collections import Counter as ctr
from typing import Final, Generator


all_anagrams: set[tuple[str, ...]] = set()
all_valid_words: list[str] = []
default_word: Final[str] = "VERMELHO"


def remove_characters(original_string: str, char_to_remove: str) -> str:
    return ''.join(sorted((ctr(original_string) - ctr(char_to_remove)).elements()))


def is_sub_anagram(super_string: str, sub_string: str) -> bool:
    if len(sub_string) > len(super_string):
        return False

    super_string_count = ctr(super_string)
    sub_string_count = ctr(sub_string)

    return all(super_string_count[key] >= value for key, value in sub_string_count.items())


def check_word(string_pattern: str) -> Generator[tuple[str, str], None, None]:
    for current_word in all_valid_words:
        if is_sub_anagram(string_pattern, current_word):
            yield (remove_characters(string_pattern, current_word), current_word)


search_palindromes_memoization: dict[str, list[str]] = {}

def search_palindromes(string_pattern: str,
                       palindrome_list: list[str] | None = None) -> None:
    if palindrome_list is None:
        palindrome_list = []

    if not string_pattern:
        all_anagrams.add(tuple(sorted(palindrome_list)))

        try:
            all_valid_words.remove(tuple(sorted(palindrome_list))[0])
        except ValueError:
            pass

        return

    if string_pattern in search_palindromes_memoization:
        all_check_words = search_palindromes_memoization[string_pattern]

        for word in all_check_words:
            search_palindromes(word[0], palindrome_list + [word[1]])

    else:
        result = check_word(string_pattern)
        search_palindromes_memoization[string_pattern] = []

        try:
            word: str = next(result)
        except StopIteration:
            return

        while True:
            try:
                search_palindromes_memoization[string_pattern].append(word)
                search_palindromes(word[0], palindrome_list + [word[1]])
                word = next(result)

            except StopIteration:
                break

try:
    input_word: str = ''.join(sorted(tmp_word)) if \
    (tmp_word := (''.join(sys.argv[1:])).upper().replace(" ", "")) else \
    default_word

    if not bool(re.fullmatch(r'[A-Z]+', input_word)):
        raise ValueError("Invalid Characters in the Expression.")

except IndexError as error:
    input_word = default_word

except ValueError as error:
    print("Error:", error)

try:
    with open(os.path.join(os.path.dirname(__file__), "anagramWords.txt"), "r") \
        as txt_file:

        while (current_file_word := txt_file.readline().strip()):
            if is_sub_anagram(input_word, current_file_word):
                all_valid_words.append(current_file_word)

except (FileNotFoundError, PermissionError, IOError) as error:
    print("An Exception While Opening the File Occured:", error)

search_palindromes(input_word)

for anagramTuple in sorted(all_anagrams):
    print(*anagramTuple)
