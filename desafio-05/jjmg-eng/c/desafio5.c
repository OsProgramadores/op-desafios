#include <stdlib.h>      // DESAFIO 5 - OsProgramadores
#include <stdio.h>       // Implementação em C
#include <string.h>      // João J.M. Gonçalves
#include <ctype.h>       // 08/01/2021

#define DELIMITERS  "\t\n{}[],:"
#define DELIMITERS1 "\t\n{}[],:\""
#define SIZEFUNC    sizeof(func_t)
#define SIZEAREA    sizeof(areas_t)
#define SIZESNOME   sizeof(snomes_t)
#define SIZENOME    sizeof(nomes_t)
#define _free(p_a)  {free(p_a); p_a = NULL;}
#define _index(i,n) {i = strlen(tok)>n ? toupper(tok[n]) - 'A' : 0; i = i<0 ? 0 : i>25 ? 25 : i;}

enum {ID, Id, Nome, NOME, Sobrenome, SOBRENOME, Salario, SALARIO, Codigo, AREA};
enum {CODIGO, CODIGO_AREA, Nome_area, NOME_AREA};

struct FUNCIONARIOS {
    char nome[32];
    char sobrenome[32];
    unsigned long salario;
    struct FUNCIONARIOS *next;
};

typedef struct FUNCIONARIOS func_t;

struct AREAS {
    char codigo[8];
    char nome[32];
    int nfunc;
    unsigned long somaSalarios;
    func_t *area_max;
    func_t *area_min;
    struct AREAS *next;
};

typedef struct AREAS areas_t;

struct NOMES {
    char nome[32];
    struct NOMES *next;
};

typedef struct NOMES nomes_t;

struct SOBRENOMES {
    char sobrenome[32];
    unsigned long salario;
    int nfunc;
    nomes_t *list;
    struct SOBRENOMES *next;
};

typedef struct SOBRENOMES snomes_t;

void InsertNodeFunc(func_t **dest, func_t **src)
{
    (*src)->next = *dest;
    *dest = *src;
    *src = NULL;
}

void FreeFunc(func_t **f)
{
    if(*f != NULL) {
        FreeFunc(&(*f)->next);
        _free(*f);
    }
}

void MaxMinSal(func_t **max, func_t **min, func_t **new_node)
{
        if(*max == NULL && *min == NULL) {
            InsertNodeFunc(max, new_node);
            (*min) = (func_t *)malloc(SIZEFUNC);
            memcpy(*min, *max, SIZEFUNC);
        }
        else {
            if((*new_node)->salario >= (*max)->salario){
                if((*new_node)->salario >  (*max)->salario) FreeFunc(max);
                InsertNodeFunc(max, new_node);
            }

            if((*min)->salario == (*max)->salario) {
                *new_node = (func_t *)malloc(SIZEFUNC);
                memcpy(*new_node, *max, SIZEFUNC);
            }

            if(*new_node != NULL) {
                if((*new_node)->salario <= (*min)->salario) {
                    if((*new_node)->salario <  (*min)->salario) FreeFunc(min);
                    InsertNodeFunc(min, new_node);
                 }
                else _free(*new_node);
            }
        }
}

void InsertNodeNome(nomes_t **dest, nomes_t **src)
{
    (*src)->next = *dest;
    *dest = *src;
    *src = NULL;
}

void FreeNome(nomes_t **f)
{
    if(*f != NULL) {
        FreeNome(&(*f)->next);
        _free(*f);
    }
}

void InsertNodeSnome(snomes_t **dest, snomes_t **src)
{
    (*src)->next = *dest;
    *dest = *src;
    *src = NULL;
}

void FreeSnome(snomes_t **f)
{
    if(*f != NULL) {
        FreeSnome(&(*f)->next);
        FreeNome(&((*f)->list));
        _free(*f);
    }
}

snomes_t *searchSnome(snomes_t **a, char *sobrenome)
{
    snomes_t *aux = *a;
    for(;aux != NULL; aux = aux->next)
        if(!strcmp(aux->sobrenome, sobrenome)) break;
    if(aux ==  NULL) {
        aux = (snomes_t *)malloc(SIZESNOME);
        memset(aux, 0, SIZESNOME);
        strcpy(aux->sobrenome, sobrenome);
        aux->list = NULL;
        aux->next = *a;
        *a = aux;
    }
    return aux;
}

