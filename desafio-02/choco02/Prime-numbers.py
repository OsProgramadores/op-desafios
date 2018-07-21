#!/usr/bin/python
from time import time

for a in range(1, 10000):
  if a == 1:
    continue
  elif (a == 2) or (a == 3) or (a == 5) or (a == 7):
    print(a)
  else:
    if (a % 2 == 0) or (a % 3 == 0) or (a % 5 == 0) or (a % 7 == 0):
      continue
    else:
      print(a)
#by /Choco02
