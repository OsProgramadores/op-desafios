import sys

def search_primes(n):
    sys.setrecursionlimit(10500)
    prime = 0
    if n == 10000:
        return 0
    for c in range(1, n + 1):
        if n % c == 0:
            prime += 1
    if prime == 2:
        print(f'[{n}]', end='')
    search_primes(n + 1)        
search_primes(1)