void InsertNodeArea(areas_t **dest, areas_t **src)
{
    (*src)->next = *dest;
    *dest = *src;
    *src = NULL;
}

void FreeArea(areas_t **f)
{
    if(*f != NULL) {
        FreeArea(&(*f)->next);
        FreeFunc(&((*f)->area_max));
        FreeFunc(&((*f)->area_min));
        _free(*f);
    }
}

areas_t *searchArea(areas_t **a, char *codigo)
{
    areas_t *aux = *a;
    for(;aux != NULL; aux = aux->next)
        if(!strcmp(aux->codigo, codigo)) break;
    if(aux ==  NULL) {
        aux = (areas_t *)malloc(SIZEAREA);
        memset(aux, 0, SIZEAREA);
        strcpy(aux->codigo, codigo);
        aux->area_max     =
        aux->area_min     = NULL;
        aux->next = *a;
        *a = aux;
    }
    return aux;
}

void print(const char *listName, const char *areaName, func_t **f)
{
    func_t *auxFunc;
    while(*f != NULL) {
        if(strstr(listName, "area") != NULL)    printf("%s|%s|%s %s|%.2f\n", listName, areaName, (*f)->nome, (*f)->sobrenome, (*f)->salario*0.01);
        else             /* "global" */         printf("%s|%s %s|%.2f\n", listName, (*f)->nome, (*f)->sobrenome, (*f)->salario*0.01);
        auxFunc = *f;
        *f = (*f)->next;
        _free(auxFunc);
    }
}

