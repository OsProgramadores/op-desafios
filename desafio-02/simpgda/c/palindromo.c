#include <stdio.h>

int ehPalindromo(unsigned long long n) {
    unsigned long long original = n;
    unsigned long long invertido = 0;

    while (n > 0) {
        invertido = invertido * 10 + (n % 10);
        n /= 10;
    }

    return original == invertido;
}

int main(void) {
    unsigned long long inicio = 0;
    unsigned long long fim = 0;

    
    if (scanf("%llu %llu", &inicio, &fim) == 2) {
        
        // Garante que o início seja menor que o fim; se não, inverte os valores
        if (inicio > fim) {
            unsigned long long temp = inicio;
            inicio = fim;
            fim = temp;
        }

        // Percorre o intervalo e imprime os palíndromos encontrados
        for (unsigned long long i = inicio; i <= fim; i++) {
            if (ehPalindromo(i)) {
                printf("%llu\n", i); 
            }
        }
    }

    return 0;
}