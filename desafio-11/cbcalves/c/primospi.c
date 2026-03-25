// compilar no unix/linux
// > gcc -Ofast primospi.c -o primospi -lm
//
// compilado no MINGW64 (Windows)
// $ gcc -Ofast primospi.c -o primospi -lm
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ORGANIZE 1000 // a cada ORGANIZE em primos eu vejo a maior sequencia e apago a array de primos

typedef struct pilist_st
{
    char *start;
    char *end;
} pilist_t; // lista de números primos extraídos de PI

//// Variáveis globais
pilist_t maior;          // maior início e final
int *primos_list = NULL; // lista de números primos de 2 até 9973
char *buffer = NULL;     // arquivo do número PI
size_t buffer_size = 0;  // tamanho do arquivo do número PI
pilist_t *lista = NULL;  // lista de primos de PI
size_t lista_size = 0;   // tamanho da lista
//// Fim das variáveis globais

void free_all() // limpeza de toda a memória alocada
{
    if (lista)
        free(lista);
    if (primos_list)
        free(primos_list);
    if (buffer)
        free(buffer);
}

void primos_init() // construtor dos primos de 1 a 9973 (solução do desafio 2)
{
    int primos_size = 4, j = 0;
    primos_list = (int *)malloc(sizeof(int) * 1230);
    if (!primos_list)
    {
        printf("Memória insuficiente para alocar a lista de números primos\n");
        exit(1);
    }
    primos_list[0] = 2;
    primos_list[1] = 3;
    primos_list[2] = 5;
    primos_list[3] = 7;
    for (int i = 11; i < 9974; i += 2)
    {
        if ((i % 5) == 0 || (i % 3) == 0)
            continue;
        for (j = 3; j < primos_size; j++)
        {
            if ((i % primos_list[j]) == 0)
                break;

            if ((i / primos_list[j]) < primos_list[j])
            {
                j = primos_size;
                break;
            }
        }
        if (j == primos_size)
        {
            primos_size++;
            primos_list[primos_size - 1] = i;
        }
    }
    primos_list[primos_size] = 0;
}

int primos_isprimo(int i) // retorna se um número está na lista de primos ou não
{
    int *p = primos_list;
    if (i < 2)
        return 0;
    while (*p && *p < i)
        p++;
    if (*p > i || *p == 0)
        return 0;
    return 1;
}

char *processar_maiorprimo_r(char *in_end, int k) // processo recursivo para achar a maior sequencia de primos possível
{
    char *max = in_end, *resp = NULL;

    for (; k < lista_size - 1; k++)
    {
        if ((in_end + 1) < lista[k].start) // como está em ordem de início, se o início ficou mais alto que o final procurado, não existe mais sequencia
            break;
        if ((in_end + 1) == lista[k].start) // se o início é igual ao final, aumenta a sequencia para verificar
        {
            resp = processar_maiorprimo_r(lista[k].end, k + 1);
            if (max < resp)
                max = resp;
        }
    }
    return max;
}

void processar_maiorprimo() // analise das recursões
{
    char *resp = NULL;

    for (int k = 0; k < lista_size - 1; k++)
    {
        resp = processar_maiorprimo_r(lista[k].end, k + 1);
        if ((maior.end - maior.start) < (resp - lista[k].start))
        {
            maior.start = lista[k].start;
            maior.end = resp;
        }
    }

    // uso a primeira posição para anotar o resultado até agora e saber se ele tem continuidade
    // no próximo processamento
    lista[0].start = maior.start;
    lista[0].end = maior.end;
    lista_size = 1;
}
void processar_quicksort(int l, int r) //sort da array de primos pelo menor endereço de "start"
{
    pilist_t *v = &lista[r];
    pilist_t tmp;
    int i = l - 1, j = r;
    if (r <= l)
        return;
    while (1)
    {
        while (lista[++i].start < v->start)
            ;
        while (v->start < lista[--j].start)
        {
            if (j == l)
                break;
        }
        if (i >= j)
            break;
        memcpy(&tmp, &lista[i], sizeof(pilist_t));
        memcpy(&lista[i], &lista[j], sizeof(pilist_t));
        memcpy(&lista[j], &tmp, sizeof(pilist_t));
    }
    memcpy(&tmp, &lista[i], sizeof(pilist_t));
    memcpy(&lista[i], &lista[r], sizeof(pilist_t));
    memcpy(&lista[r], &tmp, sizeof(pilist_t));

    processar_quicksort(l, i - 1);
    processar_quicksort(i + 1, r);
}

