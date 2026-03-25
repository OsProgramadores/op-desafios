#include "uthash.h" // https://troydhanson.github.io/uthash/  hash table utilizada no processo
#include <fcntl.h>
#include <limits.h>
#include <pthread.h> // não sei explicar pthread.h foi mais rápido que threads.h
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <unistd.h>

#define START_AREAS 2

typedef struct
{
    char *nome;
    char *sobrenome;
} funcionario_t; // funcionário

typedef struct
{
    char *codigo;
    char *nome;
    funcionario_t max[5]; // lista de max
    funcionario_t min[5]; // lista de min
    int max_salario, max_pos;
    int min_salario, min_pos;
    size_t custo;
    int total;
} area_t; // controle de max e min por área

typedef struct
{
    char *sobrenome;
    UT_hash_handle hh; // hash table
    char *max[4];      //lista de max
    int max_salario, max_pos;
    int total;
} sobrenome_t; // controle de max por sobrenome

typedef struct
{
    int max_salario;
    int min_salario;
    int total;
    size_t custo;
} global_t; // controle de max e min global

typedef struct
{
    pthread_t id; // id da thread
    char *buffer; // buffer para processar
} processar_t;    // processo das threads

// Variáveis globais
area_t *areas = NULL;
int areas_size = 0;
sobrenome_t *sobrenomes = NULL;
global_t global;
// mutex -> sinalizações para evitar colisões nos dados
pthread_mutex_t mtx_max;
pthread_mutex_t mtx_min;
pthread_mutex_t mtx_area;
pthread_mutex_t mtx_sbn1;
pthread_mutex_t mtx_sbn2;

void sobrenomes_process(char *nome, char *sobrenome, int salario) // processar o sobrenome
{
    sobrenome_t *pos = NULL;

    // a parte mais demorada é achar
    HASH_FIND_STR(sobrenomes, sobrenome, pos);
    if (pos == NULL)
    {
        pthread_mutex_lock(&mtx_sbn1); // devido a grande repetição de sobrenomes parar aqui e achar novamente gasta menos tempo
        HASH_FIND_STR(sobrenomes, sobrenome, pos);
        if (pos == NULL)
        {
            pos = (sobrenome_t *)malloc(sizeof(sobrenome_t));
            pos->sobrenome = sobrenome;
            pos->total = 0;
            pos->max_salario = 0;
            HASH_ADD_STR(sobrenomes, sobrenome, pos);
        }
        pthread_mutex_unlock(&mtx_sbn1);
    }

    pthread_mutex_lock(&mtx_sbn2);
    pos->total++;
    if (pos->max_salario < salario)
    {
        pos->max_salario = salario;
        pos->max[0] = nome;
        pos->max_pos = 1;
    }
    else if (pos->max_salario == salario)
    {
        pos->max[pos->max_pos++] = nome;
    }
    pthread_mutex_unlock(&mtx_sbn2);
}
void areas_process_max(char *nome, char *sobrenome, int salario, int cod) // processar a área e anotar o valor máximo
{
    pthread_mutex_lock(&mtx_max);
    areas[cod].custo += salario;

    if (areas[cod].max_salario < salario)
    {
        areas[cod].max_salario = salario;
        areas[cod].max_pos = 1;
        areas[cod].max[0].nome = nome;
        areas[cod].max[0].sobrenome = sobrenome;
        if (global.max_salario < salario) // deixo apenas anotado o valor global
            global.max_salario = salario;
    }
    else if (areas[cod].max_salario == salario)
    {
        areas[cod].max[areas[cod].max_pos].nome = nome;
        areas[cod].max[areas[cod].max_pos++].sobrenome = sobrenome;
    }
    pthread_mutex_unlock(&mtx_max);
}

void areas_process_min(char *nome, char *sobrenome, int salario, int cod) // processar a área e anotar o valor mínimo
{
    pthread_mutex_lock(&mtx_min);
    areas[cod].total++;

    if (areas[cod].min_salario > salario)
    {
        areas[cod].min_salario = salario;
        areas[cod].min_pos = 1;
        areas[cod].min[0].nome = nome;
        areas[cod].min[0].sobrenome = sobrenome;
        if (global.min_salario > salario) // deixo apenas anotado o valor global
            global.min_salario = salario;
    }
    else if (areas[cod].min_salario == salario)
    {
        areas[cod].min[areas[cod].min_pos].nome = nome;
        areas[cod].min[areas[cod].min_pos++].sobrenome = sobrenome;
    }
    pthread_mutex_unlock(&mtx_min);
}
int areas_get(char *codigo, int incluir)
{
    int resp = 0;
    while (resp < areas_size)
    {
        if (areas[resp].codigo && codigo[0] == areas[resp].codigo[0] && codigo[1] == areas[resp].codigo[1])
            return resp;
        resp++;
    }
    if (incluir)
    {
        pthread_mutex_lock(&mtx_area);
        if ((resp = areas_get(codigo, 0)) < INT_MAX)
        {
            pthread_mutex_unlock(&mtx_area);
            return resp;
        }
        resp = areas_size;
        areas_size++;
        areas = (area_t *)realloc(areas, sizeof(area_t) * areas_size);
        areas[resp].codigo = codigo;
        areas[resp].nome = NULL;
        areas[resp].total = 0;
        areas[resp].custo = 0;
        areas[resp].max_salario = 0;
        areas[resp].min_salario = INT_MAX;
        pthread_mutex_unlock(&mtx_area);
        return resp;
    }
    return INT_MAX;
}

