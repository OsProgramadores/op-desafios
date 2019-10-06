#include<iostream>

using namespace std;
int main(){
int cont = 0;

for(int i = 2; i<=10000;i++){
    for(int j = 2; j<=10000;j++){
    if(i%j == 0 && j <= i/2){
        cont++;
    }
}
if( cont == 0){
    cout << i << endl;
}
cont = 0;
}

    return 0;
}
