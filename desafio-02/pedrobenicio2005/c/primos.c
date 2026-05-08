#include <stdio.h>

int eh_primo(int numero) {
    if (numero <= 1) {
        return 0;
    }
    if (numero == 2) {
        return 1;
    }
    if (numero % 2 == 0) {
        return 0;
    }

    for (int i = 3; i * i <= numero; i += 2) {
        if (numero % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    printf("Numeros primos entre 1 e 10000:\n\n");

    int contador = 0;

    for (int n = 1; n <= 10000; n++) {
        if (eh_primo(n)) {
            printf("%d ", n);
            contador++;

            if (contador % 10 == 0) {
                printf("\n");
            }
        }
    }

    printf("\n\nTotal de numeros primos: %d\n", contador);

    return 0;
}