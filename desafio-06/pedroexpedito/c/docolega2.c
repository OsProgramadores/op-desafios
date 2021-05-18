// consegue solucionar em meio segundo (depende do processador, testei em um AMD Phenom 9650)
// compilar com o make ou gcc -Ofast anagrama.c -o anagrama -lm

#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MINALLOC_WORDS 24853 // se precisar carregar o arquivo inteiro
#define MAX_ANAGRAMA 16      // alocação da solução, desafio pede 16, pelos tipos de variáveis utilizados no programa não ultrapassar 126 sem mudar os tipos

char *anagrama_words[MINALLOC_WORDS]; // variável para guardar o dicionário carregado
int anagrama_words_size = 0;
char *anagramas[MAX_ANAGRAMA + 1]; // variável que guarda temporariamente o anagrama sendo formado
int anagramas_size = 0;
char *anagrama_buffer = NULL; // arquivo carregado e dividido em palavras

void anagrama_free() // libera a memória do arquivo carregado
{
    if (anagrama_buffer)
        free(anagrama_buffer);
}

void anagrama_erro(int i) // tratamento de erros
{
    printf("Foi encontrado um erro, não sendo possível continuar a execução\n");
    if (i == 1)
        printf("ERR: Memória insuficiente para formar os anagramas\n");
    else if (i == 2)
        printf("ERR: Memória insuficiente para carregar o arquivo\n");
    else if (i == 3)
        printf("ERR: Memória insuficiente para carregar o dicionário\n");
    else if (i == 4)
        printf("ERR: Arquivo de Dicionário não encontrado\n");
    anagrama_free();
    exit(1);
}

void anagrama_push() // mostrar o anagrama formado
{
    int i = 0;
    for (; i < (anagramas_size - 1); i++) // vai até a penúltima palavra
        printf("%s ", anagramas[i]);
    printf("%s\n", anagramas[i]); // na última não bota o espaço
    return;
}

char anagrama_comparar(char *s, char *para_testar, int fast) // faz a comparação entre a palavra e a string de letras para saber se pertence ao anagrama
{
    char resp = 0;
    char letras[26];
    if (fast) // verifica se ela pertence ao anagrama
    {
        memcpy(letras, para_testar, sizeof(char) * 26);
        while (*s)
        {
            if (--letras[*s++ - 'A'] < 0)
                return -1;
        }
    }
    else                             // esse "else" poderia tornar essa função insegura, mas estou usando para ganhar velocidade
    {                                // usando o fato que depois de passar pela função ele deixa as variáveis inicializadas
        for (int i = 0; i < 26; i++) // com os dados, posso então verificar se o anagrama está completo
            resp |= letras[i];
    }
    return resp;
}

// faz uma nova array de checagem tirando as letras já existentes no anagrama sendo formado
void anagrama_nteste(char *s, char *letras, char *nletras)
{
    memcpy(nletras, letras, sizeof(char) * 26);
    while (*s)
        nletras[*s++ - 'A']--;
}

// função recursiva que forma os anagramas
int anagrama_formar_r(char *letras, char **dict_in, int dict_in_size)
{
    char nletras[26];
    char **dict = NULL;
    int dict_size = 0, i;

    dict = (char **)malloc(sizeof(char *) * dict_in_size); // redução do dicionário de análise
    if (!dict)
        return -1; // tratamento de erro

    for (i = 0; i < dict_in_size; i++)
    {
        if (anagrama_comparar(dict_in[i], letras, 1) < 0) // se não pertence ao anagrama ele continua
            continue;

        if (anagrama_comparar(dict_in[i], letras, 0) == 0) // se esse anagrama estiver completo ele mostra
        {
            anagramas[anagramas_size++] = dict_in[i];
            anagrama_push();
            anagramas_size--;
        }
        else
        {
            dict[dict_size] = dict_in[i]; // forma um novo dicionário reduzido para análise
            dict_size++;
        }
    }
    for (i = 0; i < (dict_size - 1); i++) // forma anagramas com o dicionário reduzido
    {
        anagramas[anagramas_size++] = dict[i];
        anagrama_nteste(dict[i], letras, nletras);
        if (anagrama_formar_r(nletras, &dict[i + 1], (dict_size - i - 1)) == -1) // reduz ainda mais o dicionário enviado para recursão
        {
            free(dict);
            return -1; // deu erro na alocação de memória-> libera memória e continua o tratamento de erro
        }
        anagramas_size--;
    }
    free(dict);

    return 1;
}

