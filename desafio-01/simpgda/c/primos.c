#include <stdio.h>

int main() {
    int i = 0;
    int j = 0;
    int primo = 0;
    
    printf("Numeros primos entre 1 e 10000:\n");
    printf("2\n"); // 2 é o único primo par
    
    // Começa do 3 e pula números pares
    for (i = 3; i <= 10000; i += 2) {
        primo = 1;
        for (j = 3; j * j <= i; j += 2) { // só testa divisores ímpares
            if (i % j == 0) {
                primo = 0;
                break;
            }
        }
        if (primo) {
            printf("%d\n", i);
        }
    }
    return 0;
}