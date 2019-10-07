import sequtils

proc primes(to: int) : seq[int] = 
    var sieve = (2..to).toSeq
    for i, n in sieve:
        if n == 0: continue
        result.add(n)
        for j in countup(i, high(sieve), n):
          sieve[j] = 0

echo primes(10_000)