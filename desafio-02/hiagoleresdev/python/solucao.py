primes = [1]
dividers = 0
for i in range(2,10000):
    dividers = 0
    for n in range(2,10000):

        if i % n == 0:
            dividers +=1

    if dividers == 1:
        primes.append(i)

print(primes)