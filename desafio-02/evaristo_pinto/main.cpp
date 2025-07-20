#include "iostream"
#include "vector"

using namespace std;



vector<int> StoregeArray(int n){
    
    vector<int>array;

    for(int i = 0; i<=n; i++){
        array.push_back(i);
    }

    return array;
}


void numerosPrimos(int n, int total){


 vector<int> nPrimos  =  StoregeArray(total);

 for(int i = n; i<=total; i++){

    if(nPrimos[i] % 2 == 0){
       
    }else{
       
        if(nPrimos[i] == 1){
            nPrimos[i] = 2;
        }else
        if(nPrimos[i] % 3 == 0){
           if(nPrimos[i]== 3){
            nPrimos[i]==3;
           }else{
            
           }

            
        }

        cout<< nPrimos[i];

       
        
    }
    
 }

  

}

int main(){
    
    numerosPrimos(1, 10);

}