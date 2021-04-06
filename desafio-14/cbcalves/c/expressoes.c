#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct unit_st // unidade para guardar os pedaços da expressão
{
    char operacao;
    int numero;
    struct unit_st *next;
    struct unit_st *prev;
} expressao_t;

void expressao_clear(expressao_t *units) // limpeza das unidades
{
    expressao_t *tmp = NULL;
    while (units != NULL)
    {
        tmp = units;
        units = units->next;
        free(tmp);
    }
}
int expressao_operacao(char operacao, int num_a, int num_b) // função auxiliar para resolver as operações matemáticas
{
    int resp = 0;
    if (num_a == INT_MAX || num_b == INT_MAX) // se qualquer numero foi divido por zero propaga o erro
        return INT_MAX;

    switch (operacao)
    {
    case '^':
        if (num_b == 0) // qualquer número elevado a potência 0 retorna 1
        {
            resp = 1;
            break;
        }
        resp = num_a;
        for (int i = 2; i <= num_b; i++)
            resp *= num_a;
        break;
    case '*':
        resp = num_a * num_b;
        break;
    case '/':
        if (num_b == 0) // divisão por 0 não é possível
            return INT_MAX;
        resp = num_a / num_b;
        break;
    case '+':
        resp = num_a + num_b;
        break;
    case '-':
        resp = num_a - num_b;
        break;
    }
    return resp;
}
int expressao_calcular(expressao_t *units) // percorre as unidades realizando as operações
{
    expressao_t *tmp = NULL, *op = NULL;
    int resp = 0;
    char operacoes[3][2] = {{'^', 0}, {'*', '/'}, {'+', '-'}}; // agrupadas de acordo com a ordem das operações
    if (units->next == NULL) // se tem apenas uma unidade não existe operação
        return units->numero;

    for (int i = 0; i < 3; i++)
    {
        op = units->next;
        while (op != NULL)
        {
            if (op->operacao == operacoes[i][0] || op->operacao == operacoes[i][1])
            {
                op->prev->numero = expressao_operacao(op->operacao, op->prev->numero, op->numero); // guarda o resultado na unidade anterior
                op->prev->next = op->next;
                if (op->next)
                    op->next->prev = op->prev;
                tmp = op;
                op = op->prev;
                free(tmp); // vai reduzir tudo até ficar apenas uma unidade após todas as operações
            }
            op = op->next;
        }
    }
    return units->numero;
}

int expressao_processar(char *exp) // separar a expressão em unidades de operação
{
    char *p = exp, operacao = '+';
    int resp = 0, num = 0;
    expressao_t *units = NULL, *start = NULL;

    units = (expressao_t *)malloc(sizeof(expressao_t));
    if (!units)
    {
        printf("Memória insuficiente\n");
        return INT_MAX;
    }
    units->next = NULL;
    units->prev = NULL;
    units->numero = 0;
    units->operacao = '+';
    start = units;

    while (*p && *p != ')')
    {
        switch (*p)
        {
        case '(':     // resolve o parentesis e retorna um número, na recursão ele tira o ')' do texto
            *p = ' '; // ao retirar o parentesis ele volta com vários espaços em branco
            p++;
            num = expressao_processar(p);
        case ' ': // pula espaço em branco
            break;
        case '+':
        case '-':
        case '^':
        case '*':
        case '/': // guarda a unidade de operação
            units->operacao = operacao;
            units->numero = num;
            units->next = (expressao_t *)malloc(sizeof(expressao_t));
            if (!units->next)
            {
                printf("Memória insuficiente\n");
                expressao_clear(start);
                return INT_MAX;
            }
            units->next->prev = units;
            units = units->next;
            units->next = NULL;
            operacao = *p;
            num = 0;
            break;
        default:
            if (*p >= '0' && *p <= '9')
                num = num * 10 + (*p - '0');
            break;
        }
        *p = ' '; // apagar o que já foi calculado ou incluído na lista
        p++;
    }
    if (*p == ')') // apagar ) do texto evitando erro no retorno
        *p = ' ';
    units->operacao = operacao; // guarda o ultimo número
    units->numero = num;
    resp = expressao_calcular(start); // calcula a expressão

    expressao_clear(start); // limpa a memória
    return resp;
}

int expressao(char *exp)
{
    char *p = exp;
    int parenteses = 0, alternar = 1, num = 1;

    // primeiro verifica a syntax
    while (*p)
    {
        switch (*p)
        {
        case '\n': // retirar nova linha do texto se tiver
        case '\r':
            *p = 0;
            break;
        case '+':
        case '-':
        case '*':
        case '/':
        case '^':
            num = 1;
            alternar++;
            break;
        case '(':
            parenteses++;
            break;
        case ')':
            parenteses--;
            break;
        default:
            if (num && *p >= '0' && *p <= '9')
            {
                num = 0;
                alternar--;
            }
            break;
        }
        p++;
    }
    if (alternar != 0 || parenteses != 0)
        return INT_MIN;

    return expressao_processar(exp); // syntax correta, processa a expressão
}

int main(int argc, char *argv[])
{
    char entrada[201];
    int resultado = 0;
    FILE *fs = NULL;

    if (argc < 2)
    {
        printf("Uso: %s <arquivo de expressões>\n", argv[0]);
        return 0;
    }

    fs = fopen(argv[1], "r");
    if (!fs)
    {
        printf("Arquivo não encontrado\n");
        return 1;
    }
    while (fgets(entrada, sizeof(entrada) - 1, fs))
    {
        if (entrada[0] == 0)
            continue;

        resultado = expressao(entrada);
        if (resultado == INT_MAX)
            printf("ERR DIVBYZERO\n");
        else if (resultado == INT_MIN)
            printf("ERR SYNTAX\n");
        else
            printf("%d\n", resultado);
    }
    fclose(fs);

    return 0;
}