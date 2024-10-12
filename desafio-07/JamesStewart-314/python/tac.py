import sys
import os
from typing import List

try:
    filePath: str = sys.argv[1]
    if not os.path.exists(filePath): raise ValueError("Invalid Path")
except IndexError as error:
    print("Error: Please, provide a valid non-empty path.")
    exit()
except ValueError as error:
    print("Error:", error)
    exit()

seekValues: List[int] = [0]
textFile = open(filePath)

try:
    word = textFile.readline()
except UnicodeDecodeError: word = "<null>"
while word:
    seekValues.append(textFile.tell())
    try:
        word = textFile.readline()
    except UnicodeDecodeError: word = "<null>"

for idx in range(len(seekValues) - 1, -1, -1):
    textFile.seek(seekValues[idx])
    try:
        print(textFile.readline().strip())
    except UnicodeDecodeError: print("<null>")

textFile.close()
