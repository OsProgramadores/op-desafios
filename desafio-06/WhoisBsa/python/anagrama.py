""" Anagrams by WhoisBsa """
from itertools import permutations
import sys


def findPermutation(wrd, wordLine):
    """ Find the permutation of the words """
    while True:
        for i in wordLine.readlines():
            if wrd in i:
                result = True
                break
            else:
                result = False
        if result:
            parmutationList = permutations(wrd)
            for item in parmutationList:
                print(''.join(item))
            break
        else:
            print('This word is not available')
            break

with open('words.txt', 'r') as f:
    word = sys.argv[1].upper()
    findPermutation(word, f)
    f.close()

