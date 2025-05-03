#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DATAFILE "datafile"
#define BUFFER_SIZE 512
#define FILENAME_LEN 32
#define INIT_TAPE_LEN 128
#define INPUT_LEN 32
#define MAX_INPUTS 10
#define SYMBOL_LEN 10


typedef struct rule
{
    struct rule *next;
    char curr_state[SYMBOL_LEN];
    char curr_symbol;
    char new_symbol;
    char direction;
    char new_state[SYMBOL_LEN];
    char rules_filename[FILENAME_LEN];
} rule;


typedef struct tape
{
    char *symbols;
    unsigned int head;
    unsigned int offset;
    unsigned int length;
    char input[INPUT_LEN];
    char rules_filename[FILENAME_LEN];
} tape;


typedef struct input
{
    char input[INPUT_LEN];
    char rules_filename[FILENAME_LEN];
} input;


unsigned int count_inputs;
input inputs_list[MAX_INPUTS] = {0};
rule *rules_list = NULL;


void compute(void);
void debug(rule *head_list);
bool load_file(const char *file_path);
rule *log_rule(rule *head_list, char *state, char symbol, char new_symbol, char direction, char *new_state, char *rules_filename);
rule *lookup_rule(rule *head_list, char *state, char symbol, char *rules_filename);
void print(tape *ptr);
void realloc_tape(tape *ptr, const char direction);
tape *set_tape(const char *input, const char *rules_filename);
void unload_llist(rule *head_list);


int main(void)
{
    if (!load_file(DATAFILE))
    {
        return 1;
    }
    
    compute();

    unload_llist(rules_list);

    return 0;
}


void compute(void)
{
    tape *current_tape = NULL;
    for (unsigned int i = 0; i < count_inputs; i++)
    {
        input current_input = inputs_list[i];
        current_tape = set_tape(current_input.input, current_input.rules_filename);
        if (current_tape == NULL)
        {
            printf("could not set the tape head for input %s\n", current_input.input);

            return;
        }

        char current_state[SYMBOL_LEN] = "0";
        while (strncmp(current_state, "halt", 4) != 0)
        {
            char current_symbol = current_tape->symbols[current_tape->head];
            current_symbol = (current_symbol == ' ') ? '_' : current_symbol;
            
            rule *current_rule = lookup_rule(rules_list, current_state, current_symbol, current_input.rules_filename);
            if (current_rule == NULL)
            {
                memset(current_tape->symbols, ' ', current_tape->length);
                strcpy(current_tape->symbols, "ERR");

                break;
            }
            
            if (current_rule->new_symbol != '*')
            {
                current_tape->symbols[current_tape->head] = (current_rule->new_symbol == '_') ? ' ' : current_rule->new_symbol;
            }
            
            strcpy(current_state, current_rule->new_state);
            
            if (current_rule->direction == 'r')
            {
                realloc_tape(current_tape, 'r');
                current_tape->head++;
            }
            else if (current_rule->direction == 'l')
            {
                realloc_tape(current_tape, 'l');
                current_tape->head--;
            }
            else if (current_rule->direction != '*')
            {
                strcpy(current_tape->symbols, "ERR");

                break;
            }
        }

        print(current_tape);
        
        free(current_tape->symbols);
        free(current_tape);
    }
}


/**
 * @brief just for help in debugging, actually ununsed
 */
void debug(rule *head_list)
{
    int i = 0;
    for (rule *ptr = head_list; ptr != NULL; ptr = ptr->next)
    {
        ++i;
        printf("#%d, rules_file: %s | state: %s | symbol: %c | new_symbol: %c | direction: %c | new_state: %s\n",
            i, ptr->rules_filename, ptr->curr_state, ptr->curr_symbol, ptr->new_symbol, ptr->direction, ptr->new_state);
    }
}


bool load_file(const char *file_path)
{
    FILE *datafile = fopen(file_path, "rb");
    if (!datafile)
    {
        fprintf(stderr, "FAILED OPENING FILE %s\n", DATAFILE);

        return false;
    }

    char line[BUFFER_SIZE] = {'\0'};
    while (fgets(line, BUFFER_SIZE, datafile))
    {
        if (line[0] == ';') continue;

        if (count_inputs > MAX_INPUTS)
        {
            fprintf(stderr, "MAX_INPUTS REACHED\n");

            return false;
        }

        char *rules_file = strtok(line, ",");
        char *input = strtok(NULL, "\n\r\t");
        if (!rules_file || !input)
        {
            continue;
        }

        strcpy(inputs_list[count_inputs].input, input);
        strcpy(inputs_list[count_inputs].rules_filename, rules_file);
        count_inputs++;

        FILE *rules = fopen(rules_file, "rb");
        if (rules == NULL)
        {
            fprintf(stderr, "FAILED OPENING FILE %s\n", rules_file);

            return false;
        }
        
        char inline_rule[BUFFER_SIZE] = {'\0'};
        while (fgets(inline_rule, BUFFER_SIZE, rules))
        {
            if (inline_rule[0] == ';' || inline_rule[0] == '\n') continue;

            inline_rule[strcspn(inline_rule, "\r\n")] = '\0';
            
            char *token = strtok(inline_rule, ";");
            if (token == NULL)
            {
                continue;
            }

            char tmp[BUFFER_SIZE];
            strcpy(tmp, token);
            
            char *state = strtok(tmp, " ");
            char *symbol = strtok(NULL, " ");
            char *new_symbol = strtok(NULL, " ");
            char *direction = strtok(NULL, " ");
            char *new_state = strtok(NULL, " \n\r");
            
            if (!state || !symbol || !new_symbol || !direction || !new_state)
            {
                continue;
            }

            rules_list = log_rule(rules_list, state, symbol[0], new_symbol[0], direction[0], new_state, rules_file);
        }

        fclose(rules);
    }

    fclose(datafile);

    return true;
}


