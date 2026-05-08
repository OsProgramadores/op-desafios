#include <stdio.h>

int main() {

    int inicio = 1;
    int fim = 200;

    for (int i = inicio; i <= fim; i++) {

        int original = i;
        int reverso = 0;
        int temporario = i;

        while (temporario > 0) {

            int digito = temporario % 10;

            reverso = reverso * 10 + digito;

            temporario = temporario / 10;
        }

        if (original == reverso) {

            printf("%d\n", original);
        }
    }

    return 0;
}
