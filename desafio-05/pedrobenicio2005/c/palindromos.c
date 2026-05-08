#include <stdio.h>

/* * Função que inverte o número e verifica se ele é igual ao original.
 * Se o número for 121, ela gera o 121 invertido e compara.
 */
int verificar_palindromo(unsigned long long numero) {
    unsigned long long original = numero;
    unsigned long long invertido = 0;
    unsigned long long digito;

    while (numero > 0) {
        digito = numero % 10;         // Pega o último algarismo
        invertido = (invertido * 10) + digito; // Vai montando o número invertido
        numero = numero / 10;         // Remove o último algarismo do número original
    }

    // Se o invertido for igual ao original, retorna 1 (verdadeiro)
    if (original == invertido) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    unsigned long long inicio, fim;

    // O programa espera dois números (o intervalo)
    // Exemplo de entrada: 1 100
    if (scanf("%llu %llu", &inicio, &fim) != 2) {
        return 0;
    }

    // Ajuste: caso o usuário digite o maior antes do menor
    if (inicio > fim) {
        unsigned long long reserva = inicio;
        inicio = fim;
        fim = reserva;
    }

    // Percorre todos os números do início ao fim
    for (unsigned long long i = inicio; i <= fim; i++) {
        if (verificar_palindromo(i)) {
            printf("%llu\n", i);
        }
    }

    return 0;
}