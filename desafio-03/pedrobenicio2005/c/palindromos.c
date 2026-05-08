#include <stdio.h>

/**
 * Função que verifica se um número é palíndromo invertendo-o matematicamente.
 * Usa unsigned long long para suportar números grandes conforme o desafio.
 */
int eh_palindromo(unsigned long long n) {
    unsigned long long original = n;
    unsigned long long invertido = 0;

    while (n > 0) {
        invertido = (invertido * 10) + (n % 10);
        n /= 10;
    }

    return (original == invertido);
}

int main() {
    unsigned long long inicio, fim;

    // Lê o intervalo de entrada
    if (scanf("%llu %llu", &inicio, &fim) != 2) {
        return 0;
    }

    // Garante que o início seja o menor valor
    if (inicio > fim) {
        unsigned long long temp = inicio;
        inicio = fim;
        fim = temp;
    }

    // Percorre o intervalo e imprime os palíndromos
    for (unsigned long long i = inicio; i <= fim; i++) {
        if (eh_palindromo(i)) {
            printf("%llu\n", i);
        }
    }

    return 0;
}