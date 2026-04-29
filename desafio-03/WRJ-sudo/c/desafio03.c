#include <stdio.h>
#include <stdlib.h>

int main() {
    long long int num_inicial, limite, contador;
    char str_lida[20] = {0};
    char str_a_acomparar[20];
    int aux;

    // pega os valores da entrada
    scanf("%lld", &num_inicial);
    scanf("%lld", &limite);

    contador = num_inicial;

    for (contador; contador <= limite; contador++) {
        sprintf(str_lida, "%lld", contador);
        aux = 0;

        if (contador <= 9) {
            printf("%lld\n", contador);
        } else {
            int i = 0;
            // pegando o tamanho da string
            for (i; str_lida[i] != '\0'; i++) {
            }
            // criando a string invertida e colocando em outro array;
            for (i; i >= 0; i--) {
                if (str_lida[i] == '\0') {
                    continue;
                } else {
                    str_a_acomparar[aux] = str_lida[i];
                }
                aux++;
                // colocando um fim de curso na string atual
                str_a_acomparar[aux] = '\0';
            }
        }

        long long a = atoll(str_lida);
        long long b = atoll(str_a_acomparar);
        // imprime se for palindromo
        if (a == b) {
            printf("%s\n", str_lida);
        }
    }
}