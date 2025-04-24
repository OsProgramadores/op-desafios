#define _POSIX_C_SOURCE 200809L
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


#define ALPHABET_SIZE 26
#define ANA_BUCKETS 137
#define DIC_BUCKETS 937
#define MAX_EXP_SIZE 50
#define MAX_WORD_LEN 50
#define WORDS_TXT "words.txt"


typedef struct node
{
    struct node *next;

    char **words;
    size_t word_len;
    unsigned int capacity;
    unsigned int count;
    unsigned int word_chars_count[ALPHABET_SIZE];
    char key[MAX_WORD_LEN + 1];
} node;

node *dict[DIC_BUCKETS] = {NULL};
node *anagrams[ANA_BUCKETS] = {NULL};
long long anagrams_count = 0;


void add_word(node *ptr, const char *word);
void backtrack(
    char **solutions, unsigned int depth, 
    node **table, unsigned int buckets,
    unsigned int *token_chars_count, 
    unsigned int token_len
);
void banana(char **solutions, unsigned int depth);
size_t count_chars(unsigned int *word_chars_count, const char *word);
void counting_sort(char *sorted_key, const char *word);
unsigned int create_hash(const char *word, unsigned int buckets);
node *create_node(node **table, unsigned int hash, char *sorted_key);
void debug(node **table, unsigned int buckets, unsigned int min_words_count);
void find_anagrams();
node *get_node(node **table, unsigned int hash, char *sorted_key);
node *get_or_create_node(node **table, unsigned int hash, char *sorted_key);
bool load_file(FILE *input_file, unsigned int *token_chars_count);
node *realloc_words(node *ptr);
const char *tokenize(const char *expression);
bool unload_node(node *ptr);
bool unload_table(node **table, unsigned int buckets);
bool viable_word(unsigned int *token_chars_count, const char *word);


int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("usage: ./%s \"An alphabetic sentence of up to %d characters\"\n", argv[0], MAX_EXP_SIZE);
        
        return 1;
    }
    
    const char *token = tokenize(argv[1]);
    if (token == NULL)
    {
        return 1;
    }
    
    FILE *input_file = fopen(WORDS_TXT, "rb");
    if (input_file == NULL)
    {
        printf("Could not open %s\n", WORDS_TXT);
        
        return 1;
    }

    clock_t start_time = clock();

    unsigned int token_chars_count[ALPHABET_SIZE] = {0};
    for (unsigned int c = 0; token[c] != '\0'; c++)
    {
        token_chars_count[token[c] - 'A']++;
    }

    bool success = load_file(input_file, token_chars_count);
    fclose(input_file);
    if (!success)
    {
        printf("The file %s couldn't be loaded into memory.\n", WORDS_TXT);

        return 1;
    }

    find_anagrams();

    char **solutions = malloc(100 * sizeof(char *));
    if (solutions == NULL)
    {
        printf("FAILED ALLOCATING MEMORY TO SOLUTIONS\n");

        return 1;
    }

    size_t token_len = strlen(token);
    backtrack(solutions, 0, anagrams, ANA_BUCKETS, token_chars_count, token_len);
    free(solutions);
    free((void *) token);
    
    // printf("\nDEBUG DICT:\n");
    // debug(dict, DIC_BUCKETS, 1);
    
    // printf("\nDEBUG ANAGRAMS:\n");
    // debug(anagrams, ANA_BUCKETS, 1);

    unload_table(dict, DIC_BUCKETS);
    unload_table(anagrams, ANA_BUCKETS);

    clock_t end_time = clock();
    double elapsed_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;

    printf("\033[0;30;47m");
    printf(" Execution time: %.2fs | Expression(%zu): \"%s\" | Anagrams: %lli", elapsed_time, strlen(argv[1]), argv[1], anagrams_count);
    printf("\033[0m\n");

    return 0;
}


/**
 * @brief adds a word to the table node
 * @param ptr a (node *) that will receive the word (inside its words array)
 * @param word the const (char *) to be stored
 */
void add_word(node *ptr, const char *word)
{
    if (realloc_words(ptr) == NULL)
    {
        return;
    }

    char *tmp = strdup(word);
    if (tmp == NULL)
    {
        fprintf(stderr, "FAILED ALLOCATING MEMORY TO STORE '%s'\n", word);

        return;
    }

    ptr->words[ptr->count++] = tmp;
}


/**
 * @brief   does the heavy lifting
 * @param   solution a partial array of words that 'worked'
 * @param   depth the recursion level; increases when a word is found, 0 when called in main()
 * @param   table the table to search. I hope you're using 'anagrams' instead of 'dict'
 * @param   buckets the size of the table
 * @param   token_chars_count an (unsigned int *) representing the current token state,
 *          parameterized as an arr[26] with the count of its chars for use in viable_word()
 */
