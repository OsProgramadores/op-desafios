import os
from typing import List, Tuple

filePath: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frac.txt")

with open(filePath, "r") as fractionsFile:
    while (fractionContent := fractionsFile.readline().strip()):
        fractionSplitted: List[str] = fractionContent.split('/')
        
        if len(fractionSplitted) == 1:
            print(fractionContent)
            continue
        
        # len(fractionSplitted) == 2:
        try:
            fractionSimplified: Tuple[int, int] = divmod(int(fractionSplitted[0]), int(fractionSplitted[1]))
            print(f"{fractionSimplified[0]} " if fractionSimplified[0] != 0 else "", f"{fractionSimplified[1]}/{fractionSplitted[1]}" if fractionSimplified[1] != 0 else "", sep="")
            
        except ZeroDivisionError as error:
            print("ERR")
            continue