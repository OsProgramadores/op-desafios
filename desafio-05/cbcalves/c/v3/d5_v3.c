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
    UT_hash_handle hh; // hash table
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

/**
 * Processar os sobrenomes e guardando os maiores salários
 */
#define sobrenomes_process(_sobrenomes, _funcionario, _salario, _hashv, _index)                                      \
    {                                                                                                                \
        HASH_VALUE(_funcionario.sobrenome, _funcionario.sobrenome_size, _hashv);                                     \
        HASH_FIND_BYHASHVALUE(hh, _sobrenomes, _funcionario.sobrenome, _funcionario.sobrenome_size, _hashv, _index); \
        if (!_index) {                                                                                               \
            _index = &_sobrenomes[sobrenomes_size++];                                                                \
            _index->hh.key = (const char *)(_funcionario.sobrenome);                                                 \
            _index->hh.keylen = _funcionario.sobrenome_size;                                                         \
            _index->hh.hashv = _hashv;                                                                               \
            _index->total = 1;                                                                                       \
            _index->max_salario = _salario;                                                                          \
            memcpy(&_index->max[0], (nome_t *)(&_funcionario), sizeof(nome_t));                                      \
            _index->max_pos = 1;                                                                                     \
            HASH_ADD_BYHASHVALUE(hh, _sobrenomes, _hashv, _index);                                                   \
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
#define areas_process(_areas, _funcionario, _salario, _cod)                                      \
    {                                                                                            \
        areaAtual = _areas + _cod;                                                               \
        areaAtual->custo += _salario;                                                            \
        areaAtual->total++;                                                                      \
                                                                                                 \
        if (areaAtual->max_salario <= _salario) {                                                \
            if (areaAtual->max_salario < _salario) {                                             \
                areaAtual->max_salario = _salario;                                               \
                areaAtual->max_pos = 0;                                                          \
            }                                                                                    \
            memcpy(&areaAtual->max[areaAtual->max_pos++], &_funcionario, sizeof(funcionario_t)); \
        } else if (areaAtual->min_salario >= _salario) {                                         \
            if (areaAtual->min_salario > _salario) {                                             \
                areaAtual->min_salario = _salario;                                               \
                areaAtual->min_pos = 0;                                                          \
            }                                                                                    \
            memcpy(&areaAtual->min[areaAtual->min_pos++], &_funcionario, sizeof(funcionario_t)); \
        }                                                                                        \
    }

/**
 * Após terminar o processamento as threads devem juntar os resultados em um só local
 * Este é para as áreas
 */
#define merge_areas(index)                                              \
    for (j = 0; j < MAX_AREAS; j++) {                                   \
        areas = threads[0].areas + j;                                   \
        area_t *old_areas = threads[index].areas + j;                   \
                                                                        \
        if (old_areas->nome) {                                          \
            areas->nome = old_areas->nome;                              \
            areas->nome_size = old_areas->nome_size;                    \
        }                                                               \
                                                                        \
        areas->total += old_areas->total;                               \
        areas->custo += old_areas->custo;                               \
                                                                        \
        if (areas->max_salario <= old_areas->max_salario) {             \
            if (areas->max_salario < old_areas->max_salario) {          \
                if (global.max_salario < old_areas->max_salario)        \
                    global.max_salario = old_areas->max_salario;        \
                areas->max_salario = old_areas->max_salario;            \
                areas->max_pos = 0;                                     \
            }                                                           \
            memcpy(areas->max + areas->max_pos, old_areas->max,         \
                   (size_t)old_areas->max_pos * sizeof(funcionario_t)); \
            areas->max_pos += old_areas->max_pos;                       \
        }                                                               \
        if (areas->min_salario >= old_areas->min_salario) {             \
            if (areas->min_salario > old_areas->min_salario) {          \
                if (global.min_salario > old_areas->min_salario)        \
                    global.min_salario = old_areas->min_salario;        \
                areas->min_salario = old_areas->min_salario;            \
                areas->min_pos = 0;                                     \
            }                                                           \
            memcpy(areas->min + areas->min_pos, old_areas->min,         \
                   (size_t)old_areas->min_pos * sizeof(funcionario_t)); \
            areas->min_pos += old_areas->min_pos;                       \
        }                                                               \
    }

/**
 * Após terminar o processamento as threads devem juntar os resultados em um só local
 * Este é para os sobrenomes
 */
#define merge_sobrenomes(index)                                                                                   \
    {                                                                                                             \
        head = threads[index].sobrenomes;                                                                         \
        sobrenomes = threads[0].sobrenomes;                                                                       \
        while (head) {                                                                                            \
            sobrenome_t *snomeAtual;                                                                              \
            HASH_FIND_BYHASHVALUE(hh, sobrenomes, head->hh.key, head->hh.keylen, head->hh.hashv, snomeAtual);     \
            if (!snomeAtual) {                                                                                    \
                snomeAtual = head;                                                                                \
                head = head->hh.next;                                                                             \
                HASH_ADD_BYHASHVALUE(hh, sobrenomes, snomeAtual->hh.hashv, snomeAtual);                           \
                continue;                                                                                         \
            }                                                                                                     \
                                                                                                                  \
            snomeAtual->total += head->total;                                                                     \
                                                                                                                  \
            if (snomeAtual->max_salario <= head->max_salario) {                                                   \
                if (snomeAtual->max_salario < head->max_salario) {                                                \
                    snomeAtual->max_salario = head->max_salario;                                                  \
                    snomeAtual->max_pos = 0;                                                                      \
                }                                                                                                 \
                memcpy(snomeAtual->max + snomeAtual->max_pos, head->max, (size_t)head->max_pos * sizeof(nome_t)); \
                snomeAtual->max_pos += head->max_pos;                                                             \
            }                                                                                                     \
            head = head->hh.next;                                                                                 \
        }                                                                                                         \
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
    area_t *areaAtual;
    area_t *areas = ((processar_t *)processos)->areas;
    for (cod = 0; cod < MAX_AREAS; cod++) {
        areaAtual = areas + cod;
        areaAtual->codigo = NULL;
        areaAtual->nome = NULL;
        areaAtual->total = 0;
        areaAtual->custo = 0;
        areaAtual->min_salario = INT_MAX;
        areaAtual->max_salario = 0;
    }
    // inicialização de sobrenomes
    unsigned hashv;
    sobrenome_t *sobrenomeAtual;
    sobrenome_t *sobrenomes = ((processar_t *)processos)->sobrenomes;
    unsigned sobrenomes_size = 0;
    sobrenomes->hh.next = NULL;
    sobrenomes->hh.prev = NULL;
    HASH_MAKE_TABLE(hh, sobrenomes);

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

            cod = codigo[1] - '1';
            areas_process(areas, funcionario, salario, cod);
            sobrenomes_process(sobrenomes, funcionario, salario, hashv, sobrenomeAtual);
        } else if (*p == 'c') {
            p += 9;
            codigo = p;
            p += 4;
            while (*p != '"')
                p++;
            p += 8;

            if (codigo[0] == 'A' && (codigo[1] == '1' || codigo[1] == '2')) {
                cod = codigo[1] - '1';
                areas[cod].nome = p;
                p += 7;
                while (*p != '"')
                    p++;
                areas[cod].nome_size = (unsigned char)(p - areas[cod].nome);
                p++;
            } else {
                p += 9;
            }
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
#define show_area(index)                                                                               \
    {                                                                                                  \
        areas = threads[index].areas;                                                                  \
        double salariof;                                                                               \
        area_t *most_emp = areas;                                                                      \
        area_t *least_emp = areas;                                                                     \
        int j;                                                                                         \
                                                                                                       \
        for (i = 0; i < MAX_AREAS; i++) {                                                              \
            salariof = (double)areas->max_salario / 100.F;                                             \
            for (j = 0; j < areas->max_pos; j++) {                                                     \
                printf("area_max|%.*s|%.*s %.*s|%.2f\n", areas->nome_size, areas->nome,                \
                       areas->max[j].nome_size, areas->max[j].nome,                                    \
                       areas->max[j].sobrenome_size, areas->max[j].sobrenome, salariof);               \
                if (areas->max_salario == global.max_salario) {                                        \
                    printf("global_max|%.*s %.*s|%.2f\n", areas->max[j].nome_size, areas->max[j].nome, \
                           areas->max[j].sobrenome_size, areas->max[j].sobrenome, salariof);           \
                }                                                                                      \
            }                                                                                          \
            salariof = (double)areas->min_salario / 100.F;                                             \
            for (j = 0; j < areas->min_pos; j++) {                                                     \
                printf("area_min|%.*s|%.*s %.*s|%.2f\n", areas->nome_size, areas->nome,                \
                       areas->min[j].nome_size, areas->min[j].nome,                                    \
                       areas->min[j].sobrenome_size, areas->min[j].sobrenome, salariof);               \
                if (areas->min_salario == global.min_salario) {                                        \
                    printf("global_min|%.*s %.*s|%.2f\n", areas->min[j].nome_size, areas->min[j].nome, \
                           areas->min[j].sobrenome_size, areas->min[j].sobrenome, salariof);           \
                }                                                                                      \
            }                                                                                          \
                                                                                                       \
            global.total += areas->total;                                                              \
            global.custo += areas->custo;                                                              \
                                                                                                       \
            salariof = ((double)areas->custo / 100.F) / (double)areas->total;                          \
            printf("area_avg|%.*s|%.2f\n", areas->nome_size, areas->nome, salariof);                   \
                                                                                                       \
            if (areas->total > most_emp->total) {                                                      \
                most_emp = areas;                                                                      \
            }                                                                                          \
            if (areas->total < least_emp->total) {                                                     \
                least_emp = areas;                                                                     \
            }                                                                                          \
            areas++;                                                                                   \
        }                                                                                              \
        salariof = ((double)global.custo / 100.F) / (double)global.total;                              \
        printf("global_avg|%.2f\n", salariof);                                                         \
                                                                                                       \
        printf("most_employees|%.*s|%u\n", most_emp->nome_size, most_emp->nome, most_emp->total);      \
        printf("least_employees|%.*s|%u\n", least_emp->nome_size, least_emp->nome, least_emp->total);  \
    }

/**
 * Mostrar todos os sobrenomes com 2 ou mais nomes
 */
#define show_sobrenomes(index)                                                      \
    head = threads[index].sobrenomes;                                               \
    while (head) {                                                                  \
        if (head->total > 1) {                                                      \
            double salariof = (double)head->max_salario / 100.F;                    \
            for (int i = 0; i < head->max_pos; i++) {                               \
                printf("last_name_max|%.*s|%.*s %.*s|%.2f\n",                       \
                       head->hh.keylen, head->hh.key, head->max[i].nome_size,       \
                       head->max[i].nome, head->hh.keylen, head->hh.key, salariof); \
            }                                                                       \
        }                                                                           \
        head = head->hh.next;                                                       \
    }

/**
 * Apagar os sobrenomes (simplificação do processo original)
 * No processo original era excluido cada ficha antes de excluir
 * a tabela e os buckets, simplifiquei excluindo tabela e buckets
 * no local que ficam guardados.
 */
#define freeSobrenomes(index)                   \
    {                                           \
        sobrenomes = threads[index].sobrenomes; \
        free(sobrenomes->hh.tbl->buckets);      \
        free(sobrenomes->hh.tbl);               \
    }

int main(int argc, char *argv[])
{
    int fjson;
    int i;
    int j;
    struct stat f;
    char *buffer;
    size_t buffer_max;
    sobrenome_t *sobrenomes;
    sobrenome_t *head;
    area_t *areas;

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

    // inicialização do controle de threads
    unsigned threads_max = sysconf(_SC_NPROCESSORS_ONLN); // numero de processadores (* o numero de threads em cada);
    if (threads_max < 2)
        threads_max = 2;
    threads = (processar_t *)malloc(sizeof(processar_t) * threads_max);
    buffer_max = (f.st_size / threads_max) + 1; // somo 1 pois a divisão pode não ser exata

    unsigned myMemoryPos = threads_max * (sizeof(area_t) * MAX_AREAS + sizeof(sobrenome_t) * MAX_SOBRENOMES);
    void *myMemory = (void *)mmap(0, myMemoryPos, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);

    // criação das threads
    j = 0; // funciona como o resto que devia ter sido processado mas não foi na thread anterior
    myMemoryPos = 0;
    size_t buffer_end = 0;
    for (i = 0; i < threads_max; i++) {
        threads[i].buffer = buffer + buffer_end;
        buffer_end += buffer_max + j;
        j = 0;
        while (buffer[buffer_end - j] != '}') {
            j++;
        }
        threads[i].buffer_end = buffer + (buffer_end - j);

        threads[i].areas = (area_t *)(myMemory + myMemoryPos);
        myMemoryPos += sizeof(area_t) * MAX_AREAS;
        threads[i].sobrenomes = (sobrenome_t *)(myMemory + myMemoryPos);

        pthread_create(&threads[i].id, NULL, processar, &threads[i]);
        myMemoryPos += sizeof(sobrenome_t) * MAX_SOBRENOMES;
        buffer_end = (threads[i].buffer_end - buffer) + 1;
    }
    // fechamento do arquivo
    close(fjson);

    // inicialização das variaveis do global
    global.custo = 0;
    global.total = 0;
    global.max_salario = 0;
    global.min_salario = INT_MAX;

    // encerramento das threads
    pthread_join(threads[0].id, NULL);
    for (i = 0; i < MAX_AREAS; i++) {
        areas = threads[0].areas + i;
        if (global.max_salario < areas->max_salario)
            global.max_salario = areas->max_salario;
        if (global.min_salario > areas->min_salario)
            global.min_salario = areas->min_salario;
    }
    for (i = 1; i < threads_max; i++) {
        pthread_join(threads[i].id, NULL);
        merge_areas(i);
        freeSobrenomes(i);
        merge_sobrenomes(i);
    }

    // Mostrando resultado
    show_area(0);
    show_sobrenomes(0);

    //liberar toda a memória ainda alocada
    freeSobrenomes(0);
    free(threads);
    munmap(buffer, f.st_size);
    munmap(myMemory, myMemoryPos);

    return EXIT_SUCCESS;
}
