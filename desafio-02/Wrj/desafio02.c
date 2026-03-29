#include <stdio.h>

int main(){

    for(int i = 2; i <= 10000; i++){

        int cont = 1;

        for(int j = 2; j <= i; j++){
            if((i % j) == 0){
                cont++;
            }
            if(cont > 2){
                break;
            }
        }
        if(cont == 2){
            printf("%d\n", i);
        }

    }

}
