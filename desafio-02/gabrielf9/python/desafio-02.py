# Listando todos os números primos entre 1 e 10000

primes = []

for i in range(2, 10001):
  if i % 2 == 0 and i != 2:
    continue

  _isPrime = True
  for j in range(2, int(i**1/2)+1):
    if i % j == 0 and i != j:
      _isPrime = False
  
  if _isPrime:
    primes.append(i)
    print(f'{i} é primo')

print(f'Um total de {len(primes)} primos.')
