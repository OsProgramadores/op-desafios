#include <stdio.h>


int main(void) {
    char nome_pecas[][7] = {"", "Peão", "Bispo", "Cavalo", "Torre", "Rainha", "Rei"};
    int qt_pecas[7] = {0};
    int tabuleiro[][8] = {
        {4, 3, 2, 5, 6, 2, 3, 4},
        {1, 1, 1, 1, 1, 1, 1, 1},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0},
        {1, 1, 1, 1, 1, 1, 1, 1},
        {4, 3, 2, 5, 6, 2, 3, 4}
    };

    for (int index_linha = 0; index_linha < 8; index_linha++) {
        for (int index_peca = 0; index_peca < 8; index_peca++) {
            int peca_valor = tabuleiro[index_linha][index_peca];
            qt_pecas[peca_valor]++;
        }
    }

    for (int i = 1; i < 7; i++) {
        printf("%s: %d peça(s)\n", nome_pecas[i], qt_pecas[i]);
    }
}
