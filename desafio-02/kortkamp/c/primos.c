/*
 * Solucao em C para o desafio 2 do grupo Os Programadores
 * por Marcelo Kortkamp
 */


#include <stdio.h>
#include <stdlib.h>
#include <math.h>


#define LIMIT 100000

//return 1 if the number is prime, otherwise returns 0
int primo(int n){
    for(int i = sqrt(n); i > 1;i--){// SQRT to test less
        if((n % i) == 0) return(0);
    }
    return(1);
}

int main(){
    for(int i = 2; i < LIMIT; i++)
        if(primo(i))
            printf("%d\n",i);
    return(0);
}
