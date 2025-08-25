#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void imprimirPrimosAte10000() {
    int limite = 10000;
    int *eh_primo = (int*) malloc((limite + 1) * sizeof(int));
    
    for (int i = 0; i <= limite; i++) {
        eh_primo[i] = 1;
    }
    eh_primo[0] = 0;
    eh_primo[1] = 0;
    
    for (int i = 2; i * i <= limite; i++) {
        if (eh_primo[i] == 1) {
            for (int j = i * i; j <= limite; j += i) {
                eh_primo[j] = 0;
            }
        }
    }
    
    printf("Numeros primos de 1 a 10000:\n");
    for (int i = 2; i <= limite; i++) {
        if (eh_primo[i] == 1) {
            printf("%d ", i);
        }
    }
    printf("\n");
    
    free(eh_primo);
}

int main() {
    imprimirPrimosAte10000();
    return 0;
}

