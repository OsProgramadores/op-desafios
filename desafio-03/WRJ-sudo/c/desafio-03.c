#include <stdio.h>
#include <stdlib.h>

#define TAMANHO 20 //tamanho máximo de caracteres mais o '\0'

long long int inicial;
long long int final;

int programa();
int primeiro_num();
int segundo_num();

int main() {

    int excecao;


        printf("Para continuar com a busca de palindromos: Digite 1\n");
        printf("\n");
        printf("Para encerrar o programa: Digite 0\n");
        printf("\n");
        scanf("%d",&excecao);

            switch(excecao){
            case 0: return 0;
            case 1: programa();
                    break;
            default: return 0;

            }

        return 0;

}

int programa(){
    int  temp_exe=1;
    long long int contador;
    char str_lida[TAMANHO] = {0};
    char str_a_acomparar[TAMANHO];
    int aux;

    while(temp_exe){

        if(primeiro_num()){
            temp_exe = 0;
        }else{
            return 0;
        }

    }
    const long long int num_inicial = inicial ;
    temp_exe = 1;
    while(temp_exe){

        if(segundo_num()){
            temp_exe = 0;
        }else{
            return 0;
        }

    }
    const long long int limite = final;
    contador = num_inicial;

    for (contador; contador <= limite; contador++) {

        //pega o numero atual em contador e coloca na string
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
                    //pula o comando de escape para nao comprometer a execução
                    continue;
                } else {
                    str_a_acomparar[aux] = str_lida[i];
                }
                aux++;
                // colocando um fim de curso na string atual
                str_a_acomparar[aux] = '\0';
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

int primeiro_num(){

    long long numero;
    printf("Digite um numero inicial para a busca: ");

    if (scanf("%lld", &numero) == 1) {
        inicial = numero;
        return 1;
    }else {
        printf("Entrada invalida!\n");
        return 0;
    }

}

int segundo_num(){

    long long numero;

    printf("Digite um numero para o limite da busca: ");

    if (scanf("%lld", &numero) == 1) {
        final = numero;
        return 1;
    }else {
        printf("Entrada invalida!\n");
        return 0;
    }

}