// função de chamada para o recursivo
void anagrama_formar(char *letras, char **dict_in, int dict_in_size)
{
    char nletras[26];

    for (int i = 0; i < dict_in_size; i++)
    {
        if (anagrama_comparar(dict_in[i], letras, 1) < 0)
            continue;

        anagramas[anagramas_size++] = dict_in[i];
        if (anagrama_comparar(dict_in[i], letras, 0) == 0) // se a palavra é um anagrama ele mostra
            anagrama_push();
        else
        {
            anagrama_nteste(dict_in[i], letras, nletras);
            if (anagrama_formar_r(nletras, &dict_in[i + 1], (dict_in_size - i - 1)) == -1) // chama a recursão já reduzindo o dicionário
                anagrama_erro(1);                                                          // <- se deu erro na alocação de memória
        }
        anagramas_size--;
    }

    return;
}

void anagrama(char *palavra)
{
    char *s = palavra;
    char *nova_palavra = NULL;
    FILE *fs = NULL;
    char letras[26] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    size_t palavra_size = 0, size = 0;

    while (*s) // analisa a palavra de entrada pelo tamanho e quantidade de cada letra
        letras[*s++ - 'A']++, palavra_size++;

    fs = fopen("words.txt", "r"); // abre o dicionário
    if (!fs)
        anagrama_erro(4);
    fseek(fs, 0, SEEK_END);
    size = ftell(fs);
    fseek(fs, 0, SEEK_SET);

    anagrama_buffer = (char *)malloc(sizeof(char) * size);
    if (!anagrama_buffer)
        anagrama_erro(2);

    size = fread(anagrama_buffer, 1, size, fs); // carrega na memória
    s = anagrama_buffer;

    while (*s)
    {
        nova_palavra = s; // pega a palavra
        while (*s != '\n')
            s++;
        *s++ = 0;
        size = (s - nova_palavra) - 1; // determina o tamanho da palavra
        if (size == 0)
            continue;
       if (size > palavra_size || anagrama_comparar(nova_palavra, letras, 1) < 0) // se tiver o tamanho menor ou igual ao anagrama e pertencer
            continue;                                                              // ao possível anagrama ele deixa passar e inclui no dicionário
        anagrama_words_size++;

        anagrama_words[anagrama_words_size - 1] = nova_palavra;
    }
    fclose(fs);

    anagrama_formar(letras, anagrama_words, anagrama_words_size); // forma os anagramas

    anagrama_free();

    return;
}

int main(int argc, char **argv)
{
    size_t i = 0;
    char *palavra;

    if (argc < 2)
    {
        printf("Uso: %s <palavra ou \"frase\">\nMáximo de 16 letras\n", argv[0]);
        return 0;
    }

    palavra = argv[1];
    for (char *p = argv[1]; *p; p++) // corta simbolos estranhos e transforma em maiúscula a entrada
    {
        if (*p >= 'a' && *p <= 'z')
            palavra[i++] = *p + ('A' - 'a');
        else if (*p >= 'A' && *p <= 'Z')
            palavra[i++] = *p;
    }
    palavra[i] = 0;
    if (i > MAX_ANAGRAMA) // o limite do problema é de 16 letras, mudando essa macro pode ser definido um novo limite
    {
        printf("Uso: %s <palavra ou \"frase\">\nMáximo de %d letras\n", argv[0], MAX_ANAGRAMA);
        return 0;
    }

    anagrama(palavra);

    return 0;
}
