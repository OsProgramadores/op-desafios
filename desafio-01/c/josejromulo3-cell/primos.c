#include <stdio.h>

int main() {
    int i, j, primo;
    FILE *arquivo;

    arquivo = fopen("primos.txt", "w");

    if (arquivo == NULL) {
        printf("Erro ao criar o arquivo.\n");
        return 1;
    }

    for (i = 2; i <= 10000; i++) {
        primo = 1;

        for (j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                primo = 0;
                break;
            }
        }

        if (primo) {
            fprintf(arquivo, "%d\n", i);
        }
    }

    fclose(arquivo);

    printf("Números primos salvos em primos.txt\n");

    return 0;
}
