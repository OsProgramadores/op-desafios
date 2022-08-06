#include <stdio.h>
#include <stdlib.h>


/* Desafio 2 osProgramadores 
descrição: Escreva um programa para listar todos os números primos entre 1 e 10000 */


int ehPrimo(int x){
    int i, divisores = 0;

    for(i = 1; i <= x; i++){
        if(x % i == 0)
            divisores++;
    }

    if(divisores == 2)
        return 1;// é primo
    else
        return 0; // não é primo
}

int main(){
    int i;

    for(i = 1; i <= 10000; i++){
        if(ehPrimo(i) == 1) // se for primo
            printf("%d, ", i); // imprime na tela
    }
    return 0;
}