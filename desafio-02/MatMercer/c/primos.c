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

// espera um numero positivo impar maior que zero, podemos ignorar check para números pares
int isPrimo(int numImpar) {
    if (numImpar % 3 == 0) {
        return 0;
    }

    // 6k +- 1 check
    // podemos parar em raiz de N
    for (int k = 5; k * k <= numImpar; k += 6) {
        if (
                numImpar % k == 0 // 6k - 1 check
                || numImpar % (k + 2) == 0 // 6k + 1 check
           ) {
            return 0;
        }
    }

    return 1;
}

