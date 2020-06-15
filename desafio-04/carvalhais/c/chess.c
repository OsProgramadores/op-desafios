/*
 * Copyright (c) 2020 Andre Carvalhais
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the BSD license. See COPYING for details.
 */

/**
 * @file chess.c
 * @author Andre Carvalhais
 * @date 15/06/2020
 * @brief Solution for challenge #4 from OsProgramadores website
 *
 * Challenge is to write a program that can parse an input of numbers 
 * representing chess pieces without using any conditional constructs 
 * (if, else, switch, etc).
 * 
 * The input is given as an 8 by 8 grid of integers (between 0 and 6, 
 * inclusively on both ends), each integer representing a given piece 
 * type.
 * 
 * The program then should output a list containing the count for each 
 * piece type in a predefined manner.
 *
 * @see https://osprogramadores.com/desafios/d04/
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

#define CHAR_TABLE_SIZE     127

/**
 * Since conditional statements aren't allowed, the program will constitute 
 * of simple interface in which numbers are directly read from the standard 
 * input.
 * 
 * Each character acts as an index to an int array, and every character in 
 * the input is counted. This avoids the need for any conditional structure. 
 * The output only prints the char count for the relevant characters though.
 */
int main(void) {
    char *line = NULL;
    size_t length = 0;
    ssize_t num_read = 0;
    size_t index = 0;
    unsigned int char_count[CHAR_TABLE_SIZE] = { 0 };

    /* read each line from standard input until an EOF is found */
    while(num_read = getline(&line, &length, stdin) != -1) {
        index = 0;
        while(line[index] != '\0') {
            /* use the char itself as an index to the array */
            char_count[line[index++]]++;
        }
    }
    /* getline() malloc's it's buffer, hence we must free it */
    free(line);

    /* output the relevant characters count */
    printf("Peao: %d peca(s)\n", char_count['1']);
    printf("Bispo: %d peca(s)\n", char_count['2']);
    printf("Cavalo: %d peca(s)\n", char_count['3']);
    printf("Torre: %d peca(s)\n", char_count['4']);
    printf("Rainha: %d peca(s)\n", char_count['5']);
    printf("Rei: %d peca(s)\n", char_count['6']);

    return 0;
}