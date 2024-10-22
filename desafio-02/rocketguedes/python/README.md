# Sieve of Eratosthenes

Find all the prime numbers less than or equal to a given integer n by Eratosthenes' method.

The function returns a `list[int]` of prime numbers, e.g. `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]`

## Features

* Including optimization of starting from prime's square
* Can be imported and used as a module
* No edit needed, just pass the limit as an argument `(optional; default 10000)`

## Usage

```bash
python sieve.py [LIMIT]
```

It can also be imported through another script and used as a module.

```python
from sieve import sieve_of_eratosthenes

print(sieve_of_eratosthenes(120))
```