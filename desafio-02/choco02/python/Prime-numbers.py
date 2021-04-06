#!/usr/bin/python
test = []
prime = []

for a in range(2, 10000):
      if (a == 2) or (a == 3) or (a == 5) or (a == 7):
            prime.append(a)
      else:
            if (a % 2 == 0) or (a % 3 == 0) or (a % 5 == 0) or (a % 7 == 0):
                  continue
            else:
                  prime.append(a)
                  if (a <= 100):
                        test.append(a)
                        #print(a)
''' print(test)
print(prime) '''

for z in test:
      for x in prime:
            if (x % z == 0):
                  prime.remove(x)
print(prime)
#by Choco02