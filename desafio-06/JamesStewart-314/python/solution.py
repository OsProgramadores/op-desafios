#!usr/bin/python
import sys
import os
import re
import functools
from collections import Counter as ctr
from typing import Final, Generator


all_anagrams: set[tuple[str, ...]] = set()
all_valid_words: list[str] = []
default_word: Final[str] = "VERMELHO"


@functools.cache
def is_sub_anagram(super_string: str, sub_string: str) -> bool:
    super_string_count = ctr(super_string)
    sub_string_count = ctr(sub_string)

    return all(super_string_count[k] >= count for k, count in sub_string_count.items())


@functools.cache
def check_word(string_pattern: str) -> Generator[tuple[str | None, str | None], None, None]:
    for current_word in all_valid_words:
        if len(string_pattern) >= len(current_word) and is_sub_anagram(string_pattern, current_word):
            yield (''.join(sorted((ctr(string_pattern) - ctr(current_word)).elements())), current_word)


def search_palindromes(string_pattern: str,
                       palindrome_set: list[str] | None = None) -> None:

    if palindrome_set is None:
        palindrome_set = []

    if not string_pattern:
        all_anagrams.add(tuple(sorted(palindrome_set)))
        return

    result = check_word(string_pattern)
    for word in result:
        if word is not None:
            search_palindromes(word[0], palindrome_set + [word[1]])

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
    with open(os.path.join(os.path.dirname(__file__), "anagramWords.txt"), "r") as txt_file:
        while (current_file_word := txt_file.readline().strip()):
            if is_sub_anagram(input_word, current_file_word):
                all_valid_words.append(current_file_word)

except (FileNotFoundError, PermissionError, IOError) as error:
    print("An Exception While Opening File Occured:", error)

search_palindromes(input_word)

for anagramTuple in all_anagrams:
    print(*anagramTuple)
