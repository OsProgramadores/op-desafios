#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int parseInput(unsigned long long int *nA, unsigned long long int *nB);
void swap(unsigned long long int *a, unsigned long long int *b);
void iterateNumbers(unsigned long long int nA, unsigned long long int nB);
int isPalindrome(unsigned long long int number);

int main() {
    unsigned long long int nA = 0;
    unsigned long long int nB = 0;

    printf(
        "Enter two positive numbers (0 to 18446744073709551615) as boundaries, "
        "separated by a space: \n");

    while (!parseInput(&nA, &nB)) {
        printf(
            "\nInvalid input. Enter 2 positive numbers, separated by a space:");
    }

    if (nA > nB) {
        swap(&nA, &nB);
        printf(
            "\nThe smaller number was entered second; they have been "
            "swapped.\n");
    }

    printf("\nPalindromes in the range [%llu, %llu]:\n", nA, nB);
    iterateNumbers(nA, nB);

    return 0;
}

int parseInput(unsigned long long int *nA, unsigned long long int *nB) {
    char input[100];
    if (fgets(input, sizeof(input), stdin) != NULL) {
        size_t len = strlen(input);
        // removes any trailing whitespaces and updates the len
        if (len > 0 && input[len - 1] == '\n') {
            input[len - 1] = '\0';
            len--;
        }

        // rejects anything other than digits and withespace
        for (size_t i = 0; i < len; i++) {
            if (!isdigit(input[i]) && input[i] != ' ') {
                return 0;
            }
        }

        // parses the first number
        char *saveptr = NULL;
        char *token = strtok_r(input, " ", &saveptr);
        if (token != NULL) {
            *nA = strtoull(token, NULL, 10);
        } else {
            return 0;
        }

        // parses the second number
        token = strtok_r(NULL, " ", &saveptr);
        if (token != NULL) {
            *nB = strtoull(token, NULL, 10);
        } else {
            return 0;
        }
        // Check for extra tokens in the input
        if (strtok_r(NULL, " ", &saveptr) != NULL) {
            return 0;  // Failure: Extra tokens detected
        }

        return 1;
    }

    return 0;
}

void swap(unsigned long long int *a, unsigned long long int *b) {
    unsigned long long int aux = *a;
    *a = *b;
    *b = aux;
}

void iterateNumbers(unsigned long long int nA, unsigned long long int nB) {
    for (unsigned long long int i = nA; i <= nB; i++) {
        if (isPalindrome(i)) {
            printf("%llu\n", i);
        }
    }
}

int isPalindrome(unsigned long long int number) {
    unsigned long long int reversedNumber = 0;
    unsigned long long int originalNumber = number;
    unsigned long long int remainder = 0;
    while (number > 0) {
        remainder = number % 10;
        reversedNumber = reversedNumber * 10 + remainder;
        number = number / 10;
    }
    return reversedNumber == originalNumber;
}
