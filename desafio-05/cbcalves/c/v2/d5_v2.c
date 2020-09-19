#include "uthash.h" // https://troydhanson.github.io/uthash/  hash table utilizada no processo
#include <fcntl.h>
#include <limits.h>
#include <pthread.h> // não sei explicar pthread.h foi mais rápido que threads.h
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <unistd.h>

#define START_AREAS 2

typedef struct funcionario_st
{
    char *nome;
    char *sobrenome;
    int salario;
    char *codigo;
    struct funcionario_st *next;  // apontando para o próximo funcionario
    struct funcionario_st *area;  // apontando para o próximo max ou min
    struct funcionario_st *snome; // apontando para o próximo sobrenome max
} funcionario_t;                  // funcionário

typedef struct area_st
{
    char *codigo;
    char *nome;
    funcionario_t *max; // lista de max
    funcionario_t *min; // lista de min
    size_t custo;
    int total;
    int max_salario;
    int min_salario;
} area_t; // controle de max e min por área

typedef struct
{
    char *sobrenome;
    UT_hash_handle hh;  // hash table
    funcionario_t *max; //lista de max
    int total;
    int max_salario;
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
    pthread_t id;           // id da thread
    char *buffer;           // buffer para processar
    funcionario_t *coletor; // lista de funcionarios para apagar
} processar_t;              // processo das threads

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

int sobrenomes_process(void *funcionario) // processar o sobrenome
{
    funcionario_t *func = (funcionario_t *)funcionario;
    sobrenome_t *pos = NULL;
    int sinal = 0;

    // a parte mais demorada é achar
    HASH_FIND_STR(sobrenomes, func->sobrenome, pos);
    if (pos == NULL)
    {
        pthread_mutex_lock(&mtx_sbn1); // devido a grande repetição de sobrenomes parar aqui e achar novamente gasta menos tempo
        HASH_FIND_STR(sobrenomes, func->sobrenome, pos);
        if (pos == NULL)
        {
            pos = (sobrenome_t *)malloc(sizeof(sobrenome_t));
            pos->sobrenome = func->sobrenome;
            pos->total = 0;
            pos->max = NULL;
            pos->max_salario = 0;
            HASH_ADD_STR(sobrenomes, sobrenome, pos);
        }
        pthread_mutex_unlock(&mtx_sbn1);
    }

    pthread_mutex_lock(&mtx_sbn2);
    pos->total++;
    if (pos->max_salario < func->salario)
    {
        pos->max_salario = func->salario;
        pos->max = func;
        sinal = 1;
    }
    else if (pos->max_salario == func->salario)
    {
        func->snome = pos->max;
        pos->max = func;
        sinal = 1;
    }
    pthread_mutex_unlock(&mtx_sbn2);
    return sinal;
}
int areas_process_max(void *funcionario, int cod) // processar a área e anotar o valor máximo
{
    funcionario_t *func = (funcionario_t *)funcionario;
    int sinal = 0;

    pthread_mutex_lock(&mtx_max);
    areas[cod].total++;

    if (areas[cod].max_salario < func->salario)
    {
        areas[cod].max_salario = func->salario;
        areas[cod].max = func;
        pthread_mutex_unlock(&mtx_max);
        if (global.max_salario < func->salario) // deixo apenas anotado o valor global
            global.max_salario = func->salario;
        sinal = 1;
        return sinal;
    }
    else if (areas[cod].max_salario == func->salario)
    {
        func->area = areas[cod].max;
        areas[cod].max = func;
        sinal = 1;
    }
    pthread_mutex_unlock(&mtx_max);
    return sinal;
}

