#include <stdio.h>
#include <stdbool.h>

int main(){

    printf("Number 2 is prime\n");
    printf("Number 3 is prime\n");

for (int i = 5; i <= 10000; i+=2)
{
    if(i%3==0) continue;

    bool isPrime = 1;

    for (int j = 2; j * j <= i; ++j) {
        if (i % j == 0) 
            {
             isPrime = 0;
             break;
            }
    
    }
    if(isPrime){
    printf("Number %i is prime\n", i);
    }
}
return 0;

}