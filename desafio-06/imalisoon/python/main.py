#!/usr/bin/env python3
# author: Alison gh: @imalisoon

from ctypes import ArgumentError
import os
import string
import sys
import re


def search_anagrams(letters_current_expression, dictionary):
    _candidates_list = generate_candidates_list(
        letters_current_expression,
        dictionary
    )

    _possible_anagrams: str = []

    anagrams_list = generate_anagrams_list(
        letters_current_expression,
        _candidates_list,
        _possible_anagrams
    )

    anagrams_without_repetition = generate_anagrams_without_repetition(anagrams_list)

    _ordened_anagrams_list: list = get_ordened_list_string(anagrams_without_repetition)

    return _ordened_anagrams_list


def print_anagrams(anagrams):
    for item in anagrams:
        print(item)


def get_ordened_list_string(anagrams_without_repetition: list) -> list:
    _ordened_list: list = []

    for item in anagrams_without_repetition:
        _ordened_list.append(" ".join(item))

    _ordened_list.sort()

    return _ordened_list


def generate_anagrams_without_repetition(anagrams_list: list) -> list:
    _without_rep_list: list = []

    for anagram in anagrams_list:
        if anagram[0] not in _without_rep_list:
            _without_rep_list.append(anagram[0])

    return _without_rep_list


def generate_candidates_list(letters_current_expression, dictionary) -> list:
    _candidates_list: list = []

    for word in dictionary:
        if is_candidate(letters_current_expression, word[1]):
            _candidates_list.append(word)

    return _candidates_list


def generate_anagrams_list(letters_current_expression, candidates, anagram_candidates):
    if len(anagram_candidates) == 0:
        anagram_candidates = get_initial_candidates(
            letters_current_expression, candidates
        )

    candidate_is_viable = [False] * len(candidates)
    initial_anagrams_num = len(anagram_candidates)
    anagrams_unfiled = anagram_candidates.copy()

    for pos_candidate_anagram, initial_candidate in enumerate(anagram_candidates):
        anagrams_unfiled = generate_new_anagrams(
            letters_current_expression,
            candidates,
            candidate_is_viable,
            anagrams_unfiled,
            pos_candidate_anagram,
            initial_candidate
        )

    anagram_candidates = filter_candidates_invalid_anagram(anagrams_unfiled, initial_anagrams_num)

    # Verifica se há candidates que necessitam de busca extra
    _new_search = False
    for candidate in anagram_candidates:
        if candidate[2] != 0:
            _new_search = True
            break

    if _new_search:
        _candidates_filed = []

        for pos, item in enumerate(candidates):
            if candidate_is_viable[pos]:
                _candidates_filed.append(item)

        candidates = _candidates_filed

        anagram_candidates = generate_anagrams_list(
            letters_current_expression,
            candidates,
            anagram_candidates
        )

    return anagram_candidates


def filter_candidates_invalid_anagram(anagram_candidates, initial_anagrams_num) -> list:
    _candidates_anagram: list = []

    for pos, candidate in enumerate(anagram_candidates):
        if pos < initial_anagrams_num:
            if candidate[2] == 0:
                _candidates_anagram.append(candidate)

        else:
            _candidates_anagram.append(candidate)

    return _candidates_anagram


def generate_new_anagrams(
        letters_current_expression,
        candidates,
        candidates_viability,
        anagram_candidates,
        pos_candidate_anagram,
        initial_candidate
    ):
    total_candidates = len(candidates)

    if initial_candidate[2] > 0:
        pos_last_candidate = initial_candidate[1]
        next_candidate = pos_last_candidate + 1

        for pos_new_candidate in range(next_candidate, total_candidates):
            candidates_viability[pos_new_candidate] = True
            new_candidate = candidates[pos_new_candidate]
            missing_letters = anagram_candidates[pos_candidate_anagram][3]

            if is_candidate(missing_letters, new_candidate[1]):
                temp_list: list = []
                temp_list.append(new_candidate[0])
                potential_anagram = anagram_candidates[pos_candidate_anagram][0] + temp_list
                missing_letters = count_letters_missing_anagram(
                    letters_current_expression,
                    potential_anagram
                )
                total_missing_letters = get_letters_total(missing_letters)

                anagram_candidates.append((
                    potential_anagram,
                    pos_new_candidate,
                    total_missing_letters,
                    missing_letters
                ))

    return anagram_candidates


