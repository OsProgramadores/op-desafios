"""
Prime calculation based on the Sieve of Eratosthenes algorithm.
"""

def sieve_of_eratosthenes_set():
    """
    Implements the Sieve of Eratosthenes algorithm to find all prime numbers up to the given limit.

    Returns:
    - primelist (set): Set of prime numbers up to the user's nth given range.
    """
    for i in range(2, int(PRIMELIMIT**0.5) + 1):
        for j in range(i*2, PRIMELIMIT, i):
            if j in primelist:
                primelist.remove(j)

    return list(primelist)[:PRIMERANGE] if PRIMERANGE != 0 else list(primelist)

while True:
    PRIMELIMIT = input("Enter the calculation limit: ")
    try:
        PRIMELIMIT = float(PRIMELIMIT)
        if PRIMELIMIT < 0:
            print("Please enter a positive number.")
        elif PRIMELIMIT > 1000000:
            print("The limit is too high. Please enter a number less than 1000000.")
        else:
            break
    except ValueError:
        PRIMELIMIT = PRIMELIMIT.strip()
        if PRIMELIMIT == "":
            PRIMELIMIT = 100.0
            print("No given limit. It has been automatically set to 100.")
            break
        print("Invalid input. Please enter a valid number.")

if round(PRIMELIMIT) != PRIMELIMIT:
    print(f"The limit has been rounded to the nearest integer: {round(PRIMELIMIT)}")
PRIMELIMIT = int(round(PRIMELIMIT))
if PRIMELIMIT == 0:
    print("The limit has been automatically set to 100.")
    PRIMELIMIT = 100

while True:
    PRIMERANGE = input("Enter the number of prime numbers to be displayed (0 = all): ")
    try:
        PRIMERANGE = float(PRIMERANGE)
        if PRIMERANGE < 0:
            print("Please enter a positive number.")
        elif PRIMERANGE > 1000000:
            print("The limit is too high. Please enter a number less than 1000000.")
        else:
            break
    except ValueError:
        PRIMERANGE = PRIMERANGE.strip()
        if PRIMERANGE == "":
            PRIMERANGE = 0
            print("No given limit. All primes will be printed.")
            break
        print("Invalid input. Please enter a valid number.")

if round(PRIMERANGE) != PRIMERANGE:
    print(f"The limit has been rounded to the nearest integer: {round(PRIMERANGE)}")

PRIMERANGE = int(round(PRIMERANGE))

primelist = set(range(2, PRIMELIMIT))
