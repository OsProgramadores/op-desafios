#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAMANHO 21 //tamanho máximo de caracteres mais o'\n' e '\0'

long long int inicial;
long long int final;

void buscar_palindromo();
void limpar_Buffer();
int validador_num();
int get_valor();

int main() {

    int excecao;


        printf("Para continuar com a busca de palindromos: Digite 1\n");
        printf("\n");
        printf("Para encerrar o programa: Digite 0\n");
        printf("\n");
        scanf("%d",&excecao);
        limpar_Buffer();

            switch(excecao){
            case 0: return 0;
            case 1: buscar_palindromo();
                    break;
            default:
                printf("Opcao invalida.\n ");
                return 0;

            }

        return 0;

}

void buscar_palindromo(){
    int  temp_exe=1;
    long long int contador;
    char str_lida[TAMANHO] = {0};
    char str_a_acomparar[TAMANHO];


    while(temp_exe){

        if(validador_num()){
            temp_exe = 0;
        }
    }
    const long long int num_inicial = inicial ;
    temp_exe = 1;
    while(temp_exe){

        if(validador_num()){
            temp_exe = 0;
        }

    }
    const long long int limite = final;
    contador = num_inicial;

    for (contador; contador <= limite; contador++) {

        //pega o numero atual em contador e coloca na string
        sprintf(str_lida, "%lld", contador);
        int aux = 0;

            int tam_input = 0;
            // pegando o tamanho da string
            tam_input = strlen(str_lida);

            // criando a string invertida e colocando em outro array;
            for (int i = tam_input ; i >= 0; i--) {
                if (str_lida[i] == '\0') {
                    //pula o comando de escape para nao comprometer a execução
                    continue;
                } else {
                    str_a_acomparar[aux] = str_lida[i];
                }
                aux++;
                // colocando um fim de curso na string atual
                str_a_acomparar[tam_input] = '\0';
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

void limpar_Buffer(){

    int ch;

    do {
        ch = fgetc(stdin);
    }while(ch != EOF && ch != '\n');
}

int validador_num(){

    static int passada=1;
    int resposta;

    if(passada){
        printf("Digite um numero inicial para a busca: ");
        resposta = get_valor(passada);
        ++passada;
        return resposta;

    }else{
        printf("Digite um numero para o limite da busca: ");
        resposta = get_valor(passada);
        return resposta;
    }

}

int get_valor(int x){

    long long numero;
    char entrada[TAMANHO];

    fgets(entrada,TAMANHO,stdin);

    if (strchr(entrada, '\n') == NULL) {
            limpar_Buffer();
            printf("Entrada invalida: numero muito grande!\n");
            return 0;
    }

    if (sscanf(entrada,"%lld",&numero)) {
        for(int i=0; entrada[i] != '\0'; i++){
            switch(entrada[i]){
                case 48: continue;
                case 49: continue;
                case 50: continue;
                case 51: continue;
                case 52: continue;
                case 53: continue;
                case 54: continue;
                case 55: continue;
                case 56: continue;
                case 57: continue;
                case '\n': continue;
                default:
                printf("Entrada invalida!\n");
                return 0;
            }

        }
        numero = atoll(entrada);

        if(x==1){
            inicial = numero;
        }else{
            final =numero;
        }

        return 1;
    }else {
        printf("Entrada invalida!\n");
        return 0;
    }


}