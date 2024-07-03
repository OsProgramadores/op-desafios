#include <iostream>

int main()
{
    
    for(int i = 1; i<=10000; i++){
        int contadorDivisor = 0;

        for(int j = 1; j<=i; j++){
            if(i%j == 0){
                contadorDivisor++;
            }
        }
        if(contadorDivisor == 2){
            std::cout<<i<<"\n";
        }
    }

    return 0;
}
