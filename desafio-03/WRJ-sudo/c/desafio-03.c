#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <ctype.h>
#include <limits.h>

#define TAMANHO 20

long long int inicial;
long long int final;
long long numero;

char *strInicial;
char *strFinal;

int buscar_palindromo();
int get_valor(char *string);

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        printf("E preciso passar os dois valores\n");
        return 1;
    }
    if (argv[1][0] == '\0' || argv[2][0] == '\0')
    {
        printf("E preciso passar os dois valores\n");
        return 1;
    }

    if (strlen(argv[1]) >= TAMANHO || strlen(argv[2]) >= TAMANHO)
    {
        printf("Entrada invalida! Numero muito grande.\n");
        return 1;
    }

    strInicial = argv[1];
    strFinal = argv[2];

    return buscar_palindromo();
}

int buscar_palindromo()
{
    char str_lida[TAMANHO] = {0};
    char str_a_acomparar[TAMANHO];

    if (get_valor(strInicial) == 1)
    {
        return 1;
    }
    else
    {
        inicial = numero;
    }

    const long long int num_inicial = inicial;

    if (get_valor(strFinal) == 1)
    {
        return 1;
    }
    else
    {
        final = numero;
    }

    if (inicial > final)
    {
        printf("O primeiro numero precisa ser menor que o segundo\n");
        return 1;
    }

    const long long int limite = final;

    for (long long contador = num_inicial;
         contador <= limite;
         contador++)
    {
        sprintf(str_lida, "%lld", contador);

        int aux = 0;
        int tam_input = strlen(str_lida);

        for (int i = tam_input - 1; i >= 0; i--)
        {
            str_a_acomparar[aux] = str_lida[i];
            aux++;
        }

        str_a_acomparar[tam_input] = '\0';

        long long a = atoll(str_lida);
        long long b = atoll(str_a_acomparar);

        if (a == b)
        {
            printf("%s\n", str_lida);
        }

        if (contador == limite)
        {
            break;
        }
    }

    return 0;
}

int get_valor(char *string)
{
    char entrada[TAMANHO];
    char *fim;

    strncpy(entrada, string, sizeof(entrada) - 1);
    entrada[sizeof(entrada) - 1] = '\0';

    for (int i = 0; entrada[i] != '\0'; i++)
    {
        if (!isdigit((unsigned char)entrada[i]))
        {
            printf("Entrada invalida!\n");
            return 1;
        }
    }

    errno = 0;

    numero = strtoll(entrada, &fim, 10);

    if (errno == ERANGE)
    {
        printf("Entrada invalida! Numero muito grande.\n");
        return 1;
    }

    if (*fim != '\0')
    {
        printf("Entrada invalida!\n");
        return 1;
    }

    return 0;
}