int areas_process_min(void *funcionario, int cod) // processar a área e anotar o valor mínimo
{
    funcionario_t *func = (funcionario_t *)funcionario;
    int sinal = 0;

    pthread_mutex_lock(&mtx_min);
    areas[cod].custo += func->salario;

    if (areas[cod].min_salario > func->salario)
    {
        areas[cod].min_salario = func->salario;
        areas[cod].min = func;
        pthread_mutex_unlock(&mtx_min);
        if (global.min_salario > func->salario) // deixo apenas anotado o valor global
            global.min_salario = func->salario;
        sinal = 1;
        return sinal;
    }
    else if (areas[cod].min_salario == func->salario)
    {
        func->area = areas[cod].min;
        areas[cod].min = func;
        sinal = 1;
    }
    pthread_mutex_unlock(&mtx_min);
    return sinal;
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
        areas[resp].max = NULL;
        areas[resp].min = NULL;
        areas[resp].max_salario = 0;
        areas[resp].min_salario = INT_MAX;
        pthread_mutex_unlock(&mtx_area);
        return resp;
    }
    return INT_MAX;
}

void *processar(void *processos)
{
    int sinal = 1, cod;
    char *codigo = NULL;
    char *p = ((processar_t *)processos)->buffer;
    funcionario_t *ret = NULL, *novo = NULL;

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
            if (sinal) // usa o retorno dos processamentos para definir se precisa alocar outra ficha
            {
                novo = (funcionario_t *)malloc(sizeof(funcionario_t));
                novo->next = ret;
                ret = novo;
                ret->snome = NULL;
                ret->area = NULL;
                sinal = 0;
            }

            p += 4;
            while (*p != '"')
                p++;
            p += 8;
            ret->nome = p;
            p += 2;
            while (*p != '"')
                p++;
            *p = 0;

            p += 2;
            while (*p != '"')
                p++;
            p += 13;
            ret->sobrenome = p;
            while (*p != '"')
                p++;
            *p = 0;

            p += 2;
            while (*p != '"')
                p++;
            p += 10;
            ret->salario = 0;
            while (*p != '.')
            {
                ret->salario = ret->salario * 10 + *p - '0';
                p++;
            }
            p++;
            ret->salario = ret->salario * 10 + *p - '0';
            p++;
            ret->salario = ret->salario * 10 + *p - '0';

            while (*p != '"')
                p++;
            p += 8;
            ret->codigo = p;
            p += 2;
            *p = 0;
            p++;

            if (ret->codigo[0] == 'A' && ret->codigo[1] == '1') // nada aqui, circulando
                cod = 0;
            else if (ret->codigo[0] == 'A' && ret->codigo[1] == '2')
                cod = 1;
            else
                cod = areas_get(ret->codigo, 1);

            sinal += areas_process_max(ret, cod);
            sinal += areas_process_min(ret, cod);
            sinal += sobrenomes_process(ret);
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
    ((processar_t *)processos)->coletor = ret;
    return NULL;
}

void show_area_print(area_t *index)
{
    funcionario_t *func = index->max;
    double salariof;

    while (func != NULL)
    {
        salariof = (double)func->salario / 100.F;
        printf("area_max|%s|%s %s|%.2f\n", index->nome, func->nome, func->sobrenome, salariof);
        if (func->salario == global.max_salario)
            printf("global_max|%s %s|%.2f\n", func->nome, func->sobrenome, salariof);
        func = func->area;
    }
    func = index->min;
    while (func != NULL)
    {
        salariof = (double)func->salario / 100.F;
        printf("area_min|%s|%s %s|%.2f\n", index->nome, func->nome, func->sobrenome, salariof);
        if (func->salario == global.min_salario)
            printf("global_min|%s %s|%.2f\n", func->nome, func->sobrenome, salariof);
        func = func->area;
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
    funcionario_t *func;

    // sobrenomes com mais de 2 funcionários
    for (; index != NULL; index = index->hh.next)
    {
        if (index->total < 2)
            continue;
        for (func = index->max; func != NULL; func = func->snome)
        {
            salariof = (double)index->max_salario / 100.F;
            printf("last_name_max|%s|%s %s|%.2f\n", index->sobrenome, func->nome, func->sobrenome, salariof);
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
        areas[i].max = NULL;
        areas[i].min = NULL;
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
    {
        funcionario_t *coletor = processos[i].coletor;
        while (coletor != NULL)
        {
            funcionario_t *tmp = coletor;
            coletor = tmp->next;
            free(tmp);
        }
    }
    for (i = 0; i < threads_max; i++)
        free(processos[i].buffer);
    free(processos);
}
