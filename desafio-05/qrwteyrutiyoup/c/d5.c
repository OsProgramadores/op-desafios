#include <ctype.h>
#include <errno.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#ifndef _WIN32
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#endif

#include "uthash.h"

#define NAME_LEN 32
#define SURNAME_LEN 64
#define AREA_LEN 4
#define EPSILON 0.000001

struct area_t {
    char code[AREA_LEN];
    char name[NAME_LEN];
    UT_hash_handle hh;
};

struct employee_t {
    char name[NAME_LEN];
    char surname[SURNAME_LEN];
    double salary;
    char area[AREA_LEN];
    uint64_t count_in_area;
    UT_hash_handle hh;
};

struct employee_list_t {
    char key[AREA_LEN];
    struct employee_t **employees;

    uint64_t employee_count;
    uint64_t allocated_employees;

    UT_hash_handle hh;
};

struct salary_info_t {
    struct employee_t **biggest;
    uint64_t biggest_count;
    uint64_t allocated_biggest;

    struct employee_t **lowest;
    uint64_t lowest_count;
    uint64_t allocated_lowest;

    uint64_t employee_count;
    double total;
    double average;
};

struct group_salary_t {
    char key[SURNAME_LEN];

    struct employee_t **employees;
    uint64_t employee_count;
    uint64_t allocated_employees;

    struct salary_info_t salaries;
    UT_hash_handle hh;
};

struct d05_t {
    struct area_t *areas;
    struct employee_t **employees;
    uint64_t employee_count;
    uint64_t area_count;

    struct salary_info_t salaries;
    struct group_salary_t *salary_by_surname;
    struct group_salary_t *salary_by_area;
    struct employee_list_t *employees_by_area;


    struct employee_t *area_with_most_employees;
    uint64_t area_with_most_employees_count;

    uint64_t allocated_employees;
};

/* Prototypes. */
uint64_t read_employees_file(const char *, char **);
void print_employee(const struct employee_t *);
void free_group_salary(struct group_salary_t *);
int init_group_salary(struct group_salary_t *, uint64_t);
void free_employees_list(struct employee_list_t *);
int init_employees_list(struct employee_list_t *, uint64_t);
void update_salaries(struct salary_info_t *, struct employee_t *);
struct group_salary_t *calculate_salaries(struct group_salary_t **, char *, struct employee_t *);
void process_employee(struct d05_t *, struct employee_t *);
void free_salaries(struct salary_info_t *);
int init_salaries(struct salary_info_t *, uint64_t);
struct d05_t *init_d05(uint64_t);
void parse_employee(struct d05_t *, const char *, uint64_t);
struct d05_t *parse_json(const char *, uint64_t);
void print_solution(struct d05_t *);
void free_memory(struct d05_t *);

/* Implementation. */
uint64_t read_employees_file(const char *filename, char **buffer) {
#ifdef _WIN32
    FILE *fp;
    uint64_t len, read;

    if (!(fp = fopen(filename, "rb"))) {
        return 0;
    }

    if (fseek(fp, 0L, SEEK_END) == -1) {
        fprintf(stderr, "%s:%d: error seek'ing file '%s': %s\n", __FILE__, __LINE__, filename, strerror(errno));
        fclose(fp);
        return 0;
    }

    if ((len = ftell(fp)) == -1) {
        fprintf(stderr, "%s:%d: error checking length of file '%s': %s\n", __FILE__, __LINE__, filename, strerror(errno));
        fclose(fp);
        return 0;
    }

    if (fseek(fp, 0L, SEEK_SET) == -1) {
        fprintf(stderr, "%s:%d: error seek'ing file '%s' to start of file: %s\n", __FILE__, __LINE__, filename, strerror(errno));
        fclose(fp);
        return 0;
    }

    if (!(*buffer = (char *) malloc(len))) {
        fprintf(stderr, "%s:%d: error allocating memory for storing file '%s': %s\n", __FILE__, __LINE__, filename, strerror(errno));
        fclose(fp);
        return 0;
    }

    read = fread(*buffer, 1, len, fp);
    if (read != len) {
        fprintf(stderr, "%s:%d: error reading file '%s': read %d bytes; expected: %d\n", __FILE__, __LINE__, filename, read, len);
        free(buffer);
        fclose(fp);
        return 0;
    }
    fclose(fp);
    return len;
#else
    uint64_t size;
    struct stat s;
    int fd = open(filename, O_RDONLY);
    fstat(fd, &s);
    size = s.st_size;

    *buffer = (char *) mmap(0, size, PROT_READ, MAP_SHARED, fd, 0);
    return size;
#endif
}

