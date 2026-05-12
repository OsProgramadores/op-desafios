#include <stdio.h>

int main() {

    int n = 10000;

    int primo[10001];

    for (int i = 0; i <= n; i++) {
        primo[i] = 1;
    }

    primo[0] = 0;
    primo[1] = 0;

    for (int i = 2; i * i <= n; i++) {

        if (primo[i] == 1) {

            for (int j = i * i; j <= n; j += i) {
                primo[j] = 0;
            }
        }
    }

    for (int i = 2; i <= n; i++) {

        if (primo[i] == 1) {
            printf("%d\n", i);
        }
    }

    return 0;
}
