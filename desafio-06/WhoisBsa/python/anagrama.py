""" Anagrams by WhoisBsa """
from itertools import permutations
import re
import sys


def findPermutation(wrd):
    """ Find the permutation of the words """
    parmutationList = permutations(wrd)
    for item in parmutationList:
        print(''.join(item))


def checkWord(wrd, wordLine):
    """ Checks whether the word exists in the file or not """
    if re.search(r'\b' + re.escape(wrd) + r'\b', wordLine.read(), flags=re.IGNORECASE):
        findPermutation(wrd)
    else:
        print('This word is not available')


def main():
    """ Main function """
    with open('words.txt', 'r') as f:
        word = sys.argv[1].upper()
        checkWord(word, f)

if __name__ == '__main__':
    main()
