#define _LARGEFILE64_SOURCE

#include <sys/mman.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <stddef.h>
#include <stdint.h>
#include <fcntl.h>
#include <unistd.h>
#include <pthread.h>
#include "uthash_mod.h" // https://troydhanson.github.io/uthash/  hash table utilizada no processo

#define MAX_AREAS 2
#define MAX_SOBRENOMES 4917

/**
 * Estrutura usada para guardar o nome e sobrenome
 * dos funcionários de maior e menor salário
 */
typedef struct
{
    char *nome;
    unsigned char nome_size;
    char *sobrenome;
    unsigned char sobrenome_size;
} funcionario_t;

/**
 * Estrutura usada para guardar o nome
 * dos sobrenomes de maior salário
 */
typedef struct
{
    char *nome;
    unsigned char nome_size;
} nome_t;

/**
 * Estrutura usada para guardar os dados sobre
 * as áreas
 */
typedef struct
{
    char *codigo;
    char *nome;
    unsigned char nome_size;
    funcionario_t max[5]; // lista de max
    unsigned char max_pos;
    unsigned max_salario;
    funcionario_t min[5]; // lista de min
    unsigned char min_pos;
    unsigned min_salario;
    size_t custo;
    unsigned total;
} area_t;

/**
 * Estrutura usada para guardar os dados de maiores
 * salários para os sobrenomes
 */
typedef struct
{
    char *sobrenome;
    UT_hash_handle hh; // hash table
    unsigned char sobrenome_size;
    unsigned total;
    unsigned max_salario;
    nome_t max[4]; //lista de max
    unsigned char max_pos;
} sobrenome_t;

/**
 * Estrutura global de máximo, mínimo e média de salário total
 */
typedef struct
{
    unsigned max_salario;
    unsigned min_salario;
    unsigned total;
    size_t custo;
} global_t;

/**
 * Controle de Threads, com as informações necessárias
 */
typedef struct
{
    pthread_t id; // id da thread
    char *buffer; // buffer para processar
    char *buffer_end;
    area_t *areas;
    sobrenome_t *sobrenomes;
    unsigned sobrenomes_size;
} processar_t;

/**
 * Variáveis globais
 */
global_t global;
processar_t *threads; // processo das threads
char init_surname[] = "Abaine";

/**
 * Processar os sobrenomes e guardando os maiores salários
 */
#define sobrenomes_process(_sobrenomes, _funcionario, _salario, _hashv, _index)                                      \
    {                                                                                                                \
        HASH_VALUE(_funcionario.sobrenome, _funcionario.sobrenome_size, _hashv);                                     \
        HASH_FIND_BYHASHVALUE(hh, _sobrenomes, _funcionario.sobrenome, _funcionario.sobrenome_size, _hashv, _index); \
        if (!_index) {                                                                                               \
            _index = &_sobrenomes[sobrenomes_size++];                                                                \
            _index->sobrenome = _funcionario.sobrenome;                                                              \
            _index->sobrenome_size = _funcionario.sobrenome_size;                                                    \
            _index->total = 1;                                                                                       \
            _index->max_salario = _salario;                                                                          \
            memcpy(&_index->max[0], (nome_t *)(&_funcionario), sizeof(nome_t));                                      \
            _index->max_pos = 1;                                                                                     \
            HASH_ADD_BYHASHVALUE(hh, _sobrenomes, sobrenome[0], _index->sobrenome_size, _hashv, _index);             \
        } else {                                                                                                     \
            _index->total++;                                                                                         \
            if (_index->max_salario <= _salario) {                                                                   \
                if (_index->max_salario < _salario) {                                                                \
                    _index->max_salario = _salario;                                                                  \
                    _index->max_pos = 0;                                                                             \
                }                                                                                                    \
                memcpy(&_index->max[_index->max_pos++], (nome_t *)(&_funcionario), sizeof(nome_t));                  \
            }                                                                                                        \
        }                                                                                                            \
    }

/**
 * Processando as áreas e guardando os maiores e menores salários
 */