void print_employee(const struct employee_t *e) {
    if (e == NULL) {
        return;
    }
    printf("--\nName: %s\nSurname: %s\nArea: %s\nSalary: %.2f\n", e->name, e->surname, e->area, e->salary);
}

void free_group_salary(struct group_salary_t *gs) {
    if (gs == NULL) {
        return;
    }
    free(gs->employees);
    free_salaries(&gs->salaries);
    memset(gs, 0, sizeof(struct group_salary_t));
}

int init_group_salary(struct group_salary_t *gs, uint64_t approximate_employees) {
    gs->employees = (struct employee_t **) malloc(approximate_employees * sizeof(struct employee_t *));
    if (gs->employees == NULL) {
        fprintf(stderr, "%s:%d: error allocating employees\n", __FILE__, __LINE__);
        return 0;
    }
    gs->employee_count = 0;
    gs->allocated_employees = approximate_employees;

    if (!init_salaries(&gs->salaries, approximate_employees)) {
        fprintf(stderr, "%s:%d: error initializing salaries in a group salary\n", __FILE__, __LINE__);
        free(gs->employees);
        return 0;
    }
    return 1;
}

void free_employees_list(struct employee_list_t *l) {
    if (l == NULL) {
        return;
    }

    free(l->employees);
    memset(l, 0, sizeof(struct employee_list_t));
}

int init_employees_list(struct employee_list_t *l, uint64_t approximate_employees) {
    l->employees = (struct employee_t **) malloc(approximate_employees * sizeof(struct employee_t *));
    if (l->employees == NULL) {
        fprintf(stderr, "%s:%d: error allocating employees\n", __FILE__, __LINE__);
        return 0;
    }
    l->allocated_employees = approximate_employees;
    l->employee_count = 0;

    return 1;
}

void update_salaries(struct salary_info_t *s, struct employee_t *e) {
    // Biggest salaries.
    if (s->biggest_count == 0 || ((e->salary - s->biggest[0]->salary) > EPSILON)) {
        s->biggest_count = 1;
        s->biggest[0] = e;
    } else if (fabs(e->salary - s->biggest[0]->salary) < EPSILON) {
        if (s->biggest_count == s->allocated_biggest) {
            s->allocated_biggest *= 2;
            // WARNING: don't do this at home; use a separate variable to receive the return of realloc, not to lose data if it fails.
            s->biggest = (struct employee_t **) realloc(s->biggest, s->allocated_biggest * sizeof(struct employee_t *));
        }
        s->biggest[s->biggest_count++] = e;
    }
    // Lowest salaries.
    if (s->lowest_count == 0 || (e->salary - s->lowest[0]->salary) < -EPSILON) {
        s->lowest_count = 1;
        s->lowest[0] = e;
    } else if (fabs(e->salary - s->lowest[0]->salary) < EPSILON) {
        if (s->lowest_count == s->allocated_lowest) {
            s->allocated_lowest *= 2;
            // WARNING: don't do this at home; use a separate variable to receive the return of realloc, not to lose data if it fails.
            s->lowest = (struct employee_t **) realloc(s->lowest, s->allocated_lowest * sizeof(struct employee_t *));
        }
        s->lowest[s->lowest_count++] = e;
    }
    s->employee_count++;
    s->total += e->salary;
    s->average = s->total / s->employee_count;
}

struct group_salary_t *calculate_salaries(struct group_salary_t **s, char *key, struct employee_t *e) {
    struct group_salary_t *gs;
    HASH_FIND_STR(*s, key, gs);
    if (gs == NULL) {
        gs = (struct group_salary_t *) malloc(sizeof(struct group_salary_t));
        if (gs == NULL) {
            fprintf(stderr, "%s:%d: error allocating group salary\n", __FILE__, __LINE__);
            return NULL;
        }

        if (!init_group_salary(gs, 1)) {
            free(gs);
            return NULL;
        }
        strncpy(gs->key, key, sizeof(gs->key));
        gs->key[sizeof(gs->key) - 1] = '\0';
        HASH_ADD_KEYPTR(hh, *s, gs->key, strlen(gs->key), gs);
    }

