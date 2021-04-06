#! /usr/bin/python3
# -*- encoding: utf-8 -*-
"""
Script that checks if certain number is prime or not.
It works on ranges of numbers too.
"""
#import time

def is_primary(number):
    """
    Function: verifies whether a number is primary or not.
    Input: integer
    Response: boolean

    src: https://en.wikipedia.org/wiki/Primality_test
    function is_prime(n)
     if n ≤ 3
        return n > 1
     else if n mod 2 = 0 or n mod 3 = 0
        return false
     let i ← 5
     while i * i ≤ n
        if n mod i = 0 or n mod (i + 2) = 0
            return false
        i ← i + 6
     return true
    """
    if number == 1:
        return False
    if number <= 3:
        return True
    if number%2 == 0 or number%3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number%i == 0 or number%(i+2) == 0:
            return False
        i += 6
    return True

#time_start = time.time()
#primes_counter = 0
for n in range(1, 10000):
    if is_primary(n):
        print(n)
        #primes_counter += 1
#time_end = time.time()
#print("Total time: %0.2f" % (time_end - time_start))
#print("Primes found: %d" % primes_counter)