#define areas_process(_areas, _funcionario, _salario, _cod)                                          \
    {                                                                                                \
        _areas[_cod].custo += _salario;                                                              \
        _areas[_cod].total++;                                                                        \
                                                                                                     \
        if (_areas[_cod].max_salario <= _salario) {                                                  \
            if (_areas[_cod].max_salario < _salario) {                                               \
                _areas[_cod].max_salario = _salario;                                                 \
                _areas[_cod].max_pos = 0;                                                            \
            }                                                                                        \
            memcpy(&_areas[_cod].max[areas[_cod].max_pos++], &_funcionario, sizeof(funcionario_t));  \
        } else if (_areas[_cod].min_salario >= _salario) {                                           \
            if (_areas[_cod].min_salario > _salario) {                                               \
                _areas[_cod].min_salario = _salario;                                                 \
                _areas[_cod].min_pos = 0;                                                            \
            }                                                                                        \
            memcpy(&_areas[_cod].min[_areas[_cod].min_pos++], &_funcionario, sizeof(funcionario_t)); \
        }                                                                                            \
    }

/**
 * Após terminar o processamento as threads devem juntar os resultados em um só local
 * Este é para as áreas
 */
#define merge_areas(index)                                                                                 \
    for (j = 0; j < MAX_AREAS; j++) {                                                                      \
        int cod;                                                                                           \
        cod = j;                                                                                           \
                                                                                                           \
        if (threads[index].areas[j].nome) {                                                                \
            threads[0].areas[cod].nome = threads[index].areas[j].nome;                                     \
            threads[0].areas[cod].nome_size = threads[index].areas[j].nome_size;                           \
        }                                                                                                  \
                                                                                                           \
        threads[0].areas[cod].total += threads[index].areas[j].total;                                      \
        threads[0].areas[cod].custo += threads[index].areas[j].custo;                                      \
                                                                                                           \
        if (threads[0].areas[cod].max_salario <= threads[index].areas[j].max_salario) {                    \
            if (threads[0].areas[cod].max_salario < threads[index].areas[j].max_salario) {                 \
                if (global.max_salario < threads[index].areas[j].max_salario)                              \
                    global.max_salario = threads[index].areas[j].max_salario;                              \
                threads[0].areas[cod].max_salario = threads[index].areas[j].max_salario;                   \
                threads[0].areas[cod].max_pos = 0;                                                         \
            }                                                                                              \
            memcpy(&threads[0].areas[cod].max[threads[0].areas[cod].max_pos], threads[index].areas[j].max, \
                   (size_t)threads[index].areas[j].max_pos * sizeof(funcionario_t));                       \
            threads[0].areas[cod].max_pos += threads[index].areas[j].max_pos;                              \
        }                                                                                                  \
        if (threads[0].areas[cod].min_salario >= threads[index].areas[j].min_salario) {                    \
            if (threads[0].areas[cod].min_salario > threads[index].areas[j].min_salario) {                 \
                if (global.min_salario > threads[index].areas[j].min_salario)                              \
                    global.min_salario = threads[index].areas[j].min_salario;                              \
                threads[0].areas[cod].min_salario = threads[index].areas[j].min_salario;                   \
                threads[0].areas[cod].min_pos = 0;                                                         \
            }                                                                                              \
            memcpy(&threads[0].areas[cod].min[threads[0].areas[cod].min_pos], threads[index].areas[j].min, \
                   (size_t)threads[index].areas[j].min_pos * sizeof(funcionario_t));                       \
            threads[0].areas[cod].min_pos += threads[index].areas[j].min_pos;                              \
        }                                                                                                  \
    }

/**
 * Após terminar o processamento as threads devem juntar os resultados em um só local
 * Este é para os sobrenomes
 */
