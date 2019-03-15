""" Anagrams by WhoisBsa """

from itertools import permutations
import sys


def findPermutation(word, f):
    """ Find the permutation of the words """
    while True:
        for i in f.readlines():
            if word in i:
                result = True
                break
            else: 
                result = False
        
        if result:
            parmutationList = permutations(word)
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
