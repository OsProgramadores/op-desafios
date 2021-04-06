#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Macros de alocação da memória
#define MALLOC(var, type, size) var = (type *)malloc(sizeof(type) * (size))
#define REALLOC(var, type, size) var = (type *)realloc(var, sizeof(type) * (size))
#define FREE(var) free(var), var = NULL
#define ERRODEALOCAO -1
#define MINALLOC 100 // melhora na alocação de arrays
//
#define NAOACHOU -1

typedef struct // estrutura de regras
{
    size_t state; //hash do estado
    char symbol;
    char newsymbol;
    char direction;
    size_t newstate; // hash do novo estado
} regras_t;

//variáveis globais
regras_t **regras = NULL;       // array de regras
int regras_size = 0;            // numero de regras carregadas
char regras_filename[128] = ""; // arquivo carregado
// estados chave
size_t __regras_estado_geral = 0;   // '*'
size_t __regras_estado_inicial = 0; // '0'
size_t __regras_estado_halt = 0;    // 'halt'

size_t regras_hash(const char *str) // calculo de hash UNIX ELFHASH
{
    size_t h = 0, high = 0;
    while (*str)
    {
        h = (h << 4) + ((unsigned char)*str++);
        if (high == (h & 0xF0000000))
            h ^= high >> 24;
        h &= ~high;
    }
    return h;
}

void regras_quicksort(int l, int r) //sort do vetor (ou array) de regras, método de sort é quick sort
{
    regras_t *v = regras[r];
    regras_t *tmp = NULL;
    int i = l - 1, j = r;
    if (r <= l)
        return;
    while (1)
    {
        while (regras[++i]->state < v->state)
            ;
        while (v->state < regras[--j]->state)
        {
            if (j == l)
                break;
        }
        if (i >= j)
            break;
        tmp = regras[i];
        regras[i] = regras[j];
        regras[j] = tmp;
    }
    tmp = regras[i];
    regras[i] = regras[r];
    regras[r] = tmp;

    regras_quicksort(l, i - 1);
    regras_quicksort(i + 1, r);
}

void regras_free()
{
    for (int i = 0; i < regras_size; i++)
        FREE(regras[i]);
    regras_size = 0;
    FREE(regras);
}

int regras_carregar(const char *filename) // carregar as regras
{
    FILE *fs = NULL;
    char line[2048], estado[20], novoestado[20];
    regras_t *insert = NULL;

    if (strcmp(filename, regras_filename) == 0) // verifica se precisa carregar regras novas
        return 1;

    memcpy(regras_filename, filename, 128); // guarda o nome do arquivo de regras que foi carregado

    if (__regras_estado_geral == 0) // inicialização de variáveis chave na primeira chamada
    {
        line[0] = '*', line[1] = 0;
        __regras_estado_geral = regras_hash(line);
        line[0] = '0', line[1] = 0;
        __regras_estado_inicial = regras_hash(line);
        line[0] = 'h', line[1] = 'a', line[2] = 'l', line[3] = 't', line[4] = 0;
        __regras_estado_halt = regras_hash(line);
    }

    regras_free();
    MALLOC(regras, regras_t *, MINALLOC);
    if (!regras)
    {
        printf("ERRO: Alocação de memória para a array de regras, bytes não alocados: %d\n", (int)(sizeof(regras_t *) * MINALLOC));
        regras_filename[0] = 0;
        return ERRODEALOCAO;
    }

    fs = fopen(filename, "r");
    if (fs == NULL)
    {
        printf("Arquivo de regras '%s' não encontrado.\n", filename);
        abort();
    }
    while (fgets(line, sizeof(line) - 1, fs))
    {
        if (line[0] == ';' || line[0] == 10 || line[0] == '\r') // continua se for comentário ou linha vazia
            continue;
        MALLOC(insert, regras_t, 1); // aloca uma estrutura de dados
        if (!insert)
        {
            printf("ERRO: Alocação de memória para a estrutura de regra, bytes não alocados: %d\n", (int)sizeof(regras_t));
            regras_filename[0] = 0;
            regras_free();
            return ERRODEALOCAO;
        }
        sscanf(line, "%s %c %c %c %s", estado, &insert->symbol, &insert->newsymbol, &insert->direction, novoestado);
        insert->state = regras_hash(estado);
        if (novoestado[0] == 'h' && novoestado[1] == 'a' && novoestado[2] == 'l' && novoestado[3] == 't') // estado de halt
            insert->newstate = __regras_estado_halt;
        else
            insert->newstate = regras_hash(novoestado);
        regras_size++;
        if ((regras_size % MINALLOC) == 0)
        {
            REALLOC(regras, regras_t *, regras_size + MINALLOC);
            if (!regras)
            {
                printf("ERRO: Alocação de memória para a array de regras, bytes não alocados: %d\n", (int)(sizeof(regras_t *) * (MINALLOC + regras_size)));
                regras_filename[0] = 0;
                regras_free();
                return ERRODEALOCAO;
            }
        }
        regras[regras_size - 1] = insert; // carrega essa estrutura de dados no final do vetor
    }
    fclose(fs);
    regras_quicksort(0, regras_size - 1); // sort nas regras
    return 1;
}

