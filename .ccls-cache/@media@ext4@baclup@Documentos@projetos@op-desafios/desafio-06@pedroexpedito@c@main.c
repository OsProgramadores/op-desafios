/* Anagramas
 *
 * Programa recebe uma palavra e verifica quais possibilidades são validas
 *
 * DIFICULDADE:
 *
 * exemplo a palavra vermelho tem
 *
 * https://pt.wikipedia.org/wiki/Anagrama
 *
 *
 * */
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string.h>
#include <ctype.h>

#define WORDS_SIZE_MAX 24853

char wordList[WORDS_SIZE_MAX][15];

char * sort(char string[]){
  int count[256], i;
  char *sr;

  for(i=0; i<256; i++)
    count[i] = 0;

  i=0;
  while(string[i] != '\0'){
    count[(int)string[i]]++;
    i++;
  }

  sr = malloc((i+1)*sizeof(char));

  int j=0, k=0;
  for(i=0; i<256; i++){
    if(count[i]!=0){
      for(k=0; k<count[i]; k++){
 sr[j] = i;
 j++;
      }
    }
  }
  sr[j] = '\0';
  return sr;
}

int is_in_words(char *word) {
  for (int i = 0; i < WORDS_SIZE_MAX; i++) {
    if(strcmp(word, wordList[i]) == 0) {
      puts(word);
    }
  }
}

void generate(char *string_ordenada, int *letra_usada, char *word, int n,
              int k) {

  if (k < n) { // Se há mais letras a ser adicionada (quando k é menor que n):

    for (int i = 0; i < n; i++) // Percorre o vetor booleano de quais letras
                                // foram usadas e quais não
      if (letra_usada[i] == 0) { // Se a letra na posição i não foi usada:

        letra_usada[i] = 1;           // Marque-a como usada,
        word[k] = string_ordenada[i]; // Armazene em word na posição k a letra
                                      // correspondente,
        generate(string_ordenada, letra_usada, word, n,
                 k + 1); // E chame a própria função.

        letra_usada[i] = 0; // Torne a letra atual como não usada,
        for (; string_ordenada[i] == string_ordenada[i + 1]; i++)
          ; // E verifique qual é a próxima letra que seja diferente da atual,
            // avançando a posição i.
      }

  } else { // Caso já todas as letras tenham sido usadas:

    word[n] = '\0';       // Adicione o '\0', indicador de fim da string,
    printf("POSI: %s\n", word); // E imprima a string/palavra/anagrama formado.
    is_in_words(word);
  }
}


int main(int argc, char **argv) {

  if (!*++argv) {
    fprintf(stderr, "./d06 \"palavra\"\n");
    exit(EXIT_FAILURE);
  }
  FILE *fp;

  if((fp = fopen("words.txt", "r")) == NULL){
    perror("erro to open words.txt");
    exit(EXIT_FAILURE);
  }
  // tratar entrada

  char word[17];
  strcpy(word, *argv);

  for(int i = 0; word[i] != '\0'; i++) {
    if(((word[i] > 'z' || word[i] < 'A') || (word[i] > 'Z' && word[i] < 'a')) && word[i] != ' ') {
      fprintf(stderr, "invalid char\n");
      exit(EXIT_FAILURE);
    }
    word[i] = toupper(word[i]);
  }
  /* puts(word); */

  char bufferWorld[17];

  for ( int i = 0; i < WORDS_SIZE_MAX ; i++) {
    fscanf(fp,"%s\n", bufferWorld);
    strcpy(wordList[i], bufferWorld);
  }

  fclose(fp);

  char *string_ordenada =  sort(word);

  int n  = strlen(string_ordenada);

  int *letra_usada = malloc(n*sizeof(int));

  char *anagrama = malloc((n+1)*sizeof(char));

  for(int i=0; i<n; i++)
    letra_usada[i]=0;

  generate(string_ordenada, letra_usada, anagrama, n, 0);

  free(anagrama);
  free(string_ordenada);
  free(letra_usada);

  return 0;
}
