#include <iostream>

int main(){

    //Mostrar numeros primos
    std::cout << "Numeros primos" << std::endl;

    for(auto i = 1; i <= 10000; i++){
        int contador = 0;
        for(auto j = 1; j <= i; j++){
            if(i % j == 0){
                contador++;
            }
        }
        if(contador == 2){
            std::cout << i << std::endl;
        }
    }
   

    return 0;
}