int main(int argc, char *argv[])
{
    if (argc < 2) { printf("Uso: %s <arquivo json>\n", argv[0]); return 0; }
    FILE *db = fopen(argv[1],"r");
    char s[4096];
    char tok[32], *tok1;

    func_t   *global_max      = NULL,
             *global_min      = NULL,
             *global_new      = NULL,
             *auxFunc         = NULL;
    areas_t  *areas           = NULL,
             *most_employees  = NULL,
             *least_employees = NULL,
             *auxArea         = NULL,
             *p_a             = NULL;
    snomes_t *last_name_max[26][26][26][26],
             *p_s             = NULL,
             *p0              = NULL;
    nomes_t  *nome_new        = NULL;

    char *p;
    int nfunc = 0, i, j, k, l;
    unsigned long somaSalarios = 0;
    for(i = 0; i<26; i++)
    for(j = 0; j<26; j++)
    for(k = 0; k<26; k++)
    for(l = 0; l<26; l++)
        last_name_max[i][j][k][l] = NULL;
    int regArea = 0;
    int regFunc = 0;
    while(!feof(db)) {
        p = fgets(s,4096,db);
        for(tok1 = strtok(&s[strcspn(s,DELIMITERS1)], DELIMITERS1); tok1 != NULL; tok1 = strtok (NULL, DELIMITERS)) {
            if(tok1[0] == 32) tok1 = strtok(NULL, DELIMITERS);
            strcpy(tok, tok1);
            if(tok[0] == '\"') {
                 p = strrchr(tok,'\"');
                *p = 0;
                memmove(tok, tok+1, 31);
            }
            // LISTA DE FUNCIONÁRIOS
            if(!regArea) switch(regFunc) {
            case ID :
                    if(!strcmp(tok,"id")) {
                        if(global_new == NULL) global_new = (func_t *)malloc(SIZEFUNC);
                        nfunc++;
                        regFunc++;
                    }
                   break;
            case NOME:
                   strcpy(global_new->nome, tok);
                   regFunc++;
                   break;
            case SOBRENOME :
                   strcpy(global_new->sobrenome, tok);
                   _index(i,0); _index(j,1); _index(k,2); _index(l,3);
                   p_s = searchSnome(&last_name_max[i][j][k][l], tok);
                   regFunc++;
                   break;
            case SALARIO :
                    global_new->salario = atol(tok)*100+atoi(strrchr(tok,'.')+1);
                    somaSalarios += global_new->salario;

                    if(nome_new == NULL) nome_new = (nomes_t *)malloc(SIZENOME);
                    strcpy(nome_new->nome, global_new->nome);

                    if(p_s->list == NULL) {
                        InsertNodeNome(&p_s->list, &nome_new);
                        p_s->salario = global_new->salario;
                    }
                    else {
                        if(p_s->salario < global_new->salario) {
                            FreeNome(&(p_s->list));
                            p_s->salario = global_new->salario;
                        }
                        p_s->nfunc++;
                        if(p_s->salario <= global_new->salario) InsertNodeNome(&p_s->list, &nome_new);
                        else _free(nome_new);
                    }
                    if(auxFunc == NULL) auxFunc = (func_t *)malloc(SIZEFUNC);
                    memcpy(auxFunc, global_new, SIZEFUNC);
                    MaxMinSal(&global_max, &global_min, &global_new);
                    regFunc++;
                    break;
            case AREA :
                    p_a = searchArea(&areas, tok);
                    p_a->somaSalarios += auxFunc->salario;
                    MaxMinSal(&(p_a->area_max), &(p_a->area_min), &auxFunc);
                    p_a->nfunc++;
                    regFunc = 0;
                    break;
            default: regFunc++;
            }
            // LISTA DE ÁREAS
            if(!regFunc) switch(regArea) {
            case CODIGO :
                regArea = !strcmp(tok,"codigo");
                break;
            case CODIGO_AREA :
                p_a = searchArea(&areas, tok);
                regArea++;
                break;
            case NOME_AREA :
                strcpy(p_a->nome,tok);
                regArea = 0;
                break;
            default: regArea++;
            }
        }
    }
    fclose(db);

    print("global_max","",&global_max);
    print("global_min","",&global_min);
    printf("global_avg|%.2f\n", somaSalarios*0.01/nfunc);

    for(p_a = areas; p_a != NULL; p_a = p_a->next) {
        print("area_max",p_a->nome,&p_a->area_max);
        print("area_min",p_a->nome,&p_a->area_min);
        if(p_a->nfunc > 0) {
            printf("area_avg|%s|%.2f\n", p_a->nome, p_a->somaSalarios*0.01/p_a->nfunc);

            if(auxArea == NULL) auxArea = (areas_t *)malloc(SIZEAREA);
            memcpy(auxArea, p_a, SIZEAREA);
            if(most_employees != NULL && p_a->nfunc > most_employees->nfunc)  FreeArea(&most_employees);
            if(most_employees == NULL || p_a->nfunc >= most_employees->nfunc) InsertNodeArea(&most_employees, &auxArea);
            if(auxArea == NULL) auxArea = (areas_t *)malloc(SIZEAREA);
            memcpy(auxArea, p_a, SIZEAREA);
            if(least_employees != NULL && p_a->nfunc < least_employees->nfunc)  FreeArea(&least_employees);
            if(least_employees == NULL || p_a->nfunc <= least_employees->nfunc) InsertNodeArea(&least_employees, &auxArea);
        }
        if(auxArea != NULL) _free(auxArea);
    }
    FreeArea(&areas);

    for(p_a = most_employees; p_a != NULL; p_a = p_a->next)
        printf("most_employees|%s|%d\n", p_a->nome, p_a->nfunc);
    FreeArea(&most_employees);
    for(p_a = least_employees; p_a != NULL; p_a = p_a->next)
        printf("least_employees|%s|%d\n", p_a->nome, p_a->nfunc);
    FreeArea(&least_employees);

    for(i = 0; i<26; i++)
    for(j = 0; j<26; j++)
    for(k = 0; k<26; k++)
    for(l = 0; l<26; l++) {
        for(p0 = p_s = last_name_max[i][j][k][l]; p_s != NULL; p_s = p_s->next) {
            if(p_s->nfunc) {
                for(nomes_t *p = p_s->list; p != NULL; p = p->next) {
                    printf("last_name_max|%s|%s %s|%.2f\n",p_s->sobrenome, p->nome, p_s->sobrenome, p_s->salario*0.01);
                }
            }
        }
        if(p0 != NULL) FreeSnome(&p0);
    }
    return 0;
}
