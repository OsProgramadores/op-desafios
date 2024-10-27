import sys
import os
import re
from collections import Counter as ctr, deque
from typing import Final, Generator

all_anagrams: set[tuple[str, ...]] = set()
all_valid_words: deque[str] = deque()
all_valid_words_linked: dict[str, set[str]] = {}
default_word: Final[str] = "VERMELHO"


def remove_characters(original_string: str, char_to_remove: str) -> str:
    return ''.join(sorted((ctr(original_string) - ctr(char_to_remove)).elements()))


def is_sub_anagram(super_string: str, sub_string: str) -> bool:
    if len(sub_string) > len(super_string):
        return False

    super_string_count = ctr(super_string)
    sub_string_count = ctr(sub_string)

    return all(super_string_count[key] >= value for key, value in sub_string_count.items())


is_sub_anagram_memoization: dict[str, set[str]] = {}

def is_sub_anagram_memo(super_string: str, sub_string: str) -> bool:
    if len(sub_string) > len(super_string):
        return False

    if super_string in is_sub_anagram_memoization:
        if sub_string in is_sub_anagram_memoization[super_string]:
            return True

    super_string_count = ctr(super_string)
    sub_string_count = ctr(sub_string)

    return_value: bool = all(super_string_count[key] >= value for key, value in sub_string_count.items())

    if return_value:
        is_sub_anagram_memoization[super_string] = is_sub_anagram_memoization.setdefault(super_string, \
                                                    set()).union(all_valid_words_linked[sub_string])

    return return_value


def check_word(string_pattern: str) -> Generator[tuple[str, str], None, None]:
    for current_word in all_valid_words:
        if is_sub_anagram_memo(string_pattern, current_word):
            yield (remove_characters(string_pattern, current_word), current_word)

search_palindromes_memoization: dict[str, list[str]] = {}

def search_palindromes(string_pattern: str,
                       palindrome_list: list[str] | None) -> None:
    if not string_pattern:
        all_anagrams.add(tuple(sorted(palindrome_list)))
        return

    if string_pattern in search_palindromes_memoization:
        all_check_words = search_palindromes_memoization[string_pattern]

        for word in all_check_words:
            search_palindromes(word[0], palindrome_list + [word[1]])

    else:
        if not palindrome_list:
            for current_word in list(all_valid_words):
                if is_sub_anagram_memo(string_pattern, current_word):
                    search_palindromes(remove_characters(string_pattern, current_word),
                                       palindrome_list + [current_word])
                    all_valid_words.popleft()
            return

        search_palindromes_memoization[string_pattern] = []

        for word in check_word(string_pattern):
            search_palindromes_memoization[string_pattern].append(word)
            search_palindromes(word[0], palindrome_list + [word[1]])

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


for word_1 in all_valid_words:
    all_valid_words_linked[word_1] = set()

    for word_2 in all_valid_words:
        if word_1 != word_2 and is_sub_anagram(word_1, word_2):
            all_valid_words_linked[word_1].add(word_2)

search_palindromes(input_word, [])

for anagramTuple in all_anagrams:
    print(*anagramTuple)
