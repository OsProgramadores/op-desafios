import copy
import sys
import os
import re
from collections import Counter as ctr
from typing import Dict, List, Set, Tuple


def isSublist(superList: str, subList: str, /) -> bool:    
    subListElements: Dict[str, int] = ctr(subList)
    superListElements: Dict[str, int] = ctr(superList)

    for kew in subListElements.keys():
        if superListElements.get(kew, 0) < subListElements[kew]:
            return False
    
    return True


def searchPalindromes(stringPattern: str, palindromeSet = None, /) -> None:
    
    global allAnagrams, allValidWords
    
    if palindromeSet is None:
        palindromeSet = set()

    if not stringPattern:
        allAnagrams.add(tuple(sorted(palindromeSet)))
        return

    for currentWord in allValidWords:
        if isSublist(stringPattern, currentWord):
            stringPatternLettersCopy = ctr(stringPattern) - ctr(currentWord)            
            searchPalindromes(''.join(stringPatternLettersCopy.elements()), palindromeSet.union({currentWord}))
    
    return


allAnagrams: Set[Tuple[str]] = set()
allValidWords: List[str] = []
defaultWord: str = "VERMELHO"

try:
    inputWord: str = (''.join(sys.argv[1:])).upper().replace(" ", "")
    if not inputWord: inputWord = defaultWord
except IndexError as error:
    inputWord = defaultWord

if not bool(re.fullmatch(r'[A-Z]+', inputWord)): 
    raise Exception("Invalid Characters in the Expression.")

try:
    with open(os.path.join(os.path.dirname(__file__), "anagramWords.txt"), "r") as txtFile:
        while (currentFileWord := txtFile.readline().strip()):
            if isSublist(inputWord, currentFileWord):
                allValidWords.append(currentFileWord)

except Exception as error:
    print("An Exception While Opening File Occured:", error)

searchPalindromes(inputWord)

for anagramTuple in list(sorted(allAnagrams)):
    print(*anagramTuple)
