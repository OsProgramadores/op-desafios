#include <stdio.h>

int main() {
    int i, j, a = 0;

    for (i = 1; i < 10000; ++i) {
        for (j = 2; j < i; ++j) {
            if (i % j == 0) {
                a++;
            }
        }
        if (a == 0) {
            printf("%d\n", i);
        }
        a = 0;
    }

    return 0;
}