def get_initial_candidates(letters_current_expression, candidates):
    anagram_candidates: list = []

    for pos_candidate, candidate in enumerate(candidates):
        lista: list = []
        lista.append(candidate[0])
        missing_letters = count_letters_missing_anagram(
            letters_current_expression, lista
        )
        total_missing_letters = get_letters_total(missing_letters)
        anagram_candidates.append((
            lista,
            pos_candidate,
            total_missing_letters,
            missing_letters
        ))

    return anagram_candidates


def get_letters_total(missing_letters) -> int:
    _total: int = 0
    for l in missing_letters:
        _total += missing_letters[l]

    return _total


def is_anagram(letters_current_expression, anagram):
    string_conc = "".join(anagram)
    potential_anagram_letters = get_count_letters(string_conc)

    if len(letters_current_expression) != len(potential_anagram_letters):
        return False

    for letter in letters_current_expression:
        if letters_current_expression[letter] != potential_anagram_letters[letter]:
            return False

    return True


def get_file_path():
    _file_path = os.path.join("desafio-06", "imalisoon", "python", "words.txt")

    if not os.path.isfile(_file_path):
        _file_path = os.path.join("words.txt")

    return _file_path


def process_dictionary(file_path: str) -> list:
    _dictionary: list = []

    with open(file_path, "r", encoding='UTF-8') as words_file:
        for word in words_file:
            word = word.strip()
            count_letters = get_count_letters(word)
            _dictionary.append((word, count_letters))

    return _dictionary


def is_candidate(letters_current_expression, candidate_letters):
    if not isinstance(candidate_letters, dict):
        raise ArgumentError("candidate_letters deve ser um dicionário")

    for letter in candidate_letters:
        if letter not in letters_current_expression or \
                candidate_letters[letter] > letters_current_expression[letter]:
            return False

    return True


def get_count_letters(expression):
    _letters_count = {}
    for letter in expression:
        if letter in _letters_count:
            _letters_count[letter] += 1
        else:
            _letters_count[letter] = 1
    return _letters_count


def count_letters_missing_anagram(letters_current_expression, string_list) -> dict:
    current_list_letters = count_list_letters(string_list)
    missing_letters: dict = {}

    for letter in letters_current_expression:
        if letter in current_list_letters:
            missing_letters[letter] = letters_current_expression[letter] \
            - current_list_letters[letter]

        else:
            missing_letters[letter] = letters_current_expression[letter]

    return missing_letters


def count_list_letters(string_list):
    string_conc = "".join(string_list)
    _count_letters = {}

    for l in string_conc:
        if l in _count_letters:
            _count_letters[l] += 1

        else:
            _count_letters[l] = 1

    return _count_letters


def is_valid_expression(expression):
    for letter in expression:
        if letter in string.punctuation:
            return False

    return re.match('^[a-zA-Z]+$', expression)

def process_argument(argument: list) -> str or None:
    if len(argument) <= 1:
        print("[USO]: python main.py 'argumento'")
        return

    elif len(argument) > 2:
        print("[ERRO]: passe apenas 1 argumento")
        return

    elif len(argument) == 2:
        return argument[-1].upper().replace(" ", "")

def main(args):
    expression: str = ""
    argument_processed: str or None = process_argument(args)

    if not argument_processed:
        return

    expression = argument_processed


    if not is_valid_expression(expression):
        print("Expressao passada por argumento contem caracteres invalidos.")
        return

    letters_current_expression = get_count_letters(expression)
    file_path = get_file_path()
    dictionary = process_dictionary(file_path)

    anagrams = search_anagrams(letters_current_expression, dictionary)
    print_anagrams(anagrams)


if __name__ == "__main__":
    main(sys.argv)
