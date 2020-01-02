/*
 * Copyright (c) 2019 Andre Carvalhais
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the BSD license. See COPYING for details.
 */

/**
 * @file palin.c
 * @author Andre Carvalhais
 * @date 13/12/2019
 * @brief Solution for challenge #3 from OsProgramadores website
 *
 * Challenge asks to write a program to list all decimal numbers palindromes 
 * between two given numbers (initial and final). It may be assumed that:
 * - only positive integers will be used as will be used as limits
 * - single digit numbers are palindromes by definition 
 * - all number are representable as 64-bit unsigned ints
 *
 * @see https://osprogramadores.com/desafios/d03/
 */

#include <stdio.h>
#include <errno.h>
#include <limits.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdint.h>

/** 
 * Default value fir the '-b' option. */
#define DEFAULT_OPT_BASE    10
/** 
 * Maximum numeric string length. */
#define MAX_NUM_STR_LEN     25
/**
 * Program name, given by argv[0]. */
const char *program_name;

/**
 * @brief Naive test for palindromes, represented as string.
 *
 * @param s string holding the number to be tested
 * @return True if the number is palindrome, False otherwise
 */
bool is_palindrome(const char *s) {
    size_t len = strlen(s);
    int i = 0;
    int j = len - 1;
    
    if(len == 0)
        return false;
    while(i < j)
        if(s[i++] != s[j--]) 
            return false;
    return true;
}

/** 
 * @brief Displays a help message. 
 */
void help_message(void) {
    char message[] = 
"Usage: %s [OPTION]... INITIAL FINAL\n"
"Show all decimmal palindromes between INITIAL and FINAL (inclusive).\n"
"\n"
"The numbers INITIAL and FINAL must be representable as 64-bit unsigned\n" 
"ints. Also, INITAL must smaller than FINAL, otherwise it's considered an\n"
"error.\n"
"\n"
"Valid options:\n"
"   -b BASE         numeric base for INITIAL and FINAL, any decimal number\n"
"                   between 2 and 36 (default: 10)\n"
"   -h              show this help message and exit\n";

    fprintf(stdout, message, program_name);
}

/** 
 * @brief Wraps calls to strtoull() and tests for error conditions.
 *
 * @param str string that holds the number to be converted
 * @param base numeric base to be used for conversion
 * @param dest pointer memory that will stored the conversion result
 * @return True on successful conversion, False otherwise
 */
bool strtoull_wrapper(const char *str, int base, unsigned long long* dest){
    char *end;
    unsigned long long value = 0;
    
    errno = 0;
    value = strtoull(str, &end, base);
    /* an overflow has ocurred */
    if(errno == ERANGE && value == ULLONG_MAX) {
        perror("strtoull");
        return false;
    }
    /* string was empty */
    else if (end == str) {
        fprintf(stderr, "%s: empty numeric string\n", program_name);
        return false;
    }
    /* the string was only partially valid */
    else if(!(*str != '\0' && *end == '\0')) {
        fprintf(stderr, "%s: invalid numeric string\n", program_name);
        return false;
    }
    memcpy(dest, &value, sizeof(value));
    return true;
}

int main(int argc, char *argv[]) {
    int param = -1;
    bool option_h = false;
    unsigned char numeric_base = DEFAULT_OPT_BASE;
    bool option_invalid = false;
    unsigned long long value = 0;
    uint64_t initial = 0, final = 0;
    int step = 0;
    char *number_string = NULL;

    /* initialize global variables */
    program_name = argv[0];

   /* process options for program */
    while((param = getopt(argc, argv, "hb:")) != -1) {
        switch(param) {
            case 'h':
                option_h = true;
                break;
            case 'b':
                /* read number to be used as base */
                if(!strtoull_wrapper(optarg, 10, &value)){
                    fprintf(stderr, "%s: invalid base for option 'b'\n",
                            program_name);
                    option_invalid = true;
                    break;
                }
                else if(value > 36 || value < 2) {
                    fprintf(stderr, "%s: base for option 'b' out of range "
                            "-- %llu\n", program_name, value);
                    option_invalid = true;
                    break;
                }
                numeric_base = (unsigned char) value;
                break;
            case '?':
                option_invalid = true;
                break;
        }
        /* stop processing of further options if any of the following option 
         * flags are set */
        if(option_h || option_invalid)
            break;
    }
    /* take proper actions for each option flag */
    if(option_invalid) {
        exit(EXIT_FAILURE);
    }
    else if(option_h){
        help_message();
        exit(EXIT_SUCCESS);
    }

    /* if we got here, any options were valid and the relevant variables were 
     * set accordingly; in case of invalid options (or arguments), program 
     * should have already output and error message and exited */

    /* we need the remaining arguments to be exactly INITIAL and FINAL to be 
     * able to keep processing */
    if(argc - optind < 2) {
        help_message();
        exit(EXIT_FAILURE);
    }
    
    /* read initial and final values */
    if(!strtoull_wrapper(argv[optind], numeric_base, &value)){
        fprintf(stderr, "%s: invalid initial value\n", program_name);
        exit(EXIT_FAILURE);
    }
    if(value > ULONG_MAX) {
        fprintf(stderr, "%s: initial value out of range\n", program_name);
        exit(EXIT_FAILURE);
    }
    initial = (uint64_t)value;
    if(!strtoull_wrapper(argv[optind+1], numeric_base, &value)){
        fprintf(stderr, "%s: invalid final value\n", program_name);
        exit(EXIT_FAILURE);
    }
    if(value > ULONG_MAX) {
        fprintf(stderr, "%s: final value out of range\n", program_name);
        exit(EXIT_FAILURE);
    }
    final = (uint64_t)value;
    
    /* allocate space for the numeric string */
    number_string = calloc(MAX_NUM_STR_LEN, sizeof(char));
    if(number_string == NULL){
        fprintf(stderr, "%s: unable to allocate memory\n", program_name);
        exit(EXIT_FAILURE);
    }

    /* get the 'direction' of iteration, depending on the arguments */
    step = initial > final ? -1: 1;

    /* print out the palindromes */
    while(initial != (final + step)){
        snprintf(number_string, MAX_NUM_STR_LEN, "%lu", initial);
        if(is_palindrome(number_string)){
            fprintf(stdout, "%s ", number_string);
        }
        initial += step;
    }
    fprintf(stdout, "\n");
    free(number_string);
    exit(EXIT_SUCCESS);
}