    update_salaries(&gs->salaries, e);
    return *s;
}

void process_employee(struct d05_t *d05, struct employee_t *e) {
    if (d05->employee_count == d05->allocated_employees) {
        d05->allocated_employees *= 2;
        // WARNING: don't do this at home; use a separate variable to receive the return of realloc, not to lose data if it fails.
        d05->employees = (struct employee_t **) realloc(d05->employees, d05->allocated_employees * sizeof(struct employee_t *));
    }

    d05->employees[d05->employee_count++] = e;
    // char *area_code = e->area;

    char surname[64];
    memcpy(surname, e->surname, sizeof(surname));
    surname[sizeof(surname) - 1] = '\0';

    // We first update general salary information.
    update_salaries(&d05->salaries, e);

    // Then salaries by surname.
    calculate_salaries(&d05->salary_by_surname, surname, e);
    // And salaries by area.
    calculate_salaries(&d05->salary_by_area, e->area, e);

    // Now we update info on employees by area.
    struct employee_list_t *list;
    HASH_FIND_STR(d05->employees_by_area, e->area, list);
    if (list == NULL) {
        list = (struct employee_list_t *) malloc(sizeof(struct employee_list_t));
        if (!init_employees_list(list, 1)) {
            fprintf(stderr, "%s:%d: cannot initialize employees list\n", __FILE__, __LINE__);
            return;
        }
        memcpy(list->key, e->area, sizeof(list->key));
        list->key[sizeof(list->key) - 1] = '\0';
        HASH_ADD_KEYPTR(hh, d05->employees_by_area, list->key, strlen(list->key), list);
    }

    if (list->employee_count == list->allocated_employees) {
        list->allocated_employees *= 2;
        // WARNING: don't do this at home; use a separate variable to receive the return of realloc, not to lose data if it fails.
        list->employees = (struct employee_t **) realloc(list->employees, list->allocated_employees * sizeof(struct employee_t *));
    }
    list->employees[list->employee_count++] = e;

    e->count_in_area = list->employee_count;

    struct employee_t *ee;
    HASH_FIND_STR(d05->area_with_most_employees, e->area, ee);
    if (!ee) {
        HASH_ADD_KEYPTR(hh, d05->area_with_most_employees, e->area, strlen(e->area), e);
    } else {
        ee->count_in_area = list->employee_count;
    }

    if (d05->area_with_most_employees_count == 0 || list->employee_count > d05->area_with_most_employees_count) {
        d05->area_with_most_employees_count = list->employee_count;
    }
}

void free_salaries(struct salary_info_t *s) {
    free(s->biggest);
    free(s->lowest);
    memset(s, 0, sizeof(struct salary_info_t));
}

int init_salaries(struct salary_info_t *s, uint64_t approximate_employees) {
    if (s == NULL) {
        return 0;
    }
    memset(s, 0, sizeof(struct salary_info_t));

    s->biggest = (struct employee_t **) malloc(approximate_employees * sizeof(struct employee_t *));
    if (s->biggest == NULL) {
        fprintf(stderr, "%s:%d: error allocating biggest salary info\n", __FILE__, __LINE__);
        return 0;
    }
    s->allocated_biggest = approximate_employees;
    s->biggest_count = 0;

    s->lowest = (struct employee_t **) malloc(approximate_employees * sizeof(struct employee_t *));
    if (s->lowest == NULL) {
        fprintf(stderr, "%s:%d: error allocating lowest salary info\n", __FILE__, __LINE__);
        free(s->biggest);
        return 0;
    }
    s->allocated_lowest = approximate_employees;
    s->lowest_count = 0;

    s->total = 0.0;
    s->average = 0.0;
    s->employee_count = 0;

    return 1;
}

struct d05_t *init_d05(uint64_t approximate_employees) {
    struct d05_t *ret = (struct d05_t *) malloc(sizeof(struct d05_t));
    memset(ret, 0, sizeof(struct d05_t));

