import sys
import os
import re
from collections import Counter as ctr
from typing import List, Set, Tuple, Final


all_anagrams: Set[Tuple[str, ...]] = set()
all_valid_words: List[str] = []
default_word: Final[str] = "VERMELHO"


def is_sub_anagram(super_string: str, sub_string: str) -> bool:
    super_string_elements: dict[str, int] = ctr(super_string)

    return all((super_string_elements.get(kew, 0) >= value) for\
                kew, value in ctr(sub_string).items())


def search_palindromes(string_pattern: str,
                      palindrome_set: set[str] | None = None) -> None:

    if palindrome_set is None:
        palindrome_set = set()

    if not string_pattern:
        all_anagrams.add(tuple(sorted(palindrome_set)))
        return

    for currentWord in all_valid_words:
        if is_sub_anagram(string_pattern, currentWord):
            newstring_pattern_letters = ''.join((ctr(string_pattern) - \
                                        ctr(currentWord)).elements())

            search_palindromes(newstring_pattern_letters,
                              palindrome_set.union({currentWord}))

try:
    input_word: str = tmpWord if \
    (tmpWord := (''.join(sys.argv[1:])).upper().replace(" ", "")) else \
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

for anagramTuple in sorted(all_anagrams, key=lambda x: (-len(x), x)):
    print(*anagramTuple)
