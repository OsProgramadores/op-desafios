#include <stdio.h>

#define RANGE 10000

int isPrimo(int num);

int main() {

    int count = 1;
    while (count < 3) {
        printf("%d\n", ++count);
    }

    while(count <= RANGE) {
        count += 2;

        if (isPrimo(count)) {
            printf("%d\n", count);
        }
    }

    return 0;
}

// espera um numero impar
int isPrimo(int numImpar) {
    if (numImpar % 3 == 0) {

        return 0;
    }
    int c = 5;

    while (c < numImpar) {
        if (numImpar % c == 0) {
            return 0;
        }
        c += 2;
    }
    return 1;
}