    ret->employees = (struct employee_t **) malloc(approximate_employees * sizeof(struct employee_t *));
    if (ret->employees == NULL) {
        fprintf(stderr, "%s:%d: error allocating employees info (approximate employees: %lu)\n", __FILE__, __LINE__, approximate_employees);
        return NULL;
    }
    ret->allocated_employees = approximate_employees;
    ret->employee_count = 0;

    if (!init_salaries(&ret->salaries, approximate_employees)) {
        fprintf(stderr, "%s:%d: error initializing salary info\n", __FILE__, __LINE__);
        free(ret->employees);
        return NULL;
    }

    return ret;
}

void parse_employee(struct d05_t *d, const char *data, uint64_t len) {
    struct employee_t *e = (struct employee_t *) malloc(sizeof(struct employee_t));
    int quote = -1, previous_quote = 0, total_quotes = 0;
    char c;
    char buffer[16];
    for (uint64_t i = 0; i < len; i++) {
        c = data[i];
        if (c == '"') {
            total_quotes++;
            previous_quote = quote;
            quote = i;
            // {"id":1,"nome":"Aahron","sobrenome":"Abaine","salario":68379.29,"area":"PI"}.
            switch (total_quotes) {
            case 6:            // Name.
                memcpy(e->name, data + previous_quote + 1, quote - previous_quote - 1);
                e->name[quote - previous_quote - 1] = '\0';
                //          printf("name: [%s]\n", e->name);
                break;
            case 10:           // Surname.
                memcpy(e->surname, data + previous_quote + 1, quote - previous_quote - 1);
                e->surname[quote - previous_quote - 1] = '\0';
                //        printf("surname: [%s]\n", e->name);
                break;
            case 13:           // Salary.
                memcpy(buffer, data + previous_quote + 2, quote - previous_quote - 3);
                buffer[quote - previous_quote - 3] = '\0';
                e->salary = atof(buffer);
                //      printf("salary: [%s]\n", buffer);

                break;
            case 16:           // Area.
                memcpy(e->area, data + previous_quote + 1, quote - previous_quote - 1);
                e->area[quote - previous_quote - 1] = '\0';
                //    printf("area: [%s]\n", e->area);
                return process_employee(d, e);
            }
        }
    }
}

void parse_area(struct d05_t *d, const char *data, uint64_t len) {
    struct area_t *a = (struct area_t *) malloc(sizeof(struct area_t));
    int quote = -1, previous_quote = 0, total_quotes = 0;
    char c;
    for (uint64_t i = 0; i < len; i++) {
        c = data[i];
        if (c == '"') {
            total_quotes++;
            previous_quote = quote;
            quote = i;
            // {"codigo":"SM", "nome":"Gerenciamento de Software"}.
            switch (total_quotes) {
            case 4:            // Name.
                memcpy(a->code, data + previous_quote + 1, quote - previous_quote - 1);
                a->code[quote - previous_quote - 1] = '\0';
                break;
            case 8:            // Surname.
                memcpy(a->name, data + previous_quote + 1, quote - previous_quote - 1);
                a->name[quote - previous_quote - 1] = '\0';
                HASH_ADD_KEYPTR(hh, d->areas, a->code, strlen(a->code), a);
                break;
            }
        }
    }
}

struct d05_t *parse_json(const char *json, uint64_t len) {
    uint64_t approximate_employees = len / sizeof(struct employee_t);
    struct d05_t *ret = init_d05(approximate_employees);

    void (*parse) (struct d05_t *, const char *, uint64_t) = parse_employee;

    char *p = (char *) json;
    char *start = NULL;
    char c;
    while ((c = *p++)) {
        switch (c) {
        case '{':
            start = p - 1;
            break;
        case '}':
            if (start) {
                parse(ret, start, p - start);
                start = NULL;
            }
            break;
        case ']':
            // *NOW* we are done.
            if (parse == parse_area) {
                return ret;
            }
            parse = parse_area;
            break;

        }
    }
    return NULL;
}

