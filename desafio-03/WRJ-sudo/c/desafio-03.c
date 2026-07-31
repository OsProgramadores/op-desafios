#include <stdio.h>
#include <stdlib.h>

#define TAMANHO 20 //tamanho máximo de caracteres mais o '\0'

int main() {
   const long long int num_inicial, limite;
    long long int contador;
    char str_lida[TAMANHO] = {0};
    char str_a_acomparar[TAMANHO];
    int pos_escape;

    // pega os valores da entrada
    scanf("%lld", &num_inicial);
    scanf("%lld", &limite);

    contador = num_inicial;

    for (contador; contador <= limite; contador++) {

        //pega o numero atual em contador e coloca na string
        sprintf(str_lida, "%lld", contador);
        pos_escape = 0;

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
                    //pula o comando de escape para nao comprometer a execução
                    continue;
                } else {
                    str_a_acomparar[aux] = str_lida[i];
                }
                pos_escape++;
                // colocando um fim de curso na string atual
                str_a_acomparar[pos_escape] = '\0';
            }
        }

        //casting para inteiro long long
        long long a = atoll(str_lida);
        long long b = atoll(str_a_acomparar);
        // imprime se for palindromo
        if (a == b) {
            printf("%s\n", str_lida);
        }
    }
}