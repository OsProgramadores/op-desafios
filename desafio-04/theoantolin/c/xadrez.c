#include <stdio.h>
#include <stdlib.h>
#define TAMANHO 8

int main() {

int i, j;
int peao = 0, bispo = 0, cavalo = 0, torre = 0, rainha = 0, rei = 0;
int matriz[TAMANHO][TAMANHO] = {
{4,3,2,5,6,2,3,4},
{1,1,1,1,1,1,1,1},
{0,0,0,0,0,0,0,0},
{0,0,0,0,0,0,0,0},
{0,0,0,0,0,0,0,0},
{0,0,0,0,0,0,0,0},
{1,1,1,1,1,1,1,1},
{4,3,2,5,6,2,3,4}
};

	for (i = 0; i < 8; i++) {
		for(j = 0; j < 8; j++) {
		peao = matriz[i][j] == 1 ? ((peao) + 1) : peao;
		bispo = matriz[i][j] == 2 ? ((bispo) + 1) : bispo;
		cavalo = matriz[i][j] == 3 ? ((cavalo) + 1) : cavalo;
		torre = matriz[i][j] == 4 ? ((torre) + 1) : torre;
		rainha = matriz[i][j] == 5 ? ((rainha) + 1) : rainha;
		rei = matriz[i][j] == 6 ? ((rei) + 1) : rei;
		}
	}
	printf("Peao: %d pecas\n", peao);
	printf("Bispo: %d pecas\n", bispo);
	printf("Cavalo: %d pecas\n", cavalo);
	printf("Torre: %d pecas\n", torre);
	printf("Rainha: %d pecas\n", rainha);
	printf("Rei: %d pecas", rei);
return 0;
}