rule *log_rule(rule *head_list, char *state, char symbol, char new_symbol, char direction, char *new_state, char *rules_filename)
{
    rule *new = malloc(sizeof(rule));
    if (new == NULL)
    {
        fprintf(stderr, "FAILED ALLOCATING MEMORY TO LOG NEW RULE STATE\n");
        unload_llist(rules_list);

        return NULL;
    }

    strcpy(new->curr_state, state);
    new->curr_symbol = symbol;
    new->new_symbol = new_symbol;
    new->direction = direction;
    strcpy(new->new_state, new_state);
    strcpy(new->rules_filename, rules_filename);
    new->next = head_list;

    return new;
}


rule *lookup_rule(rule *head_list, char *state, char symbol, char *rules_filename)
{
    rule *state_wildcard = NULL;
    rule *symbol_wildcard = NULL;
    rule *both_wildcard = NULL;

    if (head_list == NULL)
    {
        fprintf(stderr, "INVALID LIST HEAD\n");

        return NULL;
    }

    for (rule *ptr = head_list; ptr != NULL; ptr = ptr->next)
    {
        if (strcmp(ptr->rules_filename, rules_filename) != 0) continue;

        if (strcmp(ptr->curr_state, state) == 0 && ptr->curr_symbol == symbol) return ptr;

        if (strcmp(ptr->curr_state, "*") == 0 && ptr->curr_symbol == symbol) state_wildcard = ptr;
        if (strcmp(ptr->curr_state, state) == 0 && ptr->curr_symbol == '*') symbol_wildcard = ptr;
        if (strcmp(ptr->curr_state, "*") == 0 && ptr->curr_symbol == '*') both_wildcard = ptr;
    }
    
    return state_wildcard ? state_wildcard : symbol_wildcard ? symbol_wildcard : both_wildcard ? both_wildcard : NULL;
}


void print(tape *ptr)
{
    unsigned int start = 0;
    while (ptr->symbols[start] == ' ') start++;

    unsigned int end = ptr->length - 1;
    while (ptr->symbols[end] == ' ') end--;

    printf("%s,%s,", ptr->rules_filename, ptr->input);
    for (unsigned int i = start; i <= end; i++)
    {
        printf("%c", ptr->symbols[i]);
    }

    printf("\n");
}


void realloc_tape(tape *ptr, const char direction)
{
    unsigned int expanded_length = ptr->length * 2;

    if (direction == 'l')
    {
        if (ptr->head == 0)
        {
            char *symbols = malloc(expanded_length);
            if (symbols == NULL)
            {
                fprintf(stderr, "FAILED TO REALLOCATE LEFT\n");
                unload_llist(rules_list);

                exit(1);
            }

            memset(symbols, ' ', expanded_length);
            memcpy(symbols + ptr->length, ptr->symbols, ptr->length);
            free(ptr->symbols);

            ptr->symbols = symbols;
            ptr->head += ptr->length;
            ptr->offset += ptr->length;
            ptr->length = expanded_length;
        }
    }
    
    else if (direction == 'r')
    {
        if (ptr->head + 1 >= ptr->length)
        {
            unsigned int length = ptr->length;
            char *symbols = realloc(ptr->symbols, expanded_length);
            if (symbols == NULL)
            {
                fprintf(stderr, "FAILED TO REALLOCATE RIGHT\n");
                unload_llist(rules_list);
                
                exit(1);
            }
            
            memset(symbols + length, ' ', expanded_length - length);

            ptr->symbols = symbols;
            ptr->length = expanded_length;
        }
    }
}


tape *set_tape(const char *input, const char *rules_filename)
{
    tape *t = malloc(sizeof(tape));
    if (t == NULL)
    {
        fprintf(stderr, "FAILED ALLOCATING MEMORY FOR TAPE\n");
        unload_llist(rules_list);

        return NULL;
    }
    
    strcpy(t->rules_filename, rules_filename);
    strcpy(t->input, input);
    t->length = INIT_TAPE_LEN;
    t->offset = INIT_TAPE_LEN / 2;
    t->head = t->offset;

    t->symbols = malloc(t->length);
    if (t->symbols == NULL)
    {
        fprintf(stderr, "FAILED ALLOCATING MEMORY FOR TAPE SYMBOLS\n");
        unload_llist(rules_list);

        return NULL;
    }

    memset(t->symbols, ' ', t->length);

    for (unsigned int i = 0; input[i] != '\0'; i++)
    {
        t->symbols[t->head + i] = input[i];
    }

    return t;
}


void unload_llist(rule *head_list)
{
    rule *tmp;
    for (rule *ptr = head_list; ptr != NULL; ptr = tmp)
    {
        tmp = ptr->next;
        free(ptr);
    }
}