void backtrack(
    char **solutions, 
    unsigned int depth, 
    node **table, 
    unsigned int buckets,
    unsigned int *token_chars_count, 
    unsigned int token_len
)
{
    if (token_len == 0)
    {
        banana(solutions, depth);

        return;
    }
    
    for (unsigned int i = 0; i < buckets; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            for (unsigned int w = 0; w < cursor->count; w++)
            {
                char *word = cursor->words[w];
                
                if (cursor->word_len > token_len) continue;

                if (!viable_word(token_chars_count, cursor->key)) break;
                
                if (depth > 0 && solutions[depth - 1] != NULL && strcmp(solutions[depth - 1], word) >= 0)
                {
                    continue;
                }
                
                for (unsigned int c = 0; c < ALPHABET_SIZE; c++)
                {
                    if (cursor->word_chars_count[c] == 0) continue;

                    token_chars_count[c] -= cursor->word_chars_count[c];
                    token_len -= cursor->word_chars_count[c];
                }

                solutions[depth++] = word;

                backtrack(solutions, depth, table, buckets, token_chars_count, token_len);
    
                for (unsigned int c = 0; c < ALPHABET_SIZE; c++)
                {
                    if (cursor->word_chars_count[c] == 0) continue;

                    token_chars_count[c] += cursor->word_chars_count[c];
                    token_len += cursor->word_chars_count[c];
                }

                depth--;
            }

            cursor = cursor->next;
        }
    }
}


/**
 * @brief Ya!! banana!!!!
 * @param solutions a block of 100 char pointers. used exclusively
 *                      in backtrack() for the final output
 */
void banana(char **solutions, unsigned int depth)
{
    char line[MAX_EXP_SIZE] = "";
    for (unsigned int i = 0; i < depth; i++)
    {
        anagrams_count++;
        strcat(line, solutions[i]);
        strcat(line, " ");
    }
    
    printf("%s\n", line);
}


/**
 * @brief this function allows storing in the struct an array with
 *      the count of each char in a word. it is used both in
 *      load_file(), create_node(), and counting_sort() 
 * @param word_chars_count the array to store the count
 * @param word the word to be measured
 * @return a size_t with the length of the word. the buffer[26]
 *      (unsigned int) also holds its count of each char
 */
size_t count_chars(unsigned int *word_chars_count, const char *word)
{
    size_t i = 0;
    while(word[i] != '\0')
    {
        word_chars_count[word[i++] - 'A']++;
    }

    return i;
}


/**
* @brief Sort the string using counting_sort algorithm
* @param sorted_key the sorted string
* @param word the string to be sorted
*/
void counting_sort(char *sorted_key, const char *word)
{   
    unsigned int word_chars_count[ALPHABET_SIZE] = {0};
    count_chars(word_chars_count, word);

    int k = 0;
    for (int i = 0; i < ALPHABET_SIZE; i++)
    {
        for (unsigned int j = 0; j < word_chars_count[i]; j++)
        {
            sorted_key[k++] = i + 'A';
        }
    }

    sorted_key[k] = '\0';
}


/**
 * @brief Create a hash for the bucket identification.
 * @param word a char *word to be calculated.
 * @param buckets for *dict[], for instance, use magic number DIC_BUCKETS avaiable.
 *                for *anagrams[], use ANA_BUCKETS.
 * @return A unsigned integer for the calculated hash.
 */
unsigned int create_hash(const char *word, unsigned int buckets)
{
    unsigned int hash = 0;
    for (unsigned int i =0; word[i] != '\0'; i++)
    {
        hash = (hash * 31) + (toupper(word[i]));
    }
    
    return hash % buckets;
}


/**
 * @brief   belongs to get_or_create_node(). creates a (node *) and attaches it to
 *          the specified table.
 *          initially, there was only one hash table, but creating a second one
 *          (anagrams) brought performance gains by grouping anagrams into the same node.
 *          backtrack() was happy about it, and I didn’t have to write the code twice
 * @param   table a (node **) used to group words from WORDS_TXT
 * @param   hash a uint number for direct access to the table bucket
 * @param   sorted_key the sorted word (fast-access key)
 *          to be stored in the struct
 * @param   word_len the size_t length of the string to be stored in the struct.
 *          backtrack() smiled at this too
 * @return  the created (node *) or NULL
 */