int regras_estado(size_t state, char c) // encontrar a regra para este símbolo no estado
{
    int i = 0, isecond = NAOACHOU;
    if (c == ' ') // se for ' ' (espaço) tem que mudar para '_'
        c = '_';

    while (i < regras_size && regras[i]->state != state)
        i++;
    for (; i < regras_size && regras[i]->state == state; i++) // procura se existe no estado atual
    {
        if (regras[i]->symbol == c) // achou a mais específica, retorna
            return i;
        if (regras[i]->symbol == '*') // menos específica no estado atual se a geral não existir(?)
            isecond = i;
    }

    i = 0;
    while (i < regras_size && regras[i]->state != __regras_estado_geral)
        i++;
    for (; i < regras_size && regras[i]->state == __regras_estado_geral; i++) //procura se tem no estado geral
    {
        if (regras[i]->symbol == c) // mais específica do estado geral
            return i;
        if (regras[i]->symbol == '*') // menos específica do estado geral
            isecond = i;
    }

    return isecond; // retorna NAOACHOU (-1) ou achou uma menos específica
}

char *regras_processar(const char *command) // processa a fita
{
    size_t n_regra = 0;
    int i = 0, s_len = 0;
    size_t state = __regras_estado_inicial; //estado "0" é sempre o início
    char *s = NULL;

    s_len = strlen(command);
    MALLOC(s, char, s_len + 1); // aloca e prepara a fita
    if (!s)
    {
        printf("ERRO: Alocação de memória para a fita, bytes não alocados: %d\n", (s_len + 1));
        return NULL;
    }

    memcpy(s, command, s_len + 1);

    if (s_len == 0) // string vazia não existe o q fazer
        return s;

    while (state != __regras_estado_halt) //executar até existir halt
    {
        if (i == s_len) //se leitor for maior q tamanho da string, aumenta a string
        {
            s_len++;
            REALLOC(s, char, s_len + 1);
            if (!s)
            {
                printf("ERRO: Alocação de memória para a fita, bytes não alocados: %d\n", (s_len + 1));
                return NULL;
            }
            s[i] = ' ';
            s[i + 1] = 0;
        }

        else if (i < 0) // se leitor for menor que o tamanho da string, aumenta a string e move tudo
        {
            s_len++;
            REALLOC(s, char, s_len + 1);
            if (!s)
            {
                printf("ERRO: Alocação de memória para a fita, bytes não alocados: %d\n", (s_len + 1));
                return NULL;
            }
            memcpy(&s[1], s, s_len);
            s[0] = ' ';
            i = 0;
        }
        n_regra = regras_estado(state, s[i]); // achar a regra para a leitura no atual estado
        if (n_regra == NAOACHOU)              // se não existe regra, algo de errado não está certo, abortar
        {
            if (s_len < 3)
            {
                REALLOC(s, char, 4);
                if (!s)
                {
                    printf("ERRO: Alocação de memória para a fita, bytes não alocados: %d\n", 4);
                    return NULL;
                }
            }
            s[0] = 'E', s[1] = 'R', s[2] = 'R', s[3] = 0;
            return s;
        }
        if (regras[n_regra]->newstate != __regras_estado_geral) // novo estado, ou se for '*' deixa como está
            state = regras[n_regra]->newstate;

        if (regras[n_regra]->newsymbol == '_') // se for '_' substitui por espaço
            s[i] = ' ';
        else if (regras[n_regra]->newsymbol != '*') // se não for '*' substitui a letra, se for '*' não faz nada
            s[i] = regras[n_regra]->newsymbol;

        if (regras[n_regra]->direction == 'r') // move o leitor para a direita
            i++;
        else if (regras[n_regra]->direction == 'l') // move o leitor para a esquerda,
            i--;
        else if (regras[n_regra]->direction != '*') // se for '*' não faz nada, se for diferente aborta o programa
        {
            if (s_len < 3)
            {
                REALLOC(s, char, 4);
                if (!s)
                {
                    printf("ERRO: Alocação de memória para a fita, bytes não alocados: %d\n", 4);
                    return NULL;
                }
            }
            s[0] = 'E', s[1] = 'R', s[2] = 'R', s[3] = 0;
            return s;
        }
    }
    for (i = 0; i < s_len; i++) // left trim (apagar os espaço, à esquerda da fita e mover tudo)
    {
        if (s[i] != ' ')
            break;
    }
    if (i > 0)
        memcpy(&s[0], &s[i], s_len - i + 1);
    for (i = s_len - i - 1; i >= 0; i--) // right trim (apagar os espaços, à direita da fita)
    {
        if (s[i] == ' ')
            s[i] = 0;
        else
            break;
    }

    return s;
}

int main(int argc, char *argv[])
{
    FILE *df = NULL;
    char line[2048], filename[128], command[128];
    char *fita = NULL;

    if (argc < 2)
    {
        printf("Uso: %s <datafile>\n", argv[0]);
        return 0;
    }

    df = fopen(argv[1], "r");
    if (df == NULL)
    {
        printf("Arquivo não encontrado\n");
        abort();
    }
    while (fgets(line, sizeof(line) - 1, df)) // lê a linha
    {
        sscanf(line, "%127[^,],%127[^\n]", filename, command); // separa em nome do arquivo e comando
        if (strlen(filename) == 0)                             // continua se for vazia
            continue;

        if (regras_carregar(filename) == ERRODEALOCAO) // carrega as regras
        {
            printf("Memória insuficiente para execução do programa\n");
            break;
        }
        fita = regras_processar(command); // processa a fita
        if (!fita)                        // retornou Null, deu erro na memoria ao processar o comando
        {
            printf("Memória insuficiente para execução do programa\n");
            break;
        }
        printf("%s,%s,%s\n", filename, command, fita); // posta o resultado da fita
        FREE(fita);                                    // apaga o resultado
    }
    fclose(df);
    regras_free(); // limpa a memória

    return 0;
}
