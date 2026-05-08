#include <stdio.h>

int main() {
    int n = 10000;

    for (int i = 2; i <= n; i++) {

        int prime = 1;

        for (int j = 2; j < i; j++) {

            if (i % j == 0) {
                prime = 0;
                break;
            }
        }

        if (prime == 1) {
            printf("%d\n", i);
        }
    }

    return 0;
}
