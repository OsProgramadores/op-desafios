#include <stdio.h>
#include <stdbool.h>


bool is_prime(int number);


int main(void) {
    for (int i = 1; i<= 10000; i++) {
        if (is_prime(i)) {
            printf("%d\n", i);
        }
    }
    return 0;
}


bool is_prime(int number) {
    if (number == 2 || number == 3)
        return true;

    if (number <= 1 || number % 2 == 0 || number % 3 == 0)
        return false;

    for (int i = 5; i * i <= number; i += 6) {
        if (number % i == 0 || number % (i + 2) == 0)
            return false;
    }
    return true;
}