#define merge_sobrenomes(index)                                                                                                                       \
    {                                                                                                                                                 \
        head = threads[index].sobrenomes;                                                                                                             \
        while (head) {                                                                                                                                \
            sobrenome_t *registroAtual;                                                                                                               \
            HASH_FIND_BYHASHVALUE(hh, threads[0].sobrenomes, head->sobrenome, head->sobrenome_size, head->hh.hashv, registroAtual);                   \
            if (!registroAtual) {                                                                                                                     \
                registroAtual = &threads[0].sobrenomes[threads[0].sobrenomes_size++];                                                                 \
                memcpy(registroAtual, head, sizeof(sobrenome_t));                                                                                     \
                HASH_ADD_BYHASHVALUE(hh, threads[0].sobrenomes, sobrenome[0], registroAtual->sobrenome_size, registroAtual->hh.hashv, registroAtual); \
                head = head->hh.next;                                                                                                                 \
                continue;                                                                                                                             \
            }                                                                                                                                         \
                                                                                                                                                      \
            registroAtual->total += head->total;                                                                                                      \
                                                                                                                                                      \
            if (registroAtual->max_salario <= head->max_salario) {                                                                                    \
                if (registroAtual->max_salario < head->max_salario) {                                                                                 \
                    registroAtual->max_salario = head->max_salario;                                                                                   \
                    registroAtual->max_pos = 0;                                                                                                       \
                }                                                                                                                                     \
                memcpy(&registroAtual->max[registroAtual->max_pos], head->max, (size_t)head->max_pos * sizeof(nome_t));                               \
                registroAtual->max_pos += head->max_pos;                                                                                              \
            }                                                                                                                                         \
            head = head->hh.next;                                                                                                                     \
        }                                                                                                                                             \
    }

/**
 * Processar o que leu do disco separando os nomes, sobrenomes, salários e áreas para processar
 */
void *processar(void *processos)
{
    int cod;
    unsigned salario;
    funcionario_t funcionario;
    char *codigo;
    char *p = ((processar_t *)processos)->buffer;
    char *end = ((processar_t *)processos)->buffer_end;

    // inicialização das areas
    area_t *areas = (area_t *)malloc(sizeof(area_t) * MAX_AREAS);
    for (cod = 0; cod < MAX_AREAS; cod++) {
        areas[cod].codigo = NULL;
        areas[cod].nome = NULL;
        areas[cod].nome_size = 0;
        areas[cod].total = 0;
        areas[cod].custo = 0;
        areas[cod].max_pos = 0;
        areas[cod].min_pos = 0;
        areas[cod].min_salario = INT_MAX;
        areas[cod].max_salario = 0;
    }
    // inicialização de sobrenomes
    unsigned hashv;
    sobrenome_t *sobrenomeAtual;
    sobrenome_t *sobrenomes = (sobrenome_t *)malloc(sizeof(sobrenome_t) * MAX_SOBRENOMES);
    unsigned sobrenomes_size = 1;
    sobrenomes->sobrenome = init_surname;
    sobrenomes->sobrenome_size = 6;
    sobrenomes->total = 0;
    sobrenomes->max_salario = 0;
    sobrenomes->max_pos = 0;
    sobrenomes->hh.next = NULL;
    sobrenomes->hh.prev = NULL;
    HASH_MAKE_TABLE(hh, sobrenomes);
    HASH_VALUE(&sobrenomes->sobrenome[0], sobrenomes->sobrenome_size, sobrenomes->hh.hashv);
    HASH_ADD_TO_TABLE(hh, sobrenomes, sobrenome[0], sobrenomes->sobrenome_size, sobrenomes->hh.hashv, sobrenomes);

    while (p < end) {
        while (p < end && *p != '{')
            p++;
        if (p >= end)
            break;
        while (*p != '"')
            p++;
        p++;
        if (*p == 'i') {
            // nome
            p += 4;
            while (*p != '"')
                p++;
            p += 8;
            funcionario.nome = p;
            p += 2;
            while (*p != '"')
                p++;
            funcionario.nome_size = (unsigned char)(p - funcionario.nome);

            // sobrenome
            p += 2;
            while (*p != '"')
                p++;
            p += 13;
            funcionario.sobrenome = p;
            while (*p != '"')
                p++;
            funcionario.sobrenome_size = (unsigned char)(p - funcionario.sobrenome);

            // salário
            p += 2;
            while (*p != '"')
                p++;
            p += 10;
            salario = *p - '0';
            p++;
            while (*p != '.') {
                salario = salario * 10 + *p - '0';
                p++;
            }
            p++;
            salario = salario * 10 + *p - '0';
            p++;
            salario = salario * 10 + *p - '0';

            // código
            while (*p != '"')
                p++;
            p += 8;
            codigo = p;
            p += 3;

            // if (codigo[0] == 'A' && (codigo[1] == '1' || codigo[1] == '2')) { // nada aqui, circulando
            cod = codigo[1] - '1';
            // } else {
            //     areas_get(areas, areas_size, codigo, 1, cod);
            // }

            areas_process(areas, funcionario, salario, cod);
            sobrenomes_process(sobrenomes, funcionario, salario, hashv, sobrenomeAtual);
        } else if (*p == 'c') {
            p += 9;
            codigo = p;
            p += 4;
            while (*p != '"')
                p++;
            p += 8;

            if (codigo[0] == 'A' && (codigo[1] == '1' || codigo[1] == '2')) { // nada aqui, circulando
                cod = codigo[1] - '1';
            } else {
                // areas_get(areas, areas_size, codigo, 0, cod);
                // if (cod == -1) {
                p += 9;
                continue;
                // }
            }
            areas[cod].nome = p;
            p += 7;
            while (*p != '"')
                p++;
            areas[cod].nome_size = (unsigned char)(p - areas[cod].nome);
            p++;
        }
    }
    ((processar_t *)processos)->areas = areas;
    ((processar_t *)processos)->sobrenomes = sobrenomes;
    ((processar_t *)processos)->sobrenomes_size = sobrenomes_size;

    return NULL;
}

