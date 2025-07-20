#include "iostream"
#include "vector"

using namespace std;


void numerosPares(int n, int total){


    int counter = 0;
    int primos[5];
    int i = n;
    for ( i; i <= total; i++)
    {
        if(i % 2 == 0){
             
            primos[i] = i;
            cout<<i;
            counter ++;
        }
    }
    
  

}

int main(){
    
    numerosPares(1, 10);

}