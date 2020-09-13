// compilar no unix/linux
// > gcc -Ofast primospi.c -o primospi -lm -pthread
//
// compilado no MINGW64 (Windows)
// $ gcc -Ofast primospi.c -o primospi -lm
//
#include <stdio.h>
#include <stdlib.h>
#ifndef _WIN32 // adicionado para compilar no windows
#include <pthread.h>
#include <unistd.h>
#endif // _WIN32

typedef struct pilist_st
{
    char *start;
    char *end;
    struct pilist_st *coletor; // encadeamento para limpeza de memória
} pilist_t;                    // lista de números primos extraídos de PI

typedef struct
{
    size_t id;
    char *start;
    char *end;
    char *resp;
} mythread_t; // estrutura das threads

//// Variáveis globais
char *maior_start = NULL;   // maior início
char *maior_end = NULL;     // maior final
int *primos_list = NULL;    // lista de números primos de 2 até 9973
char *buffer = NULL;        // arquivo do número PI
size_t buffer_size = 0;     // tamanho do arquivo do número PI
pilist_t *coletor = NULL;   // encadeamento da lista para limpeza
mythread_t *threads = NULL; // estrutura das threads
size_t threads_max = 0;     // máximo de threads que serão abertas
//// Fim das variáveis globais

void free_coletor() // limpeza dos números primos extraídos de PI
{
    pilist_t *tmp = NULL;
    while (coletor != NULL)
    {
        tmp = coletor;
        coletor = coletor->coletor;
        free(tmp);
    }
}

void free_all() // limpeza de toda a memória alocada
{
    free_coletor();
    if (primos_list)
        free(primos_list);
    if (threads)
        free(threads);
    if (buffer)
        free(buffer);
}

void threads_init() // construtor das threads
{
    if (threads_max == 0)
    {
#ifndef _WIN32
        threads_max = sysconf(_SC_NPROCESSORS_ONLN) * 2; // numero de processadores (* o numero de threads em cada);
#endif
        if (threads_max < 4)
            threads_max = 4;
        threads = (mythread_t *)malloc(sizeof(mythread_t) * threads_max);
        if (!threads)
        {
            printf("Memória insuficiente para processar os números primos de PI\n");
            free_all();
            exit(1);
        }
    }
    for (int i = 0; i < threads_max; i++)
    {
        threads[i].id = 0;
        threads[i].start = NULL;
        threads[i].end = NULL;
        threads[i].resp = NULL;
    }
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

pilist_t *processar_alocar() // alocação de memória para anotar um número primo extraído de PI
{
    pilist_t *pilst = NULL;
    pilst = (pilist_t *)malloc(sizeof(pilist_t));
    if (!pilst)
    {
        printf("Memória insuficiente para alocar a lista de números primos de PI\n");
        free_all();
        exit(1);
    }
    pilst->coletor = coletor;
    coletor = pilst;
    pilst->end = NULL;
    pilst->start = NULL;
    return pilst;
}

void *processar_maiorprimo_r(void *in) // processo recursivo para achar a maior sequencia de primos possível
{
    mythread_t *this_thread = (mythread_t *)in;
    pilist_t *entrada = coletor;
    char *maior = this_thread->end, *this_end = this_thread->end;
    while (entrada != NULL)
    {
        if ((this_end + 1) == entrada->start)
        {
            this_thread->end = entrada->end;
            processar_maiorprimo_r(in);
            if (maior < this_thread->resp)
                maior = this_thread->resp;
        }
        entrada = entrada->coletor;
    }
    this_thread->resp = maior;
    return 0;
}

void processar_jointhread(size_t i) // analizar o resultado das threads
{
    if (threads[i].id == 0)
        return;
#ifndef _WIN32
    pthread_join(threads[i].id, NULL);
#endif
    if ((maior_end - maior_start) < (threads[i].resp - threads[i].start))
    {
        maior_start = threads[i].start;
        maior_end = threads[i].resp;
    }
}

void processar_maiorprimo() // processo de abertura das threads
{
    pilist_t *entrada = coletor;
    int i = 0;

    threads_init();

    while (entrada != NULL)
    {
        processar_jointhread(i);
        threads[i].start = entrada->start;
        threads[i].end = entrada->end;
        threads[i].resp = NULL;
#ifndef _WIN32
        pthread_create(&threads[i].id, NULL, processar_maiorprimo_r, &threads[i]);
#else
        processar_maiorprimo_r(&threads[i]); // windows não vai abrir pthread
        threads[i].id = 1;
#endif

        if (++i == threads_max)
            i = 0;
        entrada = entrada->coletor;
    }
    for (i = 0; i < threads_max; i++)
        processar_jointhread(i);

    // uso uma das alocações para anotar o resultado até agora e saber se ele tem continuidade
    // no próximo processamento
    entrada = coletor;
    coletor = coletor->coletor;
    entrada->start = maior_start;
    entrada->end = maior_end;
    entrada->coletor = NULL;
    free_coletor();
    coletor = entrada;
}

void processar() // ler o arquivo de PI, separar os primos e chamar as funcoes que calculam as sequencias
{
    char s1[2] = {0, 0}, s2[3] = {0, 0, 0}, s3[4] = {0, 0, 0, 0}, s4[5] = {0, 0, 0, 0, 0};
    pilist_t *pilst = NULL;
    char *p = buffer;

    while (*p != '.')
        p++;
    p++;
    while (*p)
    {
        s1[0] = *p;
        s2[0] = s2[1], s2[1] = *p;
        s3[0] = s3[1], s3[1] = s3[2], s3[2] = *p;
        s4[0] = s4[1], s4[1] = s4[2], s4[2] = s4[3], s4[3] = *p;

        if (primos_isprimo(atoi(s1))) // somente 1 char
        {
            pilst = processar_alocar();
            pilst->end = p;
            pilst->start = p;
        }
        if (s2[0] && primos_isprimo(atoi(s2))) // somente 2 chars
        {
            pilst = processar_alocar();
            pilst->end = p;
            pilst->start = p - 1;
        }
        if (s3[0] && primos_isprimo(atoi(s3))) // somente 3 chars
        {
            pilst = processar_alocar();
            pilst->end = p;
            pilst->start = p - 2;
        }
        if (s4[0] && primos_isprimo(atoi(s4))) // somente 4 chars
        {
            pilst = processar_alocar();
            pilst->end = p;
            pilst->start = p - 3;
        }
        if (((p - buffer) % 10000) == 0) // a cada 10.000 números analizados ele faz o processamento e apaga a lista
        {
            if (((p - buffer) % 100000) == 0) // anota algo na tela para não parecer que ficou paralizado, é entediante aguardar sem saber o progresso
                fprintf(stdout, "%ld00K", ((p - buffer) / 100000));
            else
                fprintf(stdout, ".");
            fflush(stdout);
            processar_maiorprimo();
        }

        p++;
    }
    processar_maiorprimo(); // caso ainda tenha algum número incluído na lista processa antes de retornar
    printf("\n");
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

    maior_end++;
    *maior_end = 0;
    printf("%s\n", maior_start);

    free_all();

    return 0;
}
