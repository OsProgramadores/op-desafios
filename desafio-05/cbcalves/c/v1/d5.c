#include "uthash.h" // https://troydhanson.github.io/uthash/  hash table utilizada no processo
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Definições feitas para um melhor controle de alocação da memória (pra quem já viu o eAthena tinha créditos do Yor)
#define MALLOC(var, type, size)                                \
    if ((var = (type *)malloc(sizeof(type) * (size))) == NULL) \
    printf("Erro ao alocar no arquivo '%s', linha: %d\n", __FILE__, __LINE__), abort() // alocação de memória, se não conseguir, vai parar e mostrar a linha do erro.
#define REALLOC(var, type, size)                                     \
    if ((var = (type *)realloc(var, sizeof(type) * (size))) == NULL) \
    printf("Erro ao realocar no arquivo '%s', linha: %d\n", __FILE__, __LINE__), abort() // realocação de memória, se não conseguir, vai mostrar a linha onde teve o erro.
#define FREE(var)    \
    if (var != NULL) \
    free(var), var = NULL // após verificar se a váriavel realmente aponta pra memória, libera a memória, e diz que a váriavel agora aponta pra Null(0)
// fim das macros de alocação da memória memória

// tamanho das variáveis usadas, tem haver com a velocidade para alocar (foram feitas medidas para chegar nos numeros abaixo)
#define S_NOME 13
#define S_SOBRENOME 21
#define S_CODIGO 3
#define S_NOME_CARGO 28
// total de áreas possíveis ao fazer contas com os exemplos de dados que ele vai processar
#define TOTAL_AREAS 1296
// estou alocando todas as áreas possíveis pois é mais rápido fazer uma conta do que ficar com find

typedef struct funcionario_st
{
    // int id;
    char nome[S_NOME], sobrenome[S_SOBRENOME];
    struct funcionario_st *next;
    struct funcionario_st *area;
    struct funcionario_st *snome;
} funcionario_t; // nome e sobrenome dos funcionários

typedef struct area_st
{
    char codigo[S_CODIGO], nome[S_NOME_CARGO];
    funcionario_t *max, *min;
    unsigned long long custo;
    int total, max_salario, min_salario;
    struct area_st *global;
} area_t; // controle de max e min por área

typedef struct
{
    char sobrenome[S_SOBRENOME];
    UT_hash_handle hh;
    funcionario_t *max;
    int total, max_salario;
} sobrenome_t; // controle de max por sobrenome

typedef struct
{
    area_t *max;
    area_t *min;
    int max_size, min_size, total, max_salario, min_salario;
    unsigned long long custo;
} global_t; // controle de max e min global

// Variáveis globais
area_t *areas = NULL;
sobrenome_t *sobrenomes = NULL;

FILE *fjson = NULL; // arquivo json
char f_pos = 0;     // último char retirado
//

sobrenome_t *sobrenomes_find(char *s) // encontrar e retornar o sobrenome, se não existe ele inclui
{
    sobrenome_t *pos = NULL;
    HASH_FIND_STR(sobrenomes, s, pos);

    if (pos != NULL)
        return pos;

    MALLOC(pos, sobrenome_t, 1);
    memcpy(pos->sobrenome, s, S_SOBRENOME);
    pos->total = 0;
    pos->max = NULL;
    pos->max_salario = 0;
    HASH_ADD_STR(sobrenomes, sobrenome, pos);
    return pos;
}

void readbuffer(char *line) // leitura do arquivo até encontrar caracteres chaves
{
    for (; f_pos != EOF; f_pos = getc(fjson))
    {
        switch (f_pos)
        {
        case ' ':
        case 10:
        case '\r':
            continue;
        case ']': // indica para sair do loop e mudar pra área
            line[0] = f_pos;
            f_pos = getc(fjson);
            return;
        case '{': // inicio de sentença
            line[0] = f_pos;
            f_pos = getc(fjson);
            return;
        case ':': // estou saindo com : para aumento de velocidade de escrita de variável
        case '[': // entrada na área
            line[0] = f_pos;
            f_pos = getc(fjson);
            return;
        default:
            break;
        }
    }
}

