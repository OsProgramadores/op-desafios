#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    //Utilizei os exemplos que estavam no site.

    //Primeiro tabuleiro
    int peao,bispo,cavalo,torre,rainha,rei;
    int tabuleiro_1[64] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};

    printf("=============================\n");
    printf("\tTABULEIRO 1\n");
    printf("=============================\n\n");

    peao = bispo = cavalo = torre = rainha = rei = 0;

    for(int i = 0; i < 8; i++)
    {
        for(int j = i*8; j < (i*8)+8;j++)
        {
            printf("%i ",tabuleiro_1[j]);
            peao = tabuleiro_1[j] == 1 ? peao += 1 : peao;
            bispo = tabuleiro_1[j] == 2 ? bispo += 1 : bispo;
            cavalo = tabuleiro_1[j] == 3 ? cavalo += 1 : cavalo;//Como nao pode usar o if, utilizei operadores ternarios para armazenar as pecas.
            torre = tabuleiro_1[j] == 4 ? torre += 1 : torre;
            rainha = tabuleiro_1[j] == 5 ? rainha += 1 : rainha;
            rei = tabuleiro_1[j] == 6 ? rei += 1 : rei;
         }
        printf("\n");
    }

    printf("\nPeao: %i peca(s)",peao);
    printf("\nBispo: %i peca(s)",bispo);
    printf("\nCavalo: %i peca(s)",cavalo);
    printf("\nTorre: %i peca(s)",torre);
    printf("\nRainha: %i peca(s)",rainha);
    printf("\nRei: %i peca(s)\n",rei);


    printf("\n\n\n");
    printf("=============================\n");
    printf("\tTABULEIRO 2\n");
    printf("=============================\n\n");

    //Segundo tabuleiro
    int tabuleiro_2[64] = {4,3,2,5,6,2,3,4,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,4,3,2,5,6,2,3,4};

    peao = bispo = cavalo = torre = rainha = rei = 0;

    for(int i = 0; i < 8; i++)
    {
        for(int j = i*8; j < (i*8)+8;j++)
        {
            printf("%i ",tabuleiro_2[j]);
            peao = tabuleiro_2[j] == 1 ? peao += 1 : peao;
            bispo = tabuleiro_2[j] == 2 ? bispo += 1 : bispo;
            cavalo = tabuleiro_2[j] == 3 ? cavalo += 1 : cavalo;//Como nao pode usar o if, utilizei operadores ternarios para armazenar as pecas.
            torre = tabuleiro_2[j] == 4 ? torre += 1 : torre;
            rainha = tabuleiro_2[j] == 5 ? rainha += 1 : rainha;
            rei = tabuleiro_2[j] == 6 ? rei += 1 : rei;
         }
        printf("\n");
    }

    printf("\nPeao: %i peca(s)",peao);
    printf("\nBispo: %i peca(s)",bispo);
    printf("\nCavalo: %i peca(s)",cavalo);
    printf("\nTorre: %i peca(s)",torre);
    printf("\nRainha: %i peca(s)",rainha);
    printf("\nRei: %i peca(s)\n",rei);


    return 0;
}
