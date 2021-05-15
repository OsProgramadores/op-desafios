#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Tamanho máximo da linha */
#define MAX_LENGTH 1000

void processLine(char*);

FILE *readFile(const char*);

void printLine(int, int, int);

int main(int argc, char* argv[])
{
    FILE *arquivo = readFile(argv[1]);

    if(arquivo == NULL) {
        printf("Nome de arquivo incorreto!\n");
	printf("Digite ./desafio8 <nome-arquivo-leitura> \n");

	exit(EXIT_FAILURE);
    }

    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    while((read = getline(&line, &len, arquivo)) != -1) {
        processLine(line);
    }

    fclose(arquivo);

    if(line)
        free(line);

    return EXIT_SUCCESS;
}

FILE *readFile(const char *nomeArquivo)
{
    return fopen(nomeArquivo, "r");
}

void processLine(char *line)
{
    char *ptr;
    int count = 0;
    int numerador = 0;
    int denominador = 0;

    ptr = strtok(line, "/\n");

    while(ptr != NULL) {
        switch(count){
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

    if(ptr)
        free(ptr);

    printLine(count, numerador, denominador);

    return;
}

void printLine(int count, int numerador, int denominador)
{
    if(count == 1){
        printf("%d\n", numerador);
	return;
    }

    if(count > 1 && denominador == 0){
        printf("ERR\n");
	return;
    }

    int numResposta = 0;
    int denoResposta = 0;

    if(numerador >= denominador){
        int intResposta = numerador / denominador;
	numResposta = numerador % denominador;

	if(numResposta == 0)
	    printf("%d\n", intResposta);
	else
            printf("%d %d/%d\n", intResposta, numResposta, denominador);

	return;
    }

    int divisor = 1;

    for(int i=2; i<=numerador; i++){
        if((numerador%i) == 0 && (denominador%i) == 0)
            divisor = i;
    }

    if(divisor == 1){
        printf("%d/%d\n", numerador, denominador);
	return;
    }

    numResposta = numerador / divisor;
    denoResposta = denominador / divisor;

    printf("%d/%d\n", numResposta, denoResposta);

    return;
}
