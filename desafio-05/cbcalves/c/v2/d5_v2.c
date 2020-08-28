#include "uthash.h" // https://troydhanson.github.io/uthash/  hash table utilizada no processo
#include <fcntl.h>
#include <pthread.h> // não sei explicar pthread.h foi mais rápido que threads.h
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <unistd.h>

#define MALLOC(var, type, size) var = (type *)malloc(sizeof(type) * (size)) // versão mais perigosa sem verificação de alocação
#define FREE(var) free(var), var = NULL                                     // free e bota a variavel como Null(0)

// tamanho das variáveis usadas, tem haver com a velocidade para alocar (foram feitas medidas para chegar nos numeros abaixo)
#define S_NOME 13
#define S_SOBRENOME 21
#define S_CODIGO 3
#define S_NOME_CARGO 28
// total de áreas possíveis ao fazer contas com os exemplos de dados que ele vai processar
// estou alocando todas as áreas possíveis pois é mais rápido fazer uma conta do que ficar com find
#define TOTAL_AREAS 1296
// evitando problemas defino o maior inteiro possível
#define INT_MAX 2147483647

typedef struct funcionario_st
{
    char nome[S_NOME];
    char sobrenome[S_SOBRENOME];
    int salario;
    char codigo[S_CODIGO];
    struct funcionario_st *next;  // apontando para o próximo funcionario
    struct funcionario_st *area;  // apontando para o próximo max ou min
    struct funcionario_st *snome; // apontando para o próximo sobrenome max
} funcionario_t;                  // funcionário

typedef struct area_st
{
    char codigo[S_CODIGO], nome[S_NOME_CARGO];
    funcionario_t *max, *min; // lista de max e min
    unsigned long long custo;
    int total, max_salario, min_salario;
    struct area_st *global; // apontando para o próximo max ou min global
} area_t;                   // controle de max e min por área

typedef struct
{
    char sobrenome[S_SOBRENOME];
    UT_hash_handle hh;  // hash table
    funcionario_t *max; //lista de max
    int total, max_salario;
} sobrenome_t; // controle de max por sobrenome

typedef struct
{
    area_t *max; // lista de max
    area_t *min; // lista de min
    int max_size, min_size, total, max_salario, min_salario;
    unsigned long long custo;
} global_t; // controle de max e min global

typedef struct
{
    pthread_t id;           // id da thread
    char *buffer;           // buffer para processar
    funcionario_t *coletor; // lista de funcionarios para apagar
} processar_t;              // processo das threads

// Variáveis globais
area_t *areas = NULL;
sobrenome_t *sobrenomes = NULL;
global_t global;
// mutex -> sinalizações para evitar colisões nos dados
pthread_mutex_t mtx_max;
pthread_mutex_t mtx_min;
pthread_mutex_t mtx_sbn1;
pthread_mutex_t mtx_sbn2;

