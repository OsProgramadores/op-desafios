#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void countAndPrintPeaces(int table[]) {
  const char *pieceNames[7] = { "Vazio", "Peão", "Bispo",
    "Cavalo", "Torre", "Rainha", "Rei" };

  int pieceCounts[7] = {};

  for ( int i =0; i < 64; i++ ) {
      ++pieceCounts[table[i]];
  }

  for ( int i = 1; i < 7;i++) {
    printf("%s: %d peça(s)\n", pieceNames[i], pieceCounts[i]);
  }
}
int main(int argc, char **argv) {
  if(! *++argv) {
    fprintf(stderr,"piecesCount <file>\n");
    exit(1);
  }
  FILE *fp;

  fp = fopen(*argv, "r");

  if(fp == NULL) {
    perror("error open file");
    exit(1);
  }


  int table[65];

  char ch = getc(fp);
  int i = 0;

  while(ch != EOF) {
    if(isdigit(ch)) {
      table[i] = ch - '0';
      i++;
    }
    ch = getc(fp);
  }
  table[i] = '\0';

  countAndPrintPeaces(table);

  return 0;
}
