#include <stdio.h>

int main() {
    unsigned long long int nA = 0;
    unsigned long long int nB = 0;
    unsigned long long int aux = 0;
    scanf("%llu%llu", &nA, &nB);
    if (nA > nB) {
        aux = nA;
        nA = nB;
        nB = aux;
    }
    for (unsigned long long int i = nA; i <= nB; i++) {
        unsigned long long int n = i;
        unsigned long long int remainder = 0;
        unsigned long long int nX = 0;
        while (n > 0) {
            remainder = n % 10;
            nX = nX * 10 + remainder;
            n = n / 10;
        }
        if (nX == i) {
            printf("%llu\n", i);
        }
    }
    return 0;
}
