#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

// O programa deve ler arquivos de qualquer tamanho e funcionar com um limite de
// 512MB de memória (ler o arquivo inteiro em memória não é uma alternativa
// viável).
// compile: gcc -Wall -O2 -Wextra tac.c -g -o tac

#define MAX_BUFFER_SIZE 2097152 // cerca 2mb

void reversePrint(char *sentence) {
  long long i = 0;

  while (sentence[i] != '\0') {
    i++;
  }

  if ((i > 0) && sentence[i - 1] == '\n') {
    i -= 2;
    for (; i >= 0; i--) {
      if (sentence[i] != 0) {
        putchar(sentence[i]);
      }
    }
    puts("");
  } else {
    for (; i >= 0; i--) {
      if (sentence[i] != 0) {
        putchar(sentence[i]);
      }
    }
    puts("");
  }
}
int main(int argc, char **argv) {

  FILE *file;

  if (!*++argv) {
    fputs("Usage: tac <file>\n", stderr);
    exit(EXIT_FAILURE);
  }

  // rb ?? Sim com r para ler stream de texto o
  // ftell retorna UB

  if ((file = fopen(*argv, "rb")) == NULL) {
    perror("error openig file");
    exit(EXIT_FAILURE);
  }

  fseek(file, 0, SEEK_END);

  long size;

  size = ftell(file);

  char bufferLine[MAX_BUFFER_SIZE];

  long j = 0;

  int fseekRet;
  for (size -= 2; size >= 0; size--) {

    fseekRet = fseek(file, size, SEEK_SET);

    if (fseekRet != 0) {
      printf("%d\n", errno);
      exit(fseekRet);
    }

    if (ferror(file)) {
      perror("seek error");
      exit(EXIT_FAILURE);
    }

    bufferLine[j] = getc(file);

    if ((bufferLine[j] == '\n') || size == 0) {

      bufferLine[j + 1] = '\0';
      reversePrint(bufferLine);
      j = -1;
    }
    j++;
  }

  fclose(file);
  return 0;
}