void print_solution(struct d05_t *d05) {
    uint64_t i;
    for (i = 0; i < d05->salaries.biggest_count; i++) {
        printf("global_max|%s %s|%.2f\n", d05->salaries.biggest[i]->name, d05->salaries.biggest[i]->surname, d05->salaries.biggest[i]->salary);
    }

    for (i = 0; i < d05->salaries.lowest_count; i++) {
        printf("global_min|%s %s|%.2f\n", d05->salaries.lowest[i]->name, d05->salaries.lowest[i]->surname, d05->salaries.lowest[i]->salary);
    }
    printf("global_avg|%.2f\n", d05->salaries.average);



    struct area_t *area;
    struct group_salary_t *by_area;
    for (by_area = d05->salary_by_area; by_area; by_area = by_area->hh.next) {
        HASH_FIND_STR(d05->areas, by_area->key, area);
        for (i = 0; i < by_area->salaries.biggest_count; i++) {
            printf("area_max|%s|%s %s|%.2f\n", area->name, by_area->salaries.biggest[i]->name, by_area->salaries.biggest[i]->surname, by_area->salaries.biggest[i]->salary);
        }
        for (i = 0; i < by_area->salaries.lowest_count; i++) {
            printf("area_min|%s|%s %s|%.2f\n", area->name, by_area->salaries.lowest[i]->name, by_area->salaries.lowest[i]->surname, by_area->salaries.lowest[i]->salary);
        }
        printf("area_avg|%s|%.2f\n", area->name, by_area->salaries.average);
    }

    struct employee_t *e;
    uint64_t less_employees = d05->area_with_most_employees_count;
    for (e = d05->area_with_most_employees; e; e = e->hh.next) {
        if (e->count_in_area == d05->area_with_most_employees_count) {
            HASH_FIND_STR(d05->areas, e->area, area);
            printf("most_employees|%s|%lu\n", area->name, d05->area_with_most_employees_count);
        }
        if (e->count_in_area < less_employees) {
            less_employees = e->count_in_area;
        }
    }

    for (e = d05->area_with_most_employees; e; e = e->hh.next) {
        if (e->count_in_area != less_employees) {
            continue;
        }
        HASH_FIND_STR(d05->areas, e->area, area);
        printf("least_employees|%s|%lu\n", area->name, less_employees);
    }


    struct group_salary_t *by_surname;
    for (by_surname = d05->salary_by_surname; by_surname; by_surname = by_surname->hh.next) {
        if (by_surname->salaries.employee_count > 1) {
            for (i = 0; i < by_surname->salaries.biggest_count; i++) {
                printf("last_name_max|%s|%s %s|%.2f\n", by_surname->key, by_surname->salaries.biggest[i]->name, by_surname->salaries.biggest[i]->surname, by_surname->salaries.biggest[i]->salary);
            }
        }
    }
}

void free_memory(struct d05_t *d05) {
    if (d05 == NULL) {
        return;
    }

    struct employee_list_t *cur_list, *tmp_list;
    if (d05->employees_by_area != NULL) {
        HASH_ITER(hh, d05->employees_by_area, cur_list, tmp_list) {
            HASH_DEL(d05->employees_by_area, cur_list);
            free_employees_list(cur_list);
            free(cur_list);
        }
    }


    struct group_salary_t *cur_group, *tmp_group;
    struct group_salary_t *do_delete[] = { d05->salary_by_surname, d05->salary_by_area, NULL };
    for (int i = 0; do_delete[i]; i++) {
        HASH_ITER(hh, do_delete[i], cur_group, tmp_group) {
            HASH_DEL(do_delete[i], cur_group);
            free_group_salary(cur_group);
            free(cur_group);
        }
    }

    for (uint64_t i = 0; i < d05->employee_count; i++) {
        free(d05->employees[i]);
    }
    free(d05->employees);
    free_salaries(&d05->salaries);
}

int main(int argc, char *argv[]) {
    char *json = NULL;
    uint64_t len;

    if (argc == 1) {
        fprintf(stderr, "Usage: %s <input file>\n", argv[0]);
        return 1;
    }

    if ((len = read_employees_file(argv[1], &json)) == 0) {
        fprintf(stderr, "error trying to read file '%s'\n", argv[1]);
        return 1;
    }

    struct d05_t *d = parse_json(json, len);
    print_solution(d);
    return 0;

    // Freeing memory. Do this in real-world programs.
    free_memory(d);
    free(d);
#ifdef _WIN32
    free(json);
#else
    munmap(json, len);
#endif

    return 0;
}
