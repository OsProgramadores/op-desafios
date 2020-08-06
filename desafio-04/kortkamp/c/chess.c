#include <stdlib.h>
#include <stdio.h>

/* Example of input_file.
43256234
11111111
00000000
00000000
00000000
00000000
11111111
43256234
*/

int main(int argc, char *argv[]){
	// Declaration of vars.
	FILE *fp;
	// Initialization of table is not necessary,
	// it's here just for comprehension of input file format.
	char table[8][9] = {
		// The 9th column is the CR in input file.
		{4, 3, 2, 5, 6, 2, 3, 4, '\n'},
		{1, 1, 1, 1, 1, 1, 1, 1, '\n'},
		{0, 0, 0, 0, 0, 0, 0, 0, '\n'},
		{0, 0, 0, 0, 0, 0, 0, 0, '\n'},
		{0, 0, 0, 0, 0, 0, 0, 0, '\n'},
		{0, 0, 0, 0, 0, 0, 0, 0, '\n'},
		{1, 1, 1, 1, 1, 1, 1, 1, '\n'},
		{4, 3, 2, 5, 6, 2, 3, 4, '\n'}
	};
	char nome[7][7]= {
		"Vazio", // não usado
		"Peão",
		"Bispo",
		"Cavalo",
		"Torre",
		"Rainha",
		"Rei"
	};
	int quantidade[7] = {0};

	// Treat the input.
	if(argc != 2){
		fprintf(stderr, "Usage: %s input_file\n",argv[0]);
		return(-1);
	}
	fp = fopen(argv[1],"r");
	if(fp == NULL){
		perror("Erro abrindo arquivo");
		return(-1);
	}
	fread(table,72,1,fp);

	// The real code.
	for(int i = 0 ; i < 8 ; i++)
		for(int j = 0 ; j < 8 ; j++)
			quantidade[table[j][i]-'0']++;
	for(int i = 1; i <= 6; i++)
		printf("%s: %d peça(s)\n",nome[i],quantidade[i]);
	
	// Goodbye.
	return(0);
}