void processar() // ler o arquivo de PI, separar os primos e chamar as funcoes que calculam as sequencias
{
    char s1[2] = {0, 0}, s2[3] = {0, 0, 0}, s3[4] = {0, 0, 0, 0}, s4[5] = {0, 0, 0, 0, 0};
    char *p = buffer;

    lista = (pilist_t *)malloc(sizeof(pilist_t) * (ORGANIZE + 4));
    if (!lista)
    {
        printf("Memória insuficiente para alocar a lista de números primos de PI\n");
        free_all();
        exit(1);
    }

    while (*p != '.')
        p++;
    p++;

    fprintf(stdout, "%03d%%", 0);
    while (*p)
    {
        s1[0] = *p;
        s2[0] = s2[1], s2[1] = *p;
        s3[0] = s3[1], s3[1] = s3[2], s3[2] = *p;
        s4[0] = s4[1], s4[1] = s4[2], s4[2] = s4[3], s4[3] = *p;

        if (primos_isprimo(atoi(s1))) // somente 1 char
        {
            lista[lista_size].end = p;
            lista[lista_size].start = p;
            lista_size++;
        }
        if (s2[0] && primos_isprimo(atoi(s2))) // somente 2 chars
        {
            lista[lista_size].end = p;
            lista[lista_size].start = p - 1;
            lista_size++;
        }
        if (s3[0] && primos_isprimo(atoi(s3))) // somente 3 chars
        {
            lista[lista_size].end = p;
            lista[lista_size].start = p - 2;
            lista_size++;
        }
        if (s4[0] && primos_isprimo(atoi(s4))) // somente 4 chars
        {
            lista[lista_size].end = p;
            lista[lista_size].start = p - 3;
            lista_size++;
        }
        if (ORGANIZE < lista_size) // a cada ORGANIZE primos na lista ele faz o processamento e apaga a lista
        {
            fprintf(stdout, "\b\b\b\b%03ld%%", ((p - buffer) / 10000)); // esperar sem saber o progresso cansa
            fflush(stdout);
            processar_quicksort(0, lista_size - 1); // sort da array
            processar_maiorprimo();                 // processa a array
        }

        p++;
    }
    fprintf(stdout, "\b\b\b\b100%%");
    processar_quicksort(0, lista_size - 1);
    processar_maiorprimo(); // caso ainda tenha algum número incluído na lista, processa antes de retornar
}

int main()
{
    FILE *fs = NULL;

    fs = fopen("pi-1M.txt", "r"); // abrir o arquivo e alocar na memória para processar
    if (!fs)
    {
        printf("Erro ao ler o arquivo\n");
        exit(1);
    }
    fseek(fs, 0, SEEK_END);
    buffer_size = ftell(fs);
    fseek(fs, 0, SEEK_SET);
    buffer = (char *)malloc(sizeof(char) * (buffer_size + 1));
    if (!buffer)
    {
        printf("Memória insuficiente para abrir o arquivo\n");
        fclose(fs);
        free_all();
        exit(1);
    }
    buffer_size = fread(buffer, 1, buffer_size, fs);
    if (buffer_size == 0)
    {
        printf("Erro ao ler o arquivo\n");
        fclose(fs);
        free_all();
        exit(1);
    }
    fclose(fs);

    primos_init();
    processar();

    *++maior.end = 0; // para mostrar entre maior inicio e maior fim eu sinalizo que a string acabou em maior.end+1
    printf("\b\b\b\b%s\n", maior.start);

    free_all();

    return 0;
}
