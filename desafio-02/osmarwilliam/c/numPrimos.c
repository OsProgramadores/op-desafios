#include <stdio.h>

int main()
{
    for (int i = 1; i <= 10000; i++)
    {
        // todo número primo é divido por ele mesmo e por 1, logo, só temos duas possibilidades (1 e o próprio número)
        int count = 0;
        for (int y = 1; y <= i; y++)
        {
            if (i % y == 0)
            {
                count++;
                // iremos calcular quantas vezes um determinado número tem resto = 0.
            }
        }
        if (count == 2)
        // se count for > 2, significa que ele é divisível por 1, ele mesmo, e por outros números. Portanto, não é primo
        {
            printf("%i\n", i);
        }
    }
}