/**
 * Mostrar áreas com mais e menos funcionários e médias da área e globais
 */
#define show_area(areas)                                                                                   \
    do {                                                                                                   \
        double salariof;                                                                                   \
        area_t *most_emp = &areas[0];                                                                      \
        area_t *least_emp = &areas[0];                                                                     \
        int j;                                                                                             \
                                                                                                           \
        for (i = 0; i < MAX_AREAS; i++) {                                                                  \
            salariof = (double)areas[i].max_salario / 100.F;                                               \
            for (j = 0; j < areas[i].max_pos; j++) {                                                       \
                printf("area_max|%.*s|%.*s %.*s|%.2f\n", areas[i].nome_size, areas[i].nome,                \
                       areas[i].max[j].nome_size, areas[i].max[j].nome,                                    \
                       areas[i].max[j].sobrenome_size, areas[i].max[j].sobrenome, salariof);               \
                if (areas[i].max_salario == global.max_salario) {                                          \
                    printf("global_max|%.*s %.*s|%.2f\n", areas[i].max[j].nome_size, areas[i].max[j].nome, \
                           areas[i].max[j].sobrenome_size, areas[i].max[j].sobrenome, salariof);           \
                }                                                                                          \
            }                                                                                              \
            salariof = (double)areas[i].min_salario / 100.F;                                               \
            for (j = 0; j < areas[i].min_pos; j++) {                                                       \
                printf("area_min|%.*s|%.*s %.*s|%.2f\n", areas[i].nome_size, areas[i].nome,                \
                       areas[i].min[j].nome_size, areas[i].min[j].nome,                                    \
                       areas[i].min[j].sobrenome_size, areas[i].min[j].sobrenome, salariof);               \
                if (areas[i].min_salario == global.min_salario) {                                          \
                    printf("global_min|%.*s %.*s|%.2f\n", areas[i].min[j].nome_size, areas[i].min[j].nome, \
                           areas[i].min[j].sobrenome_size, areas[i].min[j].sobrenome, salariof);           \
                }                                                                                          \
            }                                                                                              \
                                                                                                           \
            global.total += areas[i].total;                                                                \
            global.custo += areas[i].custo;                                                                \
                                                                                                           \
            salariof = ((double)areas[i].custo / 100.F) / (double)areas[i].total;                          \
            printf("area_avg|%.*s|%.2f\n", areas[i].nome_size, areas[i].nome, salariof);                   \
                                                                                                           \
            if (areas[i].total > most_emp->total) {                                                        \
                most_emp = &areas[i];                                                                      \
            }                                                                                              \
            if (areas[i].total < least_emp->total) {                                                       \
                least_emp = &areas[i];                                                                     \
            }                                                                                              \
        }                                                                                                  \
        salariof = ((double)global.custo / 100.F) / (double)global.total;                                  \
        printf("global_avg|%.2f\n", salariof);                                                             \
                                                                                                           \
        printf("most_employees|%.*s|%u\n", most_emp->nome_size, most_emp->nome, most_emp->total);          \
        printf("least_employees|%.*s|%u\n", least_emp->nome_size, least_emp->nome, least_emp->total);      \
    } while (0)