int main(int argc, char *argv[])
{
    char codigo[S_CODIGO] = "**", usado = 0;
    char *s = NULL, line[2];
    funcionario_t *func = NULL;    // ficha dos funcionários
    funcionario_t *coletor = NULL; // coletar todos os funcionarios criados e apagar no final
    void *index = NULL;
    int salario = 0, i = 0, j = 0;
    area_t *most_emp = NULL, *least_emp = NULL;
    double salariof = 0;
    global_t global;

    //inicialização das areas
    MALLOC(areas, area_t, TOTAL_AREAS);
    for (i = 0; i < TOTAL_AREAS; i++)
    {
        areas[i].total = 0;
        areas[i].custo = 0;
        areas[i].max = NULL;
        areas[i].min = NULL;
        areas[i].global = NULL;
        areas[i].min_salario = __INT32_MAX__;
        areas[i].max_salario = 0;
    }

    // inicialização do coletor
    MALLOC(func, funcionario_t, 1);
    coletor = func;
    func->area = NULL;
    func->next = NULL;
    func->snome = NULL;

    // inicialização das variaveis do global
    global.max = NULL;
    global.min = NULL;
    global.custo = 0;
    global.max_size = 0;
    global.min_size = 0;
    global.total = 0;
    global.max_salario = 0;
    global.min_salario = __INT32_MAX__;

    if (argc < 2)
    {
        printf("Erro: Incluir o arquivo json\n./funcionario <arquivo json>\n");
        return 0;
    }

    fjson = fopen(argv[1], "r"); // abertura do arquivo
    if (fjson == NULL)
    {
        printf("Arquivo não encontrado\n");
        abort();
    }

    i = 0;
    while (f_pos != EOF)
    {
        readbuffer(line); // escreve o buffer na string até achar os carcteres de saída
        if (line[0] == '[')
            i++;
        if (line[0] == '[' && i == 1) // entra em funcionários
        {
            while (f_pos != EOF)
            {
                readbuffer(line);
                if (line[0] == ']')
                    break;
                if (line[0] != '{') // se contém { é abertura de campo
                    continue;

                if (usado) // para saber se foi incluido em algum local a ficha do funcionário e então criar outra ou reaproveita a não usada
                {          // malloc custa processamento
                    usado = 0;
                    MALLOC(func->next, funcionario_t, 1);
                    func = func->next;
                    func->area = NULL;
                    func->next = NULL;
                    func->snome = NULL;
                }
                readbuffer(line);

                // estou fazendo esse esquema abaixo para ganho de velocidade, ignorando o uso da string line, não faço verificação alguma dos dados
                while (f_pos != ':') // andar até achar :
                    f_pos = fgetc(fjson);
                f_pos = fgetc(fjson);
                s = &func->nome[0]; // posiciono o ponteiro de escrita no início do nome
                f_pos = fgetc(fjson);
                while (f_pos != '"') // pulei as '"' e cheguei no nome
                    *(s++) = f_pos, f_pos = fgetc(fjson);
                *s = 0;

                while (f_pos != ':') // mesma idéia acima
                    f_pos = fgetc(fjson);
                f_pos = fgetc(fjson);
                s = &func->sobrenome[0]; // sobrenome
                f_pos = fgetc(fjson);
                while (f_pos != '"')
                    *(s++) = f_pos, f_pos = fgetc(fjson);
                *s = 0;

                while (f_pos != ':')
                    f_pos = fgetc(fjson);
                f_pos = fgetc(fjson);
                salario = 0;         // salario
                while (f_pos != ',') // no salário faço logo a transformação em inteiro pulando o . e fazendo conta pra incluir as casas decimais
                {
                    salario = (salario * 10) + (f_pos - '0');
                    f_pos = fgetc(fjson);
                    if (f_pos == '.')
                        f_pos = fgetc(fjson);
                }

                while (f_pos != ':')
                    f_pos = fgetc(fjson);
                f_pos = fgetc(fjson);
                s = &codigo[0]; // codigo
                f_pos = fgetc(fjson);
                while (f_pos != '"')
                    *(s++) = f_pos, f_pos = fgetc(fjson);
                *s = 0;

                ///// analise da area (maior e menor salario, lista dos maiores e menores salarios)
                // conta para achar a área
                j = (codigo[0] - ((codigo[0] < 'A') ? '0' : 'A' - 10)) * 36;
                j += codigo[1] - ((codigo[1] < 'A') ? '0' : 'A' - 10);
                index = (void *)&areas[j];
                memcpy(((area_t *)index)->codigo, codigo, S_CODIGO);
                ((area_t *)index)->total++;
                ((area_t *)index)->custo += salario;
                if (((area_t *)index)->max_salario < salario)
                {
                    if (salario > global.max_salario)
                        global.max_salario = salario;
                    ((area_t *)index)->max_salario = salario;
                    ((area_t *)index)->max = func;
                    usado = 1;
                }
                else if (((area_t *)index)->max_salario == salario)
                {
                    func->area = ((area_t *)index)->max;
                    ((area_t *)index)->max = func;
                    usado = 1;
                }
                if (((area_t *)index)->min_salario > salario)
                {
                    if (salario < global.min_salario)
                        global.min_salario = salario;
                    ((area_t *)index)->min_salario = salario;
                    ((area_t *)index)->min = func;
                    usado = 1;
                }
                else if (((area_t *)index)->min_salario == salario)
                {
                    func->area = ((area_t *)index)->min;
                    ((area_t *)index)->min = func;
                    usado = 1;
                }
                ///// global (analise do global, guardo apenas os maiores e menores salários, depois eu escrevo a lista da área onde estão)
                global.total++;
                global.custo += salario;

                ///// sobrenomes (analise dos sobrenomes, guardando os maiores salários de cada sobrenome)
                index = (void *)sobrenomes_find(func->sobrenome);
                ((sobrenome_t *)index)->total++;
                if (((sobrenome_t *)index)->max_salario < salario)
                {
                    ((sobrenome_t *)index)->max_salario = salario;
                    ((sobrenome_t *)index)->max = func;
                    usado = 1;
                }
                else if (((sobrenome_t *)index)->max_salario == salario)
                {
                    func->snome = ((sobrenome_t *)index)->max;
                    ((sobrenome_t *)index)->max = func;
                    usado = 1;
                }
            }
        }
        else if (line[0] == '[' && i == 2) // entra na descrição das áreas
        {
            while (f_pos != EOF)
            {
                readbuffer(line);
                if (line[0] == ']')
                    break;
                if (line[0] != '{')
                    continue;
                readbuffer(line);
                s = &codigo[0];
                f_pos = fgetc(fjson); //a linha já vem posicionada no : eu pulo a aspa e começo a escrever o código
                while (f_pos != '"')
                    *(s++) = f_pos, f_pos = fgetc(fjson);
                *s = 0;

                j = (codigo[0] - ((codigo[0] < 'A') ? '0' : 'A' - 10)) * 36;
                j += codigo[1] - ((codigo[1] < 'A') ? '0' : 'A' - 10);
                index = (void *)&areas[j];
                while (f_pos != ':') // passo até o : e posiciono para escrever a descrição da área
                    f_pos = fgetc(fjson);
                f_pos = fgetc(fjson);
                if (((area_t *)index)->total == 0) // área não tem funcionários, não gasto processamento escrevendo variável
                    continue;
                s = &((area_t *)index)->nome[0];
                f_pos = fgetc(fjson);
                while (f_pos != '"')
                    *(s++) = f_pos, f_pos = fgetc(fjson);
                *s = 0;
            }
        }
    }
    fclose(fjson);

    // loops para mostrar os resultados, iniciando com as áreas
    for (i = 0; i < TOTAL_AREAS; i++)
    {
        if (areas[i].total == 0)
            continue;
        index = (void *)&areas[i];

        if (((area_t *)index)->max_salario == global.max_salario) // anotando os maiores salários
        {
            ((area_t *)index)->global = global.max;
            global.max = (area_t *)index;
        }
        if (((area_t *)index)->min_salario == global.min_salario) // anotando os menores salários
        {
            ((area_t *)index)->global = global.min;
            global.min = (area_t *)index;
        }
        if (((area_t *)index)->total > 0)
        {
            salariof = ((double)((area_t *)index)->custo / 100.F) / (double)((area_t *)index)->total;
            printf("area_avg|%s|%.2f\n", ((area_t *)index)->nome, salariof);

            if (most_emp == NULL || ((area_t *)index)->total > most_emp->total) // área com mais funcionários
                most_emp = (area_t *)index;
            if (least_emp == NULL || ((area_t *)index)->total < least_emp->total) // área com menos funcionários
                least_emp = (area_t *)index;
        }
        for (func = ((area_t *)index)->max; func != NULL; func = func->area)
        {
            salariof = (double)((area_t *)index)->max_salario / 100.F;
            printf("area_max|%s|%s %s|%.2f\n", ((area_t *)index)->nome, func->nome, func->sobrenome, salariof);
        }
        for (func = ((area_t *)index)->min; func != NULL; func = func->area)
        {
            salariof = (double)((area_t *)index)->min_salario / 100.F;
            printf("area_min|%s|%s %s|%.2f\n", ((area_t *)index)->nome, func->nome, func->sobrenome, salariof);
        }
    }
    // globais de maior e menor salários
    salariof = ((double)global.custo / 100.F) / (double)global.total;
    printf("global_avg|%.2f\n", salariof);
    for (index = (void *)global.max; index != NULL; index = (void *)((area_t *)index)->global)
    {
        for (func = ((area_t *)index)->max; func != NULL; func = func->area)
        {
            salariof = (double)global.max_salario / 100.F;
            printf("global_max|%s %s|%.2f\n", func->nome, func->sobrenome, salariof);
        }
    }
    for (index = (void *)global.min; index != NULL; index = (void *)((area_t *)index)->global)
    {
        for (func = ((area_t *)index)->min; func != NULL; func = func->area)
        {
            salariof = (double)global.min_salario / 100.F;
            printf("global_min|%s %s|%.2f\n", func->nome, func->sobrenome, salariof);
        }
    }

    printf("most_employees|%s|%d\n", most_emp->nome, most_emp->total);
    printf("least_employees|%s|%d\n", least_emp->nome, least_emp->total);

    // sobrenomes de mais de 2 funcionários
    for (index = (void *)sobrenomes; index != NULL; index = (void *)((sobrenome_t *)index)->hh.next)
    {
        if (((sobrenome_t *)index)->total < 2)
            continue;
        for (func = ((sobrenome_t *)index)->max; func != NULL; func = func->snome)
        {
            salariof = (double)((sobrenome_t *)index)->max_salario / 100.F;
            printf("last_name_max|%s|%s %s|%.2f\n", ((sobrenome_t *)index)->sobrenome, func->nome, func->sobrenome, salariof);
        }
    }

    //liberar toda a memória alocada (usando 'valgrind' para checar eficiencia da limpeza)
    FREE(areas);
    while (sobrenomes != NULL)
    {
        sobrenome_t *current_user, *tmp;
        HASH_ITER(hh, sobrenomes, current_user, tmp)
        {
            HASH_DEL(sobrenomes, current_user); /* delete it (users advances to next) */
            free(current_user);                 /* free it */
        }
    }
    while (coletor != NULL)
    {
        funcionario_t *tmp = coletor;
        coletor = tmp->next;
        FREE(tmp);
    }
    return 0;
}