node *create_node(node **table, unsigned int hash, char *sorted_key)
{
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        fprintf(stderr, "FAEILED ALLOCATING MEMORY TO A NEW NODE\n");

        return NULL;
    }

    /**
     * This will be a default values set for the node.
     * capacity = 4 will be double avery time that it reaches
     * the own limit, to avoid realloc() for every word.
     * This will cost us O(log2n)
     */
    
    strcpy(n->key, sorted_key);

    unsigned int word_chars_count[ALPHABET_SIZE] = {0};
    n->word_len = count_chars(word_chars_count, sorted_key);    
    memcpy(n->word_chars_count, word_chars_count, ALPHABET_SIZE * sizeof(unsigned int));

    n->words = NULL;
    n->capacity = 4;
    n->count = 0;

    n->next = table[hash];
    table[hash] = n;

    return n;
}


/**
 * @brief a little help never hurts
 */
void debug(node **table, unsigned int buckets, unsigned int min_words_count)
{
    unsigned int words_count = 0, nodes_count = 0, empty_buckets = 0, filled_buckets = 0;
    for (unsigned int i = 0; i < buckets; i++)
    {
        node *cursor = table[i];

        if (cursor != NULL) filled_buckets++;

        while (cursor != NULL)
        {
            nodes_count++;

            if (cursor->count >= min_words_count)
            {
                char **word = cursor->words;
                for (unsigned int j = 0; j < cursor->count; j++)
                {
                    if (j > 0) printf("\033[;34m");
                    printf("[DEBUG (%d)] cursor->words[%d]: [\033[1;33m%s\033[0m], key: [\033[1;33m%s\033[0m], @node: \033[1;30;47m 0x%p \033[0m\n", words_count++ + 1, j, word[j], cursor->key, cursor);
                    if (j > 0) printf("\033[0m");
                }
            }

            cursor = cursor->next;
        }
    }

    empty_buckets = buckets - filled_buckets;
    double load_factor = nodes_count / (double) buckets;

    printf("\033[1;30;47m");
    printf("Nodes: %d | Words: %d | Filled buckets: %d | Empty buckets: %d | Load factor: %.2f", nodes_count, words_count, filled_buckets, empty_buckets, load_factor);
    printf("\033[0m");
    printf("\n");
}


/**
 * @brief scans *dict[], finds words that are anagrams and groups them into a
 *        single node inside the (char **) words array. I observed a 50–60%
 *        performance gain here. backtrack() loves candy...
 * @param token the token computed by tokenize()
 */
void find_anagrams()
{
    for (unsigned int i = 0; i < DIC_BUCKETS; i++)
    {
        node *cursor = dict[i];        
        while (cursor != NULL)
        {
            unsigned int hash = create_hash(cursor->key, ANA_BUCKETS);
            
            for (unsigned int j = 0; j < cursor->count; j++)
            {
                char *word = cursor->words[j];

                node *anagram = get_or_create_node(anagrams, hash, cursor->key);                
                add_word(anagram, word);
            }
            
            cursor = cursor->next;
        }
    }
}


/**
 * @brief looks for a (node *) and returns its address
 * @param table the table to be scanned
 * @param hash the (unsigned int) bucket computed by create_hash()
 *               where the word is most likely to be
 * @param sorted_key the sorted word capable of grouping the anagrams
 * @return a (node *) if found, NULL otherwise
 */
node *get_node(node **table, unsigned int hash, char *sorted_key)
{
    node *cursor = table[hash];
    while (cursor != NULL)
    {
        if (strcmp(cursor->key, sorted_key) == 0)
        {
            return cursor;
        }

        cursor = cursor->next;
    }

    return NULL;
}


/**
 * @brief   search for a node by its sorted key in the hash table, or create it if it doesn't exist.
 *          It's just the switch whose choose between get_node() and create_node() accordingly
 * @param   table pointer to the hash table.
 * @param   hash the precomputed hash index where the node should be searched/inserted.
 * @param   sorted_key a alphabetically sorted string used as the node's key.
 * @param   word_len the size_t length for the word
 * @return  a pointer to the found or newly created node, or NULL if memory allocation fails.
 */
node *get_or_create_node(node **table, unsigned int hash, char *sorted_key)
{
    /***
     * Browse an search for the key into the provided hash. If found
     * return the address
     */
    node *ptr = get_node(table, hash, sorted_key);
    if (ptr != NULL)
    {
        return ptr;
    }

    /**
     * If failed in searching, create a new node and deliver his ptr
     */
    return create_node(table, hash, sorted_key);
}


/**
 * @brief   loads WORDS_TXT into the nodes in the hash table
 * @param   input_file FILE pointer returned by fopen()
 * @return  bool
 */
