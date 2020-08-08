"""
Autor: Roberto Arruda
#02 - Primos
"""
for num in range(1, 10000 + 1):
  for n in range(2, num - 1):
    if (num % n == 0):
      break
  else:
    print("{} é primo".format(num), end='\n')
