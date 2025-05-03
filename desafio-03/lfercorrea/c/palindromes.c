#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define LEN 20

bool is_palindrome(size_t number);
size_t prompt_number(const char *prompt_text);

int main(void)
{
    size_t initial_number = prompt_number("Type the initial number: ");
    if (initial_number == (size_t)-1)
    {
        return 1;
    }

    size_t terminal_number = prompt_number("Type te terminal number: ");
    if (terminal_number == (size_t)-1)
    {
        return 1;
    }

    // unsigned int initial_number = 1;
    // unsigned int terminal_number = 100000;
    
    if (initial_number > terminal_number)
    {
        fprintf(stderr, "there's nno point in setting initial number greater than the terminal number\n");

        return 1;
    }

    for (size_t i = initial_number; i <= terminal_number; i++)
    {
        if (is_palindrome(i))
        {
            printf("%zu\n", i);
        }
    }

    return 0;
}


bool is_palindrome(size_t number)
{
    if (number < 10) return true;

    size_t normal = number, inverted = 0;
    while (normal > 0)
    {
        size_t rest = normal % 10;
        inverted = (inverted * 10) + rest;

        normal /= 10;
    }

    return number == inverted;
}


size_t prompt_number(const char *prompt_text)
{
    char input[LEN] = {'\0'};

    printf("%s", prompt_text);

    if (fgets(input, sizeof(input), stdin) == NULL)
    {
        fprintf(stderr, "fgets() failure\n");

        return (size_t)-1;
    }

    input[strcspn(input, "\n")] = '\0';
    if (input[0] == '\0') {
        fprintf(stderr, "input cannot be empty\n");

        return (size_t)-1;
    }

    char *alpha;
    unsigned long long number = strtoull(input, &alpha, 10);
    if (*alpha != '\0')
    {
        fprintf(stderr, "you've typed an alpha char\n");

        return (size_t)-1;
    }

    if (number <= 0)
    {
        fprintf(stderr, "please start with a number greater than 0 in the fisrt prompt\n");

        return (size_t)-1;
    }

    return (size_t)number;
}
