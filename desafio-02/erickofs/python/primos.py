"""
Module docstring for prime10001.py.

Prime calculation based on the Sieve of Eratosthenes algorithm.
"""
# def sieve_of_eratosthenes():
#     """
#     Implements the Sieve of Eratosthenes algorithm to find all prime numbers up to a given limit.

#     Returns:
#     - primelist (list): List of prime numbers up to the given limit.
#     """
#     primelimit = 1001

#     primelist = []

#     primelist.extend(range(2, primelimit))
#     # Iterate through every number from 2 to the square root of the limit.
#     for i in range(2, int(primelimit**0.5) + 1):
#         for j in range(i*2, primelimit, i):
#             if j in primelist:
#                 primelist.remove(j)
#     # Return the list of prime numbers.
#     return primelist

# print(sieve_of_eratosthenes())

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

# while True:
#     try:
#         PRIMERANGE = int(input("Enter the number of prime numbers to be displayed (0 = all): "))
#         # if primerange is not integer, round it to the nearest integer and raise message
#         if PRIMERANGE != int(PRIMERANGE):
#             PRIMERANGE = round(PRIMERANGE)
#             print("The range has been rounded to the nearest integer.")
#         # if no value assigned to primerange, consider it as 0 and raise message
#         elif PRIMERANGE == "" :
#             PRIMERANGE = int("0")
#             print("No given range. It has been automatically set to 0.")
#         # if primerange is greater than limit, raise message as out of range
#         elif PRIMERANGE > PRIMELIMIT:
#             print("The variable is out of range. Please enter a number between 0 and the limit.")
#         # if primerange is less than 0, raise message as error
#         elif PRIMERANGE < 0:
#             print("Please enter a number greater than 0.")
#         # if primerange is between 0 and limit, break the loop
#         else:
#             break
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")

primelist = set(range(2, PRIMELIMIT))

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

for prime in sieve_of_eratosthenes_set():
    print(prime)
