#include <stdio.h>

int main(void)
{
    int begin = 100;
    int end = 1000;

    for (int i = begin; i <= end; i++)
    {
        int aux = i;
        int rev = 0;

        while (aux != 0)
        {
            rev = rev * 10 + aux % 10;
            aux = aux / 10;
        }
        if (rev == i)
        {
            printf("%d\n", i);
        }
    }
    return 0;
}
