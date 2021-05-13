#include <stdio.h>
#include <stdlib.h>

int palindromo_1e2digitos(int x, int y);
int palindromo_3digitos(int x, int y);
int palindromo_4digitos(int x, int y);

int main(void){
    int inicio, final;
    /*O usuario vai digitar o numero de inicio e fim do intervalo para
    detectar os palindromos.*/
    printf("\n\n\t==== D E T E C T O R   D E   P A L I N D R O M O S ====\n\n");
    printf("Abaixo, digite o inicio e fim do intervalo.\n");
    printf("OBS: o fim do intervalo deve ser de no maximo n <= 10000\n\n");
    /*Duas verificacoes com DO para que o usuario nao digite um valor fora do intervalo permitido*/
    do{
        printf("Inicio do intervalo: ");
        scanf("%i",&inicio);
        if(inicio >= 9999)
        {
            printf("\tEsse valor nao e permitido\n");
        }
    }
    while(inicio >= 9999);
    do{
        printf("Fim do intervalo: ");
        scanf("%i",&final);
        if(final >= 10000)
        {
            printf("\tEsse valor nao e permitido\n");
        }
    }
    while(final >= 10000);
    printf("\n\n\t==== P A L I N D R O M O S entre [%i] e [%i] ====\n\n",inicio, final);
    /*Funcoes para verificar os palindromos*/
    palindromo_1e2digitos(inicio, final);
    palindromo_3digitos(inicio, final);
    palindromo_4digitos(inicio, final);
    printf("\n\n");
    return 0;
}
int palindromo_1e2digitos(int x, int y){
    printf("\n");
    int array[100];
    int mod[100];
    int div[100];
    for(int i = 0; i <= 100; i++){
        array[i] = i;
        if(array[i] < 10 && array[i] >= x && array[i] <= y)
        {
            printf("[%i]",array[i]);
        }
        else if (array[i] > 10 && array[i]% 11 == 0 && array[i] >= x && array[i] <= y)
        {
            printf("[%i]",array[i]);
        }
    }
}
int palindromo_3digitos(int x, int y){
    printf("\n");
    int array[1000];
    int mod[1000];
    int div[1000];

    for(int i = 100; i <= 1000; i++){
        array[i] = i;
        mod[i] = array[i]%10;
        div[i] = array[i]/100;
        if (mod[i] == div[i] && array[i] >= x && array[i] <= y)
        {
            printf("[%i]",array[i]);
        }
    }
    printf("\n");
}
int palindromo_4digitos(int x, int y){
    printf("\n");
    int array[10000];
    int mod,div,mod1,mod2,prod = 0;

    for(int i = 1000; i <= 10000; i++){
        array[i] = i;
        mod = array[i]%100;
        div = array[i]/100;

        if (mod < div || (mod%11 == 0 && div%11 == 0)){
            mod1 = mod%10;
            mod2 = mod/10;
            prod = mod1*10 + mod2;
            if(prod == div && array[i] >= x && array[i] <= y)
            {
                printf("[%i]",array[i]);
            }
        }
        if (mod > div && array[i] >= x && array[i] <= y){
            mod1 = mod%10;
            mod2 = mod/10;
            prod = mod1*10 + mod2;
            if(prod == div && array[i] >= x && array[i] <= y)
            {
                printf("[%i]",array[i]);
            }
        }
    }
}
