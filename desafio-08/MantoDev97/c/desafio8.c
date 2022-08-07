//Desafio 8 osProgramadores. MantoDev97.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LENGTH 500 //definindo tamanho da linha

void processLine(char *);
FILE *readFile(const char *);
void printLine(int, int, int);
int main(int argc, char *argv[])
{
    FILE *arquivo = readFile(argv[1]);

    if (arquivo == NULL)
    {
        printf("Erro nome de arquivo\n"); //definindo mensagem de erro (nome do arquivo)
        printf("digite ./desafio8 frac.txt \n"); //instrução para corrigir o erro nome do arquivo
        exit(EXIT_FAILURE);
    }

    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    while ((read = getline(&line, &len, arquivo)) != -1)
    {
        processLine(line);
    }

    fclose(arquivo);

    if (line)
        free(line);
     return EXIT_SUCCESS;
}

FILE *readFile(const char *nomeArquivo)
{
    return fopen(nomeArquivo, "r");
}

void processLine(char *line)
{
    //declarando variaveis
    char *ptr;
    int count = 0;
    int numerador = 0;
    int denominador = 0;

    ptr = strtok(line, "/\n");

    while (ptr != NULL)
    {
        switch (count)
        {
        case 0:
            numerador = atoi(ptr);
                break;
        case 1:
            denominador = atoi(ptr);
                break;
        default:
            exit(EXIT_FAILURE);
        }

        count++;
        ptr = strtok(NULL, "/\n");
    }

    if (ptr)
        free(ptr);

    printLine(count, numerador, denominador);
        return;
}

void printLine(int count, int numerador, int denominador) //trabalhando com int variaveis
{
    if (count == 1)
    {
        printf("%d\n", numerador);
         return;
    }
    if (count > 1 && denominador == 0)
    {
        printf("ERR\n"); //erro na entrada numero 0(zero)
         return;
    }
    //declarando variaveis
    int numeradorResposta = 0;
    int denominadorResposta = 0;
    if (numerador >= denominador)
    {
        int intResposta = numerador / denominador;
        numeradorResposta = numerador % denominador;

        if (numeradorResposta == 0) //se numeradorResposta true
            printf("%d\n", intResposta); //imprimi intResposta
        else
            printf("%d %d/%d\n", intResposta, numeradorResposta, denominador); //imprimi intResposta/numeradorResposta

        return;
    }

    int divisor = 1;
    for (int i = 2; i <= numerador; i++)
    {
        if ((numerador % i) == 0 && (denominador % i) == 0)
            divisor = i;
    }
        if (divisor == 1)
    {
        printf("%d/%d\n", numerador, denominador);
        return;
    }
    numeradorResposta = numerador / divisor;
    denominadorResposta = denominador / divisor;
    printf("%d/%d\n", numeradorResposta, denominadorResposta);

    return;
}
