#include <stdio.h>


int palindromo(int b);
int main(){

    int inicio, fim, i;

    while (1)
    {
        printf("Digite dois numeros positivos e separados por espaço: ");
        scanf("%d %d", &inicio, &fim);


        // checando se os valores são positivos.

        if (inicio >= 0 && fim >= 0)
        {

            // adicionando o menor numero ao inicio.

            if (inicio < fim)
            {
                for (i = inicio + 1; i <= fim; i++)
                {
                    if (palindromo(i))
                    {
                        printf(" %d ", i);
                    }
                }

                
            } // caso o usuario digite o ultimo numero com primeiro.
            else
            {
                for (i = fim + 1; i <= inicio; i++)
                {
                    if (palindromo(i))
                    {
                        printf(" %d ", i);
                    }
                }
            }
            break;

            
        }   // caso seja negativo.
        else
        {
            printf("Os valores são invalidos!\n\n");
        }
    }

    printf("\n");
    return 0;
}


// verificando se o numero é palindromo.
int palindromo(int b)
{
    int invertido = 0, resto, x;

    x = b;

    while (x != 0)
    {
        resto = x % 10;
        invertido = (invertido * 10) + resto;
        x = x / 10;
    }

    if (invertido == b)
    {
        return 1;
    }
    return 0;
}