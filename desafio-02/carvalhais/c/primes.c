/*
 * Copyright (c) 2019 Andre Carvalhais
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the BSD license. See COPYING for details.
 */

/**
 * @file primes.c
 * @author Andre Carvalhais
 * @date 13/12/2019
 * @brief Solution for challenge #2 from OsProgramadores website
 *
 * Challenge asks to write a program to list all prime numbers between 1 and 
 * 10000, on any preferred language.
 *
 * @see https://osprogramadores.com/desafios/d02/
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

/** 
 * Biggest number to be tested for primality. */
#define MAX_VALUE   10000

/** 
 * Holds a list of all prime numbers within given range, calculated on the 
 * fly. */
unsigned *primes;
/** 
 * Holds a list containing numbers up to sqrt(MAX_VALUE) squared, used to give 
 * boundaries on primality test calculations. */
unsigned *squares;

/**
 * @brief Test a number for primality using an online algorithm
 * 
 * @param n number to be tested
 * @param m maximum divisor to be tried
 * @param list list containing all prime numbers up to at least m 
 * @return True if n is prime, False otherwise
 */
bool is_prime(unsigned n, unsigned m, const unsigned *list) {
    size_t i;
    /* test n against all primes given on a list of prime numbers up to a 
     * specified maximum; the list is expected to contain all prime numbers 
     * prior to m, which is the case for an online algorithm such as this 
     * one */
    for(i = 0; list[i] <= m; i++){
        /* uncomment to get debugging info */
        //printf("testing %u against %u (max %u)\n", n, list[i], m);
        /* if list[i] equals 0, it means we reached the end of the list */
        if(list[i] == 0) break;
        /* if there is no remainder, n has a divisor and is composite */
        if(!(n % list[i])) return false;
    }
    /* otherwise n must be prime */
    return true;
}

int main(int argc, char *argv[]) {
    /* biggest number to be tested, set to default */
    unsigned max = MAX_VALUE;
    /* index for the primes list */
    unsigned pindex = 0;
    /* index for the squares list */
    unsigned sindex = 0;
    /* current bumber being tested */
    unsigned current = 0;
    /* biggest number to be squared in the squares list */
    unsigned smax = 0;
    /* scratch variable */
    unsigned t = 0;

    /* rough estimation of maximum number of primes in given range */
    primes = (unsigned *) calloc(max / 2, sizeof(unsigned));
    /* maximum number of squares we need to keep for prime calculations */
    smax = (unsigned) ceil(sqrt(max));
    squares = (unsigned *) calloc(smax + 1, sizeof(unsigned));
    /* exit with an error if memory can't be allocated */
    if(primes == NULL || squares == NULL) {
        printf("Unable to allocate memory.\n");
        free(primes);
        free(squares);
        return -1;
    }
    /* initialize the primes list, it can't be empty for the online algorithm 
     * to work, so store the first prime number */
    primes[pindex++] = 2;
    /* initialize the squares list */
    for(sindex = 0; sindex <= smax; sindex++)
        squares[sindex] = sindex * sindex;
    
    /* make sindex point to the first 'usable' square */
    sindex = 2;
    
    /* initialize current to account for the first prime already in the list; 
     * also, since the first prime is also the only even prime ever, we can 
     * skip every other even number by incrementing in steps of 2 */
    for(current = 3; current <= max; current += 2) {
       /* when current grows big enough (up to the next perfect square), it 
        * means we must get a new boundary for the primality test */
       if(current >= squares[sindex]) {
            sindex++;
        }
        /* boundary for the primality test is the biggest whole number whose 
         * square is smaller than the current number being tested, that equals 
         * the previous sindex */
        if(is_prime(current, sindex-1, primes)){
            primes[pindex++] = current;
        }
    }

    for(t = 0; t < pindex; t++){
        printf("%u ", primes[t]);
    }
    printf("\n");
    
    free(primes);
    free(squares);
    return 0;
}