void *processar(void *processos)
{
    int cod, salario;
    char *nome, *sobrenome, *codigo;
    char *p = ((processar_t *)processos)->buffer;

    while (*p)
    {
        while (*p && *p != '{')
            p++;
        if (*p == 0)
            break;
        while (*p != '"')
            p++;
        p++;
        if (*p == 'i')
        {
            p += 4;
            while (*p != '"')
                p++;
            p += 8;
            nome = p;
            p += 2;
            while (*p != '"')
                p++;
            *p = 0;

            p += 2;
            while (*p != '"')
                p++;
            p += 13;
            sobrenome = p;
            while (*p != '"')
                p++;
            *p = 0;

            p += 2;
            while (*p != '"')
                p++;
            p += 10;
            salario = 0;
            while (*p != '.')
            {
                salario = salario * 10 + *p - '0';
                p++;
            }
            p++;
            salario = salario * 10 + *p - '0';
            p++;
            salario = salario * 10 + *p - '0';

            while (*p != '"')
                p++;
            p += 8;
            codigo = p;
            p += 2;
            *p = 0;
            p++;

            if (codigo[0] == 'A' && codigo[1] == '1') // nada aqui, circulando
                cod = 0;
            else if (codigo[0] == 'A' && codigo[1] == '2')
                cod = 1;
            else
                cod = areas_get(codigo, 1);

            areas_process_max(nome, sobrenome, salario, cod);
            areas_process_min(nome, sobrenome, salario, cod);
            sobrenomes_process(nome, sobrenome, salario);
        }
        else if (*p == 'c')
        {
            p += 9;
            codigo = p;
            p += 2;
            *p = 0;
            p += 2;
            while (*p != '"')
                p++;
            p += 8;

            if (codigo[0] == 'A' && codigo[1] == '1') // nada aqui, circulando
                cod = 0;
            else if (codigo[0] == 'A' && codigo[1] == '2')
                cod = 1;
            else
            {
                cod = areas_get(codigo, 0);
                if (cod == INT_MAX)
                {
                    p += 9;
                    continue;
                }
            }
            areas[cod].nome = p;
            p += 7;
            while (*p != '"')
                p++;
            *p = 0;
            p++;
        }
    }
    return NULL;
}

void show_area_print(area_t *index)
{
    double salariof;
    int i;

    salariof = (double)index->max_salario / 100.F;
    for (i = 0; i < index->max_pos; i++)
    {
        printf("area_max|%s|%s %s|%.2f\n", index->nome, index->max[i].nome, index->max[i].sobrenome, salariof);
        if (index->max_salario == global.max_salario)
            printf("global_max|%s %s|%.2f\n", index->max[i].nome, index->max[i].sobrenome, salariof);
    }
    salariof = (double)index->min_salario / 100.F;
    for (i = 0; i < index->min_pos; i++)
    {
        printf("area_min|%s|%s %s|%.2f\n", index->nome, index->min[i].nome, index->min[i].sobrenome, salariof);
        if (index->min_salario == global.min_salario)
            printf("global_min|%s %s|%.2f\n", index->min[i].nome, index->min[i].sobrenome, salariof);
    }
}

void show_area() // mostrar os resultados por área e global
{
    int i = 0;
    double salariof;
    area_t *index, *most_emp = &areas[0], *least_emp = &areas[0];

    for (; i < areas_size; i++)
    {
        index = &areas[i];

        show_area_print(index);

        global.total += index->total;
        global.custo += index->custo;

        salariof = ((double)index->custo / 100.F) / (double)index->total;
        printf("area_avg|%s|%.2f\n", index->nome, salariof);

        if (index->total > most_emp->total) // área com mais funcionários
            most_emp = index;
        if (index->total < least_emp->total) // área com menos funcionários
            least_emp = index;
    }
    salariof = ((double)global.custo / 100.F) / (double)global.total;
    printf("global_avg|%.2f\n", salariof);

    printf("most_employees|%s|%d\n", most_emp->nome, most_emp->total);
    printf("least_employees|%s|%d\n", least_emp->nome, least_emp->total);
}

