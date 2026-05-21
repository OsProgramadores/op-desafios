#include <stdio.h>

// Calcula o Máximo Divisor Comum usando o algoritmo de Euclides
unsigned long long mdc(unsigned long long a, unsigned long long b) {
    while (b != 0) {
        unsigned long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

void simplificar_e_imprimir(unsigned long long numerador, unsigned long long denominador) {
    if (denominador == 0) {
        printf("ERR\n");
        return;
    }
    
    unsigned long long parte_inteira = numerador / denominador;
    unsigned long long resto = numerador % denominador;
    
    if (resto == 0) {
        // Divisão exata
        printf("%llu\n", parte_inteira);
    } else {
        // Simplifica a parte fracionária
        unsigned long long divisor = mdc(resto, denominador);
        unsigned long long num_simp = resto / divisor;
        unsigned long long den_simp = denominador / divisor;
        
        if (parte_inteira > 0) {
            printf("%llu %llu/%llu\n", parte_inteira, num_simp, den_simp);
        } else {
            printf("%llu/%llu\n", num_simp, den_simp);
        }
    }
}

int main(void) {
    char linha[256];
    unsigned long long numerador = 0;
    unsigned long long denominador = 0;
    
    while (fgets(linha, sizeof(linha), stdin) != NULL) {
        int lidos = sscanf(linha, "%llu/%llu", &numerador, &denominador);
        
        if (lidos == 1) {
            // Número inteiro (denominador implícito = 1)
            printf("%llu\n", numerador);
        } else if (lidos == 2) {
            // Fração
            simplificar_e_imprimir(numerador, denominador);
        }
    }
    
    return 0;
}