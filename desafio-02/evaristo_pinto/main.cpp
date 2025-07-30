#include "iostream"
#include "vector"

using namespace std;


 int VerificandoEprimo(int n){

    int counter = 0;
    for (int i = 1; i <= n; i++)
    {
         if(n % i == 0){
           counter ++;
         } 
    }

    if(counter == 2){
        return 1;

    }else{
        return 0;
    }
    
 }

 void ListarPrimos(int inicio, int fim){

    for (int i = inicio; i <= fim; i++)
    {
        
            if(VerificandoEprimo(i) == 1){
                cout<<i;
            }
        
    }
    

 }

int main(){
    
    ListarPrimos(1, 100);

}