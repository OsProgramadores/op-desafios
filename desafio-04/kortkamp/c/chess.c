#include <stdlib.h>
#include <stdio.h>

int main(){
	int table[8][8] = {
		{4, 3, 2, 5, 6, 2, 3, 4},
		{1, 1, 1, 1, 1, 1, 1, 1},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0},
		{1, 1, 1, 1, 1, 1, 1, 1},
		{4, 3, 2, 5, 6, 2, 3, 4}
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

	for(int i = 0 ; i < 8 ; i++)
		for(int j = 0 ; j < 8 ; j++)
			quantidade[table[j][i]]++;

	for(int i = 1; i <= 6; i++)
		printf("%s: %d peça(s)\n",nome[i],quantidade[i]);
	return(0);
}
