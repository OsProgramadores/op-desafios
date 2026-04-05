#include <stdio.h>

int main() {

    int num_primos[10001];

     num_primos[0] = 0;
     num_primos[1] = 0;
    //assume todos os numeros como primo
    for(int i = 2; i<=10000;i++){
        num_primos[i] = 1;

    }
    //verifica se os numeros a partir do 2 sao primos
    for (int i = 2; i <= 10000; i++) {
        int prox_numero;

        if(num_primos[i] == 1){

            for (prox_numero=i*i; prox_numero <= 10000; prox_numero++) {
                if(prox_numero%i==0){
                num_primos[prox_numero] = 0;


                }

            }
        }
    }
    //imprime todos os numeros primos
    for(int i = 0; i<=10000;i++){

        if(num_primos[i] == 1){
            printf("%d\n", i );
        }
    }

    return 0;


}