int sobrenomes_process(void *funcionario) // processar o sobrenome
{
    funcionario_t *func = (funcionario_t *)funcionario;
    sobrenome_t *pos = NULL;
    int sinal = 0;

    // a parte mais demorada é achar
    pthread_mutex_lock(&mtx_sbn1);
    HASH_FIND_STR(sobrenomes, func->sobrenome, pos);
    if (pos == NULL)
    {
        MALLOC(pos, sobrenome_t, 1);
        memcpy(pos->sobrenome, func->sobrenome, S_SOBRENOME);
        pos->total = 0;
        pos->max = NULL;
        pos->max_salario = 0;
        HASH_ADD_STR(sobrenomes, sobrenome, pos);
    }
    // libera o prox da fila
    pthread_mutex_unlock(&mtx_sbn1);

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
int areas_process_max(void *funcionario) // processar a área e anotar o valor máximo
{
    funcionario_t *func = (funcionario_t *)funcionario;
    int sinal = 0, cod = (func->codigo[0] - ((func->codigo[0] < 'A') ? '0' : 'A' - 10)) * 36;
    cod += func->codigo[1] - ((func->codigo[1] < 'A') ? '0' : 'A' - 10);

    pthread_mutex_lock(&mtx_max);
    areas[cod].total++;
    areas[cod].custo += func->salario;

    if (areas[cod].max_salario < func->salario)
    {
        areas[cod].max_salario = func->salario;
        areas[cod].max = func;
        pthread_mutex_unlock(&mtx_max);
        if (global.max_salario < func->salario) // deixo apenas anotado o valor global
            global.max_salario = func->salario;
        sinal = 1;
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

int areas_process_min(void *funcionario) // processar a área e anotar o valor mínimo
{
    funcionario_t *func = (funcionario_t *)funcionario;
    int sinal = 0, cod = (func->codigo[0] - ((func->codigo[0] < 'A') ? '0' : 'A' - 10)) * 36;
    cod += func->codigo[1] - ((func->codigo[1] < 'A') ? '0' : 'A' - 10);

    pthread_mutex_lock(&mtx_min);
    if (areas[cod].min_salario > func->salario)
    {
        areas[cod].min_salario = func->salario;
        areas[cod].min = func;
        pthread_mutex_unlock(&mtx_min);
        if (global.min_salario > func->salario) // deixo apenas anotado o valor global
            global.min_salario = func->salario;
        sinal = 1;
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

void *processar(void *processos)
{
    int sinal = 1, cod = 0;
    char codigo = 0;
    char *p = NULL, *s = NULL;
    funcionario_t *ret = NULL, *new = NULL;

    p = ((processar_t *)processos)->buffer;
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
                MALLOC(new, funcionario_t, 1);
                new->next = ret;
                ret = new;
                ret->snome = NULL;
                ret->area = NULL;
                sinal = 0;
            }

            p += 4;
            while (*p != '"')
                p++;
            p += 8;
            s = ret->nome;
            while (*p != '"')
                *(s++) = *(p++);
            *s = 0;

            p += 2;
            while (*p != '"')
                p++;
            p += 13;
            s = ret->sobrenome;
            while (*p != '"')
                *(s++) = *(p++);
            *s = 0;

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
            ret->codigo[0] = *(p++);
            ret->codigo[1] = *(p++);
            ret->codigo[2] = 0;
            sinal += areas_process_max(ret);
            sinal += areas_process_min(ret);
            sinal += sobrenomes_process(ret);
        }
        else if (*p == 'c')
        {
            p += 9;
            cod = (*p - ((*p < 'A') ? '0' : 'A' - 10)) * 36;
            codigo = *p;
            p++;
            cod += *p - ((*p < 'A') ? '0' : 'A' - 10);
            areas[cod].codigo[0] = codigo;
            areas[cod].codigo[1] = *p;
            areas[cod].codigo[2] = 0;

            p += 3;
            while (*p != '"')
                p++;
            p += 8;
            s = areas[cod].nome;
            while (*p != '"')
                *(s++) = *(p++);
            *s = 0;
        }
    }
    ((processar_t *)processos)->coletor = ret;
    return NULL;
}

void show_area() // mostrar os resultados por área e global
{
    int i = 0;
    double salariof = 0;
    area_t *index = NULL, *most_emp = NULL, *least_emp = NULL;
    funcionario_t *func = NULL;

    for (i = 0; i < TOTAL_AREAS; i++)
    {
        if (areas[i].total == 0)
            continue;
        index = &areas[i];

        if (index->max_salario == global.max_salario) // anotando os maiores salários
        {
            index->global = global.max;
            global.max = index;
        }
        if (index->min_salario == global.min_salario) // anotando os menores salários
        {
            index->global = global.min;
            global.min = index;
        }
        global.total += index->total;
        global.custo += index->custo;

        if (index->total > 0)
        {
            salariof = ((double)index->custo / 100.F) / (double)index->total;
            printf("area_avg|%s|%.2f\n", index->nome, salariof);

            if (most_emp == NULL || index->total > most_emp->total) // área com mais funcionários
                most_emp = index;
            if (least_emp == NULL || index->total < least_emp->total) // área com menos funcionários
                least_emp = index;
        }
        for (func = index->max; func != NULL; func = func->area)
        {
            salariof = (double)index->max_salario / 100.F;
            printf("area_max|%s|%s %s|%.2f\n", index->nome, func->nome, func->sobrenome, salariof);
        }
        for (func = index->min; func != NULL; func = func->area)
        {
            salariof = (double)index->min_salario / 100.F;
            printf("area_min|%s|%s %s|%.2f\n", index->nome, func->nome, func->sobrenome, salariof);
        }
    }
    // globais de maior e menor salários
    salariof = ((double)global.custo / 100.F) / (double)global.total;
    printf("global_avg|%.2f\n", salariof);
    for (index = global.max; index != NULL; index = index->global)
    {
        for (func = index->max; func != NULL; func = func->area)
        {
            salariof = (double)global.max_salario / 100.F;
            printf("global_max|%s %s|%.2f\n", func->nome, func->sobrenome, salariof);
        }
    }
    for (index = global.min; index != NULL; index = index->global)
    {
        for (func = index->min; func != NULL; func = func->area)
        {
            salariof = (double)global.min_salario / 100.F;
            printf("global_min|%s %s|%.2f\n", func->nome, func->sobrenome, salariof);
        }
    }

    printf("most_employees|%s|%d\n", most_emp->nome, most_emp->total);
    printf("least_employees|%s|%d\n", least_emp->nome, least_emp->total);
}
void show_sobrenomes() // mostrar os resultados por sobrenomes
{
    double salariof = 0;
    sobrenome_t *index = NULL;
    funcionario_t *func = NULL;

    // sobrenomes com mais de 2 funcionários
    for (index = sobrenomes; index != NULL; index = index->hh.next)
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
    int fjson = 0, i = 0, j = 0;
    void *nada = NULL; // sem função, criado para o pthread
    struct stat f;
    char *buffer = NULL;
    processar_t *processos; // coletar todos os funcionarios criados e apagar no final
    size_t threads_max = 0, buffer_size = 0, buffer_max = 0;

    if (argc < 2)
    {
        printf("Uso: %s <arquivo json>\n", argv[0]);
        return 0;
    }

    fjson = open(argv[1], O_RDONLY);
    if (fjson < 0)
    {
        printf("Arquivo não encontrado\n");
        abort();
    }
    i = fstat(fjson, &f);
    if (fjson < 0)
    {
        printf("Arquivo não encontrado\n");
        abort();
    }
    //inicialização das areas
    MALLOC(areas, area_t, TOTAL_AREAS);
    for (i = 0; i < TOTAL_AREAS; i++)
    {
        areas[i].total = 0;
        areas[i].custo = 0;
        areas[i].max = NULL;
        areas[i].min = NULL;
        areas[i].global = NULL;
        areas[i].min_salario = INT_MAX;
        areas[i].max_salario = 0;
    }
    // inicialização das variaveis do global
    global.max = NULL;
    global.min = NULL;
    global.custo = 0;
    global.max_size = 0;
    global.min_size = 0;
    global.total = 0;
    global.max_salario = 0;
    global.min_salario = INT_MAX;
    // inicialização da sinalização
    pthread_mutex_init(&mtx_max, NULL);
    pthread_mutex_init(&mtx_min, NULL);
    pthread_mutex_init(&mtx_sbn1, NULL);
    pthread_mutex_init(&mtx_sbn2, NULL);

    //inicialização do controle de threads
    threads_max = sysconf(_SC_NPROCESSORS_ONLN); // numero de processadores (* o numero de threads em cada);
    if (threads_max < 2)
        threads_max = 2;
    MALLOC(processos, processar_t, threads_max);
    buffer_max = (f.st_size / threads_max) + 1; // somo 1 pois a divisão pode não ser exata

    // incialização das threads
    j = 0; // funciona como o resto que devia ter sido processado mas não foi na thread anterior
    for (i = 0; i < threads_max; i++)
    {
        MALLOC(buffer, char, buffer_max + j);
        buffer_size = read(fjson, buffer, buffer_max + j);
        for (j = 0; buffer[buffer_size - j - 1] != '}'; j++)
            ;
        buffer[buffer_size - j - 1] = 0;
        processos[i].buffer = buffer;
        pthread_create(&processos[i].id, NULL, processar, &processos[i]);
        lseek(fjson, -j, SEEK_CUR);
    }
    close(fjson);
    // encerramento das threads
    for (i = 0; i < threads_max; i++)
        pthread_join(processos[i].id, &nada);

    show_area();
    show_sobrenomes();

    // inicio da limpeza geral
    pthread_mutex_destroy(&mtx_max);
    pthread_mutex_destroy(&mtx_min);
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
    FREE(areas);
    for (i = 0; i < threads_max; i++)
    {
        funcionario_t *coletor = processos[i].coletor;
        while (coletor != NULL)
        {
            funcionario_t *tmp = coletor;
            coletor = tmp->next;
            FREE(tmp);
        }
    }
    for (i = 0; i < threads_max; i++)
        FREE(processos[i].buffer);
    FREE(processos);
}