void show_sobrenomes() // mostrar os resultados por sobrenomes
{
    double salariof;
    sobrenome_t *index = sobrenomes;
    int i;

    // sobrenomes com mais de 2 funcionários
    for (; index != NULL; index = index->hh.next)
    {
        if (index->total < 2)
            continue;
        salariof = (double)index->max_salario / 100.F;
        for (i = 0; i < index->max_pos; i++)
        {
            printf("last_name_max|%s|%s %s|%.2f\n", index->sobrenome, index->max[i], index->sobrenome, salariof);
        }
    }
}

int main(int argc, char *argv[])
{
    int fjson, i, j;
    struct stat f;
    char *buffer = NULL;
    processar_t *processos; // coletar todos os funcionarios criados e apagar no final
    size_t threads_max = 0, buffer_max = 0;

    if (argc < 2)
    {
        printf("Uso: %s <arquivo json>\n", argv[0]);
        return 0;
    }

    fjson = open(argv[1], O_RDONLY);
    if (fjson < 0)
    {
        printf("Arquivo não encontrado\n");
        exit(1);
    }
    i = fstat(fjson, &f);
    if (i < 0)
    {
        printf("Arquivo não encontrado\n");
        exit(1);
    }
    //inicialização das areas
    areas = (area_t *)malloc(sizeof(area_t) * START_AREAS);
    areas_size = START_AREAS;
    for (i = 0; i < START_AREAS; i++)
    {
        areas[i].codigo = NULL;
        areas[i].nome = NULL;
        areas[i].total = 0;
        areas[i].custo = 0;
        areas[i].max_pos = 0;
        areas[i].min_salario = INT_MAX;
        areas[i].max_salario = 0;
    }
    // inicialização das variaveis do global
    global.custo = 0;
    global.total = 0;
    global.max_salario = 0;
    global.min_salario = INT_MAX;
    // inicialização da sinalização
    pthread_mutex_init(&mtx_max, NULL);
    pthread_mutex_init(&mtx_min, NULL);
    pthread_mutex_init(&mtx_area, NULL);
    pthread_mutex_init(&mtx_sbn1, NULL);
    pthread_mutex_init(&mtx_sbn2, NULL);

    // inicialização do controle de threads
    threads_max = sysconf(_SC_NPROCESSORS_ONLN); // numero de processadores (* o numero de threads em cada);
    if (threads_max < 2)
        threads_max = 2;
    processos = (processar_t *)malloc(sizeof(processar_t) * threads_max);
    buffer_max = (f.st_size / threads_max) + 1; // somo 1 pois a divisão pode não ser exata

    // criação das threads
    j = 0; // funciona como o resto que devia ter sido processado mas não foi na thread anterior
    for (i = 0; i < threads_max; i++)
    {
        size_t buffer_size;
        buffer = (char *)malloc(sizeof(char) * (buffer_max + j));
        buffer_size = read(fjson, buffer, buffer_max + j);
        for (j = 0; buffer[buffer_size - j - 1] != '}'; j++)
            ;
        processos[i].buffer = buffer;
        pthread_create(&processos[i].id, NULL, processar, &processos[i]);
        buffer[buffer_size - j - 1] = 0;
        lseek(fjson, -j, SEEK_CUR);
    }
    close(fjson);
    // encerramento das threads
    for (i = 0; i < threads_max; i++)
        pthread_join(processos[i].id, NULL);

    show_area();
    show_sobrenomes();

    // inicio da limpeza geral
    pthread_mutex_destroy(&mtx_max);
    pthread_mutex_destroy(&mtx_min);
    pthread_mutex_destroy(&mtx_area);
    pthread_mutex_destroy(&mtx_sbn1);
    pthread_mutex_destroy(&mtx_sbn2);

    //liberar toda a memória alocada (usando 'valgrind' para checar eficiencia da limpeza)
    while (sobrenomes != NULL)
    {
        sobrenome_t *current_user, *tmp;
        HASH_ITER(hh, sobrenomes, current_user, tmp)
        {
            HASH_DEL(sobrenomes, current_user); /* delete it (users advances to next) */
            free(current_user);                 /* free it */
        }
    }
    free(areas);
    for (i = 0; i < threads_max; i++)
        free(processos[i].buffer);
    free(processos);
}
