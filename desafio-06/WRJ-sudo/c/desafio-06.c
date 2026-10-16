#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define WORDLEGTH 16

void converter_para_maiusculo(char string[]);
void ordenar_string(char x[]);
int comparar_string(char string1[], char string2[]);

int tamanho_string;

int main(int argc, char *argv[])
{
    char string[WORDLEGTH];
    char anagrama[WORDLEGTH];
    char anagramaOrdenado[WORDLEGTH];
    char *strEntrada;

    FILE *file;

    if (argc != 2)
    {
        printf("Execute o comando passando apenas um argumentos: ./desafio4 <palavra>\n");
        return 1;
    }
    if (argv[1][0] == '\0' || ' ')
    {
        printf("O argumento passado deve ser string nao vazia\n");
        return 1;
    }
    if (strlen(argv[1]) >= WORDLEGTH)
    {
        printf("Entrada invalida! Palavra muito grande.\n");
        return 1;
    }
    int j = 0;
    for (int i = 0; argv[1][i] != '\0'; i++)
    {

        if (isspace((unsigned char)argv[1][i]))
        {
            continue;
            j++;
        }
        else
        {
            string[j] = argv[1][i];
            j++;
        }
    }
    string[j] = '\0';

    for (int i = 0; string[i] != '\0'; i++)
    {

        if (!isalpha((unsigned char)string[i]))
        {
            printf("O argumento passado deve ser string composta apenas por letras \n");
            return 1;
        }
    }

    strEntrada = string;

    tamanho_string = strlen(strEntrada);

    converter_para_maiusculo(strEntrada);
    ordenar_string(strEntrada);

    file = fopen("words.txt", "r");

    if (file == NULL)
    {
        return 0;
    }

    while (fgets(anagrama, WORDLEGTH, file) != NULL)
    {

        anagrama[strcspn(anagrama, "\n")] = '\0';

        if (strlen(strEntrada) != strlen(anagrama))
        {
            continue;
        }

        strcpy(anagramaOrdenado, anagrama);
        ordenar_string(anagramaOrdenado);
        if (comparar_string(strEntrada, anagramaOrdenado) == 0)
        {

            printf("%s\n", anagrama);
        }
        else
        {
            continue;
        }
    }
    fclose(file);
    return 0;
}

void converter_para_maiusculo(char string[])
{

    for (int i = 0; string[i] != '\0'; i++)
    {
        string[i] = toupper((unsigned char)string[i]);
    }
}

void ordenar_string(char x[])
{

    int hold;
    int passada;
    int tamanho_string;
    int limite;

    tamanho_string = strlen(x);
    limite = tamanho_string - 1;

    for (int loop = 0; loop < tamanho_string; loop++)
    {
        passada = 0;

        for (int i = 0; i < limite; i++)
        {

            if (x[i] > x[i + 1])
            {
                hold = x[i];
                x[i] = x[i + 1];
                x[i + 1] = hold;
                passada++;
            }
        }
        limite--;
        // verifica se precisa de uma nova passada
        if (passada == 0)
        {
            break;
        }
    }
}

int comparar_string(char string1[], char string2[])
{

    for (int i = 0; i < tamanho_string; i++)
    {

        if (string1[i] != string2[i])
        {
            return 1;
        }
    }
    return 0;
}