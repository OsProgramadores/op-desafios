#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *bigbase(int basein, int baseout, char *numero)
{
    char bases[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    char *resp = NULL, *p = numero;
    int resto = 0, aux = 0;

    // restrições ao funcionamento, as bases não podem ser maiores que a string contendo todos os símbolos possíveis
    // matemáticamente não existe base 1 e 0, pois não são possíveis de serem representadas
    // o limite de tamanho no final do if é da descrição do desafio
    if (basein > strlen(bases) || baseout > strlen(bases) || baseout < 2 || basein < 2 || (basein == 62 && strlen(numero) > 30))
    {
        resp = (char *)malloc(sizeof(char) * 4);
        if (!resp)
        {
            printf("Memória insuficiente!");
            return NULL;
        }
        resp[0] = '?', resp[1] = '?', resp[2] = '?', resp[3] = 0;
        return resp;
    }

    while (*p)
    {
        resto = 0;
        while (*p)
        {
            for (aux = 0; aux < basein; aux++) // encontrar a posição do símbolo em 'bases' vai dizer o valor numérico dele
            {
                if (bases[aux] == *p)
                    break;
            }
            if (aux == basein) // se não encontrar até o limite de basein, significa que o símbolo não pertence a base de entrada
            {
                if (!resp || strlen(resp) < 3)
                {
                    resp = (char *)realloc(resp, sizeof(char) * 4);
                    if (!resp)
                    {
                        printf("Memória insuficiente!");
                        return NULL;
                    }
                }
                resp[0] = '?', resp[1] = '?', resp[2] = '?', resp[3] = 0;
                return resp;
            }
            // basicamente a operação matemática sendo feita é saída = entrada / baseout símbolo por símbolo pois é string
            aux += (resto * basein);     // soma o resto da divisão anterior ao novo valor encontrado
            resto = aux % baseout;       // calculo do resto do valor pela base de saída
            *p++ = bases[aux / baseout]; // guardar o valor inteiro na string de entrada para continuar usando na conta
        }
        if (resp) // aumento da string de saída a cada interação (não sei qual tamanho terá até o final)
        {
            aux = strlen(resp);
            resp = (char *)realloc(resp, sizeof(char) * (aux + 2));
            if (!resp)
            {
                printf("Memória insuficiente!");
                return NULL;
           }
            memcpy(&resp[1], &resp[0], sizeof(char) * (aux + 1)); // move o conteúdo atual para o fim da string, o próximo elemento é no início da string
        }
        else
        {
            resp = (char *)malloc(sizeof(char) * 2);
            resp[1] = 0;
            if (!resp)
            {
                printf("Memória insuficiente!");
                return NULL;
            }
        }
        resp[0] = bases[resto]; // o resto dessa operação vai preenchendo a string de saída
        p = numero;
        while (*p == '0') // pula os '0' à esquerda da string de entrada
            p++;
    }
    return resp;
}

int main(int argc, char **argv)
{
    int basein = 0, baseout = 0;
    char numero[200], *novo_numero = NULL;

    if (argc > 1)
    {
        printf("Uso 1: $ %s\nBase_In Base_Out Numero\nEx: 10 16 100\n Ctrl+C para sair\n\n", argv[0]);
        printf("Uso 2: $ %s < [arquivo com os dados]\n", argv[0]);
        return 1;
    }

    while (fgets(numero, sizeof(numero), stdin))
    {
        sscanf(numero, "%d %d %s", &basein, &baseout, numero);
        novo_numero = bigbase(basein, baseout, numero);
        if (!novo_numero)
            break;
        printf("%s\n", novo_numero);
        free(novo_numero);
        novo_numero = NULL;
    }
    return 0;
}
