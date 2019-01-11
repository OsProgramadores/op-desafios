#include <stdio.h>
#include <locale.h>
#define T 8

int main() {
    setlocale(LC_ALL, "Portuguese");

    int tabuleiro[T][T];
    int x;
    int y;
    int peao = 0;
    int bispo = 0;
    int cavalo = 0;
    int torre = 0;
    int rainha = 0;
    int rei = 0;

    //preenchendo a matriz com as peças
    for(x = 0; x < T; x++) {
        printf("Digite a(s) peça(s) da linha %d(separada(s) por espaço(s)):", x + 1);
        for(y = 0; y < T; y++) {
            scanf("%d", &tabuleiro[x][y]);
        }
    }

    //verificando e guardando a quantidade de peças com o operaor ternário
    for(x = 0; x < T; x++) {
        for(y = 0; y < T; y++) {
            peao = tabuleiro[x][y] == 1 ? peao += 1:peao;
            bispo = tabuleiro[x][y] == 2 ? bispo += 1:bispo;
            cavalo = tabuleiro[x][y] == 3 ? cavalo += 1:cavalo;
            torre =  tabuleiro[x][y] == 4 ? torre += 1:torre;
            rainha = tabuleiro[x][y] == 5 ? rainha += 1:rainha;
            rei = tabuleiro[x][y] == 6 ? rei += 1:rei;
        }
    }

    printf("\n");

    //Imprimindo a quantidade de cada peça
    printf("Peão: %d peça(s)\n", peao);
    printf("Bispo: %d peça(s)\n", bispo);
    printf("Cavalo: %d peça(s)\n", cavalo);
    printf("Torre: %d peça(s)\n", torre);
    printf("Rainha: %d peça(s)\n", rainha);
    printf("Rei: %d peça(s)\n", rei);
}
