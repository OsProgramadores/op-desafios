#include <stdio.h>
#include <stdlib.h>

void palindromo_1e2digitos(void);
void palindromo_3digitos(void);
void palindromo_4digitos(void);

int main(void)
{
    printf("\n\t\t\tPALINDROMOS DE 1 E 2 DIGITOS\n\n");
    palindromo_1e2digitos();
    printf("\n\n");
    printf("\t\t\tPALINDROMOS DE 3 DIGITOS\n\n");
    palindromo_3digitos();
    printf("\n");
    printf("\t\t\tPALINDROMOS DE 4 DIGITOS\n\n");
    palindromo_4digitos();
    printf("\n\n");
    return 0;
}

void palindromo_1e2digitos(void)
{
    int array[100];
    int mod[100];
    int div[100];

    for(int i = 0; i <= 100; i++)
    {
        array[i] = i;
        if(array[i] < 10)
        {
            printf("[%i]",array[i]);
        }
        else if (array[i] > 10 && array[i]% 11 == 0)
        {
            printf("[%i]",array[i]);
        }
    }
}


void palindromo_3digitos(void)
{
    int array[1000];
    int mod[1000];
    int div[1000];

    for(int i = 100; i <= 1000; i++)
    {
        array[i] = i;
        mod[i] = array[i]%10;
        div[i] = array[i]/100;
        if (mod[i] == div[i])
        {
            printf("[%i]",array[i]);
        }
    }
    printf("\n");

}

void palindromo_4digitos(void)
{
    int array[10000];
    int mod,div,mod1,mod2,prod = 0;

    for(int i = 1000; i <= 10000; i++)
    {
        array[i] = i;
        mod = array[i]%100;
        div = array[i]/100;

        if (mod < div || (mod%11 == 0 && div%11 == 0))
        {
            mod1 = mod%10;
            mod2 = mod/10;
            prod = mod1*10 + mod2;
            if(prod == div)
            {
                printf("[%i]",array[i]);
            }
        }
        if (mod > div)
        {
            mod1 = mod%10;
            mod2 = mod/10;
            prod = mod1*10 + mod2;
            if(prod == div)
            {
                printf("[%i]",array[i]);
            }
        }
    }
}

