#include <stdio.h>

int main()
{
    for (int i = 1; i <= 10000; i++)
    {
        // todo número primo é divido por ele mesmo e por 1, logo, só temos duas possibilidades (1 e o próprio número)
        int count = 0;
        for (int j = 2; j < i / 2; j++) // entretando, não é necessário iterar por todos números, para otimizar iremos análisar sempre até a metade do determinado número
        // exemplo, dentre os divisores de 64, o 32 é o último número, uma vez que a partir do 32 nenhum número terá resto = 0, 
        // assim como 15, a partir do 7,5 não é necessário procurar algum divisor
        {
            if (i % j == 0)
            {
                count++;
                // iremos calcular quantas vezes um determinado número tem resto = 0.
            }
        }
        if (count == 0)
        {
            printf("%i\n", i);
        }
    }
    return 0;
}