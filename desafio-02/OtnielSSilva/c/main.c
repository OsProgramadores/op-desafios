#include <stdio.h>
// Algoritmo: número primos de 1 - 10000
int main() {
    int min = 0, max = 10000, i, j, primo;

    for (i = min; i <= max; i++) {
        if (i == 0 || i == 1) {
            primo = 0; // excluindo 0 e 1 (não são primos)
        } else {
            primo = 1;
            for (j = 2; j < i; j++) {
                if (i % j == 0) {
                    primo = 0; // excluindo números não primos
                }
            }
        }
        if (primo == 1) {
            printf("%i\n", i); // imprimindo os números primos
        }
    }

    return 0;
}