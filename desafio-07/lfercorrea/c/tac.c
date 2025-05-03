#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BLOCK_SIZE 512


typedef struct node
{
    struct node *next;
    struct node *prev;
    int offset;
    char text[BLOCK_SIZE];
} node;


void unload_llist(node *ptr);


int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "usage: %s [file path]\n", argv[0]);

        return 1;
    }

    FILE *input_file = fopen(argv[1], "rb");
    if (input_file == NULL)
    {
        fprintf(stderr, "FAILED OPENING %s\n", argv[1]);

        return 1;
    }

    node *list = NULL;
    int count = 0;

    char line[BLOCK_SIZE];
    while (fgets(line, BLOCK_SIZE, input_file))
    {
        line[strcspn(line, "\r\n")] = '\0';
        if (line[0] == '\0') continue;

        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fprintf(stderr, "FILED ALLOCATING MEMORY\n");
            unload_llist(list);

            return 1;
        }

        strcpy(n->text, line);
        n->offset = count++;

        n->prev = NULL;
        n->next = list;

        if (list != NULL)
        {
            list->prev = n;
        }
        
        list = n;
    }

    /**
     * browse backward
     */
    // node *last = list;
    // while (last != NULL && last->next != NULL)
    // {
    //     last = last->next;
    // }

    // while (last != NULL)
    // {
    //     printf("%s\n", last->text);

    //     last = last->prev;
    // }
    
    /**
     * browse forward
     */
    for (node *n = list; n != NULL; n = n->next)
    {
        printf("%s\n", n->text);
    }
    
    fclose(input_file);
    unload_llist(list);

    return 0;
}


void unload_llist(node *ptr)
{
    while (ptr != NULL)
    {
        node *tmp = ptr->next;
        free(ptr);

        ptr = tmp;
    }
}
