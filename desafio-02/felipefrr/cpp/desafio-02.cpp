#include <iostream>
#include <cmath>
using namespace std;


void isPrime(int max){
    int isNotPrime = 0;
    for(int i = 2; i <= max; i++){
        for(int j = 2; j != i && j <= (int)sqrt(i); j++){
            if(i % j == 0){
                isNotPrime = 1;
                break;
            }
            isNotPrime = 0;
        }
        if(!isNotPrime)
            cout << i << endl;
    }
    return;
}

int main() {
  isPrime(10000);
  return 0;
}