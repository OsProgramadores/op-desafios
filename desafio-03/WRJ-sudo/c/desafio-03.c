#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#define TAMANHO 20 // tamanho máximo de caracteres mais o '\0'

long long int inicial;
long long int final;
char *strInicial;
char *strFinal;

int buscar_palindromo();
int validador_num();
int get_valor();
void imprimir(char *str);

int main(int argc, char *argv[])
{

    if (argc < 3)
    {
        printf("E preciso passar os dois valores\n");
        return 0;
    }
    else if (strlen(argv[1]) >= TAMANHO || strlen(argv[2]) >= TAMANHO)
    {
        printf("Entrada invalida! Numero muito grande.\n");
        return 0;
    }
    else
    {
        strInicial = argv[1];
        strFinal = argv[2];
        return buscar_palindromo();
    }
}

int buscar_palindromo()
{
    long long int contador;
    char str_lida[TAMANHO] = {0};
    char str_a_acomparar[TAMANHO];

    if (get_valor(1) == 0)
    {
        return 0;
    }

    const long long int num_inicial = inicial;

    if (get_valor(2) == 0)
    {
        return 0;
    }

    if (inicial > final)
    {

        printf("O primeiro numero precisa ser menor que o segundo \n");
        return 0;
    }

    const long long int limite = final;

    for (long long contador = num_inicial; contador <= limite; contador++)
    {

        // pega o numero atual em contador e coloca na string
        sprintf(str_lida, "%lld", contador);
        int aux = 0;

        int tam_input = 0;
        // pegando o tamanho da string
        tam_input = strlen(str_lida);

        // criando a string invertida e colocando em outro array;
        for (int i = tam_input - 1; i >= 0; i--)
        {

            str_a_acomparar[aux] = str_lida[i];
            aux++;
            // colocando um fim de curso na string atual
            str_a_acomparar[tam_input] = '\0';
        }

        // casting para inteiro long long
        long long a = atoll(str_lida);
        long long b = atoll(str_a_acomparar);
        // imprime se for palindromo
        if (a == b)
        {
            printf("%s\n", str_lida);
        }
        // para o loop para caso de overflow
        if (contador == limite)
        {
            break;
        }
    }
}

int get_valor(int x)
{

    long long numero;
    char entrada[TAMANHO];
    char *fim;
    if (x == 1)
    {
        int i = 0;
        while (*strInicial != '\0')
        {
            entrada[i] = *strInicial;
            strInicial++;
            i++;
        }
        entrada[i] = '\0';
    }
    else
    {
        int i = 0;
        while (*strFinal != '\0')
        {
            entrada[i] = *strFinal;
            strFinal++;
            i++;
        }
        entrada[i] = '\0';
    }

    for (int i = 0; entrada[i] != '\0'; i++)
    {
        switch (entrada[i])
        {
        case 48:
            continue;
        case 49:
            continue;
        case 50:
            continue;
        case 51:
            continue;
        case 52:
            continue;
        case 53:
            continue;
        case 54:
            continue;
        case 55:
            continue;
        case 56:
            continue;
        case 57:
            continue;
        case '\n':
            continue;
        default:
            printf("Entrada invalida!\n");
            return 0;
        }
    }
    errno = 0;
    numero = strtoll(entrada, &fim, 10);
    if (errno == ERANGE)
    {
        // verifica se entrada está dentro do limite long long int
        printf("Entrada invalida! Numero muito grande.\n");
        return 0;
    }

    if (x == 1)
    {
        inicial = numero;
    }
    else
    {
        final = numero;
    }

    return 1;
}