/**
 * Mostrar todos os sobrenomes com 2 ou mais nomes
 */
#define show_sobrenomes(index)                                                                 \
    while (index) {                                                                            \
        if (index->total > 1) {                                                                \
            double salariof = (double)index->max_salario / 100.F;                              \
            for (int i = 0; i < index->max_pos; i++) {                                         \
                printf("last_name_max|%.*s|%.*s %.*s|%.2f\n",                                  \
                       index->sobrenome_size, index->sobrenome, index->max[i].nome_size,       \
                       index->max[i].nome, index->sobrenome_size, index->sobrenome, salariof); \
            }                                                                                  \
        }                                                                                      \
        index = index->hh.next;                                                                \
    }

/**
 * Apagar os sobrenomes (simplificação do processo original)
 * No processo original era excluido cada ficha antes de excluir
 * a tabela e os buckets, simplifiquei excluindo tabela e buckets
 * no local que ficam guardados e a array de sobrenomes.
 */
#define freeSobrenomes(sobrenomes)         \
    {                                      \
        free(sobrenomes->hh.tbl->buckets); \
        free(sobrenomes->hh.tbl);          \
        free(sobrenomes);                  \
    }

int main(int argc, char *argv[])
{
    int fjson;
    int i;
    int j;
    struct stat f;
    char *buffer;
    size_t buffer_max;
    sobrenome_t *head;

    if (argc < 2) {
        printf("Uso: %s <arquivo json>\n", argv[0]);
        return 0;
    }
    fjson = open(argv[1], O_RDONLY | __O_NOATIME | O_LARGEFILE);
    if (fjson < 0) {
        printf("Arquivo não encontrado\n");
        exit(EXIT_FAILURE);
    }
    fstat(fjson, &f);
    buffer = (char *)mmap(0, f.st_size, PROT_READ, MAP_SHARED, fjson, 0);
    if (buffer == MAP_FAILED) {
        printf("Erro ao abrir arquivo\n");
        exit(EXIT_FAILURE);
    }

    // inicialização das variaveis do global
    global.custo = 0;
    global.total = 0;
    global.max_salario = 0;
    global.min_salario = INT_MAX;

    // inicialização do controle de threads
    unsigned threads_max = sysconf(_SC_NPROCESSORS_ONLN); // numero de processadores (* o numero de threads em cada);
    if (threads_max < 2)
        threads_max = 2;
    threads = (processar_t *)malloc(sizeof(processar_t) * threads_max);
    buffer_max = (f.st_size / threads_max) + 1; // somo 1 pois a divisão pode não ser exata

    // criação das threads
    j = 0; // funciona como o resto que devia ter sido processado mas não foi na thread anterior
    size_t buffer_end = 0;
    for (i = 0; i < threads_max; i++) {
        threads[i].buffer = &buffer[buffer_end];
        buffer_end += buffer_max + j;
        j = 0;
        while (buffer[buffer_end - j] != '}') {
            j++;
        }
        threads[i].buffer_end = &buffer[buffer_end - j];
        pthread_create(&threads[i].id, NULL, processar, &threads[i]);
        buffer_end = threads[i].buffer_end - buffer + 1;
    }

    // encerramento das threads
    pthread_join(threads[0].id, NULL);
    for (i = 0; i < MAX_AREAS; i++) {
        if (global.max_salario < threads[0].areas[i].max_salario)
            global.max_salario = threads[0].areas[i].max_salario;
        if (global.min_salario > threads[0].areas[i].min_salario)
            global.min_salario = threads[0].areas[i].min_salario;
    }
    for (i = 1; i < threads_max; i++) {
        pthread_join(threads[i].id, NULL);
        merge_areas(i);
        merge_sobrenomes(i);
        freeSobrenomes(threads[i].sobrenomes);
        free(threads[i].areas);
    }
    head = threads[0].sobrenomes;

    // Mostrando resultado
    show_area(threads[0].areas);
    show_sobrenomes(head);

    //liberar toda a memória ainda alocada
    freeSobrenomes(threads[0].sobrenomes);
    free(threads[0].areas);
    free(threads);

    munmap(buffer, f.st_size);
    close(fjson);

    return EXIT_SUCCESS;
}