bool load_file(FILE *input_file, unsigned int *token_chars_count)
{
    char word[MAX_WORD_LEN + 2];    
    while (fgets(word, sizeof(word), input_file) != NULL)
    {
        word[strcspn(word, "\r\n")] = '\0';

        if (!viable_word(token_chars_count, word)) continue;
             
        size_t word_len = strlen(word);
        char sorted_key[word_len + 1];
        counting_sort(sorted_key, word);        
        unsigned int hash = create_hash(word, DIC_BUCKETS);        

        node *ptr = get_or_create_node(dict, hash, sorted_key);
        add_word(ptr, word);
    }

    return true;
}


/**
 * @brief helper for the add_word() function to place anagrams into the same array
 * inside the (node *) struct in the (*ptr).words field
 */
node *realloc_words(node *ptr)
{
    if (ptr->words == NULL)
    {
        char **tmp = malloc(sizeof(char *) * ptr->capacity);
        if (tmp == NULL)
        {
            fprintf(stderr, "FAILED ALLOCATING MEMORY TO A NEW WORDS VECTOR\n");

            return NULL;
        }

        ptr->words = tmp;
    }

    else if (ptr->count == ptr->capacity)
    {
        ptr->capacity *= 2;        
        char **tmp = realloc(ptr->words, sizeof(char *) * ptr->capacity);
        if (tmp == NULL)
        {
            fprintf(stderr, "FAILED REALLOCATING MEMORY TO GROW THE VECTOR WORDS CAPACITY\n");

            return NULL;
        }

        ptr->words = tmp;
    }

    return ptr;
}


/**
 * @brief   just cut the user entered spaces and block the execution if a
 *          non-alpha char were found, and loads a const char * into the heap
 * @param   expression the user entered expression in the terminal (in argv[1])
 * @return  a const (char *) with MAX_EXP_SIZE length
 */
const char *tokenize(const char *expression)
{
    size_t len = strlen(expression);
    if (len > MAX_EXP_SIZE)
    {
        printf("Expressions cannot have more than %d chars.\n", MAX_EXP_SIZE);

        return NULL;
    }

    // sizeof(char) is aways 1, yeah, i know...
    char *token = calloc(len + 1, sizeof(char));

    for (unsigned int c = 0, shift = 0; c <= len; c++)
    {
        if (expression[c] == '\0') break;
        
        if (expression[c] == ' ') continue;

        if (!isalpha(expression[c]))
        {
            printf("An invalid non-alpha char was entered.\n");

            return NULL;
        }

        token[shift++] = toupper(expression[c]);
    }

    return token;
}


/**
 * @brief   frees the memory allocated by the nodes. should be used both on
 *          dict and anagrams, iteratively freeing each pointer found along the way.
 *          this is a helper function for unload_table()
 * @param   ptr a (node *) to follow through its (*ptr).next field
 * @return  bool
 */
bool unload_node(node *ptr)
{
    while (ptr != NULL)
    {
        if (ptr->words != NULL)
        {
            for (unsigned int j = 0; j < ptr->count; j++)
            {
                // printf("[child vector] Cleaning vector words[%d] = \"%s\"\n", j, ptr->words[j]);
                free(ptr->words[j]);
            }

            free(ptr->words);
        }

        node *next = ptr->next;
        free(ptr);

        // printf("\t-> node 0x%p successfully cleared.\n", ptr);
        ptr = next;
    }

    return true;
}

/**
 * @brief   interactively calls to unload_table() providing both 
 *          anagrams and dict number of buckets
 * @param   table a (node **) table
 * @param   buckets unsigned int number related to the max table rows
 * @return  bool
 */
bool unload_table(node **table, unsigned int buckets)
{
    for (unsigned int i = 0; i < buckets; i++)
    {
        unload_node(table[i]);
    }

    return true;
}


/**
 * @brief   this function is used both in load_file() and
 *          backtrack(), with the goal of reducing the search space.
 *          unlike the situation in backtrack(), however,
 *          in load_file() the token state is already known. each recursion
 *          in backtrack happens right after a reconfiguration of the token state
 *          (parameterized as (uint)token_chars_count[])
 * 
 * @param   token_chars_count the current state of the token, parameterized
 * @param   word the word to be verified
 * @return  bool
 */
bool viable_word(unsigned int *token_chars_count, const char *word)
{
    unsigned int shift = 0;
    unsigned int endpoint = 0;

    while (word[shift] != '\0')
    {
        unsigned int c = word[shift++] - 'A';

        if (token_chars_count[c] == 0)
        {
            break;
        }
        
        token_chars_count[c]--;
        endpoint++;
    }
    
    for (unsigned int i = 0; i < endpoint; i++)
    {
        unsigned int c = word[i] - 'A';
        token_chars_count[c]++;
    }

    return shift == endpoint;
}