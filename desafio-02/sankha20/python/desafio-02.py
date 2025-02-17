primes = [2]
def is_prime(n: int) -> bool:
    if n in primes:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for prime in primes:
        if prime > n ** 0.5:
            break
        if n % prime == 0:
            return False
    return True
def generate_primes_list(n: int) -> list:
    for i in range(3, n):
        if is_prime(i):
            primes.append(i)
generate_primes_list(10000)
print("\n".join(map(str, primes)))