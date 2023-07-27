#!/usr/bin/python3

INITIAL_NUMBER = 1
LAST_NUMBER = 10_000

for number in range(INITIAL_NUMBER, LAST_NUMBER+1):
    is_prime = True

    if number == 1:
        continue

    for divisor in range(2, number):

        if (number % divisor == 0):
            is_prime = False
            break
    
    if is_prime:
        print(number)
