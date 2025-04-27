#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define BUFFER_SIZE 512
#define MAX_NUM_SIZE 20


int get_mdc(int num, int den);


int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "usage: %s [file path]\n", argv[0]);

        return 1;
    }

    FILE *input_file = fopen(argv[1], "rb");
    if (input_file == NULL)
    {
        fprintf(stderr, "failed opening %s\n", argv[1]);

        return 1;
    }

    char line[BUFFER_SIZE];
    while (fgets(line, BUFFER_SIZE, input_file))
    {
        line[strcspn(line, " \r\n")] = '\0';

        if (line[0] == '\0') continue;

        if (!strchr(line, '/'))
        {
            printf("%s\n", line);

            continue;
        }

        int div = (int)strcspn(line, "/");

        char s_num[MAX_NUM_SIZE] = {'\0'};
        for (int i = 0; i < div; i++)
        {
            s_num[i] = line[i];
        }

        char s_den[MAX_NUM_SIZE] = {'\0'};
        for (int i = 0, j = div + 1; line[j] != '\0'; i++, j++)
        {
            s_den[i] = line[j];
        }

        int num = atoi(s_num);
        int den = atoi(s_den);
        
        if (den == 0)
        {
            printf("ERR\n");

            continue;
        }

        else if (den == 1)
        {
            printf("%d\n", num);

            continue;
        }

        int mdc = get_mdc(num, den);
        // printf("mdc = %d | ", mdc);

        if (num == den)
        {
            printf("%d\n", 1);
        }

        else if (num > den)
        {
            int division = num / den;
            int rest = num % den;

            if (rest == 0)
            {
                printf("%d\n", division);

                continue;
            }
            
            printf("%d %d/%d\n", division, rest, den);
        }

        else if (num < den)
        {
            if (((num / mdc) / (den / mdc)) == num / den)
            {
                num /= mdc;
                den /= mdc;
            }

            printf("%d/%d\n", num, den);
        }
    }

    fclose(input_file);

    return 0;
}


int get_mdc(int num, int den)
{
    while (den != 0)
    {
        int r = num % den;
        num = den;
        den = r; 
    }

    return num;
}
